---
layout: post
title: 프로그래머스 코딩테스트 연습 Level 1 파이썬 41문제
subtitle: 문제 풀이
tags: [python, programmers, level 1]
comments: true
---

연휴 겸 코딩테스트 연습!

프로그래머스 주소:
https://programmers.co.kr/learn/challenges?tab=all_challenges

## Level 1, Python3

목차

1. [크레인 인형뽑기 게임](#크레인-인형뽑기-게임)

2. [두 개 뽑아서 더하기](#두-개-뽑아서-더하기)

3. [완주하지 못한 선수](#완주하지-못한-선수)

4. [모의고사](#모의고사)

5. [체육복](#체육복)

6. [K번째 수](#k번째-수)

7. [2016년](#2016년)

8. [가운데 글자 가져오기](#가운데-글자-가져오기)

9. [같은 숫자는 싫어](#같은-숫자는-싫어)

10. [나누어 떨어지는 숫자 배열](#나누어-떨어지는-숫자-배열)

11. [두 정수 사이의 합](#두-정수-사이의-합)

12. [문자열 내 마음대로 정렬하기](#문자열-내-마음대로-정렬하기)

13. [문자열 내 p와 y의 개수](#문자열-내-p와-y의-개수)

14. [문자열 내림차순으로 배치하기](#문자열-내림차순으로-배치하기)

15. [문자열 다루기 기본](#문자열-다루기-기본)

16. [서울에서 김서방 찾기](#서울에서-김서방-찾기)

17. [소수 찾기](#소수-찾기)

18. [수박수박수박수박수박수?](#수박수박수박수박수박수)

19. [문자열을 정수로 바꾸기](#문자열을-정수로-바꾸기)

20. [시저 암호](#시저-암호)

21. [약수의 합](#약수의-합)

22. [이상한 문자 만들기](#이상한-문자-만들기)

23. [자릿수 더하기](#자릿수-더하기)

24. [자연수 뒤집어 배열로 만들기](#자연수-뒤집어-배열로-만들기)

25. [정수 내림차순으로 배치하기](#정수-내림차순으로-배치하기)

26. [정수 제곱근 판별](#정수-제곱근-판별)

27. [제일 작은 수 제거하기](#제일-작은-수-제거하기)

28. [짝수와 홀수](#짝수와-홀수)

29. [키패드 누르기](#키패드-누르기)

30. [최대공약수와 최소공배수](#최대공약수와-최소공배수)

31. [콜라츠 추측](#콜라츠-추측)

32. [평균 구하기](#평균-구하기)

33. [하샤드 수](#하샤드-수)

34. [핸드폰 번호 가리기](#핸드폰-번호-가리기)

35. [행렬의 덧셈](#행렬의-덧셈)

36. [x만큼 간격이 있는 n개의 숫자](#x만큼-간격이-있는-n개의-숫자)

37. [직사각형 별찍기](#직사각형-별찍기)

38. [예산](#예산)

39. [비밀지도](#비밀지도)

40. [실패율](#실패율)

41. [다트 게임](#다트-게임)






### 크레인 인형뽑기 게임
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
:star: 크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다. 
```python 
if board[len(board)-1][m-1] == 0:
    break 
```
마지막 보드까지 m번째 라인에서 바닥까지(len(board)-1이 마지막) 쭉 0인 경우에 아무런 일도 일어나지않으니까 break 하고 다음으로 넘어가준다!

:star:  모든 인형은 1 x 1 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다.
```python
for l in range(len(board)):
.
.
.
            if board[l][m-1] != 0:
                if len(bucket)>0 and (board[l][m-1] == bucket[len(bucket)-1]) :
                    del bucket[len(bucket)-1]
                    board[l][m-1] = 0
                    answer += 2
                else:
                    bucket.append(board[l][m-1])
                    board[l][m-1] = 0
```
board[l][m-1]이 0인 경우에는 인형이 없는거니까 쭉~ 내려가고(if)
0이 아닌 경우에만 bucket(인형을 담는 바구니)에 인형을 추가해준다(else). 그런데 bucket에 이미 내가 넣을 인형과 똑같은게 있다면, bucket안의 인형은 삭제해주고(del) board[1][m-1]의 인형은 뺀 것으로 처리(0으로 바꿈)해준다. 왜냐면 인형이 2개 이상이면 터지니까(answer +=2)!

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
### 모의고사
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
:star: 좀 .. 비효율적인 방법으로 풀었다. 다른 문제들도 비효율적이겠지만.. 이건 유난히 더 비효율적으로.. 어차피 완전탐색이니까 수포자들이 찍는 패턴이 담긴 리스트의 길이를 모두 10000으로 만들어줬다..!

### 체육복
```python
def solution(n, lost, reserve):
    answer = [1 for i in range(n)]
    for r in reserve:
        answer[r-1] += 1
    for l in lost:
        answer[l-1] -= 1

    for i in range(n):
        if i+1<n and answer[i]== 0 and answer[i+1]>1:
            answer[i+1] -= 1
            answer[i] = 1
        elif i>0 and answer[i] == 0 and answer[i-1]>1:
            answer[i-1] -= 1
            answer[i] = 1
    return n-answer.count(0)
```
:star: 처음에는 계속 틀렸는데 

> Greedy algorithM: 그때 그때 최선이라고 생각되는 선택을 하는 것. 최적해가 아닐 때도 있다!

이 개념을 딱 보고 답을 생각해냈다!

:star: 계속 틀렸던 이유는 바로 '여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.' 이 조건! 문제 좀 제대로 읽는 습관을 들여야겠다:disappointed_relieved:.

1. 체육복을 가지고 있는 학생은 1, 없는 학생은 0이라고 가정
2. 학생의 수만큼 리스트를 만듬(다 가지고 있다고 가정, 1)
3. 여벌 체육복을 가지고 왔으면 +1
4. 도난 당했으면 -1

이렇게 하면 학생들이 보유한 체육복수가 담긴 리스트가 만들어지고, 체육복이 없는 학생(answer[i] == 0) 앞뒤로 여벌 체육복을 가진 학생(answer[i-1]>1)이 있는지 없는지 체크!
있으면 여벌있는 학생한테는 -1, 없는 학생한테는 +1 

그리고 최종적으로 답은 학생의 수 - 체육복이 없는 학생의 수!




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
:star: 그냥 하면 시간 초과 걸린다

:star: '에라토스테네스의 체'를 사용해야 한다

:star: 알고리즘
1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다. 그림에서 회색 사각형으로 두른 수들이 여기에 해당한다.
2. 2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
3. 자기 자신을 제외한 2의 배수를 모두 지운다.
4. 남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
5. 자기 자신을 제외한 3의 배수를 모두 지운다.
6. 남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
7. 자기 자신을 제외한 5의 배수를 모두 지운다.
8. 남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
9. 자기 자신을 제외한 7의 배수를 모두 지운다.
10. 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.

출처: https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

### 수박수박수박수박수박수
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
### 이상한 문자 만들기
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
:star: 이건 공백만 잘 처리하면 된다.. strip으로 공백 없애서 리스트 만들지말고 공백이 나올때마다 초기화해주는 변수(c)를 선언하면 쉽게 해결!

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
:star: 제곱근은 n^(1/2)니까! 파이썬에서 ^는 ** 이니까! n의 제곱근 x를 구해주고 정수인지 실수인지 판별하기위해서 x%1을 한다.

ex. 11.0 % 1 = 0.0 -> 정수

ex. 11.123 % 1 = 0.123 -> 실수

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
### 키패드 누르기
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
:star: 이건 맨하탄 거리를 사용해서 푸는 문제다. 
> 맨하탄거리는 항상 유클리드 거리보다 크거나 같다. 맨하탄 거리 d는 |a1 - b1| + |a2 - b2| 이다.

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
:star: n과 m의 최소 공배수는 'n * m / 최대공약수'이다. 


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
### 비밀지도
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
### 다트 게임
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

