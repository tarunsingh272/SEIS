# _19_7_3_1_base_postal.py

class BasePostalAddress:
    def __init__(self, country, recipient):
        self.country = country
        self.recipient = recipient

    def display(self):
        print(self.recipient)
        print(self.country)

    def validate(self):
        return self.recipient != '' and self.country != ''
