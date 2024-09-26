def calc_deposit():
    month_salary = int(input('Enter your month salary: '))
    deposit_percentage = int(
        input('Enter percentage of deposit of your month salary: ')
    )
    year_percentage = int(input('Enter year bank percentage of deposit: '))

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
                return
            else:
                print(f'\nYour balance: {balance}')
        i += 1


calc_deposit()
