a, b = map(int,input().split())
print(a|b) #두 정수를 비트단위로 or 계산을 수행한 결과를 10진수로 출력
#비트단위 or 연산은 둘 중 하나라도 1인 자리를 1로 만들어주는 것
#이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서도 효과적으로 사용됨