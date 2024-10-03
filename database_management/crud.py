# crud.py

from database import get_session
from models import Customer, Product, Order, OrderItem

# Create new customers, products, and orders
def create_customer(name:str, email:str) -> None:
    session = get_session()
    new_customer = Customer(name=name, email=email)
    session.add(new_customer)
    session.commit()
    session.close()

def create_product(name:str, price:float, stock_quantity:int) -> None:
    session = get_session()
    new_product = Product(name=name, price=price, stock_quantity=stock_quantity)
    session.add(new_product)
    session.commit()
    session.close()

def create_order(customer_id:int, product_quantities:dict[str:int]) -> None:
    session = get_session()  # Use the session from get_session
    # Fetch products to match names with IDs
    products = {product.name: product for product in session.query(Product).all()}
    
    # Create the order
    order = Order(customer_id=customer_id)
    session.add(order)
    session.commit()  # Commit first to generate order ID
    
    # Create order items based on product names
    for product_name, quantity in product_quantities.items():
        if product_name in products:
            product = products[product_name]
            order_item = OrderItem(order_id=order.id, product_id=product.id, quantity=quantity)
            session.add(order_item)
        else:
            print(f"Product '{product_name}' not found!")
    
    session.commit()
    session.close()  # Close the session

# Read customers, products, and orders
def get_customers():
    session = get_session()
    customers = session.query(Customer).all()
    session.close()
    return customers

def get_products():
    session = get_session()
    products = session.query(Product).all()
    session.close()
    return products

def get_orders():
    session = get_session()
    orders = session.query(Order).all()
    session.close()
    return orders

# Update a product's price
def update_product_price(product_id:int, new_price:float) -> None:
    session = get_session()
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        product.price = new_price
        session.commit()
    session.close()

# Delete a customer
def delete_customer(customer_id:int) -> None:
    session = get_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
    session.close()
