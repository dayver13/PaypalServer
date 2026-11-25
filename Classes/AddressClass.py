
class Address_Information:

    country_code = ''
    address_line_1 = ''
    address_line_2 = ''
    postal_code = ''

    def __init__(self, country_code, add_line1, add_line2, pos_code):
        self.country_code = country_code
        self.address_line_1 = add_line1
        self.address_line_2 = add_line2
        self.postal_code = pos_code
