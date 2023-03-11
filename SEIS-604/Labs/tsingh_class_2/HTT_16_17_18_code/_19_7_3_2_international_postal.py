# _19_7_3_2_international_postal.py

import _19_7_3_1_base_postal as p

class IrishPostalAddress(p.BasePostalAddress):
    def __init__(self, recipient, postalCode):
        super().__init__("IRELAND", recipient)
        self.postalCode = postalCode

    def display(self):
        print(self.recipient)
        print(self.postalCode)
        print(self.country)

    def validate(self):
        return super().validate() and len(self.postalCode) == 7

class USPostalAddress(p.BasePostalAddress):
    def __init__(self, recipient, street, city, state, zipcode):
        super().__init__("USA", recipient)
        self.street = street
        self.city = city
        self.state = state
        self.zip = zipcode

    def display(self):
        print(self.recipient)
        print(self.street)
        print(self.city + ", " + self.state + "  " + self.zip)
        print(self.country)

    def validate(self):
        return (super().validate() and self.city != '' and
            len(self.state) == 2 and
            (len(self.zip) == 5 or len(self.zip) == 9)) # modded
