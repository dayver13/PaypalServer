from paypalserversdk.models.address import Address
from paypalserversdk.models.card_request import CardRequest
from Classes.CardClass import Card_information


def card(PaymentCard: Card_information):
    card_request = CardRequest(
        name=PaymentCard.name,
        number=PaymentCard.number,
        expiry=PaymentCard.expiry,
        security_code=PaymentCard.security,
        billing_address=Address(
            country_code=PaymentCard.address.country_code,
            address_line_1=PaymentCard.address.address_line_1,
            address_line_2=PaymentCard.address.address_line_2,
            postal_code=PaymentCard.address.postal_code
        )
    )

    return card_request
