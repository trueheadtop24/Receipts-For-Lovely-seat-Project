# Receipts-For-Lovely-seat-Project
creating a receipt in Python
Receipts for Lovely Loveseats
We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.

In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

Please note: Projects do not run tests against your code. This experience is more open to your interpretation and gives you the freedom to explore. Remember that all variables must be declared before they are referenced in your code.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Tasks
20/20 complete
Mark the tasks as complete by checking them off
Adding In The Catalog

Let’s add in our first item, the Lovely Loveseat that is the store’s namesake. Create a variable called lovely_loveseat_description and assign to it the following string:

Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.

Copy to Clipboard


Great, now let’s create a price for the loveseat. Create a variable lovely_loveseat_price and set it equal to 254.00.


Let’s extend our inventory with another characteristic piece of furniture! Create a variable called stylish_settee_description and assign to it the following string:

Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.

Copy to Clipboard


Now let’s set the price for our Stylish Settee. Create a variable stylish_settee_price and assign it the value of 180.50.


Fantastic, we just need one more item before we’re ready for business. Create a new variable called luxurious_lamp_description and assign it the following:

Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.

Copy to Clipboard


Let’s set the price for this item. Create a variable called luxurious_lamp_price and set it equal to 52.15.


In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well.

Define the variable sales_tax and set it equal to .088. That’s 8.8%.

Our First Customer

Our first customer is making their purchase! Let’s keep a running tally of their expenses by defining a variable called customer_one_total. Since they haven’t purchased anything yet, let’s set that variable equal to 0 for now.


We should also keep a list of the descriptions of things they’re purchasing. Create a variable called customer_one_itemization and set that equal to the empty string "". We’ll tack on the descriptions to this as they make their purchases.


Our customer has decided they are going to purchase our Lovely Loveseat! Add the price to customer_one_total.


Let’s start keeping track of the items our customer purchased. Add the description of the Lovely Loveseat to customer_one_itemization.


Our customer has also decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.


Let’s keep the itemization up-to-date and add the description of the Luxurious Lamp to our itemization.


They’re ready to check out! Let’s begin by calculating sales tax. Create a variable called customer_one_tax and set it equal to customer_one_total times sales_tax.


Add the sales tax to the customer’s total cost.


Let’s start printing up their receipt! Begin by printing out the heading for their itemization. Print the phrase "Customer One Items:".


Print customer_one_itemization.


Now add a heading for their total cost: Print out "Customer One Total:"


Now print out their total! Our first customer now has a receipt for the things they purchased.


Congratulations! We created our catalog and served our first customer. We used our knowledge of strings and numbers to create and update variables. We were able to print out an itemized list and a total cost for our customer. Lovely!
