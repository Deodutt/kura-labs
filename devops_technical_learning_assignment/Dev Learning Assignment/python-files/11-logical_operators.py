# is_income_high = True
is_good_credit = True
is_criminal_record = False

# if is_income_high and is_good_credit:
#     print("Eligible for loan")

# if is_income_high or is_good_credit:
#     print("Eligible for loan")
# else:
#     print("Sorry you are not eligible for a loan")


# if application has good credit and doesnt have a criminal record
if is_good_credit and not is_criminal_record:
    print("Eligible for loan")
else:
    print("Sorry you are not eligible for a loan")