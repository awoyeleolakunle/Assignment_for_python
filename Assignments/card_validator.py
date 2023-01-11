totalEven = 0
sum_of_odds = 0
doubled_number = 0
card_numbers = input("enter your credit card number ")

if len(card_numbers)>=13 and len(card_numbers)<=16:

    for i in range(0, len(card_numbers), 2):
        doubled_number = int(card_numbers.__getitem__(i))*2
        if doubled_number > 9:
            doubled_number = (doubled_number//10) + (doubled_number % 10)
        totalEven += doubled_number

    if len(card_numbers) % 2!=0:
        len(card_numbers)+1
    else:
        for i in range(1, len(card_numbers)+1,+2):
            sum_of_odds+= int(card_numbers.__getitem__(i))

    sum_of_even_and_odd = totalEven + sum_of_odds

else:
    print("please enter a valid number between 13 and 16")


def lines():
    print("****************************************")

lines()
if card_numbers.__getitem__(0) == "4" and sum_of_even_and_odd % 10 == 0:
    print("**Credit card Type :  VISA CARD" "\n""**Credit Card Number :", int(card_numbers),"\n"
    '**Credit card digit length',len(card_numbers),"\n""**Credit Card Validity Status : Valid")
    lines()
elif card_numbers.__getitem__(0) == "4":
    print("**Credit card Type :  VISA CARD" "\n""**Credit Card Number :", int(card_numbers),"\n"
    '**Credit card digit length',len(card_numbers),"\n""**Credit Card Validity Status : invalid")
    lines()
if card_numbers.__getitem__(0) == "5" and sum_of_even_and_odd % 10 == 0:
    print("**Credit card Type :  Master CARD" "\n""**Credit Card Number :", int(card_numbers),"\n"
    '**Credit card digit length',len(card_numbers),"\n""**Credit Card Validity Status : Valid")
    lines()
elif card_numbers.__getitem__(0) == "5":
    print("**Credit card Type :  Master CARD" "\n""**Credit Card Number :", int(card_numbers),"\n"
    '**Credit card digit length',len(card_numbers),"\n""**Credit Card Validity Status : invalid")
    lines()
if card_numbers.__getitem__(0) == "3" and card_numbers.__getitem__(1)=="7" and sum_of_even_and_odd % 10 == 0:
    print("**Credit card Type :  AmericanExpress CARD" "\n""**Credit Card Number :", int(card_numbers),"\n"
    '**Credit card digit length',len(card_numbers),"\n""**Credit Card Validity Status : Valid")
    lines()
elif card_numbers.__getitem__(0) == "3" and card_numbers.__getitem__(1)=="7":
    print("**Credit card Type :  AmericanExpress CARD" "\n""**Credit Card Number :", int(card_numbers),"\n"
    '**Credit card digit length',len(card_numbers),"\n""**Credit Card Validity Status : invalid")
    lines()



