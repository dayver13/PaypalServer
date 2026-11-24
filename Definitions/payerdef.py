from paypalserversdk.models.name import Name
from paypalserversdk.models.payer import Payer
from Classes.PayerClass import Payer_Information


def payer_def(payerInfo: Payer_Information):

    payer = Payer(
        email_address=payerInfo.email,
        payer_id=payerInfo.id,
        name=Name(
            given_name=payerInfo.name,
            surname=payerInfo.surname
        )
    )

    return payer
