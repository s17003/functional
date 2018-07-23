import operator as op
def exec(n):
    return op.eq(op.mod(n, 2), 0)

def display(f, *args):
    print(f(*args))

if __name__ == "__main__":
    n = int(input())
    f = lambda x: (('No'), ('Yes'))[x]
    display(f, is_even(n))
