
class PurchasedUnitReqInfo:
    amount = '',
    item = '',
    shipping = '',
    tax = '',
    handling = '',
    insurance = '',
    description = '',
    referenceID = '',
    customID = ''

    def __init__(self, item, shipping, tax, handling, insurance, description, referenceID, customID):
        self.item = str(item)
        self.shipping = str(shipping)
        self.tax = str(tax)
        self.handling = str(handling)
        self.insurance = str(insurance)
        self.amount = str(item+shipping+tax+handling+insurance)
        self.description = description
        self.referenceID = referenceID
        self.customID = customID
