'''
문제
동호와 규완이는 212호에서 문자열에 대해 공부하고 있다. 
김진영 조교는 동호와 규완이에게 특별 과제를 주었다. 
특별 과제는 특별한 문자열로 이루어 진 사전을 만드는 것이다. 
사전에 수록되어 있는 모든 문자열은 N개의 "a"와 M개의 "z"로 이루어져 있다. 
그리고 다른 문자는 없다. 
사전에는 알파벳 순서대로 수록되어 있다.

규완이는 사전을 완성했지만, 동호는 사전을 완성하지 못했다. 
동호는 자신의 과제를 끝내기 위해서 규완이의 사전을 몰래 참조하기로 했다. 
동호는 규완이가 자리를 비운 사이에 몰래 사전을 보려고 하기 때문에, 문자열 하나만 찾을 여유밖에 없다.

N과 M이 주어졌을 때, 
규완이의 사전에서 K번째 문자열이 무엇인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 N, M, K가 순서대로 주어진다.

출력
첫째 줄에 규완이의 사전에서 K번째 문자열을 출력한다. 
만약 규완이의 사전에 수록되어 있는 문자열의 개수가 K보다 작으면 -1을 출력한다.
'''

import sys
from math import factorial

def calc(n, m):
    return factorial(m+n) / (factorial(m) * factorial(n))

n, m, k = map(int, sys.stdin.readline().split())

if k > calc(n,m):
    print(-1)
    exit()

k -= 1
result = ""

while True:
    if n == 0 or m == 0:
        break

    tmp = calc(n-1, m)
    if tmp > k:
        result += "a"
        n -= 1
    else:
        result += "z"
        m -= 1
        
        k -= tmp
print(result + "z" * m + "a" * n)