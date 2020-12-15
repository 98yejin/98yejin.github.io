---
layout: post
title: Windows powershell 오류 고치기
tags: [windows, powershell]
comments: true
---

처음 윈도우즈 파워쉘을 실행했을 때도.. 뭘 설치하려고 할 때도 항상

```
                . : 이 시스템에서 스크립트를 실행할 수 없으므로 C:\Users\yejinpark\Documents\WindowsPowerShell\profile.ps1 파일을 로드  할 수 없습니다. 자세한 내용은 about_Execution_Policies(https://go.microsoft.com/fwlink/?LinkID=135170)를 참조하십시오.  위치 줄:1 문자:3
+ . 'C:\Users\yejinpark\Documents\WindowsPowerShell\profile.ps1'
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : 보안 오류: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
    
```

위와 같은 경고문이 나왔다.

그리고 찾은 해결 방법

1. 관리자 권한으로 윈도우즈 파워쉘을 실행한다.

2. 'ExecutionPolicy' 라고 입력해보자.

```
Restricted
```

라고 반환되면 운이 좋은거다. 여기 나오는 방법으로 해결이 된다. 만약 Unrestricted라고 나오면 다른 해결 방법을 찾아야 한다.

3. 'Set-ExecutionPolicy Unrestricted' 라고 입력해보자.

4. 이제 마지막으로 'ExecutionPolicy' 라고 입력해보자. 'Unrestricted'라고 나오면 다시 모듈을 사용해서 뭐든 해보자. 


