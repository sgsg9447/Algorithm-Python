# 바이너리 서치
#target: 찾고자하는값
#data : 오름차순으로 정렬된 list
#start : data의 처음 값 인덱스
#end : data의 마지막 값 인덱스
#mid : start, end의 중간 인덱스
#구현 개요 : 자료의 중간값이 찾고자 하는 값인지 검사, > 아니라면 대소관계를 비교하여 start, end 이동 > 재귀!

# data 중에서 target 을 검색하여 index 값을 return 한다.
# 없으면 None을 return한다.


def binary_search(target, data): 
    data.sort() #자료는 무조건 오름차순 정렬이여야하니까!
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:   
            end = mid -1

    return None

# 테스트용 코드
if __name__ == "__main__":
  li = [i**2 for i in range(11)]
  target = 9
  idx = binary_search(target, li)

  if idx:
      print('답',li[idx])
  else:
      print("찾으시는 타겟 {}가 없습니다".format(target))


#-------------------------------------------------------------------------------------------------#
#바이너리서치 재귀적 구현!

# data는 오름차순으로 정렬된 리스트 
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binary_search_recursion(target, start, end, data)

# 테스트용 코드
if __name__ == '__main__':
    li = [i*3 for i in range(11)]
    target = 6
    idx = binary_search_recursion(target, 0, 10, li)

    print(li)
    print(idx)