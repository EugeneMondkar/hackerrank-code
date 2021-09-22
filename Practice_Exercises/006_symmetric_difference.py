# Problem Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

size_n = int(input())
set_n = set(map(int, input().split()))

size_m = int(input())
set_m = set(map(int, input().split()))

difference_n_from_m = set_n.difference(set_m)
difference_m_from_n = set_m.difference(set_n)
difference_n_from_m.update(difference_m_from_n)
symmetric_difference = difference_n_from_m
symmetric_difference = list(symmetric_difference)
symmetric_difference.sort()

for x in symmetric_difference:
    print(x)