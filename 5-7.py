import json
profit = {}
av_pr_dict = {}
prof = 0
av_profit = 0
i = 0
with open('5-7.txt', 'r') as f:
    for line in f:
        name, form, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit[name] >= 0:
            prof = prof + profit[name]
            i += 1
    if i != 0:
        av_profit = prof / i
    else:
        print(f'Все сработали в убыток, прибыли нет.')
    av_pr_dict = {'Average profit': round(av_profit)}
    print(av_pr_dict) #смотрим только словарь средней прибыли
    print(f'Прибыль фирм: {profit}') #смотрим словарь прибылей всех фирм
list = [profit, av_pr_dict] #объединение двух словарей в один список и вывод этого на экран
print(list)

with open('5-7.json', 'w') as write_js:
    json.dump(list, write_js)
    js_str = json.dumps(list)
    print(f'Json файл: {js_str}')