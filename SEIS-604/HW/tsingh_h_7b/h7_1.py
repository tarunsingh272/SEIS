# h7_1.py
#
import random
from timeit import Timer
from bubble import bubble_sort
from short_bubble import bubble_sort_short
from selection import selection_sort
from insertion import insertion_sort
from merge import merge_sort

def bubble(lst):
    bubble_sort(lst)

def bubble2(lst):
    bubble_sort_short(lst)

def selection(lst):
    selection_sort(lst)

def insertion(lst):
    insertion_sort(lst)

def merge(lst):
    merge_sort(lst)

n = int(input("Enter the value N"))
lst = [random.randint(1, n) for k in range(n)]

print("List is: ", lst)
print("First 5 elements before sort: ", lst[0:5])
bubble(lst)
print("First 5 elements after bubble sort: ", lst[0:5])

lst = [random.randint(1, n) for k in range(n)]
print("First 5 elements before sort: ", lst[0:5])
bubble2(lst)
print("First 5 elements after bubble short sort: ", lst[0:5])

lst = [random.randint(1, n) for k in range(n)]
print("First 5 elements before sort: ", lst[0:5])
insertion(lst)
print("First 5 elements after insertion sort: ", lst[0:5])

lst = [random.randint(1, n) for k in range(n)]
print("First 5 elements before sort: ", lst[0:5])
selection(lst)
print("First 5 elements after selection sort: ", lst[0:5])

lst = [random.randint(1, n) for k in range(n)]
print("First 5 elements before sort: ", lst[0:5])
merge(lst)
print("First 5 elements after merge sort: ", lst[0:5])
