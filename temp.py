def exec(xs):
    return xs

def display(f, *args):
    print(f(*args))

if __name__ == "__main__":
    xs = [input() for _ in range(2)]
    display('\n'.join, exec(xs))
