# Receipt Calculator

def print_receipt(items):
    total = 0
    print("\nReceipt:")
    print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Quantity", "Price", "Total"))
    print("-" * 50)

    for item, (quantity, price) in items.items():
        item_total = quantity * price
        total += item_total
        print("{:<20} {:<10} {:<10} {:<10.2f}".format(item, quantity, price, item_total))

    print("-" * 50)
    print("{:<40} {:<10.2f}".format("Total", total))

def main():
    items = {}
    
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        
        quantity = int(input(f"Enter quantity of {item_name}: "))
        price = float(input(f"Enter price of {item_name}: "))
        
        items[item_name] = (quantity, price)
    
    print_receipt(items)

if __name__ == "__main__":
    main()
