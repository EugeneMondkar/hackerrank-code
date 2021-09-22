# Problem Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Tutorial Link: https://www.hackerrank.com/challenges/list-comprehensions/tutorial

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    
    i_list = range(x + 1)
    j_list = range(y + 1)
    k_list = range(z + 1)

    result = [[i, j, k] for i in i_list for j in j_list for k in k_list if ((i + j + k) != n)]

    print(result)