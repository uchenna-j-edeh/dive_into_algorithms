
def rpm(x,y):
    """
    first creat 2 lists; halving and doubling
    halving list is halved ignoring the reminder untl it hits 1
    doubling is doubled until we reach the length of the halving column
    placing both list side by side, delete the row that is even
    finally sum all the doubling list
    E.g rpm(89,18) return 1602
    """
    halving = [x]
    doubling = [y]

    while (x > 1):
        x = x // 2
        halving.append(x)

    while (len(doubling) < len(halving)):
        y = y * 2
        doubling.append(y)


    for i in range(len(halving)):
        if halving[i] % 2 == 0: # is even
            doubling[i] = 0

    return sum(doubling)


print(rpm(89,18))