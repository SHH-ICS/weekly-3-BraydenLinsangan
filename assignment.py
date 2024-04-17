import time
time.sleep(0.5)
print("Welcome to Joseph Manuel Davuis' Pizza Parlor!")
time.sleep(1)
print("What pizza size would you like, we serve L or XL")
PizzaSize = input()
Price = 0
if PizzaSize != "L" and PizzaSize != "XL":
  print("Sorry, we only sell L or XL.")
elif PizzaSize == "L":
  time.sleep(1)
  print("How many toppings?")
  Price = 6
  Toppings = int(input())
  if Toppings < 1:
    print("We only serve pizzas with 1-4 toppings.")
  if Toppings > 4:
    print("We only serve pizzas with 1-4 toppings.")
  if Toppings == 1:
    Price = (Price+1)
    Subtotal = Price
    Tax = (Subtotal*0.13)
    Total = (Subtotal+Tax)
    print("Here is the cost for the pizza.")
    time.sleep(1)
    print("Subtotal $",Subtotal)
    time.sleep(0.75)
    print("Total $" ,Total)
  elif Toppings == 2:
    Price = (Price+1.75)
    Subtotal = Price
    Tax = (Subtotal*0.13)
    Total = (Subtotal+Tax)
    print("Here is the cost for the pizza.")
    time.sleep(1)
    print("Subtotal $",Subtotal)
    time.sleep(0.75)
    print("Total $" ,Total)
  elif Toppings == 3:
    Price = (Price+2.50)
    Subtotal = Price
    Tax = (Subtotal*0.13)
    Total = (Subtotal+Tax)
    print("Here is the cost for the pizza.")
    time.sleep(1)
    print("Subtotal $",Subtotal)
    time.sleep(0.75)
    print("Total $" ,Total)
  elif Toppings == 4:
    Price = (Price+3.35)
    Subtotal = Price
    Tax = (Subtotal*0.13)
    Total = (Subtotal+Tax)
    print("Here is the cost for the pizza.")
    time.sleep(1)
    print("Subtotal $",Subtotal)
    time.sleep(0.75)
    print("Total $" ,Total)
if PizzaSize == "XL":
  time.sleep(1)
  print("How many toppings?")
  Price = 10
  Toppings = int(input())
  if Toppings < 1:
    print("We only serve pizzas with 1-4 toppings.")
  if Toppings > 4:
    print("We only serve pizzas with 1-4 toppings.")
  if Toppings == 1:
    Price = (Price+1)
    Subtotal = Price
    Tax = (Subtotal*0.13)
    Total = (Subtotal+Tax)
    print("Here is the cost for the pizza.")
    time.sleep(1)
    print("Subtotal $",Subtotal)
    time.sleep(0.75)
    print("Total $" ,Total)
  elif Toppings == 2:
    Price = (Price+1.75)
    Subtotal = Price
    Tax = (Subtotal*0.13)
    Total = (Subtotal+Tax)
    print("Here is the cost for the pizza.")
    time.sleep(1)
    print("Subtotal $",Subtotal)
    time.sleep(0.75)
    print("Total $" ,Total)
  elif Toppings == 3:
    Price = (Price+2.50)
    Subtotal = Price
    Tax = (Subtotal*0.13)
    Total = (Subtotal+Tax)
    print("Here is the cost for the pizza.")
    time.sleep(1)
    print("Subtotal $",Subtotal)
    time.sleep(0.75)
    print("Total $" ,Total)
  elif Toppings == 4:
    Price = (Price+3.35)
    Subtotal = Price
    Tax = (Subtotal*0.13)
    Total = (Subtotal+Tax)
    print("Here is the cost for the pizza.")
    time.sleep(1)
    print("Subtotal $",Subtotal)
    time.sleep(0.75)
    print("Total $" ,Total)