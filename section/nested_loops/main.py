produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

for grocery in groceries:
    for item in grocery:
        print(f"Item name: {item}")