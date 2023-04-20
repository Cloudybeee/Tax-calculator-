income= int(input("Enter your single income: "))
deduct=13850
if income <= 11000:
    tax= income *.10 - deduct
elif income < 44725 :
    tax= income * .12 -deduct
elif income < 95375 :
    tax = income * .22 - deduct
elif income< 182100 :
    tax = income * .32 -deduct
elif income < 231250:
    tax = income * .35 -deduct
else :    tax = income * .37
if tax > 0 :
    print ("your tax is", tax )
if tax <0 :
    print ("your tax return is ", abs(tax))