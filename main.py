from Classes.AddressClass import Address_Information
from Classes.CardClass import Card_information
from Classes.PayerClass import Payer_Information
from Classes.PurchaseUnitReqClass import PurchasedUnitReqInfo
from paypalconnect import PaypalClient
from Definitions.order_requestdef import order_req


Address = Address_Information("CR", "MiCasa", "Micasa2", "40305")
Card = Card_information('John Doe', '4032038763365750',
                        '2031-11', '234', Address)
Payer = Payer_Information(
    'sb-pmvmn54032268@personal.example.com', 'Y694KF74KYNDW', 'John', 'Doe')
PurchasedUR = PurchasedUnitReqInfo(
    190, 12, 19, 6, 2, 'Phone', 'xxxxx', 'xxxxxy')
OrderR = order_req(Payer, Card, PurchasedUR)

PaypalC = PaypalClient()

PaypalC.addBody(OrderR)

PaypalC.createorder()
PaypalC.confirm_order()
