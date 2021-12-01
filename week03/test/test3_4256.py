# 전위 순회에서 루트 노드를 알 수 있다
# 중위 순회에서 루트를 기준으로 왼쪽 서브트리와 오른쪽 서브트리를 알 수 있다.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def get_postorder(pre_o, in_o):
    length = len(pre_o)
    if length <= 1:
        return pre_o
    root = pre_o[0]
    idx = in_o.index(root)  # 중위 순회에서 루트 노드의 인덱스
    left_subtree = get_postorder(pre_o[1:idx+1], in_o[:idx])
    right_subtree = get_postorder(pre_o[idx+1:], in_o[idx+1:])
    return left_subtree + right_subtree + [root]
if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        
        preorder = list(input().split())
        inorder = list(input().split())
        result = get_postorder(preorder, inorder)
        print(*result)