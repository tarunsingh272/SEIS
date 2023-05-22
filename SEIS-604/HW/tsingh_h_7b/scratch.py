import short_bubble as s
import random
N = 100

li = [random.randint(1,N) for x in range(N) ]

s.bubble_sort_short(li)