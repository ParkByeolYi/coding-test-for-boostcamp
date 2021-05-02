a, b, c = map(int,input().split())

if a%2==0 : #if 조건식 : a를 2로 나눈 나머지가 0, 즉 짝수이면 True, 아니면 False
  print(a) #조건식의 평가값이 True인 경우 실행시킬 명령을 들여쓰기를 이용해 순서대로 작성

if b%2==0 :
  print(b)

if c%2==0 :
  print(c)

print("끝") #들여쓰기를 하지 않은 부분의 조건식에 상관이 없음

'''
python에서는 논리적 실행단위인 코드블록을 표현하기 위해 들여쓰기 사용
들여쓰기 방법은 탭(tap), 공백(space) 4개 등 여러가지 방법을 사용할 수 있지만 한 소스코드 내에서 들여쓰기 길이와 방법은 똑같아야 한다!
'''