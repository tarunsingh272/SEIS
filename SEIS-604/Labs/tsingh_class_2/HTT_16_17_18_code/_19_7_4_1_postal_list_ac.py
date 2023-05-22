# _19_7_4_1_postal_list_ac.py

import _19_7_3_2_international_postal as p # not needed in notebook

addrList = [p.IrishPostalAddress("Alf Jones", "A26F4G9"),
            p.USPostalAddress("Abe Jones", "103 Anywhere Ln",
                "Greenville", "SC", "29609"),
            p.IrishPostalAddress("Gabe Jones", "A65F4E2")]

for addr in addrList:
    addr.display()
