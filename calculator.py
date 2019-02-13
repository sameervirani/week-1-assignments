#enter total_amount
#enter tip_amount
#create function to calculate tip and will print tip amount for user

total = float(input('Enter the total amount'))
tip_percentage = (input('Enter the tip percentage amount (whole number)'))
tip_percentage = (tip_percentage)/100
print(total*tip_percentage)
