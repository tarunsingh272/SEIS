# Listing 7

# _dsp-4_12_2_listing7.py

def make_change_1(coin_denoms, change):

     if change in coin_denoms:

         return 1

     min_coins = float("inf")

     for i in [c for c in coin_denoms if c <= change]:

         num_coins = 1 + make_change_1(

             coin_denoms, change - i

         )

         min_coins = min(num_coins, min_coins)

     return min_coins



print(make_change_1([1, 5, 10, 25], 63))