class Food:
    def __init__(self, name, price, ingredients, cuisine):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.rating = 0
        self.total_ratings = 0
        self.num_ratings = 0

    def set_price(self, new_price):
        self.price = new_price

    def add_rating(self, new_rating):
        self.total_ratings += new_rating
        self.num_ratings += 1
        self.rating = self.total_ratings / self.num_ratings

class RestaurantStaff:
    def __init__(self, name):
        self.name = name
        self.foods = []

    def define_food(self):
        num_foods = int(input("How many foods do you want to define? "))
        for _ in range(num_foods):
            name = input("Enter food name: ")
            price = float(input("Enter food price: "))
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            cuisine = input("Enter cuisine type (Iranian/Foreign): ")
            food = Food(name, price, ingredients, cuisine)
            self.foods.append(food)
            print(f"Added {food.name} with price {food.price}, ingredients {food.ingredients}, and cuisine {food.cuisine}")
        return self.foods

    def update_food_price(self):
        food_name = input("Enter food name to update: ")
        new_price = float(input("Enter new price: "))
        for food in self.foods:
            if food.name == food_name:
                food.set_price(new_price)
                print(f"Updated price for {food.name} to {new_price}")
                return
        print("Food not found!")

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.cuisine_preference = ""

    def set_cuisine_preference(self):
        self.cuisine_preference = input("Do you prefer Iranian or Foreign cuisine? ")

    def order_food(self, staff):
        food_name = input("Enter food name to order: ")
        for food in staff.foods:
            if food.name == food_name and food.cuisine == self.cuisine_preference:
                print(f"{self.name} ordered {food.name}")
                self.orders.append(food)
                return
        print("Food not found or doesn't match your cuisine preference!")

    def rate_food(self):
        food_name = input("Enter food name to rate: ")
        rating = float(input("Enter your rating (1-5): "))
        for food in self.orders:
            if food.name == food_name:
                food.add_rating(rating)
                print(f"{self.name} rated {food.name} with a rating of {rating}")
                print(f"New average rating: {food.rating}")
                return
        print("Food not found in your orders!")

    def ask_for_invoice(self):
        response = input(f"{self.name}, do you want an invoice for your order? (yes/no): ")
        if response.lower() == 'yes':
            print("Generating invoice...")
            self.print_invoice()

    def print_invoice(self):
        print(f"Invoice for {self.name}:")
        total_price = 0
        for food in self.orders:
            print(f"{food.name}: ${food.price}")
            total_price += food.price
        print(f"Total: ${total_price}")

# Sample usage
staff = RestaurantStaff("mehdi")
staff.define_food()

customer = Customer("reza")
customer.set_cuisine_preference()
customer.order_food(staff)
customer.rate_food()
customer.ask_for_invoice()
