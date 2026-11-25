from paypalserversdk.models.amount_breakdown import AmountBreakdown
from paypalserversdk.models.amount_with_breakdown import AmountWithBreakdown
from paypalserversdk.models.disbursement_mode import DisbursementMode
from paypalserversdk.models.money import Money
from paypalserversdk.models.payee_base import PayeeBase
from paypalserversdk.models.payment_instruction import PaymentInstruction
from paypalserversdk.models.platform_fee import PlatformFee
from paypalserversdk.models.purchase_unit_request import PurchaseUnitRequest
from Classes.PurchaseUnitReqClass import PurchasedUnitReqInfo
import os


def purchasedUnitReq(PurchasedUnitRInf: PurchasedUnitReqInfo):
    purchase_unit_request = PurchaseUnitRequest(
        amount=AmountWithBreakdown(
            currency_code='USD',
            value=PurchasedUnitRInf.amount,
            breakdown=AmountBreakdown(
                item_total=Money(
                    currency_code='USD',
                    value=PurchasedUnitRInf.item
                ),
                shipping=Money(
                    currency_code='USD',
                    value=PurchasedUnitRInf.shipping
                ),
                handling=Money(
                    currency_code='USD',
                    value=PurchasedUnitRInf.handling
                ),
                tax_total=Money(
                    currency_code='USD',
                    value=PurchasedUnitRInf.tax
                ),
                insurance=Money(
                    currency_code='USD',
                    value=PurchasedUnitRInf.insurance
                )
            )
        ),
        reference_id=PurchasedUnitRInf.referenceID,
        payee=PayeeBase(
            email_address=os.environ['PAYPAL_PAYEE_EMAIL']
        ),
        description=PurchasedUnitRInf.description,
        custom_id=PurchasedUnitRInf.customID
    )

    return purchase_unit_request
