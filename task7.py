#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
dotA = int(input('Введите точку А: '))
dotB = int(input('Введите точку B: '))
dotC = int(input('Введите точку C: '))

partAC = dotC - dotA
partBC = dotC - dotB

print ('Длина отрезка АС: ' + str(partAC) + '\nДлина отрезка ВС: ' + str(partBC))
print ('Сумма отрезков AC и BC: ' + str(partAC + partBC))