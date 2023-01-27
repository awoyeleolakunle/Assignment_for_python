from enum import Enum


class CreditCardType(Enum):
    VISA_CARD: str = '4'
    MASTER_CARD: str = '5'
    AMERICAN_EXPRESS_CARD: str = '37'
    DISCOVERY_CARD: str = '6'

    def __init__(self, content: str):
        self.content = content
