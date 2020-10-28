---
layout: post
title: Cognitive class.ai 강의 조금 더 편하게 듣기!
subtitle: 파이썬 뚝딱 뚝딱😗
tags: [ibm, clouders, cognitive class, python]
comments: true
---

클라우더스에서는 매달 스킬 업 미션으로 Cognitive Class에서 정해진 코스를 하나 수강하게 한다.

매달 의무적으로 공부해야 하는 건 정말 좋다. 하지만.. 내 영어 실력이 뛰어나지 않은 건 문제가 된다..!

어느정도는 알아듣지만.. 가끔씩 모르는 단어도 있고, 내가 제대로 이해한게 맞는지 확인하고 싶어진다. 

그래서 만들었다! 이걸 번역기라고 해야할지.. 뭐라 해야할지 모르겠지만 ㅋㅋㅋㅋ 날 위한 프로그램..!

## 왜 만들었나🤨?

![why](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/trans/why-en.PNG?raw=true)

자, 이걸 보면 강의 옆에 친절하게 스크립트가 적혀있다. 천천히 집중해서 보면 영어 실력도 오르고 클라우드 실력도 오르겠지만..
가끔씩 바쁠 때에는.. 조금 힘들다 ㅎㅎ 아니면 너무 많이 공부해서 머리가 아픈날이라던가! 그럴때는 영어가 읽기 싫다!

![why-ko](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/trans/why.PNG?raw=true)

그래서 구글 확장 기능을 사용해서 번역해서 본다..? 어후.. 딱봐도 알겠지만 차라리 영어로 읽는게 나을정도다 ㅎㅎ

물론 구글 번역이 나쁜게 아니고 스크립트가 하나 하나 끊겨있다보니 그런거지만 ...

![ah-ha](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/trans/4414e4b03504654e00abf12f2b51b7b9.jpg?raw=true)

그러면 스크립트를 다시 붙여주면 되겠구나!

라고 생각했다. 아주 간단한 생각 ㅎ 게다가 Cognitive Class.ai 는 정말 친절하다. 스크립트를 다운로드 받을 수 있게 해준다.

그리고 문자열 처리는 파이썬이 제일 쉽다. 다른 언어가 더 쉬울수도 있겠지만 일단 나한테는 파이썬이 제일 쉽다.

## 그래서 결과물은🙄?

![compare](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/trans/compare.PNG?raw=true)

왼쪽 텍스트파일이 결과물이고, 왼쪽이 홈페이지에서 바로바로 되는 구글 번역이다. 사람에 따라 다를 수도 있겠지만 일단 나한테는 내 프로그램의 결과물이 더 보기좋다.

내가 보기편하려고 만들었으니까 ㅎ..

## 프로그램 실행방법

![folder](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/trans/%EC%BA%A1%EC%B2%98.PNG?raw=true)

1. 번역하고 싶은 스크립트들이 담긴 폴더를 만든다. 나의 경우에는 before 폴더가 번역하고 싶은 폴더다.
![before](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/trans/before.PNG?raw=true)

2. script.exe를 더블 클릭한다.

![cmd](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/trans/1.PNG?raw=true)

3. 이런 창이 나온다. 여기에 1번에서 만든 폴더를 입력해주면 된다. 나는 before라고 입력했다. 그리고 나면 ㅁㅁㅁ.txt complete, ㅁㅁㅁㅁㅁ.txt complete... 진행 과정을 알려주고.. 종료되면 꺼진다.
4. result 폴더를 확인해보자.

![result](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/trans/result.PNG?raw=true)

여기에 번역된 파일들이 있다. 참고로 번역된 파일은 '번역 전 파일 제목-translated.txt'로 나온다.

### 영문 파일과 한글 파일을 비교해보자🍥

![en](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/trans/before-script.PNG?raw=true)

이게 다운로드 받은 파일 

![ko](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/trans/after-script.PNG?raw=true)

이게 결과물!

### 코드

```python
from googletrans import Translator
import os
```
사용한 라이브러리.

googletrans 는 pip로 설치하면 된다.

```python
def cleanup(script):
	result = ""
	for s in script:
		if s[len(s)-2] == '.':
			result += s
		else:
			result += s.replace('\n', ' ')
	return result

def trans(script):
	translator = Translator()
	result = translator.translate(script, dest='ko').text
	return result
```

딱 두개 함수만 만들었다. 사실 함수 만들 필요도 없이 간단했지만, 그래도 함수 만드는게 예쁘고 깔끔하니까 만들었다.

cleanup함수는 스크립트를 일반적인 문장처럼 만들어주고,
trans함수는 스크립트를 한국어로 번역해준다.


```python
def main():
	folder = input('Folder containing files to be translated :')
	title_list = os.listdir('./'+folder+'/')
	for title in title_list:
		with open('./'+folder+'/'+title, 'r', -1, 'utf-8') as file:
			content = file.readlines()
		result = cleanup(content)

		with open('./result/'+title[:len(title)-4]+'-translated.txt', 'w', -1, 'utf-8') as file:
			file.write(trans(result))
		print(title+' complete')


if __name__ == "__main__":
	main()
```

메인함수에서는 보이는 그대로 번역할 문서가 담긴 폴더 이름을 입력받고, 함수들을 호출하고 결과물을 내준다.


