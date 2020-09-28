---
layout: post
title: Codility 코딜리티 lesson1. Iterations, lesson2. Arrays
subtitle: 문제 풀이
tags: [python, codility]
comments: true
---

코딜리티 코딜리티 말만 들었지 처음 풀어보는데 프로그래머스랑 문제 풀이 환경이 비슷하다!
테스트 케이스 추가하는 방법이 다르고, 코딜리티는 시간 복잡도를 보여준다
그리고 무슨 테스트케이스 틀렸는지 보여줘서 디버깅할때 좋다

## lesson1. Iterations

### 1. BinaryGap
Find longest sequence of zeros in binary representation of an integer.

```python
def solution(N):
    list1 = []
    for c, i in enumerate(bin(N)):
        if i == '1':
            list1.append(c)
    tmp = []
    for i in range(len(list1)-1):
        tmp.append(list1[i+1]-list1[i]-1)
    answer = 0
    if len(tmp) != 0:
        answer = max(tmp)
    return answer
```

## lesson2. Arrays

### 1. CyclicRotation
Rotate an array to the right by a given number of steps.

```python
def solution(A, K):
    if len(A) == 0:
        return A
    N=len(A)-1
    while (K>0):
        K -= 1
        A = [A[N]]+A[:N]
    return A
```

### 2. OddOccurrencesInArray
Find value that occurs in odd number of elements.

```python
def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort() 
    for i in range(0, len(A), 2):
        if i+1 == len(A):
            return A[i]
        elif A[i] != A[i+1]:
            return A[i]
```

Detected time complexity: O(N) or O(N*log(N))

처음에 
```python
def solution(A):
    tmp = set(A)
    ans = {A.count(t):t for t in tmp}
    return ans[1]
```
이렇게 풀었다가 시간복잡도는 당연히 O(N**2)에다가 어딘가 틀린 부분도 있어서 많이 고민했다
얼마전에 프로그래머스에서 hash 써서 효율 높였다고 신나서 여기저기 hash 쓰고 다닌게 문제였던 것 같다
자료구조는 반드시 적재적소에..
테스트케이스로 [3,3,9,9,10] 이거만 추가해보면 i+1 == len(A) 추가해야하는거 바로 알 수 있었는데
테스트 케이스 추가해서 실험해볼 생각을 못했던게 패착.. 
