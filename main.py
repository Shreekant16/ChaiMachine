from menu import Menu, resources


def sufficient(order):
    for item in resources:
        if resources[item] >= order[item]:
            return True


def money():
    print("Enter your money here,")
    total = int(input("Enter 10 rs notes : ")) * 10
    total += int(input("Enter 20 rs notes : ")) * 20
    total += int(input("Enter 50 rs notes : ")) * 50
    total += int(input("Enter 100 rs notes : ")) * 100
    return total


profit = 0


def change(req, given):
    global profit
    change = given - req
    profit += req
    print(f"This {change} rs in change.")


def make(order):
    for item in resources:
        resources[item] -= order[item]


def report():
    print(f"Powder is {resources['powder']}gm")
    print(f"Milk is {resources['milk']}ml")
    print(f"Masala is {resources['masala']}gm")
    print(f"Profit is {profit} rs")


end = False
while not end:
    order = input("Enter Your order (chai/ black tea/ jaggery tea) : ")
    if order == 'off':
        print('Sorry we are temporarily closed')
        end = True
    elif order == 'report':
        report()
    else:
        drink = Menu[order]
        if sufficient(drink['ingredients']):
            given = money()
            if given >= drink['cost']:
                change(drink['cost'], given)
                make(drink['ingredients'])
                print(f"Enjoy your {order}")
