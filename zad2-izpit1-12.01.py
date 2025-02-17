from statistics import quantiles


class ClothesShop:
    def __init__(self, id, type, brand, price, quantity):
      self.id = id
      self.type = type
      self.brand = brand
      self.price = price
      self.quantity = quantity

    def clothes_info(self):
        print(f"{self.id}-{self.type}-{self.brand}-{self.price}-{self.quantity}")

    def change_price(self):
        price = int(input())
        self.price = price

    def change_qty(self):
        quantity = int(input())
        self.quantity = quantity

def search_by_id(clothes_list, id):
    for clothes in clothes_list:
        if clothes.id == id:
            clothes.clothes_info()
            break

def search_by_brand(clothes_list, brand):
    for clothes in clothes_list:
        if clothes.brand == brand:
            clothes.clothes_info()

def sell_clothe_by_id(clothes_list, id, num):
    hasClothes = False
    for clothes in clothes_list:
        if clothes.id == id and clothes.num >= num:
            print("Успешна продажба")
            hasClothes = True
            clothes.quantity -= num
        elif clothes.id == id and   clothes.num < num:
            print("Недостатъчна наличност")
            hasClothes = True

    if hasClothes == False:
        print("Не е открит такъв продукт")

if __name__ == "__main__":
    clothes_list = []
    clothes1 = ClothesShop(2, 'short', 'Nike', 120, 12)
    clothes2 = ClothesShop(3, 'short', 'Adidas', 200, 5)
    clothes3 = ClothesShop(5, 'T-shirt', 'Nike', 150, 3)
    clothes_list.append(clothes1)
    clothes_list.append(clothes2)
    clothes_list.append(clothes3)

    id = int(input())
    search_by_id(clothes_list,id)

    brand = input()
    search_by_brand(clothes_list, brand)

    id = int(input())
    num = int(input())
    sell_clothe_by_id(clothes_list, id, num)
