import math

quantity = lambda x : math.ceil(x / 3 / 18)
price = lambda x : quantity(x)*80

area = int(input("Area in m^2 to be painted: "))

print("You will need", quantity(area), f"paint cans and a total of R${"{:.2f}".format(price(area))}" )