from random import randint

def generate_testdata(rows, cols, outfile):
    with open(outfile, 'w') as f:
        for _ in range (rows):
            toprint = [randint(0,1)] * cols
            print(f, ','.join(toprint))

def f():
    return 1
