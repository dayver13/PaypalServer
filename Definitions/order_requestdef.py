from paypalserversdk.models.order_request import OrderRequest
from paypalserversdk.models.checkout_payment_intent import CheckoutPaymentIntent
from paypalserversdk.models.processing_instruction import ProcessingInstruction
from paypalserversdk.models.order_application_context import OrderApplicationContext
from paypalserversdk.models.order_application_context_landing_page import OrderApplicationContextLandingPage
from paypalserversdk.models.order_application_context_shipping_preference import OrderApplicationContextShippingPreference
from paypalserversdk.models.order_application_context_user_action import OrderApplicationContextUserAction
from Definitions.payerdef import payer_def
from Definitions.purchasedUnitRequestdef import purchasedUnitReq
from Classes.PurchaseUnitReqClass import PurchasedUnitReqInfo
from Classes.PayerClass import Payer_Information
from Classes.CardClass import Card_information
from Definitions.paymentsourcedef import payment_source


def order_req(Payer: Payer_Information, Card: Card_information, PurchasedUnitR: PurchasedUnitReqInfo):
    intent = CheckoutPaymentIntent.CAPTURE
    purchase_units = [purchasedUnitReq(PurchasedUnitR)]
    payer = payer_def(Payer)
    payment_sour = payment_source(Card)
    application_context = OrderApplicationContext(
        brand_name='brand_name8',
        locale='es-CR',
        landing_page=OrderApplicationContextLandingPage.BILLING,
        user_action=OrderApplicationContextUserAction.CONTINUE
    )
    order_requt = OrderRequest(intent=intent, purchase_units=purchase_units,
                               payment_source=payment_sour, payer=payer, application_context=application_context)

    return order_requt
