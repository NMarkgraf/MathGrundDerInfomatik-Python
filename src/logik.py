def oder(x, y):
    return(x or y)


def und(x, y):
    return(x and y)


def xoder(x, y):
    return((x or y) and not(x and y))


def impl(x, y):
    return(not(x) and y)
    
    
def p(A):
    return "w" if A else "f"


if __name__ == '__main__':
    """
    for A in (True, False):
        for B in (True, False):
            print(f"{p(A)} {p(B)} {p(oder(A, B))} {p(und(A, B))} {p(xoder(A, B))}")
    """

    print(f"A B C D E | Ausdruck ")
    print("-"*21)
    for A in (True, False):
        for B in (True, False):
            for C in (True, False):
                for D in (True, False):
                    for E in (True, False):
                        print(f"{p(A)} {p(B)} {p(C)} {p(D)} {p(E)} | {p(impl(impl(A, oder(und(B, C), D)), E))} ")

