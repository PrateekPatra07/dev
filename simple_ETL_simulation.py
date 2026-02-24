import csv

input_file = "data.csv"
output_file = "sales_data.csv"

total_amount = 0
total_quantity = 0
valid_rows = 0

try:
    # ---------------- EXTRACT ----------------
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    cleaned_data = []

    # ---------------- TRANSFORM ----------------
    for row in rows:
        try:
            order_id = int(row["order_id"])
            customer = row["customer"]

            # Convert amount and quantity to proper types
            amount = float(row["amount"])
            quantity = int(row["quantity"])

            # Create new column
            total_price = amount * quantity

            cleaned_data.append({
                "order_id": order_id,
                "customer": customer,
                "amount": amount,
                "quantity": quantity,
                "total_price": total_price
            })

            total_amount += total_price
            total_quantity += quantity
            valid_rows += 1

        except (ValueError, TypeError):
            print(f"Skipping invalid row: {row}")

    # ---------------- LOAD ----------------
    with open(output_file, "w", newline="") as file:
        fieldnames = ["order_id", "customer", "amount", "quantity", "total_price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(cleaned_data)

    # ---------------- SUMMARY ----------------
    if valid_rows > 0:
        average_sale = total_amount / valid_rows
        print("\nETL Completed Successfully!")
        print("Valid Rows:", valid_rows)
        print("Total Revenue:", total_amount)
        print("Average Sale:", average_sale)
    else:
        print("No valid data found.")

except FileNotFoundError:
    print("Input file not found!")