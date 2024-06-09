import statistics
import math

with open('studyA.csv', 'r') as f:
    kw_list = f.read().split("\n")
    kw_list.remove('');
    
    study_list = []
    
    for kw in kw_list:
    	study_list.append(int(kw))
    
    answer = sorted(study_list)
    #answer = kw_list.sort(reverse=true)
    print(answer)
    
    print('最大値')
    print(max(answer))
    print('最小値')
    print(min(answer))
    print('中央値')
    print(statistics.median(answer))
    print('平均値')
    print(statistics.mean(answer))
    print('標準偏差値')
    print(statistics.pstdev(answer))