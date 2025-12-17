import json
import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Функция для получения JWT токена
def get_jwt_token(token_url, client_id, client_secret):
    print("Получаем JWT токен...")
    params = {
        'grant_type': 'client_credentials',
        'response_type': 'id_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'validity': 3600
    }

    resp = requests.post(token_url, params=params)
    resp.raise_for_status()
    print("JWT токен получен.")
    return resp.content.decode('utf8')

# Функция для обновления кастомного поля в NetBox
def update_netbox_custom_field(netbox_url, netbox_token, vm_name, custom_field_value):
    print(f"Начинаем обновление кастомного поля для ВМ: {vm_name}")
    
    headers = {
        'Authorization': f'Token {netbox_token}',
        'Content-Type': 'application/json'
    }

    search_url = f"{netbox_url}/api/virtualization/virtual-machines/?name={vm_name}"
    response = requests.get(search_url, headers=headers)
    print(f"Ответ от NetBox при поиске ВМ: статус {response.status_code}")

    if response.status_code == 200:
        result = response.json()
        print(f"Ответ от NetBox (данные): {result}")

        if result['count'] > 0:
            vm_id = result['results'][0]['id']
            print(f"ID ВМ: {vm_id}")

            update_url = f"{netbox_url}/api/virtualization/virtual-machines/{vm_id}/"
            data = {
                'custom_fields': {
                    'Node_Name': custom_field_value
                }
            }
            print(f"Данные для обновления: {data}")

            update_response = requests.patch(update_url, headers=headers, json=data)
            print(f"Ответ от NetBox при обновлении ВМ: статус {update_response.status_code}")
            print(f"Ответ от NetBox (обновление): {update_response.json()}")

            update_response.raise_for_status()
        else:
            print(f"ВМ с именем {vm_name} не найдена.")
    else:
        print(f"Ошибка при поиске ВМ в NetBox: {response.status_code} {response.text}")
        response.raise_for_status()

# Функция для локального тестирования работы скрипта
def process_site_file(site_config, netbox_url, netbox_token):
    print(f"Начинаем обработку сайта: {site_config['url']}")
    print("Выполняем запрос списка ВМ из локального файла...")

    try:
        vm_file = open(f'sample_vm_{site_config['mrf']}.json', 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f"Нет информации по ВМ для сайта {site_config['mrf']}")
        return
    else:
        vms = json.load(vm_file)
    
    data_compute = vms['data']
    print("Список ВМ получен.")

    print("Выполняем запрос списка хостов из локального файла...")

    try:
        hosts = open(f'sample_node_{site_config['mrf']}.json', 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f"Нет информации по хостам для сайта {site_config['mrf']}")
        return
    else:
        hosts = json.load(hosts)

    compute_data = []
    for item in data_compute:
        stack_id = item.get('stackId')
        if not stack_id:
            compute_data.append({'name_compute': 'НЕТ ВМ', 'stackId': None})
        else:
            compute_data.append({'name_compute': item.get('name'), 'stackId': stack_id})
    
    data_nodes = hosts['data']
    print("Список хостов получен.")

    nodes_data = [{'name_node': item.get('name'), 'stackId': item.get('stackId')} for item in data_nodes]

    print("Мержим данные...")
    df_compute = pd.DataFrame(compute_data)
    df_nodes = pd.DataFrame(nodes_data)
    merged_df = pd.merge(df_compute, df_nodes, on='stackId', how='left')

    print("Добавляем МРФ...")
    merged_df['mrf'] = site_config['mrf']
    
    print("Обновляем кастомное поле в NetBox...")
    for _, row in merged_df.iterrows():
        update_netbox_custom_field(netbox_url, netbox_token, row['name_compute'], row['name_node'])
    
    print(f"Обработка сайта {site_config['url']} завершена.")
    return merged_df

# Функция для обработки сайта из конфигурации
def process_site(site_config, netbox_url, netbox_token):
    print(f"Начинаем обработку сайта: {site_config['url']}")
    
    token_url = f"https://sso-{site_config['url']}/v1/oauth/access_token"
    compute_list_url = f"https://{site_config['url']}/restmachine/cloudbroker/compute/list"
    nodes_list_url = f"https://{site_config['url']}/restmachine/cloudbroker/node/list"
    
    JWT = get_jwt_token(
        token_url,
        os.getenv(site_config['client_id_env']),
        os.getenv(site_config['client_secret_env'])
    )
    
    headers = {'Authorization': f'bearer {JWT}'}

    print("Выполняем запрос списка ВМ...")
    response_compute = requests.post(compute_list_url, headers=headers)
    response_compute.raise_for_status()
    data_compute = response_compute.json()['data']
    print("Список ВМ получен.")

    compute_data = []
    for item in data_compute:
        stack_id = item.get('stackId')
        if not stack_id:
            compute_data.append({'name_compute': 'НЕТ ВМ', 'stackId': None})
        else:
            compute_data.append({'name_compute': item.get('name'), 'stackId': stack_id})

    print("Выполняем запрос списка хостов...")
    response_nodes = requests.post(nodes_list_url, headers=headers)
    response_nodes.raise_for_status()
    data_nodes = response_nodes.json()['data']
    print("Список хостов получен.")

    nodes_data = [{'name_node': item.get('name'), 'stackId': item.get('stackId')} for item in data_nodes]

    print("Мержим данные...")
    df_compute = pd.DataFrame(compute_data)
    df_nodes = pd.DataFrame(nodes_data)
    merged_df = pd.merge(df_compute, df_nodes, on='stackId', how='left')

    print("Добавляем МРФ...")
    merged_df['mrf'] = site_config['mrf']
    
    print("Обновляем кастомное поле в NetBox...")
    for _, row in merged_df.iterrows():
        update_netbox_custom_field(netbox_url, netbox_token, row['name_compute'], row['name_node'])
    
    print(f"Обработка сайта {site_config['url']} завершена.")
    return merged_df

# Главная функция для обработки всех сайтов
def main():
    print("Запускаем основной процесс...")
    
    netbox_url = "http://localhost:8000"
    netbox_token = os.getenv("NETBOX_TOKEN")

    with open('config.json', 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)

    all_sites_data = []
    
    for site in config['sites']:
        print(f"Обрабатываем сайт: {site['url']}")
#        site_data = process_site(site, netbox_url, netbox_token)
        site_data = process_site_file(site, netbox_url, netbox_token)
        all_sites_data.append(site_data)
    
    final_df = pd.concat(all_sites_data, ignore_index=True)
    
    output_file = 'vm_de_netbox_info.xlsx'
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    final_df.to_excel(writer, index=False)
    print(f"Файл '{output_file}' успешно создан.")
    writer.close()

if __name__ == "__main__":
    main()