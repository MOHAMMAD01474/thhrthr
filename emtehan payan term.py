class Restaurant:
    def __init__(self):
        self.menu = {}
        self.total_sales = 0 

    def add_food(self, name, price):
        self.menu[name] = price
        print(f"Added {name} for {price} Hezar Toman")

    def show_menu(self):
        for name, price in self.menu.items():
            print(f"{name}: {price} Hezar Toman")

    def order_food(self, name):
        if name in self.menu:
            print(f"Ordered {name} for {self.menu[name]} Hezar Toman")
            self.total_sales += self.menu[name]  
        else:
            print(f"Sorry, {name} is not available")

    def show_total_sales(self):
        print(f"Total sales: {self.total_sales} Hezar Toman") 


def main():
    restaurant = Restaurant()
    password = "1743784554"  

    while True:
        user_type = input("Are you a customer or staff? (Enter 'customer' or 'staff'): ").strip().lower()
        
        if user_type == "customer":
            print("\nMenu:")
            restaurant.show_menu()
            food_item = input("Enter the food item you want to order: ").strip()
            restaurant.order_food(food_item)
            break
        
        elif user_type == "staff":
            entered_password = input("Enter the staff password: ").strip()
            if entered_password == password:
                while True:
                    action = input("Do you want to add a new food item or show the menu? (Enter 'add' or 'show'): ").strip().lower()
                    if action == "add":
                        food_name = input("Enter the name of the food: ").strip()
                        food_price = float(input("Enter the price of the food: ").strip())
                        restaurant.add_food(food_name, food_price)
                    elif action == "show":
                        print("\nMenu:")
                        restaurant.show_menu()
                    else:
                        print("Invalid action. Please enter 'add' or 'show'.")
                    
                    another_action = input("Do you want to perform another action? (yes/no): ").strip().lower()
                    if another_action != "yes":
                        break
            else:
                print("Incorrect password. Access denied.")
        else:
            print("Invalid input. Please enter 'customer' or 'staff'.")

    print("\nTotal Sales:")
    restaurant.show_total_sales()

if __name__ == "__main__":
    main()
