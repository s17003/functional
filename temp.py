import operator as op
from functools import partial

def exec(a, b, c):
    f = lambda x: op.add(1,x)
    return map(partial(op.add, 1), [a, b, c])

def display(f, *args):
    print(f(*args))

if __name__ == "__main__":
    a, b, c = [int(input()) for _ range(3)]
    display('\n'.join, exec(a, b, c))
