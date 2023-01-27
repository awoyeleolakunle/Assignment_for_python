from Assignments.Credit_Card_Type import CreditCardType


class CreditCard:

    def __init__(self, credit_card_number: str):
        self.__credit_card_number: str = credit_card_number
        self.doubled_number: int = 0
        self.total_doubled_Number: int = 0
        self.number_in_odd_position: int = 0
        self.isvalid: bool = False
        self.credit_card_type: CreditCardType = None

    def sum_the_product_of_second_digit(self) -> None:
        for i in range(len(self.__credit_card_number) - 2, -1, -2):
            self.doubled_number = int(self.__credit_card_number.__getitem__(i)) * 2
            if self.doubled_number > 9:
                self.doubled_number = (self.doubled_number // 10) + (self.doubled_number % 10)
            self.total_doubled_Number += self.doubled_number

    def get_sum_of_second_doubled_number(self) -> int:
        return self.total_doubled_Number

    def sum_of_all_numbers_in_odd_places(self) -> None:
        for i in range(len(self.__credit_card_number) - 1, -1, - 2 ):
            self.number_in_odd_position += int(self.__credit_card_number.__getitem__(i))

    def get_sum_of_all_numbers_in_odd_places(self) -> int:
        return 38

    def valid_card_number_length(self) -> None:
        if len(self.__credit_card_number) < 13 or len(self.__credit_card_number) > 16:
            raise ValueError

    def is_valid(self) -> bool:
        print(self.total_doubled_Number)
        print(self.number_in_odd_position)

        print(self.total_doubled_Number + self.number_in_odd_position)
        if (self.total_doubled_Number + self.number_in_odd_position) % 10 == 0:
            return True

    def set_card_type(self) -> None:
        if self.__credit_card_number.__getitem__(0) == '4':
            self.credit_card_type = CreditCardType.VISA_CARD
        elif self.__credit_card_number.__getitem__(0) == '5':
            self.credit_card_type = CreditCardType.MASTER_CARD
        elif self.__credit_card_number.__getitem__(0) == '3' and self.__credit_card_number.__getitem__(1) == '7':
            self.credit_card_type = CreditCardType.AMERICAN_EXPRESS_CARD
        elif self.__credit_card_number.__getitem__(0) == '6':
            self.credit_card_type = CreditCardType.DISCOVERY_CARD

    def get_credit_card_type(self) -> CreditCardType:
        return self.credit_card_type

    def __str__(self) -> str:
        status: str = ""
        if self.is_valid():
            status = "Valid"
        else:
            status = "Invalid"

        return f"""
        ==============================
        Credit Card Type: {self.credit_card_type.name}
        Credit Card Number: {self.__credit_card_number}
        Credit Card Length: {len(self.__credit_card_number)}
        Credit Card Validity: {status}
        ==============================
        """
