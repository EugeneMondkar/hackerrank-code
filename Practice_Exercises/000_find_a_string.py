# Problem Link: https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    
    count = 0
    sub_len = len(sub_string)
    
    i = 0
    while i <= (len(string) - sub_len):
        extracted_string = string[i:(i + sub_len)]
        if sub_string == extracted_string:
            count += 1  
    
        i += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)