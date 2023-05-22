# lab_8_1.py

# an attempt at solving the 4-gallon/3-gallon bottle problem of
#   DSP-4.15 Exercise 12

def bottle_move(A, B, history, visited):
    # history is str describing each move from (0,0) to current move
    #   augmented as we recurse

    # visit is immutable str, not global list
    # try changing visited to a list that's appended in every call

    if f'({A},{B}), ' in visited:
        return  # already processed this state

    visited = visited + f"({A},{B}), " # mark (A,B) as visited

    # print (visited)

    if A== 2:
        print("found it!")
        print (visited)
        print (history)
        return

    # not all states are reachable: try the next one...

    # if A == 1 and B == 1:
    #     print("found it!")
    #     print (history)
    #     return

    if A==0:
        bottle_move(4,B,history+f"filled A(0) with water, ",visited)
    if B==0:
        bottle_move(A, 3, history + f"filled B(0) with water, ",visited)
    if A==4:
        bottle_move(0,B, history + f"emptied A(4), ",visited)
    if B==3:
        bottle_move(A,0, history + f"emptied B(3), ",visited)
    # pour A into B
    if A >= 3-B:
        bottle_move(A-(3-B), 3, history + f"poured A({A}) into B({B}),  ", visited)
    else: # A < 3-B: pour all of A into B
        bottle_move(0,B+A, history + f"poured A({A}) into B({B}), ", visited)
    # pour B into A
    if B >= 4-A:
        bottle_move(4, B-(4-A), history + f"poured B({B}) into A({A}), ", visited)
    else: # A < 3-B: pour all of B into A
        bottle_move(A+B, 0, history + f"poured B({B}) into A({A}), ", visited)



def main():

    history = ''
    visited = ''

    bottle_move(0, 0, history,visited)
    print (history)
    print (visited)

main()