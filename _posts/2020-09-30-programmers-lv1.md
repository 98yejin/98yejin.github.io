---
layout: post
title: 프로그래머스 코딩테스트 연습 Level 1 Python3 
subtitle: 문제 풀이
tags: [python, programmers, level 1]
comments: true
---

연휴 겸 코딩테스트 연습!

프로그래머스 주소:
https://programmers.co.kr/learn/challenges?tab=all_challenges

## Level 1, Python3

### 크레인 인형뽑기 게임:fire:
```python
def solution(board, moves):
    answer = 0
    bucket = []
    for m in moves:
        for l in range(len(board)):
            if board[len(board)-1][m-1] == 0:
                break
            if board[l][m-1] != 0:
                if len(bucket)>0 and (board[l][m-1] == bucket[len(bucket)-1]) :
                    del bucket[len(bucket)-1]
                    board[l][m-1] = 0
                    answer += 2
                else:
                    bucket.append(board[l][m-1])
                    board[l][m-1] = 0
                break
    return answer
```
### 두 개 뽑아서 더하기
```python
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j:
                answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer
```
### 완주하지 못한 선수
```python
def solution(participant, completion):
    answer = ''
    dict1 = {}
    for p in participant:
        if p not in dict1:
            dict1[p] = 0
        if p in dict1:
            dict1[p] = dict1.get(p) + 1
    for c in completion:
        dict1[c] = dict1.get(c)-1
    for p in participant:
        if dict1[p] == 1:
            answer = p
    return answer
```
### 모의고사:fire:
```python
def solution(answers):
    student_1 = [1, 2, 3, 4, 5] * (10000//5)
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (10000//8)
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000//10)
    
    score = {1 : 0,
            2 : 0,
            3: 0}
    
    for i, a in enumerate(answers):
        if a == student_1[i]:
            score[1] += 1            
        if a == student_2[i]:
            score[2] += 1
        if a == student_3[i]:
            score[3] += 1
    
    answer = sorted(score.items(), key = lambda x:x[1], reverse = True)
    
    if answer[0][1] == answer[1][1] and answer[1][1] == answer[2][1]:
        return [answer[0][0], answer[1][0], answer[2][0]]
    if answer[0][1] == answer[1][1]:
        return [answer[0][0], answer[1][0]]
    
    return [answer[0][0]]
```
### 체육복:fire:
```python
def solution(n, lost, reserve):
    distance = [1 for i in range(n)]
    for r in reserve:
        distance[r-1] += 1
    for l in lost:
        distance[l-1] -= 1

    for i in range(n):
        if i+1<n and distance[i]== 0 and distance[i+1]>1:
            distance[i+1] -= 1
            distance[i] = 1
        elif i>0 and distance[i] == 0 and distance[i-1]>1:
            distance[i-1] -= 1
            distance[i] = 1
    return n-distance.count(0)
```
### K번째 수
```python
def solution(array, commands):
    answer = []
    for c in commands:
        ans = array[c[0]-1:c[1]]
        ans.sort()
        i = c[2]
        answer.append(ans[c[2]-1])
    return answer
```
### 2016년
```python
import datetime

def solution(a, b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    answer = day[datetime.date(2016,a,b).weekday()]
    return answer
```
### 가운데 글자 가져오기
```python
def solution(s):
    ln = len(s)
    if len(s) % 2 == 0:
        return s[int(ln/2)-1:int(ln/2)+1]
    if len(s) % 2 != 0:
        return s[int(ln//2)]
```
### 같은 숫자는 싫어
```python
def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0:
            answer.append(a)
            # arr.remove(a)
        elif a != answer[len(answer)-1]:
            answer.append(a)
        # elif a
    return answer
```
### 나누어 떨어지는 숫자 배열
```python
def solution(arr, divisor):
    answer = []
    for a in arr:
        if a%divisor == 0:
            answer.append(a)
    answer.sort()
    if answer == []:
        answer = [-1]
    return answer
```
### 두 정수 사이의 합
```python
def solution(a, b):
    if b>=a:
        answer = a
        while(a<b):
            a += 1
            answer += a
    elif a>b:
        answer = b
        while(a>b):
            b += 1
            answer += b
    return answer
```
### 문자열 내 마음대로 정렬하기
```python
def solution(strings, n):
    answer = []
    strings.sort()
    dict1 = {}
    for s in strings:
        dict1[s] = s[n]
    print(dict1)
    dict2 = sorted(dict1.items(), key=lambda x:x[1])
    for d in dict2:
        answer.append(d[0])
    
    return answer
```
### 문자열 내 p와 y의 개수
```python
def solution(s):
    answer = True
    if s.count('p')+s.count('P') != s.count('y')+s.count('Y'):
        answer = False
    return answer
```
### 문자열 내림차순으로 배치하기
```python
def solution(s):
    return ''.join(sorted(s, reverse=True))
```
### 문자열 다루기 기본
```python
def solution(s):
    if len(s) != (4 or 6):
        return False
    for ss in s:
        if ss.isalpha() == True:
            return False
    return True
```
### 서울에서 김서방 찾기
```python
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 %d에 있다"%i
```
### 소수 찾기
```python
def solution(n):
    a = [False,False] + [True]*(n-1)
    primes=[]
    print(a)
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    print(primes)
    return len(primes)
```
### 수박수박수박수박수박수?
```python
def solution(n):
    answer = ''
    for i in range(n):
        if i%2 == 0:
            answer += '수'
        elif i%2 != 0:
            answer += '박'
    return answer
```
### 문자열을 정수로 바꾸기
```python
def solution(s):
    answer = int(s)
    return answer
```
### 시저 암호
```python
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+n)%26 +ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+n)%26 +ord('a'))
    return ''.join(s)
```
### 약수의 합
```python
def solution(n):
    answer = 0
    i = 0
    while (i<n):
        i+=1
        if (n%i == 0):
            answer += i
    return answer
```
### 이상한 문자 만들기:fire:
```python
def solution(s):
    c = 0
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            c = 0
        elif c%2 == 0:
            if s[i]!= ' ':
                answer += s[i].upper()
            c += 1
        elif c%2 != 0:
            if s[i]!= ' ':
                answer += s[i].lower()
            c += 1
    return answer
```
### 자릿수 더하기
```python
def solution(n):
    n = str(n)
    return sum([int(n[i]) for i in range(len(n))])
```
### 자연수 뒤집어 배열로 만들기
```python
def solution(n):
    n = str(n)[::-1]
    answer = [int(n[i]) for i in range(len(n))]
    return answer
```
### 정수 내림차순으로 배치하기
```python
def solution(n):
    n = str(n)
    return int(''.join(sorted([n[i] for i in range(len(n))], reverse = True)))
```
### 정수 제곱근 판별
```python
def solution(n):
    x = n ** (1/2)
    if x%1 > 0:
        return -1
    return (x+1)**2
```
### 제일 작은 수 제거하기
```python
def solution(arr):
    if len(arr) < 2:
        return [-1]
    arr.remove(min(arr))
    return arr
```
### 짝수와 홀수
```python
def solution(num):
    return "Even" if num%2 == 0 else "Odd"
```
### 키패드 누르기:fire:
```python
def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    value = {1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2),
            '*': (3, 0),
            0: (3, 1),
            '#': (3, 2)
            }
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left = num
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right = num
        else:
            left_distance = abs(value[num][0] - value[left][0]) + abs(value[num][1] - value[left][1])
            right_distance = abs(value[num][0] - value[right][0]) + abs(value[num][1] - value[right][1])
            if left_distance == right_distance:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num
            elif left_distance < right_distance:
                answer += 'L'
                left = num
            elif left_distance > right_distance:
                answer += 'R'
                right = num
                
    return answer
```
### 최대공약수와 최소공배수
```python
def solution(n, m):
    answer = [1, 1]
    if n == m:
        return [m, m]
    if n>m:
        a = m
        b = n
    elif n<=m:
        a = n
        b = m
    
    i = 0
    divisor = []
    while (i<a):
        i+=1
        if a%i == 0 and b%i == 0:
            divisor.append(i)
    
    if len(divisor) == 1:
        answer[1] = a*b
    elif b%a == 0:
        answer[0] = max(divisor)
        answer[1] = b
    answer = [max(divisor),a*b/max(divisor)]
    return answer
```
### 콜라츠 추측
```python
def solution(num):
    answer = 0
    
    while(num!=1):
        if num%2 == 0:
            num /= 2
        elif num%2 != 0:
            num = (num*3)+1
        answer += 1
        if answer == 500:
            break
            
    if answer == 500:
        return -1
    return answer
```
### 평균 구하기
```python
def solution(arr):
    return sum(arr)/len(arr)
```
### 하샤드 수
```python
def solution(x):
    y = str(x)
    c = 0
    
    for i in range(len(y)):
        c += int(y[i])
        
    if x%c == 0:
        return True
    
    return False
```
### 핸드폰 번호 가리기
```python
def solution(phone_number):
    return (len(phone_number)-4) * '*' + phone_number[len(phone_number)-4:]
```
### 행렬의 덧셈
```python
def solution(arr1, arr2):
    answer = arr1[:]
    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            answer[i][j]+=arr2[i][j]
    return answer
```
### x만큼 간격이 있는 n개의 숫자
```python
def solution(x, n):
    return [x+(x*i) for i in range(n)]
```
### 직사각형 별찍기
```python
a, b = map(int, input().strip().split(' '))
print(('*'*a+'\n')*b)
```
### 예산
```python
def solution(d, budget):
    answer = 0
    t = 0

    d.sort()
    for dd in d:
        if t+dd <= budget:
            t += dd
            answer += 1
    return answer
```
### [1차] 비밀지도
```python
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        ans = (bin(int(arr1[i])|int(arr2[i])))[2:].zfill(n).replace('0', ' ').replace('1', '#')
        answer.append(ans)
        
    return answer
```
### 실패율
```python
def solution(N, stages):
    answer = {}
    user = len(stages)
    current = 0
    
    for n in range(N):
        if stages.count(n+1) == 0:
            answer[n+1] = 0
        elif stages.count(n+1) != 0:
            answer[n+1] = stages.count(n+1)/(user-current)
        current += stages.count(n+1)
    
    sol = sorted(answer.items(), reverse= True, key = lambda x:x[1])
    
    return [s[0] for s in sol]
```
### [1차] 다트 게임
```python
def solution(dartResult):
    calc = []
    ans = []
    count = 0
    
    tmp = []
    for d in dartResult:
        if d.isdigit():
            tmp.append(d)
        elif d.isalpha():
            calc.append(int(''.join(tmp)))
            tmp.clear()
    
    for d in (dartResult):
        if d.isalpha():
            count += 1
            if d == 'S':
                ans.append(calc[count-1])
            if d == 'D':
                ans.append(calc[count-1]**2)
            elif d == 'T':
                ans.append(calc[count-1]**3)
        elif d == '*':
            if count>1:
                ans[count-1] *= 2
                ans[count-2] *= 2
            elif count == 1:
                ans[count-1] *= 2
        elif d == '#':
            ans[count-1] *= -1
            
    return sum(ans)
```

