import pickle

with open('region_extend_corpus.txt', 'r', encoding='utf-8') as f:
    with open('Q_no_repeat_extend', 'wb') as q_f:
        with open('A_no_repeat_extend', 'wb') as a_f:
            Q_no_repeat_list = []
            A_no_repeat = []
            for line in f:
                q_list = []
                a_list = []
                line_st = line.strip().split('\t')
                if len(line_st) < 2:
                    continue
                print(line_st)
                for q in line_st[0]:
                    q_list.append(q)
                for a in line_st[1]:
                    a_list.append(a)
                q_f.write(pickle.dumps(tuple(q_list)))
                a_f.write(pickle.dumps(tuple(a_list)))
