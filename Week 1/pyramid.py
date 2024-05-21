def pyramid(n):
    count = 1

    for i in range(n):
        # Print leading spaces
        for j in range(n-i):
            print(' ', end='')

        # Print stars
        for k in range(count):
            print('*', end='')

        # for j in range(i):
        #     print(' ', end=' ')

        print()
        count += 2


n = 5
pyramid(n)
