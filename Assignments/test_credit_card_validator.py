from unittest import TestCase

from Assignments.credit_card import CreditCard

from Assignments.Credit_Card_Type import CreditCardType


class CreditCardValidatorTest(TestCase):

    def test_that_second_from_right_to_left_are_doubled(self):
        credit_card: CreditCard = CreditCard("4388576018402626")
        credit_card.sum_the_product_of_second_digit()
        self.assertEqual(37, credit_card.get_sum_of_second_doubled_number())

    def test_sum_of_all_numbers_in_odd_position(self):
        credit_card: CreditCard = CreditCard("4388576018402626")
        credit_card.sum_of_all_numbers_in_odd_places()
        self.assertEqual(38, credit_card.get_sum_of_all_numbers_in_odd_places())

    def test_invalid_card_length_throws_exemption(self):
        credit_card: CreditCard = CreditCard("43885760184026266666")
        credit_card.valid_card_number_length()
        with self.assertRaises(ValueError):
            credit_card.valid_card_number_length()

    def test_card_validity(self):
        credit_card: CreditCard = CreditCard("4388576018402626")
        self.assertTrue(credit_card.is_valid())

    def test_credit_card_is_of_four_types_bases_the_digits_of_the_card_number(self):
        credit_card: CreditCard = CreditCard("4388576018402626")
        credit_card.set_card_type()
        self.assertEqual(CreditCardType.VISA_CARD, credit_card.get_credit_card_type())

    def test_string_representation_of_card_validity(self):
        credit_card: CreditCard = CreditCard("5591130100773414")
        credit_card.valid_card_number_length()
        credit_card.sum_the_product_of_second_digit()
        credit_card.sum_of_all_numbers_in_odd_places()
        credit_card.set_card_type()
        expected: str = """
        ==============================
        Credit Card Type: MASTER_CARD
        Credit Card Number: 5591130100773414
        Credit Card Length: 16
        Credit Card Validity: Valid
        ==============================
        """
        self.assertEqual(expected, credit_card.__str__())
