# Problem Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_value = max(arr)
    runner_up = min(arr)

    for x in arr:
        if x > runner_up and x < max_value:
            runner_up = x
    
    print(runner_up)

    