  from typing import final


class Shoes:
    def __init__(self, brand, price, color, size, quantity):
        self.brand = brand
        self.price = price
        self.color = color
        self.size = size
        self.quantity = quantity

    def Sale(self, quantity):
        self.quantity -= quantity

    def Purchase(self, quantity):
        self.quantity += quantity

shoes_list = []
shoes1 = Shoes("Nike", 420, "white", 37, 4)
shoes2 = Shoes("Adidas", 230, "black", 41, 7)
shoes3 = Shoes("Armani", 410, "white", 37, 4)
shoes4 = Shoes("Gues", 200, "white", 37, 10)
shoes5 = Shoes("Nike AirFoce", 190, "white", 37, 3)
shoes6 = Shoes("Gues", 700, "white", 35, 9)
shoes7 = Shoes("Nike", 90, "white", 40, 7)

shoes_list.append(shoes1)
shoes_list.append(shoes2)
shoes_list.append(shoes3)
shoes_list.append(shoes4)
shoes_list.append(shoes5)
shoes_list.append(shoes6)
shoes_list.append(shoes7)

def sort_price(list_shoes):
    list_shoes_sorted = sorted(list_shoes, key=lambda shoes: shoes.price, reverse=True)
    for shoes in list_shoes_sorted:
        print(f"{shoes.brand} {shoes.price} {shoes.color} {shoes.size} {shoes.quantity}")

sort_price(shoes_list)

def shoes_searching(list_shoes, brand, size):
    for shoes in list_shoes:
        shoes_price = shoes.price
        shoes_sum = 0
        shoes_sum += shoes_price
        average = shoes_sum / len(list_shoes)

    for shoes in shoes_list:
        if shoes.brand == brand and shoes.size == size and shoes.price < average:
            print(f"{shoes.brand} {shoes.size}")

def cheapest_shoes(shoes_list,  color):
    shoes_color_list = []
    for shoes in shoes_list:
        if shoes.color == color:
            shoes_color_list.append(shoes)

    if len(shoes_color_list) > 0:
        sorted_shoes_color_list = sorted(shoes_color_list, key=lambda shoes: shoes.price)
        final_shoes = sorted_shoes_color_list[0]
        print(final_shoes)
    else:
        print("color is not avaliable")
        colors = []
        for shoes in shoes_list:
            color.append(shoes.color)
        final_colors = set(colors)
        for color in final_colors:
            print(color)

def delete_shoes(shoes_list, brand):
    for shoes in shoes_list:
        if shoes.brand == brand:
            shoes_list.remove(shoes)
            for shoes in shoes_list:
                print(f"{shoes.brand} {shoes.price} {shoes.color} {shoes.size} {shoes.quantity}")

# def delete_shoes(shoes_list, brand):
#     new_shoes_list = [shoes for shoes in shoes_list if shoes.brand != brand]
#     for shoes in new_shoes_list:
#         print(shoes)



        # for shoes in shoes_list:
        #         print(shoes.color)
