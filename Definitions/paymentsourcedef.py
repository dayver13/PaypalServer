from paypalserversdk.models.payment_source import PaymentSource
from Definitions.card import card
from Classes.CardClass import Card_information


def payment_source(CardInf: Card_information):
    payment_card = card(CardInf)
    payment_source = PaymentSource(payment_card)
    return payment_source
