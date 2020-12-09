---
layout: post
title: Windows pysqlcipher 설치하기(x64, win10, sqlcipher, open ssl, vs2019) 
tags: [sqlcipher, pysqlcipher]
comments: true
---

sqlite를 사용하다가 sqlcipher를 파이썬에서 사용해야 하는 일이 생겼다.
그래서 설치 좀 해볼까 했는데 정말 안됐다.
인터넷에서 여기저기 돌아다니면서 해봤지만 다 안되고
결국 핸드폰 루팅의 끝판은 순정이라는 말이 있듯이 공식 메뉴얼을 보고 성공했다.

### 1. [Win64 setup — Compiling SQLCipher](https://github.com/sqlitebrowser/sqlitebrowser/wiki/Win64-setup-%E2%80%94-Compiling-SQLCipher)

요령부리지말고 시키는대로 하면 된다.. 쉽게할려고 블로그 찾다가 하루를 날려보고 깨달았다

open ssl은 설치를 마친 후 무조건! 환경변수 설정을 해야한다. OPENSSL_CONF도 시스템 변수에 추가하는 것을 잊지말자 

### 2. [pysqlcipher](https://github.com/rigglemania/pysqlcipher3)

여기는 다 그대로 하면 되는데 vs 2019 community edition의 경우에는 경로가 조금 다르다.

C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29333\include

open ssl 폴더를 위의 경로에 넣어줘야 한다.

그리고 sqlite3.lib sqlcipher.lib(1단계에서 sqlchiper 빌드에 성공하면 나옴) 두 파일을 C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29333\lib\x64 경로로 넣어준다.

위의 과정을 다 마치고 깃헙에서 클론을 해와서 설치를 진행하면 된다..!! 

```
$ git clone https://github.com/rigglemania/pysqlcipher3
$ cd pysqlcipher3
$ python setup.py build
$ python setup.py install
```

만약 pysqlcipher 의 src 폴더 경로의 헤더파일들이 sqlcipher.h 를 가져올 수 없다고 나오면 헤더파일에 가서 sqlcipher/sqlcipher.h 를 sqlcipher.h 로 변경하는 작업을 하자.
그리고 해당 폴더에 sqlcipher.h를 복사해서 넣어주면 된다



