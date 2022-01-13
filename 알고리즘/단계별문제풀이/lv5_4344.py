n = int(input())
for i in range(n):
    s_list = list(map(int,input().split()))
    print('s_list :', s_list)
    avg = sum(s_list[1:])/s_list[0]
    print(avg)
    cnt = 0
    
    for score in s_list[1:]:
        if score > avg:
            cnt +=1
    
    rate = cnt/s_list[0] *100
    print(f'{rate:.3f}%')

#2. '{}'를 이용한 포맷팅 : 변수 타입 관계 없이 {} 속에 값을 입력한다.
# {:.nf} - 실수를 표현할 때 소수점 아래 n번 째 자리까지만 표현되도록 반올림.