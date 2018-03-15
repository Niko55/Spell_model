import numpy as np
import random
import csv

row_1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
row_2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
row_3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

rowl_1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
rowl_2 = ['0', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
rowl_3 = ['0', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '0', '0']

matrix = np.asmatrix([rowl_1, rowl_2, rowl_3])
articles = ['the', 'a', 'an']

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

Reader1 = csv.reader(open('homonyms_corr.csv', newline=''))
dic1 = []
for row in Reader1:
    dic1.append(row)
        
class noise_gen():
    def __init__(self, matrix, char):
        self.a = 0       
    def random_pick(self, matrix, char):
        list_words = []
        x_i, x_j = 0, 0
        for i in range(0, 3):
            for j in range(0, 10):
                if matrix[i, j] == char:
                    x_i = i
                    x_j = j  
        if x_i == 0 and x_j == 0:
            list_words.extend([matrix[x_i+1, x_j], matrix[x_i, x_j+1], matrix[x_i+1, x_j+1]])
        elif x_i == 1 and x_j == 1:
            list_words.extend([matrix[x_i-1, x_j+1], matrix[x_i, x_j+1], matrix[x_i, x_j+1], matrix[x_i-1, x_j], matrix[x_i+1,x_j], matrix[x_i-1, x_j-1], matrix[x_i, x_j-1], matrix[x_i+1, x_j-1]])
        elif x_i == 2 and x_j == 1:
            list_words.extend([matrix[x_i, x_j-1], matrix[x_i-1, x_j-1], matrix[x_i-1, x_j], matrix[x_i-1, x_j+1], matrix[x_i, x_j+1]])
        elif x_i == 0 and x_j <= 8 and x_j >= 1:        
            list_words.extend([matrix[x_i, x_j-1], matrix[x_i+1, x_j], matrix[x_i+1, x_j+1], matrix[x_i, x_j+1]])
        elif x_i == 1 and x_j >= 1 and x_j <= 8:        
            list_words.extend([matrix[x_i-1, x_j-1], matrix[x_i, x_j-1], matrix[x_i+1, x_j-1], matrix[x_i+1, x_j], matrix[x_i+1, x_j+1], matrix[x_i, x_j+1], matrix[x_i-1, x_j+1], matrix[x_i-1, x_j]])
        elif x_i == 2 and x_j <= 8 and x_j > 1:        
            list_words.extend([matrix[x_i, x_j-1], matrix[x_i, x_j+1], matrix[x_i-1, x_j+1], matrix[x_i-1, x_j]])
        elif x_i == 0 and x_j == 9:
            list_words.extend([matrix[x_i, x_j-1], matrix[x_i+1, x_j]])
        elif x_i == 1 and x_j == 9:
            list_words.extend([matrix[x_i-1,x_j], matrix[x_i-1,x_j-1], matrix[x_i,x_j-1], matrix[x_i+1,x_j-1], matrix[x_i+1,x_j]])    
        corr_list = [i for i in list_words if i != '0']
        choice = ''   
        choice = random.choice(corr_list)
        return choice
    def delt_letter(self, word):
        lst = list(word)    
        i = np.random.randint(len(lst))
        del lst[i]
        word_r = ''.join(str(j) for j in lst)
        return word_r
    def substitute(self, word):
        lst = list(word)
        i = np.random.randint(len(word))    
        lst[i] = self.random_pick(matrix, lst[i])
        word_r = ''.join(str(j) for j in lst)
        return word_r
    def add_space(self, word):
        lst = list(word)    
        i = np.random.randint(1,len(lst))
        lst.insert(i, ' ')
        word_r = ''.join(str(j) for j in lst)
        return word_r
    def insert_letter(self,word):
        word_r = ''
        a = []
        lst = list(word)    
        i = np.random.randint(1,len(lst))    
        a_prev_i = self.random_pick(matrix, lst[i-1])
        a_i = self.random_pick(matrix, lst[i])
        a_i = [i for i in a_i if i != '0']
        a_prev_i = [i for i in a_prev_i if i != '0']    
        a.extend([a_prev_i, a_i])
        x_i = np.random.choice(len(a[0:]))
        y_i = np.random.choice(len(a[0]))
        lst.insert(i, a[x_i][y_i])
        word_r = ''.join(str(e) for e in lst)
        return word_r
    def transposition(self, word):
        lst = list(word)
        i = np.random.randint(len(lst))
        j = np.random.randint(len(lst))
        l_temp = lst[j]
        lst[j] = lst[i]
        lst[i] = l_temp
        word_r = ''.join(str(e) for e in lst)
        return word_r
    
    def comp_words(self, sent):
        sent_r = ''
        sent_list = sent.split()
        lmd = [0, 1, 2]
        m = np.random.choice(lmd)   
        if m == 0:
            pass
        elif m == 1:
            x_i = np.random.randint(1,len(sent_list))
            sent_list[x_i:x_i+2] = [''.join(sent_list[x_i:x_i+2])]
        elif m==2:
            for i in range(m):
                x_i = np.random.randint(len(sent_list))
                sent_list[x_i:x_i+2] = [''.join(sent_list[x_i:x_i+2])]   
        for word in sent_list:
            sent_r += " " + word
        return sent_r
    
    def error_sent(self, sent):
        func_list = [self.delt_letter, self.substitute, self.add_space, self.insert_letter, self.transposition]
        sent1 = self.comp_words(sent)
        sent_list = sent1.split()
        sent_r = ''
        sent_corr_list = []
        indexa = []    
        for i in sent_list:
            if i in sent_list and i not in articles:            
                sent_corr_list.append(i)
        for j in range(len(sent_list)):        
            if sent_list[j] in articles:
                indexa.append(j)
        index_list = np.random.choice(len(sent_corr_list), int(len(sent_corr_list)/3))
        f_list = [1, 2, 3]
        m = np.random.choice(f_list)
        if m == 1:
            for l in index_list:
                i = np.random.choice(len(func_list), m)
                i_int = int(i)
                sent_corr_list[l] = func_list[i_int](sent_corr_list[l])
        
        elif m == 2:
            for l in index_list:
                i,j = np.random.choice(len(func_list), m)
                i_int = int(i)
                j_int = int(j)
                sent_corr_list[l] = func_list[i_int](func_list[j_int](sent_corr_list[l]))            
        elif m == 3:
            for l in index_list:
                i,j,k = np.random.choice(len(func_list), m)
                i_int = int(i)
                j_int = int(j)
                k_int = int(k)
                sent_corr_list[l] = func_list[i_int](func_list[j_int](func_list[k_int](sent_corr_list[l]))) 
        for k in indexa:
            sent_corr_list.insert(k, sent_list[k]) 
        for word in sent_corr_list:
            sent_r += " " + word
        return sent_r, sent
    
    def LD(self, s, t):
        if s == "":
            return len(t)
        if t == "":
            return len(s)
        if s[-1] == t[-1]:
            cost = 0
        else:
            cost = 1
       
        res = min([self.LD(s[:-1], t)+1,
                  self.LD(s, t[:-1])+1, 
                  self.LD(s[:-1], t[:-1]) + cost])
        return res
    
    def word_ret(self, word, dic_list):
        l = len(word)
        dic_ret = []
        dic_ret1 = []
        for w in dic_list:
            if len(w) == l+1 or len(w) == l-1:
                dic_ret.append(w)
        for i in dic_ret:
            if self.LD(word, i) == 1 or self.LD(word, i) == 2:
                dic_ret1.append(i)
        return dic_ret1
    
    def replace_hmn(self, sent, dic):
        sent_r = ''
        index = []
        index_i = []   
        sent_list = sent.split()
        m = np.random.randint(4)    
        for j in range(len(dic)):
            for i in range(len(sent_list)):
                if sent_list[i] == dic[j][0]:
                    index.append(i)
                elif sent_list[i] == dic[j][1]:
                    index.append(i)                
        for k in index:
            if k not in index_i:
                index_i.append(k)
        if m == 0:
            return sent
        if m == 1:
            n = np.random.choice(index_i)
            for j in range(len(dic)):
                if sent_list[n] == dic[j][0]:
                    sent_list[n] = dic[j][1]
                elif sent_list[n] == dic[j][1]:
                    sent_list[n] = dic[j][0]
            for word in sent_list:
                sent_r += " " + word
            return sent_r
        if m == 2:
            n = np.random.choice(index_i, 2)
            for i in n:
                for j in range(len(dic)):
                    if sent_list[i] == dic[j][0]:
                        sent_list[i] = dic[j][1]
                    elif sent_list[i] == dic[j][1]:
                        sent_list[i] = dic[j][0]
            for word in sent_list:
                sent_r += " " + word
            return sent_r
    
        if m == 3:
            n = np.random.choice(index_i, 3)
            for i in n:
                for j in range(len(dic)):
                    if sent_list[i] == dic[j][0]:
                        sent_list[i] = dic[j][1]
                    elif sent_list[i] == dic[j][1]:
                        sent_list[i] = dic[j][0]
            for word in sent_list:
                sent_r += " " + word
            return sent_r
    
sent = 'When the Python interpreter reads a source file, it executes all of the code found in it.'
    
if __name__ == "__main__":
    noise = noise_gen(matrix, 'g')
    noise_choice = noise.random_pick(matrix,'g')
    sub = noise.substitute('word')
    error = noise.error_sent(sent)
    print (error)
