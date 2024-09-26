def calc_tip():
    n = int(input('Write number of meals: '))
    prices = []

    for i in range(n):
        price = int(input('Write a price of meal #' + str(i + 1) + ': '))
        prices.append(price)

    if n <= 0:
        print('\n' + 'Please, write a correct number of meals!')
        return

    tip = int(input('Write a percentage of tip: '))

    total_price_of_meals = sum(prices)

    if total_price_of_meals > 2000:
        total_price_of_meals = round(0.9 * total_price_of_meals, 2)

    total_price_of_tip = round(tip / 100 * total_price_of_meals, 2)
    total_price = round(total_price_of_meals + total_price_of_tip, 2)

    print('\n' + 'Total price of meals: ' + str(total_price_of_meals))
    print('Total price of tip: ' + str(total_price_of_tip))
    print('Total price: ' + str(total_price))


calc_tip()
