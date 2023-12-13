from inventory import resources, MENU

quarters_price_value = 0.25
dimes_price_value = 0.10
nickles_price_value = 0.05
pennies_price_value = 0.01

ESPRESSO = 'espresso'
LATTE = 'latte'
CAPPUCINO = 'cappuccino'

expresso_ingredient = MENU[ESPRESSO]
latte_ingredient = MENU[LATTE]
capuccino_ingredient = MENU[CAPPUCINO]

wallet = 0.00

switch_off_machine = False

# 1.Ask users input
# 3.Check money drawn
# 4.Give back the value and report the resouces
# 5. give back the change for xtra cash
print('Good Morning !!!')


def is_resource_available(source, user_choice_ingredient):
    resources_available = False
    if (source['water'] >= user_choice_ingredient['water']):
        if (source['milk'] >= user_choice_ingredient['milk']):
            if (source['coffee'] >= user_choice_ingredient['coffee']):
                resources_available = True

    return resources_available


def deductTheSource(source, user_choice_ingredient):
    source['water'] -= user_choice_ingredient['water']
    source['milk'] -= user_choice_ingredient['milk']
    source['coffee'] -= user_choice_ingredient['coffee']


def report():
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")
    print(f"Water : {resources['water']}")
    print(f"Money {wallet} $")






while (not switch_off_machine):
    user_choice = input('What do you like to have today? espresso/latte/cappuccino?  ')

    if user_choice == 'report':
        report()
    elif user_choice == 'off':
        print('Machine is OFF')
        switch_off_machine = True
    else:
        print('Please insert your coins')
        print(
            f"espresso : {MENU['espresso']['cost']} ; latte : {MENU['latte']['cost']} cappuccino : {MENU['cappuccino']['cost']}")
        print(
            f"quarter:{quarters_price_value}$ dime:{dimes_price_value}$ nickles: {nickles_price_value}$ pennies{pennies_price_value}$")




        # 2.Check resources available based on users choice

        quarters_count = float(input('How many quarters?'))
        dimes_count = float(input('How many dimes?'))
        nikles_count = float(input('How many nickles?'))
        pennies_count = float(input('How many pennies?'))
        users_money = round(
            (float(quarters_count * quarters_price_value) + float(dimes_count * dimes_price_value) + float(
                nikles_count * nickles_price_value) + float(pennies_count * pennies_price_value)), 2)

        if (user_choice == ESPRESSO):
            is_resource_available(resources, expresso_ingredient['ingredients'])
            if (users_money >= expresso_ingredient['cost']):
                print('Enjoy your cup of ESPRESSO ')
                deductTheSource(resources, expresso_ingredient['ingredients'])
                print(f"Here is your excess Money . Keep the change {round(users_money - expresso_ingredient['cost'],2)}")
                wallet += expresso_ingredient['cost']
                report()

        elif (user_choice == LATTE):
            is_resource_available(resources, latte_ingredient['ingredients'])
            if (users_money >= latte_ingredient['cost']):
                print('Enjoy your cup of LATTE ')
                deductTheSource(resources, latte_ingredient['ingredients'])
                print(f"Here is your excess Money . Keep the change {round(users_money - latte_ingredient['cost'],2)}")
                wallet += latte_ingredient['cost']
                report()

        elif (user_choice == CAPPUCINO):
            is_resource_available(resources, capuccino_ingredient['ingredients'])
            if (users_money >= capuccino_ingredient['cost']):
                print('Enjoy your cup of CAPPUCINO ')
                deductTheSource(resources, capuccino_ingredient['ingredients'])
                print(f"Here is your excess Momey . Keep the change {round(users_money - capuccino_ingredient['cost'],2)}")
                wallet += capuccino_ingredient['cost']
                report()

        else:
            print('Invalid choice')
