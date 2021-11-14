'''
그리디 알고리즘(2) - (빼거나 나눠서) 1이 될 때까지(과정의 최소 횟수 구하기)
문제 해결 아이디어: 최대한 많이 나누기. 
2 이상의 수로 나누는 작업이 1일 빼는 작업보다 수를 훨씬 많이 줄임.
정당성 분석: 빼는 거 보다 나누는 게 수를 빨리 줄임
'''

n, k = map(int, input().split())

result = 0

while True:
  target = (n // k) * k
  result += (n - target)
  n = target
  
  if n < k:
    break
    
  result += 1
  n //=k
  
result += (n - 1)
print(result)
