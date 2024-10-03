# main.py

from crud import create_customer, create_product, create_order, get_customers, get_products, get_orders, update_product_price, delete_customer

def create_customer_interaction():
    """Prompts user to create a new customer."""
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    create_customer(name, email)
    print(f"Customer '{name}' created successfully!\n")


def create_product_interaction():
    """Prompts user to create a new product."""
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock_quantity = int(input("Enter product stock quantity: "))
    create_product(name, price, stock_quantity)
    print(f"Product '{name}' created successfully!\n")


def create_order_interaction():
    """Prompts user to create a new order."""
    customer_id = int(input("Enter customer ID to create order for: "))
    product_quantities = {}
    
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity for {product_name}: "))
        product_quantities[product_name] = quantity

    try:
        create_order(customer_id, product_quantities)
        print(f"Order created for customer ID {customer_id}.\n")
    except Exception as e:
        print(f"Failed to create order: {e}")


def main():
    while True:
        print("=== Grocery Store Management ===")
        print("1. Create Customer")
        print("2. Create Product")
        print("3. Create Order")
        print("4. View Customers")
        print("5. View Products")
        print("6. View Orders")
        print("7. Update Product Price")
        print("8. Delete Customer")
        print("9. Exit")

        choice = input("Select an option (1-9): ")

        if choice == '1':
            create_customer_interaction()
        elif choice == '2':
            create_product_interaction()
        elif choice == '3':
            create_order_interaction()
        elif choice == '4':
            print("Customers:", get_customers())
        elif choice == '5':
            print("Products:", get_products())
        elif choice == '6':
            print("Orders:", get_orders())
        elif choice == '7':
            product_id = int(input("Enter product ID to update price: "))
            new_price = float(input("Enter new price: "))
            update_product_price(product_id, new_price)
            print("Product price updated successfully!\n")
        elif choice == '8':
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)
            print("Customer deleted successfully!\n")
        elif choice == '9':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
