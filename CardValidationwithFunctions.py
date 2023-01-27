from Assignments.card_validator import lines


#class creditCard:




def calculate_credit_card_number( card_numbers):
        totalEven = 0
        sum_of_odds = 0
        doubled_number = 0

        for i in range(0, len(card_numbers), 2):
            doubled_number = int(card_numbers.__getitem__(i)) * 2
            if doubled_number > 9:
                doubled_number = (doubled_number // 10) + (doubled_number % 10)
            totalEven += doubled_number

        if len(card_numbers) % 2 != 0:
            len(card_numbers) + 1
        else:
            for i in range(1, len(card_numbers) + 1, +2):
                sum_of_odds += int(card_numbers.__getitem__(i))

        sum_of_even_and_odd = totalEven + sum_of_odds

        if sum_of_even_and_odd % 10 == 0:
            card_numbers = "valid"
        else:
            card_numbers = "invalid"
        print(f"Card Status : {card_numbers}")
        lines()

def show_credit_card_type_and_validity(credit_card_number):
        lines()
        if credit_card_number.__getitem__(0) == '5':
            card_type = "Master Card"
            print(f"Credit Card Type: {card_type}")
            print(f"Credit Card Number: {credit_card_number}")
            print(f"Credit Card Length: {len(credit_card_number)}")

        if credit_card_number.__getitem__(0) == '4':
            card_type = "Visa Card"
            print(f"Credit Card Type: {card_type}")
            print(f"Credit Card Number: {credit_card_number}")
            print(f"Credit Card Length: {len(credit_card_number)}")

        if credit_card_number.__getitem__(0) == '3' and '7' == credit_card_number._getitem_(1):
            card_type = "American Express"
            print(f"Credit Card Type: {card_type}")
            print(f"Credit Card Number: {credit_card_number}")
            print(f"Credit Card Length: {len(credit_card_number)}")

        if credit_card_number.__getitem__(0) != '4' and credit_card_number.__getitem__(
        0) != '5' and credit_card_number.__getitem__(0) != '3':

            card_type = 'Invalid'
            print(f"credit Card Type: {card_type}")
            print(f"Credit Card Number: {credit_card_number}")
            print(f"Credit Card Length: {len(credit_card_number)}")
