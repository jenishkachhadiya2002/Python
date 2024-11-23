class StockManagement:
    def __init__(self):
        self.stock = {}

    def add_item(self, item_name, quantity, price):
        """Add a new item or update an existing item in the stock."""
        if item_name in self.stock:
            self.stock[item_name]['quantity'] += quantity
        else:
            self.stock[item_name] = {'quantity': quantity, 'price': price}
        print(f"Item '{item_name}' added/updated successfully.")

    def update_stock(self, item_name, quantity):
        """Update the stock of an existing item."""
        if item_name in self.stock:
            self.stock[item_name]['quantity'] += quantity
            print(f"Stock for '{item_name}' updated successfully.")
        else:
            print(f"Item '{item_name}' not found in stock.")

    def view_stock(self):
        """Display the current stock."""
        if not self.stock:
            print("No items in stock.")
        else:
            print("Current stock:")
            for item, details in self.stock.items():
                print(f"{item} - Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

    def check_availability(self, item_name, quantity):
        """Check if sufficient stock is available for a purchase order."""
        if item_name in self.stock:
            if self.stock[item_name]['quantity'] >= quantity:
                print(f"Sufficient stock available for '{item_name}'.")
            else:
                print(f"Not enough stock for '{item_name}'. Available: {self.stock[item_name]['quantity']}")
        else:
            print(f"Item '{item_name}' not found in stock.")

    def purchase_item(self, item_name, quantity):
        """Process an order and decrease stock accordingly."""
        if item_name in self.stock:
            if self.stock[item_name]['quantity'] >= quantity:
                self.stock[item_name]['quantity'] -= quantity
                total_cost = self.stock[item_name]['price'] * quantity
                print(f"Purchased {quantity} of '{item_name}'. Total cost: ${total_cost:.2f}")
            else:
                print(f"Not enough stock for '{item_name}'. Available: {self.stock[item_name]['quantity']}")
        else:
            print(f"Item '{item_name}' not found in stock.")


# Example usage
def main():
    stock_manager = StockManagement()

    # Adding some initial stock items
    stock_manager.add_item('Apple', 50, 0.5)
    stock_manager.add_item('Banana', 30, 0.3)
    stock_manager.add_item('Orange', 20, 0.8)

    # View current stock
    stock_manager.view_stock()

    # Update stock for an item
    stock_manager.update_stock('Apple', 20)

    # Check stock availability before making a purchase
    stock_manager.check_availability('Banana', 15)

    # Make a purchase
    stock_manager.purchase_item('Apple', 10)

    # View stock after purchase
    stock_manager.view_stock()

if __name__ == "__main__":
    main()
