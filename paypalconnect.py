from paypalserversdk.paypal_serversdk_client import PaypalServersdkClient
from paypalserversdk.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from paypalserversdk.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from paypalserversdk.logging.configuration.api_logging_configuration import LoggingConfiguration
from paypalserversdk.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from paypalserversdk.configuration import Environment
from paypalserversdk.models.order_request import OrderRequest
from paypalserversdk.models.checkout_payment_intent import CheckoutPaymentIntent
from paypalserversdk.models.amount_with_breakdown import AmountWithBreakdown
from paypalserversdk.models.purchase_unit_request import PurchaseUnitRequest
from OrdersController import OrderController
import logging


class PaypalClient:
    client: PaypalServersdkClient
    OrderCon: OrderController

    def __init__(self):
        self.client = PaypalServersdkClient(
            client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
                o_auth_client_id='BAAAB83RyuLrVrzRMCujN4hsCwcMIdg864wn-gop_RD3svGiR-NMozaccjpOo_Tuy_DGMMmtnhKQzW7Q3Q',
                o_auth_client_secret='ECbeRhdssacQiyBeEPME5jqZ-G5UX8Fx-H1bGZNzUSTYojhlyqkG_Xbz9l5TK1h1L91Rk3M_joC6VNai'
            ),
            environment=Environment.SANDBOX,
            logging_configuration=LoggingConfiguration(
                log_level=logging.INFO,
                request_logging_config=RequestLoggingConfiguration(
                    log_body=True
                ),
                response_logging_config=ResponseLoggingConfiguration(
                    log_headers=True
                )
            )
        )

    def addBody(self, OrderR: OrderRequest):
        self.OrderCon = OrderR

    def createorder(self):

        result = self.OrderCon.create_order(self.client)

        return result

    def confirm_order(self):

        result = self.OrderCon.confirm_order(self.client)
        return result
