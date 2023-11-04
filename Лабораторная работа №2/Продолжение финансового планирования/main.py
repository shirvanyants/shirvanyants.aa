salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
mounths = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
for i in range(1,mounths+1):
    money_capital = money_capital - salary + spend
    spend = spend * (increase + 1)
money_capital = round(money_capital,2)# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
print(f"Подушка безопасности, чтобы протянуть {mounths} месяцев без долгов:", money_capital)
