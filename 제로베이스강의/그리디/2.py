#부분 배낭 문제
#무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
# 물건1 무게 w: 10 가치 v: 10
# 물건2 무게 w: 15 가치 v: 12
# 물건3 무게 w: 20 가치 v: 10
# 물건4 무게 w: 25 가치 v: 8
# 물건5 무게 w: 30 가치 v: 5

data_list = [(10,10),(15,12),(20,10),(25,8),(30,5)]
# data_list = sorted(data_list, key = lambda x : x[1] / x[0], reverse = True) # 5/30 = 무게 단위당 가치는 0.16 즉 reverse=True 를 통해 무게대비 가치가 높은거 부터 기준으로 sorted!! 

def get_max_valule(data_list, capacity):
    #가장 먼저 할것을 골라야지 
    data_list = sorted(data_list, key = lambda x : x[1] / x[0], reverse = True)
    total_value = 0
    detalis = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            detalis.append([data[0],data[1],1]) #물건의 무게, 가치, 그 물건을 몇 프로 넣엇느냐
        else:
            fraction = capacity / data[0]
            total_value += data[1]*fraction
            detalis.append([data[0],data[1],fraction])
            break
    return total_value,detalis

print(get_max_valule(data_list,30))