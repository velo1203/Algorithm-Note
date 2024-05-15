import sys
input = sys.stdin.readline # 유클리드 호제법 최대공약수 1850번

A,B = map(int,input().strip().split())
while True:
    c = A % B
    if c == 0:
        break
    A = B
    B = c

print("1"*B)