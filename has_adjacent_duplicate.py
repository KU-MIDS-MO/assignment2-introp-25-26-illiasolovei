# 1) has_adjacent_duplicate(L)
#    Return True if the list L has any two equal elements next to each other.
#    otherwise return False.
#    Empty or 1-element lists → False.


from utils import hommade_len


def has_adjacent_duplicate(L):
    lnofL = hommade_len(L)
    for id, elem in enumerate(L):
        if id + 1 == lnofL:
            return False
        if elem == L[id + 1]:
            return True
    return False
