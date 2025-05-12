import sys

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("\n--- Product Inventory ---")
    print("{:<20} {:<10} {:<15} {:<15}".format("Product Name", "Quantity", "Price per Unit", "Category"))
    print("-" * 60)
    for item in inventory:
        print("{:<20} {:<10} {:<15.2f} {:<15}".format(
            item["product_name"], item["quantity"], item["price_per_unit"], item["category"]
        ))

def search_item(inventory, search_term, search_field):
    results = [
        item for item in inventory
        if search_term.lower() in item[search_field].lower()
    ]
    return results

def update_item(inventory, item_name):
    for item in inventory:
        if item["product_name"].lower() == item_name.lower():
            print(f"Found product: {item['product_name']}")
            while True:
                try:
                    choice = input("Update quantity (q) or price (p)? (q/p): ").lower()
                    if choice == 'q':
                        new_quantity = int(input("Enter new quantity: "))
                        if new_quantity < 0:
                            raise ValueError("Quantity cannot be negative.")
                        item["quantity"] = new_quantity
                        print("Quantity updated.")
                        break
                    elif choice == 'p':
                        new_price = float(input("Enter new price: "))
                        if new_price < 0:
                            raise ValueError("Price cannot be negative.")
                        item["price_per_unit"] = new_price
                        print("Price updated.")
                        break
                    else:
                        print("Invalid choice. Enter 'q' or 'p'.")
                except ValueError as e:
                    print(f"Error: {e}")
            return
    print(f"Product with name '{item_name}' not found.")

def analyze_inventory(inventory):
    category_totals = {}
    for item in inventory:
        category = item["category"]
        total_value = item["quantity"] * item["price_per_unit"]
        if category in category_totals:
            category_totals[category] += total_value
        else:
            category_totals[category] = total_value

    print("\n--- Inventory Analysis ---")
    print("Total value of products by category:")
    for category, total in category_totals.items():
        print(f"{category}: {total:.2f} UAH")

    most_valuable_category = max(category_totals, key=category_totals.get)
    print(f"\nCategory with the highest total value: {most_valuable_category} "
          f"({category_totals[most_valuable_category]:.2f} UAH)")

    try:
        low_stock_threshold = int(input("Enter the minimum quantity for checking: "))
        if low_stock_threshold < 0:
            raise ValueError("Threshold must be a non-negative number.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    low_stock_items = [
        item for item in inventory if item["quantity"] < low_stock_threshold
    ]
    if low_stock_items:
        print(f"\nProducts with quantity below {low_stock_threshold}:")
        for item in low_stock_items:
            print(f"{item['product_name']} ({item['quantity']} pcs)")
    else:
        print(f"\nAll products have sufficient quantity (more than {low_stock_threshold} pcs).")

def main():
    inventory = [
        {"product_name": "T-Shirt", "quantity": 50, "price_per_unit": 250.00, "category": "Clothing"},
        {"product_name": "Jeans", "quantity": 30, "price_per_unit": 800.00, "category": "Clothing"},
        {"product_name": "Sneakers", "quantity": 20, "price_per_unit": 1200.00, "category": "Footwear"},
        {"product_name": "Sweatshirt", "quantity": 40, "price_per_unit": 600.00, "category": "Clothing"},
        {"product_name": "Smartphone", "quantity": 10, "price_per_unit": 25000.00, "category": "Electronics"},
        {"product_name": "Headphones", "quantity": 25, "price_per_unit": 2000.00, "category": "Electronics"},
        {"product_name": "Keds", "quantity": 15, "price_per_unit": 900.00, "category": "Footwear"}
    ]

    while True:
        print("\n--- Menu ---")
        print("1. View Inventory")
        print("2. Search Product")
        print("3. Update Product")
        print("4. Analyze Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
            if choice == 1:
                display_inventory(inventory)
            elif choice == 2:
                while True:
                    search_field = input("Search by name (n) or category (c)? (n/c): ").lower()
                    if search_field == 'n':
                        search_term = input("Enter product name to search: ")
                        results = search_item(inventory, search_term, "product_name")
                        break
                    elif search_field == 'c':
                        search_term = input("Enter product category to search: ")
                        results = search_item(inventory, search_term, "category")
                        break
                    else:
                        print("Invalid field choice. Enter 'n' or 'c'.")
                if results:
                    display_inventory(results)
                else:
                    print("Products not found.")
            elif choice == 3:
                item_name = input("Enter the name of the product to update: ")
                update_item(inventory, item_name)
            elif choice == 4:
                analyze_inventory(inventory)
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()