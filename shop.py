# Online Shopping Cart System in Python

# Product class - Represents a product available for purchase
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price  # Encapsulation: Price is private to protect direct access
        self.quantity = quantity

    def get_price(self):
        """Return the price of the product."""
        return self._price

    def set_price(self, price):
        """Set a new price, ensuring it is positive."""
        if price > 0:
            self._price = price
        else:
            raise ValueError("Price must be positive.")

    def __str__(self):
        """Display product details."""
        return f"Product: {self.name}, Price: ${self._price}, Quantity: {self.quantity}"


# Cart class - Manages the shopping cart operations
class Cart:
    def __init__(self):
        self.items = {}  # Dictionary to hold products in the cart

    def add_product(self, product, quantity=1):
        """Add a product to the cart or update quantity if it exists."""
        if product.name in self.items:
            self.items[product.name].quantity += quantity
        else:
            if quantity > 0:
                self.items[product.name] = product
                self.items[product.name].quantity = quantity
            else:
                raise ValueError("Quantity must be positive.")

    def update_product(self, product_name, quantity):
        """Update the quantity of a specific product in the cart."""
        if product_name in self.items:
            if quantity > 0:
                self.items[product_name].quantity = quantity
            else:
                self.remove_product(product_name)
        else:
            print("Product not found in cart.")

    def remove_product(self, product_name):
        """Remove a product from the cart by its name."""
        if product_name in self.items:
            del self.items[product_name]
        else:
            print("Product not found in cart.")

    def calculate_total(self):
        """Calculate the total cost of items in the cart."""
        total = sum(item.get_price() * item.quantity for item in self.items.values())
        return total

    def show_cart(self):
        """Display all products in the cart."""
        if self.items:
            for product in self.items.values():
                print(product)
        else:
            print("Your cart is empty.")

    def checkout(self):
        """Proceed to checkout, displaying total and clearing the cart if not empty."""
        if not self.items:
            print("Cannot proceed to checkout. Your cart is empty.")
            return
        total = self.calculate_total()
        print(f"Total amount: ${total}")
        print("Proceeding to checkout...")
        self.items.clear()  # Clear cart after checkout
        print("Thank you for your purchase!")


# User class - Represents a customer managing their shopping cart
class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()  # Each user has a unique cart

    def add_to_cart(self, product, quantity):
        """Add a product to the user's cart."""
        try:
            self.cart.add_product(product, quantity)
            print(f"Added {quantity} of {product.name} to cart.")
        except ValueError as e:
            print(e)

    def update_cart_item(self, product_name, quantity):
        """Update the quantity of a specific product in the cart."""
        self.cart.update_product(product_name, quantity)

    def remove_from_cart(self, product_name):
        """Remove a product from the cart by its name."""
        self.cart.remove_product(product_name)

    def view_cart(self):
        """View the current contents of the cart."""
        print(f"{self.name}'s Cart:")
        self.cart.show_cart()

    def checkout(self):
        """Initiate the checkout process."""
        self.cart.checkout()


# Main program - Demonstrates system functionalities
def main():
    # Sample products available in the store
    product1 = Product("Laptop", 1000, 10)
    product2 = Product("Phone", 500, 20)
    product3 = Product("Headphones", 100, 15)

    # Create a user and simulate shopping actions
    user = User("Alice")

    # Add products to the cart
    user.add_to_cart(product1, 1)
    user.add_to_cart(product2, 2)
    user.add_to_cart(product3, 1)

    # View cart contents
    user.view_cart()

    # Update a product's quantity in the cart
    user.update_cart_item("Phone", 1)
    user.view_cart()

    # Remove a product from the cart
    user.remove_from_cart("Headphones")
    user.view_cart()

    # Complete checkout process
    user.checkout()

    # Attempt to view cart after checkout
    user.view_cart()


# Run the program if this file is executed directly
if __name__ == "__main__":
    main()

