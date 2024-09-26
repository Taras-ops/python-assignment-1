def fahreheit_to_celsius(t):
    return round((t - 32) / 1.8, 2)


def transform_temperatures():
    temperatures_celsius = []

    for i in range(7):
        temperature = input('Write the temperature in Fahrenheit degreees of the ' + str(i + 1) + ' day of the week: ')

        while not temperature.isdigit():
            temperature = input('Please, Write the temperature in Fahrenheit degreees of the ' + str(i + 1) + ' day of the week: ')

        temperature_celsius = fahreheit_to_celsius(int(temperature))

        if temperature_celsius < 10:
            print('\n' + 'Cold!' + '\n')
        elif temperature_celsius <= 28:
            print('\n' + 'Warm!' + '\n')
        elif temperature_celsius <= 36:
            print('\n' + 'Hot!' + '\n')
        else:
            print('\n' + 'Very hot!' + '\n')

        temperatures_celsius.append(temperature_celsius)

    average_temperature = round(sum(temperatures_celsius) /
                                len(temperatures_celsius), 2)
    max_temperature = max(temperatures_celsius)
    min_temperature = min(temperatures_celsius)

    print(f'Average temperature in Celcius degree: {average_temperature}')
    print(f'Max temperature in Celcius degree: {max_temperature}')
    print(f'Min temperature in Celcius degree: {min_temperature}')


transform_temperatures()
