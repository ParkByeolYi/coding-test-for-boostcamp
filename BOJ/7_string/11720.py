#2	11720	숫자의 합
#정수를 문자열로 입력받는 문제. Python처럼 정수 크기에 제한이 없다면 상관 없으나, 예제 3은 일반적인 정수 자료형에 담기에 너무 크다는 점에 주목합시다.

n = int(input())
m = input()
m = list(m) #문자열을 한 글자씩 끊어서 리스트로 바꾸는 방법
total = 0

for i in m :
  i = int(i)
  total += i

print(total)