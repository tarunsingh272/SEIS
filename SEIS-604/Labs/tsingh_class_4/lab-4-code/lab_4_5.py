# Implement a radix sorting machine.
#
# A radix sort for base 10 integers is a mechanical sorting technique
# that utilizes a collection of bins, one main bin and 10 digit bins.

# Each bin acts like a queue and maintains its values in the order
#   that they arrive.

# Create 10 Queues, one for each digit.  Name them place_N, N=0..9

# The algorithm begins by placing each number in the main bin.

# Then it considers each value digit by digit, starting with the ones digit.

# The first value is removed and placed in a digit bin corresponding to
# the digit being considered.

# For example, if the ones digit is being considered,
# 534 is placed in digit bin 4 and 667 is placed in digit bin 7.

# Once all the values are placed in the corresponding digit bins,
# the values are collected from bin 0 to bin 9 and placed back in the main bin.

# The process continues with the tens digit, the hundreds, and so on.

# After the last digit is processed, the main bin contains the values in order.

# Start by creating the main bin (queue),
#   and read integers to sort from user, adding to bin
#   (keep track of greatest int largest, to use in algorithm)


#