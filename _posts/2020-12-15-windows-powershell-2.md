---
layout: post
title: Windows Powershell로 컴퓨터 재부팅(다시 시작)이 필요한지 판단하는 방법
tags: [windows, powershell]
comments: true
---

## Windows 재부팅 필요 여부 

1. Windows Powershell 에 들어가서 PendingReboot 모듈을 설치한다.
```
Install-Module -Name PendingReboot
```

2. 모듈을 사용한다.
```
1. Test-PendingReboot -Detailed # 자세한 정보를 알 수 있다.
2. Test-PendingReboot # 재부팅 필요 여부만 알 수 있다.
```

---

## Python에서 Powershell 사용하기 

파이썬에서 Windows Powershell 사용하는 방법은 파이썬에서 cmd를 사용하는 방법과 비슷하다.

[예시 1](https://stackoverflow.com/questions/21944895/running-powershell-script-within-python-script-how-to-make-python-print-the-pow).
```python3
import subprocess
import sys
p = subprocess.Popen(['powershell.exe', 'C:\\Temp\\test.ps1'], stdout=sys.stdout)
```

[예시 2](https://www.phillipsj.net/posts/executing-powershell-from-python/).

```python3
import subprocess

def run(self, cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed
```

