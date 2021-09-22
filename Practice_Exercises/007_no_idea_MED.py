# Problem Link: https://www.hackerrank.com/challenges/no-idea/problem

n,m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

happiness_score = 0 

# My Original Solution
# for x in arr:
#     if x in set_a:
#         happiness_score += 1
#     if x in set_b:
#         happiness_score -= 1

# Alternative Solution
happiness_score = sum([(x in set_a) - (x in set_b) for x in arr])

print(happiness_score)

