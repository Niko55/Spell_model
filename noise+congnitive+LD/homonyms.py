import csv
import numpy as np

Reader = csv.reader(open('homonyms_corr.csv', newline=''))
dic = []
for row in Reader:
    dic.append(row)

sent = "Alice's great surprise, the Duchess's voice died away, even in the middle of her favourite word moral, and the arm that was linked into hers began to tremble."

def replace_hmn(sent, dic):
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

if __name__ == "__main__":    
    print(replace_hmn(sent, dic))