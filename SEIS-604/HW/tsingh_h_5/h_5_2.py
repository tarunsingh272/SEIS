# h_5_2.py
# Tarun Singh

# Add your UnorderedList methods append() and index() from Lab 5,
#   then also implement pop() and insert()

import unorderedlist

def main():
    # add code to test all 4 new UnorderedList methods,
    #   beyond the sample code that follows
    lst = unorderedlist.UnorderedList()
    lst.add(47)
    lst.add(23)
    print(lst)
    lst.remove(23)
    print(lst)
    lst.append(96)
    print(lst)
    lst.append(232)
    print(lst)
    lst.append(9)
    print(lst)
    print(lst.index(96))
    lst.pop()
    lst.insert(2,"hello")
    print(lst)

main()