lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxorious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxorious_lamp_price = 52.15

sales_tax = .088 

customer_one_total = 0 
customer_one_itemization = ""

customer_one_total + lovely_loveseat_price
customer_one_total += luxorious_lamp_price

customer_one_itemization = luxorious_lamp_description
customer_one_itemization = lovely_loveseat_description + " " + luxorious_lamp_description
customer_one_tax = (customer_one_total * sales_tax)

customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print(customer_one_total)
