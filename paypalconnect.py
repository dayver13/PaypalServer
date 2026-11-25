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
import os
from dotenv import load_dotenv

load_dotenv()


class PaypalClient:
    client: PaypalServersdkClient
    OrderCon: OrderController

    def __init__(self):
        self.client = PaypalServersdkClient(
            client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
                o_auth_client_id=os.environ['PAYPAL_CLIENT_ID'],
                o_auth_client_secret=os.environ['PAYPAL_CLIENT_SECRET']
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
        OrderC = OrderController()
        self.OrderCon = OrderC
        self.OrderCon.addbody(OrderR)

    def createorder(self):

        result = self.OrderCon.create_order(self.client)

        return result

    def confirm_order(self):

        result = self.OrderCon.confirm_order(self.client)
        return result
