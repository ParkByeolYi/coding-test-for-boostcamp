#윤년

n = int(input())

#윤년인 경우
if n%4==0 and n%100!=0 : #나머지를 구하는 연산자 %를 사용하여 나머지가 0이면 배수, 0이 아니면 배수가 아니다.
  print('1')
elif n%400==0 :
  print('1')
else : #윤년이 아닌 경우
  print('0')