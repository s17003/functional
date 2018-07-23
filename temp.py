def exec(s):
    return s

def display(f, *args):
    print(f(*args))

if __name__ == "__main__":
    s = input()
    identity = lambda x: x
    display(identity, exec(s))
