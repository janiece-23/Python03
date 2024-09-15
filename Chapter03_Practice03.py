def triangle01(char, level):
    for i in range(level):
        print(char*(i+1))

def triangle02(char, level):
    print('\n'.join(char*(i+1) for i in range(level)))

triangle01('L', 5)
triangle02('L', 5)