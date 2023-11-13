# 입력 받기, n개의 자연수는 리스트
n, m, k = map(int, input().split())
num = list(map(int, input().split()))

sorted_num = sorted(num, reverse=True) # 큰 수부터 정렬
first = sorted_num[0] # 가장 큰 수
second = sorted_num[1] # 두 번째로 큰 수

# 반복 구간 [반복횟수 (first) k + (second) 1] 을 m에서 나눈 몫과 나머지
a, b = divmod(m, k+1)

# a와 반복 부분의 곱, b와 first의 곱의 합
big_number = a*(first*k + second) + b*first
print(big_number) # 답안 출력
