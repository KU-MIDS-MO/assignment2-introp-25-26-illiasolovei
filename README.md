[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/iR_zthER)
# Introduction to Programming
# Winter semester 2025/26 — Assignment2

#Note:
Same as in Assignment 1, all concepts required to complete these exercises have been covered in the lectures and examples.
You should be able to solve each problem using only what has been taught so far; basic data types, lists, tuples, loops, if statements, and functions.

# Tasks(each has a starter.py and a pytest file):  

1) has_adjacent_duplicate(L)
   Return True if the list L has any two equal elements next to each other.
   otherwise return False.
   Empty or 1-element lists → False.

2) swap_ends(L, k)
   Return a NEW list formed by swapping the first k elements with the last k
   elements. Keep the order of elements inside each part the same.
   Also return the number of swaps performed as a tuple (new_list, num_swaps).
   Do NOT change the original list.
   If k <= 0, the list is empty, or k is larger than half of the list length,
   return (a copy of L, 0).

3) breakdown_time(seconds)
   Convert a non-negative integer number of seconds into as few units as
   possible using 3600, 60, and 1. Return a dictionary like {3600: h, 60: m, 1: s}.
   If input is invalid (not int or negative), return -1.
   For seconds == 0, return {}.
