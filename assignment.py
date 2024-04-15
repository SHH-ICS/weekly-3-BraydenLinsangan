import time
print("Welcome to gaymers' Pizza Parlor!")
time.sleep(1)
print("What pizza size would you like, we serve L or XL")
PizzaSize = input()
Price = 0
if PizzaSize != "L" and PizzaSize != "XL":
  print("Sorry, we only sell L or XL.")
elif PizzaSize == "L":
  print("How many toppings?")
  Price = 6
elif PizzaSize == "XL":
  print("How many toppings?")
  Price = 10
Toppings = input()
if Toppings <= "1" and Toppings >= "5":
  print("We only serve pizzas with 1-4 toppings.")
if Toppings == "1":
  Price = (Price+1)
elif Toppings == "2":
  Price = (Price+1.75)
elif Toppings == "3":
  Price = (Price+2.50)
elif Toppings == "4":
  Price = (Price+3.35)
Subtotal = Price
Tax = (Subtotal*0.13)
Total = (Subtotal+Tax)
print("Here is the cost for the pizza.")
time.sleep(1)
print(Subtotal)
time.sleep(0.75)
print(Total)