from AddressClass import Address_Information


class Card_information:
    name = '',
    number = '',
    expiry = '',
    security = '',
    address: Address_Information

    def __init__(self, name, number, expiry, security, Address: Address_Information):
        self.name = name,
        self.number = number,
        self.expiry = expiry,
        self.security = security,
        self.address = Address_Information
