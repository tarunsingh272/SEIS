# _19_7_1_address_class_1.py

class Address:
    def __init__(self, recipient, addressLines, country):
        self.country = country
        self.recipient = recipient
        self.addressLines = addressLines


addr = Address('Abe Jones', ['123 Somewhere Ln', 'Greenville, SC  29609'], 'USA')
print(addr)
