# Credit_card_validation

# 1.delete_dashes_between

card_number = input("Enter your credit card #: ")
card_number = card_number.replace("-","")

# 2.Add_alldigits-in-the-odd-places
sum_even = 0
sum_odd = 0
for x in card_number [::2]:
    sum_odd += int(x)
# 3.Double-every-seconddigit-fromright2left
for x in card_number [1::2]:
    x = int(x)*2
    if x>= 10:
        sum_even += 1 + (x % 10)
    else:
        sum_even += x
# 4. sum-the-total-of2and3
total = sum_odd + sum_even

# 5.If-the-total-is-divisable-by10-creditcard-isvalid
if total % 10 ==0:
    print("VALID")
else:
    print("INVALID")
