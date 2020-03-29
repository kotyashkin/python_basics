earns = float(input('Выручка фирмы за месяц (рубли): '))
exspences = float(input('Издержки: '))
if earns > exspences:
    profit = earns - exspences
    rent = profit / earns
    print(f"Месяц отработан с прибылью: {profit} руб.\n"
          f"рентабельность: {rent*100} %\n")
    n = int(input('Сколько сотрудников в фирме? '))
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет: {profit/n} руб.")
else:
    res = exspences - earns
    print(f"Убыток в этом месяце составил: {res} рублей")