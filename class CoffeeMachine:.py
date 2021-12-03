"""
Isabella Nordstrom
CSE20 Hari Kuttivelil
Assignment 10.1 - Implement a class based on a real world object. 
"""

class CoffeeShop:
    def __init__(self, cup_size=None, coffee=None, milk=None, order=None):
        #Creating private data attributes for the cup, coffee, and milk so i can use them later in my methods. 
        self.__cup_size = cup_size 
        self.__coffee = coffee
        self.__milk = milk
        #Creating a class variable for the entire order of the coffee. 
        if order is None:
            #The information will be stored in a dictionary. 
            self.coffee_order = {}
        else:
            self.coffee_order = order
    #Method that sets the size of the cup. 
    def set_cup(self, user_cup):
        #Setting the private data attribute to a variable. 
        self.__cup_size = user_cup
        #Setting the cup size equal to the dictionary value. 
        value = self.__cup_size
        #Updating the class dictionary. 
        self.coffee_order.update(Size=value)
    #Method that returns the desired cup size. 
    def get_cup(self):
        return self.__cup_size
    #Method that sets the type of coffee.
    def set_coffee(self, user_coffee):
        self.__coffee = user_coffee
        value = self.__coffee
        self.coffee_order.update(Coffee=value)
    def get_coffee(self):
        return self.__coffee
    #Method that sets the type of milk.
    def set_milk(self, user_milk):
        self.__milk = user_milk
        value = self.__milk
        self.coffee_order.update(Milk=value)
    def get_milk(self):
        return self.__milk
    #Method that returns the order as a string. 
    def call_order(self):
        print(f"You ordered a {self.__cup_size}, {self.__coffee} roast coffee with {self.__milk} milk.")
    #Method that returns the order as a dictionary. 
    def get_order(self):
        return self.coffee_order
    #A method that interacts with the user to get the order through user inputs. 
    def coffee_shop(self):
        print("Hello! Welcome to Bella's Coffee Shop!")
        #The user input becomes the cup size. 
        cup_input = input("What size would you like? Small, Medium, or Large: ")
        #Puts the new cup input into the set_cup method. 
        self.set_cup(cup_input)
        #Does the same for the coffee and the milk. 
        coffee_input = input("What coffee roast would you like? Light, Medium, or Dark: ")
        self.set_coffee(coffee_input)
        #Asks the user if they want milk.
        milk = input("Do you want milk? Yes or No: ")
        #If yes, it will set the milk to the user input. 
        if milk == "Yes":
            milk_input = input("What kind of milk would you like? Oat, Almond, or Soy: ")
            self.set_milk(milk_input)
        else:
            milk == "No"
        #Call the order using call_order().
        self.call_order()

def main():
    coffee = CoffeeShop()
    coffee.coffee_shop()
    print(coffee.get_order())
    coffee.set_cup("Large")
    coffee.set_coffee("Light")
    coffee.set_milk("Soy")
    print(coffee.get_order())
    
    
if __name__ == "__main__":
    main()