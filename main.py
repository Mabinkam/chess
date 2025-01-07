def pawn_check(x1, y1, x2, y2):
    return x1 == x2 and y2 - y1 == 1

print(pawn_check(1,2,3,4))

def rook_check(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

def bishop_check(x1, y1, x2, y2)