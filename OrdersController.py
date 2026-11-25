from paypalserversdk.models.order_request import OrderRequest
from paypalserversdk.paypal_serversdk_client import PaypalServersdkClient
import uuid


class OrderController:
    body: OrderRequest
    id = ''

    def __init__(self):
        pass

    def addbody(self, OrderR: OrderRequest):
        self.body = OrderR

    def create_order(self, client: PaypalServersdkClient):
        orderreform = {'body': self.body, 'prefer': 'return=minimal',
                       'paypal_request_id': str(uuid.uuid4())}
        orders = client.orders
        result = orders.create_order(orderreform)

        if result.is_success():
            self.id = result.body.id
            return result.body.id
        elif result.is_error():
            return 0

    def confirm_order(self, client: PaypalServersdkClient):
        collect = {
            'id': self.id,
            'prefer': 'return=minimal'
        }

        result = client.orders.confirm_order(collect)

        if result.is_success():
            print(result.body)
            return True
        elif result.is_error():
            return False
