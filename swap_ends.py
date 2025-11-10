# 2) swap_ends(L, k)
#    Return a NEW list formed by swapping the first k elements with the last k
#    elements. Keep the order of elements inside each part the same.
#    Also return the number of swaps performed as a tuple (new_list, num_swaps).
#    Do NOT change the original list.
#    If k <= 0, the list is empty, or k is larger than half of the list length,
#    return (a copy of L, 0).


from utils import hommade_len


def swap_ends(L, k):
    cpofL = L.copy()
    if k <= 0 or hommade_len(L) == 0 or k > hommade_len(L) // 2:
        return (cpofL, 0)

    for i in range(0, k):
        last = cpofL.pop(hommade_len(L) - (i + 1))
        first = cpofL.pop(i)
        cpofL.insert(0, last)
        cpofL.append(first)

    # hear me out: why counting swaps if can return k back?
    return (cpofL, k)
