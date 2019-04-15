import pickle

with open('Q_no_repeat.txt', 'r', encoding='utf-8') as f:
    Q_no_repeat_list = []
    for line in f:
        list = []
        line_st = line.strip()
        for s in line_st:
            list.append(s)
        Q_no_repeat_list.append(tuple(list))

with open('Q_no_repeat', 'wb') as f:
    f.write(pickle.dumps(Q_no_repeat_list))

with open('A_no_repeat.txt', 'r', encoding='utf-8') as f:
    A_no_repeat = []
    for line in f:
        list = []
        line_st = line.strip()
        for s in line_st:
            list.append(s)
        A_no_repeat.append(tuple(list))

with open('A_no_repeat', 'wb') as f:
    f.write(pickle.dumps(A_no_repeat))
