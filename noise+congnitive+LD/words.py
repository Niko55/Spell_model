import numpy as np
import csv

Reader = csv.reader(open('words_list.csv'))

dic = []
for row in Reader:
    dic.append(row)

dic_list = []
for i in range(len(dic)):
    if len(dic[i][0]) == 1:
        pass
    else:
        dic_list.append(dic[i][0])
    
def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])
    return res
#this is the case for if the start letter is same
'''  
def word_ret(word, dic_list):
    wl = list(word)
    dic_ret = [w for w in dic_list if w.startswith(wl[0])]
    dic1_ret = []
    for i in range(len(dic_ret)):
        if LD(word, dic_ret[i]) == 1 or LD(word, dic_ret[i]) == 2:
            dic1_ret.append(dic_ret[i])
    return dic1_ret
'''
##following is the case when we take length of +1/-1 and then use edit distance of 1 and 2
def word_ret(word, dic_list):
    l = len(word)
    dic_ret = []
    dic_ret1 = []
    for w in dic_list:
        if len(w) == l+1 or len(w) == l-1:
            dic_ret.append(w)
    for i in dic_ret:
        if LD(word, i) == 1 or LD(word, i) == 2:
            dic_ret1.append(i)
    return dic_ret1

if __name__ == "__main__":
    word = input("Enter a word: ")
    ls = word_ret(word, dic_list)
    print(ls)

    
