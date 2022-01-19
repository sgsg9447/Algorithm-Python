# 회문(回文) 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말한다. 예를 들어 ‘abba’ ‘kayak’, ‘reviver’, ‘madam’은 모두 회문이다. 만일 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열을 “유사회문”(pseudo palindrome)이라고 부른다. 예를 들어 ‘summuus’는 5번째나 혹은 6번째 문자 ‘u’를 제거하여 ‘summus’인 회문이 되므로 유사회문이다.

# 여러분은 제시된 문자열을 분석하여 그것이 그 자체로 회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 아니면 회문이나 유사회문도 아닌 일반 문자열인지를 판단해야 한다. 만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다. 




import sys

T = int(sys.stdin.readline())



def is_palindrome(str):
    left_false = False
    right_false = False
    for i in range(len(str)//2):
        if str[i] != str[len(str)-1-i]:
            # 앞 글자 삭제후 비교
            for j in range(i,len(str)//2):
                if str[j+1] != str[len(str)-1-j]:
                    left_false = True

            # 뒤 글자 삭제후 비교
            for j in range(i,len(str)//2):
                if str[j] != str[len(str)-1-j -1]:
                    right_false = True 
            
            if left_false and right_false:
                return 2
            elif left_false or right_false:
                return 1

    return 0

for _ in range(T):
    print(is_palindrome(sys.stdin.readline().rstrip()))