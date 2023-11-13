n, m = map(int, input().split()) # 입력
card = [] # 빈 리스트 만들기

for i in range(n): 
    row = list(map(int, input().split())) # 리스트로 입력
    card.append(min(row)) # 최솟값을 카드리스트에 추가

# 각 줄의 최솟값 중 최댓값 구하기
print(max(card))