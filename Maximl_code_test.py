from collections import defaultdict   

def find_sub_string(str): 
    str_siz = len(str) 
    dist_count = len(set([x for x in str]))
    x = 0
    a = 0
    a_ind = -1
    b = 9999999999
    count = defaultdict(int) 
    for i in range(str_siz): 
        count[str[i]] += 1
        if count[str[i]] == 1: 
            x += 1
        if x == dist_count: 
            while count[str[a]] > 1: 
                if count[str[a]] > 1: 
                    count[str[a]] -= 1
                a += 1
            win_siz = i - a + 1
            if b > win_siz: 
                b = win_siz 
                a_ind = a 
    z = str[a_ind: a_ind + b] 
    return(len(z))
str1 = input()
print(find_sub_string(str1)) 
