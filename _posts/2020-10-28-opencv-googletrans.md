---
layout: post
title: Python과 OpenCV로 실시간 번역기 만들기
subtitle: 특정 영역 모니터링
tags: [python, translate, googletrans,pytesseract, pynput, PIL, mss, cv2]
comments: true
---

## 왜🍳?

기껏 [스크립트 번역기](https://98yejin.github.io/2020-10-28-cognitive-class/)를 만들었는데, 이번 달에 수강해야하는 강의에는 스크립트가 안올라와 있었다..
대신 자막이 동영상 자체에 올라와 있었다.
그래서 자막을 바로 바로 받아와서 처리하면 되겠다고 생각했다.

## 사용한 라이브러리🍖

- numpy : 영상이 사실상 행렬이니까 많이 쓰게 된다
- cv2 : 말할 필요도 없는 OpenCV
- mss : 빠른 스크린샷을 찍을 때 많이 쓰는 라이브러리
- PIL : Python Imaging Library 니까 Python에서 영상 처리를 할 때 쓰겠구나라고 생각할 수 있고 그게 맞다. 참고로 설치할 때는 pip install pillow로 설치한다.
- pynput : 마우스 이벤트 처리할 때 쓴다
- pytesseract : tesseract라고 영상에서 텍스트만 뽑아올 때 쓰는 라이브러리다. 구글에서 하는 프로젝트라고 들었던 것 같다.
- googletrans : 어제도 썼던 번역 용도

## 결과🍧

pytesseract의 정확도가 안좋아서 굳이 쓸 필요가 없을 정도다. 번역이야 문장들을 다시 붙여줘서 다시 하니까 훨씬 낫긴 한데.. 그렇게 하면 실시간 처리라기보단.. 약간 멈칫!했다가 실행되는 느낌??

그냥 영어 실력도 늘릴 겸 영어로 강의를 듣는게 좋을 것 같다. 근데 c++을 사용하면 쓸만한 결과물이 나올거같다. 영상 전처리만 해주면 속도도 빨라지고 정확도도 올라갈테니..



## 과정(코드)🥞

```python
import numpy as np
import cv2
from mss import mss
from PIL import Image
from pynput.mouse import Button, Controller as MouseController
from pytesseract import *
from googletrans import Translator
```

꽤 많은 라이브러리들을 불러왔다. 사실 쓸 필요 없는 것도 보이는데, 일단은 빨리 빨리 만들어보고 싶어서 효율성은 별로 신경안쓰고 만들었다.
개발은 일단 실행이 되게 만드는 것부터 시작해야한다고 생각한다. 그러고나서 점진적으로 개선하고... 처음부터 완벽하게 하려다가 되는게 없다는 것을 알게되고 마음을 바꿨다..

참고로 pynput을 호출할 때 Controller as MouseController라고 한 이유는 원래 마우스만 불러온게 아니라, 키보드도 불러왔었기 때문이다.
그런데 내 편의성만 줄이면 굳이 불러올 필요가 없어서, 그냥 빼고 마우스만 사용했다. 지금 보니까 Button은 안불러와도 됐을거같다. 

```python

def mouse_location():
	mouse = MouseController()

	location = []
	cnt = 0

	if (input() == 's'):
		print ("Current position: " + str(mouse.position))
		location.append(mouse.position)
		cnt += 1

	if (input() == 'e'):
		print ("Current position: " + str(mouse.position))
		location.append(mouse.position)
		cnt += 1

	if cnt == 2:
		top = location[0][1]
		left = location[0][0]
		width = abs(location[1][0] - location[0][0])
		height = abs(location[0][1] - location[1][1])
		return [top, left, width, height]
```

마우스 위치를 받아온다. 사실 리스너 불러와서하면 더 예쁘게 할 수 있다. 편의성을 높여서 마우스 드래그도 되고.. 근데 그러면 괜히 더 느려지고, 외부 라이브러리를 더 불러와야하길래
일단 기능만 테스트하는 목적이니까 기본적인 input()함수를 사용해서 마우스 위치를 받아왔다.

```python
def trans(en_txt):
	translator = Translator()
	result = translator.translate(en_txt, dest='ko').text
	return result
```

번역하는 부분이다. [저번 포스팅](https://98yejin.github.io/2020-10-28-cognitive-class/)에서 자세히 설명했으니까 패스.

```python
def main():

	location = mouse_location()
	bounding_box = {'top': location[0], 'left': location[1], 'width': location[2], 'height': location[3]}

	sct = mss()

	translate = []
	while True:
		# 영역 지정
		sct_img = sct.grab(bounding_box)
		cv2.imshow('screen', np.array(sct_img))
		# img to txt
		img = Image.fromarray(np.array(sct_img))
		txt = pytesseract.image_to_string(img, lang='eng')

		if len(translate) == 0:
			translate.append(txt)
			print(trans(txt))
		elif translate[len(translate)-1] != txt and len(txt)!= 0:
			translate.append(txt)
			print(trans(txt))

		if (cv2.waitKey(1) & 0xFF) == ord('q'):
			cv2.destroyAllWindows()
			break
			
if __name__ == '__main__':
	main()
```

main함수다. 위에서 지정한 마우스 s(start coordinate), e(end coordinate)에 맞게 바운딩 박스를 만들어서, 내가 원하는 영역만 계속 보게 해준다.

이게 모니터링이니까.. 음.. 동영상에서 특정 인물을 찾아야할때 여기에 얼굴 인식 모델 하나만 불러와서 쓰면 될 것 같다..

저번에 드라마보니까 특정 색의 옷을 입은 사람을 찾기위해 영상에 필터를 끼워서 검사하는 것도 봤는데, 그렇게 해봐도 재밌을 것 같다.

조금 헷갈렸던 부분이 pytesseract에 np array를 넣는 방법이었는데.. 그냥 fromarray로 하니까 되서 조금 허무했다 ㅋㅋㅋ

역시 문서를 제대로 읽어야하는 것 같다.

그리고 저 if, elif 부분은 영어 문장을 어제도 했던 것처럼.. 문장이 끊어져있으면 이어주는 용도로 만들다가 만거다.

한번 실행해보고 이정도가지고는 어디 못쓰겠다는 생각을 해서 깔끔하게 중단했다.

이제 곧. . 저녁을 먹어야하기때문에.. 코딩을 할 수가 없다.. 배가 부르고 나서도 .. 이걸 개선하고 싶다면 개선하겠지만.. 뭔가 그럴거같지않다..ㅎ

또 다른거 만들어보고 싶어져서 아마 내일도 안할거같고.. 다음에 또 생각이 나면 한번 c++로 해봐야겠다..


## 실행 동영상🍕

보여주기 위한거니까.. 영어가 어떻게 인식되는지도 출력하기위해 print(trans(txt))의 위에 print(txt)를 추가했다

[![Video Label](http://img.youtube.com/vi/wYYoG-9jo3A/0.jpg)](https://youtu.be/wYYoG-9jo3A)

클릭하면 동영상으로 이동!
