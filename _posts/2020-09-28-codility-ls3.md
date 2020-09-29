---
layout: post
title: Codility 코딜리티 Lesson 3 Time Complexity
subtitle: 문제 풀이
tags: [python, codility]
comments: true
---

## Lesson 3 Time Complexity


### 1. FrogJmp

Count minimal number of jumps from position X to Y.
```python
def solution(X, Y, D):
    if X==Y:
        return 0
    if (Y-X)%D == 0:
        return ((Y-X)//D)
    return ((Y-X)//D)+1
```
Detected time complexity: O(1)

문제 풀다보니까 느껴지는건데 수학이 엄청 중요한거같다..
Lesson 3까지만 풀고 백준가서 수학 문제를 풀어야겠다
1~N까지 더하는 문제도 for문 써서 할수도 있지만, n(n+1)/2 공식을 쓰면 확 빨라지고 (O(N)->O(1))
소수 찾는 문제도 에라토스네스의 체인가 그거 써서 푸니까 타임아웃이 됐던 문제가 풀렸다

### 2. PermMissingElem

Find the missing element in a given permutation.
```python
def solution(A):
    lst = [0] * (len(A)+1)
    for a in A:
        lst[a-1] = 1
    return lst.index(0)+1
```
