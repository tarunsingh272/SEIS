# lab_3_2.py

from timeit import Timer


def test1(n):
    l = []
    for i in range(n):
        l = l + [i]


def test2(n):
    l = []
    for i in range(n):
        l.append(i)


def test3(n):
    l = [i for i in range(n)]


def test4(n):
    l = list(range(n))

t1 = Timer("test1()","from __main__ import test1")
print(t1.timeit(1000), "ms per call")

t2 = Timer("test2()","from __main__ import test2")
print(t2.timeit(1000))

t3 = Timer("test3()","from __main__ import test3")
print(t3.timeit(1000))

t4 = Timer("test4()","from __main__ import test4")
print(t4.timeit(1000))

# wrap the above tests in a loop that divides the timings for n==100..1000 by 100's
#  by O(f(n)), where f(n) is your guess as to the performance

for n in range(100,2100,100):
    t1 = Timer("test1(n)", "from __main__ import test1,n")

    fn = n*n # replace by correct f(n) such that test1() has O(f(n)) performance
    print(f't1/fn for n=={n} is: {t1.timeit(1000)/fn}')

    # modify the following in a similar way:

    t2 = Timer("test2(n)", "from __main__ import test2")
    print(t2.timeit(1000)/n) # O(1)

    t3 = Timer("test3(n)", "from __main__ import test3")
    print(t3.timeit(1000)/n)

    t4 = Timer("test4(n)", "from __main__ import test4")
    print(t4.timeit(1000))

#