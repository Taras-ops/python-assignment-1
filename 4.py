def calc_deposit():
    month_salary = input('Enter your month salary: ')

    while not month_salary.isdigit():
        month_salary = input('Please, enter your month salary: ')

    deposit_percentage = input('Enter percentage of deposit of your month salary: ')

    while not deposit_percentage.isdigit():
        deposit_percentage = input('Please, enter percentage of deposit of your month salary: ')

    year_percentage = input('Enter year bank percentage of deposit: ')

    while not year_percentage.isdigit():
        year_percentage = input('Please, enter year bank percentage of deposit: ')

    month_salary = int(month_salary)
    deposit_percentage = int(deposit_percentage)
    year_percentage = int(year_percentage)

    balance = 0
    i = 1

    while True:
        balance += round(month_salary * deposit_percentage / 100, 2)

        if i % 12 == 0:
            balance += round(balance * year_percentage / 100, 2)
        print(f'Your balance of {i} month: {balance}')

        if i % 12 == 0:
            number = int(
                input('\nWrite 0 to withdraw saving or 1 to continue deposit: ')
            )

            while number != 0 and number != 1:
                number = int(
                    input('Please, write 0 to withdraw saving or 1 to continue deposit: ')
                )

            if number == 0:
                print(f'\nYour balance: {balance}')
                return

        i += 1


calc_deposit()
