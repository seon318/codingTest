n, k = map(int, input().split()) # 입력 받기
total = 0 # 실행횟수

while not n==1: # n이 1이 될 때까지 반복
    a, b = divmod(n, k) # n/k의 몫과 나머지
    total += b # 1번 연산 실행횟수 더하기 (n-1)
    total += 1 # 2번 연산 실행횟수 더하기
    n = a # k로 나눈 뒤 남은 몫을 다시 n으로 설정

print(total)