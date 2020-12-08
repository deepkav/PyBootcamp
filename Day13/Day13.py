class CoffeeMachine:

    def __init__(self, Water, Milk, Coffee, Money):
        self.Water = Water
        self.Milk = Milk
        self.Coffee = Coffee
        self.Money = Money


    def resources(self, choice, beverage):
        self.choice = choice
        self.beverage = beverage
        if self.Water - self.beverage[0] < 0:
            print("Sorry there is not enough Water")
        elif self.Milk - self.beverage[1] < 0:
            print("Sorry there is not enough Milk")
        elif self.Coffee - self.beverage[2] < 0:
            print("Sorry there is not enough Coffee")
        else:
            return True

    def processCoins(self,beverage):
        print("Accepted coins 'quarter $0.25, dime $0.1, nickle $0.05, penny $0.01': ")
        self.payment = 0.0
        self.payment += int(input('Enter No.of quarters coins:')) * 0.25
        if self.payment < self.beverage[3]:
            self.payment += int(input('Enter No.of dimes coins:')) * 0.1
        if self.payment < self.beverage[3]:
            self.payment += int(input('Enter No.of nickle coins:')) * 0.05
        if self.payment < self.beverage[3]:
            self.payment += int(input('Enter No.of pennies:')) * 0.01

        self.checkTransaction(beverage)


    def checkTransaction(self,beverage):
        if self.payment < self.beverage[3]:
            print("Sorry that's not enough Money. Money refunded.")
            return None
        elif self.payment > self.beverage[3]:
            self.Money += self.beverage[3]
            self.change = round(self.payment - self.beverage[3], 2)
            print(f"Here is $",self.change," dollars in change.")
        else:
            self.Money += self.payment
        self.payment = 0

        self.MakeCoffee()


    def MakeCoffee(self):
        self.Water -= self.beverage[0]
        self.Milk -= self.beverage[1]
        self.Coffee -= self.beverage[2]
        print("Here is your ",self.choice," Enjoy!")

    def report(self):
        print("Water: ",self.Water," ml")
        print("Milk: ",self.Milk," ml")
        print("Coffee: ",self.Coffee," grams")
        print("Money: $",self.Money)


machine1 = CoffeeMachine(10500, 750, 200, 0)


espresso = [250, 0, 20, 1.75]
latte = [200, 150, 24, 2.50]
cappuccino = [300, 200, 20, 2.95]

while True:
    print('\nEspresso :$',espresso[3])
    print('latte :$',latte[3])
    print('cappuccino :$',cappuccino[3])

    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "espresso":
        if machine1.resources(choice, espresso):
            print('You have choosen espresso ')
            machine1.processCoins(espresso)
    elif choice == "latte":
        if machine1.resources(choice, latte):
            print('You have choosen latte ')
            machine1.processCoins(latte)
    elif choice == "cappuccino":
        if machine1.resources(choice, cappuccino):
            print('You have choosen cappuccino ')
            machine1.processCoins(cappuccino)
    elif choice == "report":
        machine1.report()
    elif choice == "off":
        break;