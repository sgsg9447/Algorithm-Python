n= int(input())
cnt = 0

def q_check(q_list, newQ):
    for i in range(len(q_list)):
        if newQ in q_list:
            return False
        if abs[len(q_list)- i] == abs[newQ - q_list[i]]:
            return False

    else:
        return True


def dfs(q_list, newQ):
    global cnt
    
    if len(q_list) == n:
        cnt += 1
    elif q_check(q_list,newQ):
        for i in range(n):
            dfs(q_list+[newQ], i)

print(cnt)
    
