from random import randint

def generate_testdata(rows, cols, outfile):
    with open(outfile, 'w') as f:
        for _ in range (rows):
            toprint = [str(randint(0,1)) for _ in range(cols)]
            f.write(','.join(toprint) + '\n')

def f():
    return 1
