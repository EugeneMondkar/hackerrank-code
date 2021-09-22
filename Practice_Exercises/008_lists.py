# Problem Link: https://www.hackerrank.com/challenges/python-lists/problem
# Tutorial Link: https://www.hackerrank.com/challenges/python-lists/tutorial
# Helpful Research: https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python


some_list = []

n = int(input())

commands = []

for _ in range(n):
    commands.append(input())

for command in commands:

    statment = command.split()
    if len(statment) == 3:
        statment = "some_list." + statment[0] + "(" + str(statment[1]) + ", " +  str(statment[2]) + ")"
    elif len(statment) == 2:
        statment = "some_list." + statment[0] + "(" + str(statment[1]) + ")"
    elif len(statment) == 1 and statment[0] != "print":
        statment = "some_list." + statment[0] + "()"
    else:
        statment = "#ignore"
        print(some_list)

    exec(statment)


# Alternative Solution (Shorter)
# n = input()
# l = []
# for _ in range(n):
#     s = raw_input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print l
