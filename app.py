import sqlite3
from functions import add_seasonal_flavor
from functions import add_allergen
from functions import add_ingredient
from functions import add_customer_suggestion 
from functions import add_seasonal_flavor
from functions import add_to_cart 
from functions import allergen_exists
from functions import search_flavors
from functions import filter_flavors_by_season


def main_menu():
    while True:
        print("Ice Cream Parlor Cafe")
        print("1. Add Seasonal Flavor")
        print("2. Add Ingredient")
        print("3. Add Customer Suggestion")
        print("4. Add Allergen")
        print("5. Add to Cart")
        print("6. Search Flavors")
        print("7. Filter Flavors by Season")
        print("8. View Cart")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter flavor name: ")
            ingredients = input("Enter ingredients (comma separated): ")
            season = input("Enter season: ")
            add_seasonal_flavor(name, ingredients, season)
        elif choice == '2':
            name = input("Enter ingredient name: ")
            add_ingredient(name)
        elif choice == '3':
            flavor_name = input("Enter suggested flavor name: ")
            suggested_by = input("Enter your name: ")
            allergens = input("Enter allergens (comma separated, if any): ")
            add_customer_suggestion(flavor_name, suggested_by, allergens)
        elif choice == '4':
            name = input("Enter allergen name: ")
            if allergen_exists(name):
                print("Allergen already exists.")
            else:
                add_allergen(name)
        elif choice == '5':
            flavor_id = int(input("Enter flavor ID to add to cart: "))
            add_to_cart(flavor_id)
        elif choice == '6':
            keyword = input("Enter keyword to search flavors: ")
            results = search_flavors(keyword)
            for row in results:
                print(row)
        elif choice == '7':
            season = input("Enter season to filter flavors: ")
            results = filter_flavors_by_season(season)
            for row in results:
                print(row)
        elif choice == '8':
            conn = sqlite3.connect('ice_cream_parlor.db')
            c = conn.cursor()
            c.execute('SELECT * FROM cart')
            cart_items = c.fetchall()
            conn.close()
            for item in cart_items:
                print(item)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
