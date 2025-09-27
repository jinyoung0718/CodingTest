from collections import deque

def solution(s):
    queue = deque(s)
    answer = 0
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for _ in range(len(s)):
        stack = []
        is_valid = True
        
        for ch in queue:
            if ch in "([{":   # 열림 괄호면 push
                stack.append(ch)
            else:             # 닫힘 괄호면 매칭 확인
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    is_valid = False
                    break
                    
        if is_valid and not stack:  # 전부 짝이 맞아야 valid
            answer += 1
        
        # 문자열 회전
        queue.append(queue.popleft())
    
    return answer
