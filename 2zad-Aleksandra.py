class Car:

    def __init__(self, car_brand, car_model, car_price, car_color, manifacture_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_price = car_price
        self.car_color = car_color
        self.manifacture_year = manifacture_year

    def display_info(self):
        print(f"{self.car_brand}-{self.car_model}-{self.car_price}-{self.car_color}-{self.manifacture_year}")

def sort_price(car_list, car_price):
    sorted_car_list = sorted(car_list, key=lambda car:car.price, reverse=True)
    for car in sorted_car_list:
        car.display_info()

def list_by_brand(car_list, car_brand):
    for car in car_list:
        if car.car_brand == car_brand:
            car.display_info()

def search_color(car_list, car_color):
    list_same_color = []
    for car in car_list:
        if car.car_color == car_color:
            list_same_color.append(car)
    sorted_list_same_color = sorted(list_same_color, key=lambda car:car.price, reverse = True)
    # sorted_list_same_color = sort(reverse=True)
    result_car = sorted_list_same_color[0]
    return result_car

def newest_car(car_list, manifacture_year):
    newest_car_list = []
    for car in car_list:
        if car.manifacture_year == 2022:
            newest_car_list.append(car)
    return newest_car_list

if __name__ == "__main__":
    car_list = []

    car1 = Car("BMW", "E90", 11000, "blue", 2006)
    car2 = Car("BMW", "E40", 9000, "black", 2003)
    car3 = Car("BMW", "E90", 11000, "blue", 2006)
    car4 = Car("BMW", "E90", 11000, "blue", 2006)
    car5 = Car("BMW", "E90", 11000, "blue", 2006)
    car6 = Car("BMW", "E90", 11000, "blue", 2006)
    car7 = Car("BMW", "E90", 11000, "blue", 2006)

    car_list.append(car1)
    car_list.append(car2)
    car_list.append(car3)
    car_list.append(car4)
    car_list.append(car5)
    car_list.append(car6)
    car_list.append(car7)

    search_color(car_list, "blue")



