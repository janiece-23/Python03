def rectangle01(c, cols, rows):
    for j in range(rows):
        for i in range(cols):
            print(c, end='')

        print()

def rectangle02(c, cols, rows):
    for j in range( rows ):
        print(c*cols)

def rectangle03(c, cols, rows):
    print('\n'.join([''.join([c]*cols)]*rows))

def rectangle04(c, cols, rows):
    print((c*cols + '\n'*rows))

rectangle01('H', 5,4)
rectangle02('C', 5,4)
rectangle03('B', 5,4)
rectangle04('A', 5, 4)
