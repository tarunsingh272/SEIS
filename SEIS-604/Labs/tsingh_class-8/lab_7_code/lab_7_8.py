# lab_7_8.py

# a first attempt at solving the 4-gallon/3-gallon bottle problem of
#   DSP-4.15 Exercise 12

# INCOMPLETE!

def bottle_move(amt_in_A, amt_in_B, history):
    ''' search for '''
    if amt_in_A == 0 and amt_in_B == 0:
        print ("found it!")
        print (history)
        return

    if amt_in_A == 4: # A full?
        if amt_in_B == 0:
            msg = "fill A with 4 gallons of water"
            history += msg
            bottle_move(0,0,history)
            return
        elif amt_in_B > 0:
            msg = f"pour {3-amt_in_B} into A"

    if amt_in_B == 3: # B full
        if amt_in_A == 0:
            msg = "fill B with 3 gallons of water"
            history += msg
            bottle_move(0,0,history)
            return
        elif amt_in_A > 0:
            msg = ""

        return

    # try emptying A

    # try emptying B

    # try pouring A into B

    # try pouring B into A




def main():

    history = ""
    bottle_move(2, 0, history)