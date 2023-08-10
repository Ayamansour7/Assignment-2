#Question 7
# Define a class called Item
class Item:
    def __init__(self, barcode, name, price):
        self.barcode = barcode   # Item barcode
        self.name = name   # Item name
        self.price = price   # Item price

# Define a function to create a receipt
def create_receipt():
    items = [
        Item("001", "Item 1", 10),   # Create Item objects with barcodes, names, and prices
        Item("002", "Item 2", 15),
        Item("003", "Item 3", 20)
    ]

    receipt = []   # List to store receipt items
    total_amount = 0   # Variable to store the total amount

    while True:
        start_new_receipt = input("Start a new receipt? (yes/no): ")   # Prompt the user to start a new receipt

        if start_new_receipt.lower() == "no":   # If the user enters 'no', break out of the loop
            break

        if start_new_receipt.lower() != "yes":   # If the user enters neither 'yes' nor 'no', print an error message and continue to the next iteration
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

        receipt_items = []   # List to store items in the current receipt

        while True:
            barcode = input("Enter the item barcode: ")   # Prompt the user to enter the item barcode
            quantity = int(input("Enter the quantity purchased: "))   # Prompt the user to enter the quantity of the item purchased

            item = next((item for item in items if item.barcode == barcode), None)   # Find the item in the items list that matches the entered barcode

            if item is None:   # If no item is found with the entered barcode, print an error message and continue to the next iteration
                print("Invalid barcode. Please enter a valid barcode.")
                continue

            total_cost = item.price * quantity   # Calculate the total cost of the item(s) purchased
            receipt_items.append((item, quantity, total_cost))   # Add the item, quantity, and total cost as a tuple to the receipt_items list

            add_another_item = input("Add another item? (yes/no): ")   # Prompt the user to add another item to the current receipt

            if add_another_item.lower() == "no":   # If the user enters 'no', break out of the inner loop
                break

            if add_another_item.lower() != "yes":   # If the user enters neither 'yes' nor 'no', print an error message and continue to the next iteration
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue

        receipt.extend(receipt_items)   # Add the items in the current receipt to the main receipt list
        total_amount += sum(total_cost for _, _, total_cost in receipt_items)   # Update the total amount by summing the total costs of the current receipt items

        print("Receipt:")   # Print the current receipt
        for item, quantity, total_cost in receipt_items:
            print(f"{item.name} - Quantity: {quantity} - Total Cost: {total_cost}")

        print(f"Total Amount: {total_amount}")   # Print the total amount of the receipt
        print()

    return receipt   # Return the final receipt


# Example usage
receipt = create_receipt()   # Call the create_receipt() function to create a receipt
