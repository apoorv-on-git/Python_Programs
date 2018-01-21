#Function to check if bishop can kill pawn by moving in up right direction
def upper_right(l, bishop):
    first = bishop[0]
    second = bishop[1]
    number = int(second)
    hold = []
    if number == 8:
        return []
    paces = ''
    for i in l[l.index(first)+1:]:
        number = number + 1
        paces = i + str(number)
        hold.append(paces)
    return hold

#Function to check if bishop can kill pawn by moving in up left direction
def upper_left(l, bishop):
    first = bishop[0]
    second = bishop[1]
    number = int(second)
    hold = []
    if number == 8:
        return []
    paces = ''
    l = l[:l.index(first)]
    l = l[::-1]
    for i in l:
        number = number + 1
        #if number == 0:
            #break
        paces = i + str(number)
        hold.append(paces)
    return hold

#Function to check if bishop can kill pawn by moving in down right direction
def down_right(l, bishop):
    first = bishop[0]
    second = bishop[1]
    number = int(second)
    hold = []
    paces = ''
    if number == 1:
        return []
    for i in l[l.index(first) + 1:]:
        number = number - 1
        if number == 0:
            break
        paces = i + str(number)
        hold.append(paces)
    return hold

#Function to check if bishop can kill pawn by moving in down left direction
def down_left(l, bishop):
    first = bishop[0]
    second = bishop[1]
    number = int(second)
    hold = []
    paces = ''
    if number == 1:
        return []
    l = l[:l.index(first)]
    l = l[::-1]
    for i in l:
        number = number - 1
        if number == 0:
            break
        paces = i + str(number)
        hold.append(paces)
    return hold

#Function to check if the bishop can kill pawn
def bishopAndPawn(bishop, pawn):
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    u_r = upper_right(l, bishop)
    if pawn in u_r:
        return True
    u_l = upper_left(l, bishop)
    if pawn in u_l:
        return True
    d_r = down_right(l, bishop)
    if pawn in d_r:
        return True
    d_l = down_left(l, bishop)
    if pawn in d_l:
        return True
    return False
