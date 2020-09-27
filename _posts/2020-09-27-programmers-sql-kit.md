---
layout: post
title: 프로그래머스 SQL 고득점 Kit
subtitle: 문제 풀이
tags: [sql, programmers]
comments: true
---

SQL에 대한 기억을 되살릴 겸 문제를 풀어보았다. 다른 사람들 풀이 보니까 Inner join이나 Full outer join 같은거 많이 사용하던데... 나는 그냥 내가 기억나는 내가 편한 방법대로 했다..
다 풀고 나니까 어느새 밤 ^^..

### SELECT
1. 모든 레코드 조회하기
```
    SELECT ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
```
2. 역순 정렬하기
```
    SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC
```
3. 아픈 동물 찾기
```
    SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION='Sick' GROUP BY ANIMAL_ID
```
4. 어린 동물 찾기
```
    SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged' ORDER BY ANIMAL_ID
```
5. 동물의 아이디와 이름
```
    SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID
```
6. 여러 기준으로 정렬하기
```
    SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC
```
7. 상위 n개 레코드 : LIMIT 
```
    SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1
```

### SUM, MAX, MIN
1. 최댓값 구하기
```
SELECT MAX(DATETIME) AS '시간' FROM ANIMAL_INS
```
2. 최솟값 구하기
```
SELECT MIN(DATETIME) FROM ANIMAL_INS
```
3. 동물 수 구하기
```
SELECT COUNT(ANIMAL_ID) AS 'count' FROM ANIMAL_INS
```
4. 중복 제거하기
```
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
```

### GROUP BY
1. 고양이와 개는 몇 마리 있을까 
```
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count 
FROM ANIMAL_INS 
WHERE ANIMAL_TYPE IN ('Cat', 'Dog') 
GROUP BY ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE
```
2. 동명 동물 수 찾기 : COUNT, GROUP BY, HAVING
```
SELECT NAME, COUNT(NAME) AS 'COUNT' 
FROM ANIMAL_INS 
GROUP BY NAME 
HAVING COUNT>1 
ORDER BY NAME
```
3. 입양 시각 구하기(1) : HOUR(), AS 
```
SELECT HOUR(DATETIME) AS 'HOUR', COUNT(HOUR(DATETIME)) AS 'COUNT' 
FROM ANIMAL_OUTS 
WHERE (HOUR(DATETIME)>8 AND HOUR(DATETIME)<20) 
GROUP BY (HOUR(DATETIME)) 
ORDER BY (HOUR(DATETIME))
```
4. 입양 시각 구하기(2) : SET
```
SET @hour := -1;
SELECT (@hour := @hour +1) AS 'HOUR', 
(SELECT COUNT(*) FROM animal_outs WHERE hour(datetime)=@hour) AS 'COUNT' 
FROM animal_outs 
WHERE @hour < 23
```

### IS NULL
1. 이름이 없는 동물의 아이디 : IS NULL
```
select animal_id as ANIMAL_ID from animal_ins where name is null order by animal_id
```
2. 이름이 있는 동물의 아이디 : IS NOT NULL
```
select animal_id as ANIMAL_ID from animal_ins where name is not null order by animal_id
```
3. NULL 처리하기 : IFNULL(,)
```
select animal_type as ANIMAL_TYPE, ifnull(name, 'No name') as NAME, sex_upon_intake as SEX_UPON_INTAKE 
from animal_ins
```
이 부분은.. NULL 처리 어떻게 하는지 기억안나서 구글링 하다가 다른 사람들이 소문자로 쓴거보고 
그제서야 소문자를 써도 된다는 것을 깨닫고 소문자로 풀었던 부분 ㅋㅋㅋ
근데 대문자가 가독성 더 좋은거 같아서 이 다음부터는 대문자로 풀었다

### JOIN
1. 없어진 기록 찾기
```
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_OUTS AS T1 
WHERE T1.ANIMAL_ID NOT IN (SELECT T2.ANIMAL_ID FROM ANIMAL_INS AS T2) 
ORDER BY ANIMAL_ID
```
2. 있었는데요 없었습니다 
```
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME 
FROM ANIMAL_INS, ANIMAL_OUTS 
WHERE ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME AND ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID 
ORDER BY ANIMAL_INS.DATETIME
```
3. 오랜 기간 보호한 동물(1) 
```
SELECT NAME, DATETIME 
FROM ANIMAL_INS 
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS) 
ORDER BY DATETIME 
LIMIT 3
```
4. 보호소에서 중성화한 동물 
```
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.ANIMAL_TYPE, ANIMAL_INS.NAME 
FROM ANIMAL_INS, ANIMAL_OUTS 
WHERE ANIMAL_INS.SEX_UPON_INTAKE != ANIMAL_OUTS.SEX_UPON_OUTCOME AND ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID 
ORDER BY ANIMAL_ID
```

### String, Date
1. 루시와 엘라 찾기 : IN () 
```
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE 
FROM ANIMAL_INS 
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty') 
ORDER BY ANIMAL_ID
```
2. 이름에 el이 들어가는 동물 찾기 : LIKE
```
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'Dog' 
ORDER BY NAME
```
3. 중성화 여부 파악하기 : CASE
```
SELECT ANIMAL_ID, NAME, 
       CASE SEX_UPON_INTAKE WHEN 'Neutered Male' THEN 'O' WHEN 'Spayed Female' THEN 'O' ELSE 'X' END AS '중성화'
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID
```
4. 오랜 기간 보호한 동물(2) : TIMESTAMPDIFF
```
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME 
FROM ANIMAL_INS, ANIMAL_OUTS 
WHERE ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID 
ORDER BY TIMESTAMPDIFF(SECOND, ANIMAL_OUTS.DATETIME, ANIMAL_INS.DATETIME) 
LIMIT 2
```
5. DATETIME에서 DATE로 형 변환 : DATE_FORMAT
```
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, "%Y-%m-%d") AS '날짜' 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID
```


저녁에 풀기시작했는데 지금이 12시가 다되가는거보면 푸는데 꽤 오래 걸렸다..
하지만 알고리즘은 한두문제 푸는데도 다섯시간이 훌쩍가니까 뭐!
딱히 어려운 문제는 없었다.
알고리즘도 이정도 속도로만 풀리면 좋겠다.. 열심히 해야지!!!
