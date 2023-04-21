## file error
```
Traceback (most recent call last):
  File "D:\image\image.py", line 80, in <module>
    cv2.imshow(cropped_basename, cropped_image)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
cv2.error: OpenCV(4.7.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:971: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'
```
* input file 없어서 생긴 error, argv[1] 값을 넣어주자

### datetime error
(base) PS D:\image> py .\image.py .\cat.bmp
Traceback (most recent call last):
  File "D:\image\image.py", line 7, in <module>
    time_value=datetime.now().strftime('%c').replace(" ","").replace(".","_")
module 'datetime' has no attribute 'now'

* datetime은 기본적으로 type, value가 따로 묶여서 저장된다. str으로 형변환 해주자


### name error

Traceback (most recent call last):
  File "D:\image\image.py", line 76, in <module>
    cv2.imwrite(name, roi)
cv2.error: OpenCV(4.7.0) D:\a\opencv-python\opencv-python\opencv\modules\imgcodecs\src\loadsave.cpp:692: error: (-2:Unspecified error) could not find a writer for the specified extension in function 'cv::imwrite_'

* 구체적으로는 string형태와 확장자가 없어서 생긴 에러이다. 제목형태를 맞춰주자

### type error

UnboundLocalError                         Traceback (most recent call last)
Cell In[21], line 15, in onMouse(event, x, y, flags, param)
     13 color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
     14 #print (color)
---> 15 str =''.join(map(str,color))
     16 if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼 다운, 드래그 시작 
     17     isDragging = True

UnboundLocalError: cannot access local variable 'str' where it is not associated with a value

localvalue에 접근 할수 없는 에러 정확히는 str 함수랑 변수명이 str로 같아서 생긴 에러이다.

### 응답없음

입력이미지 변수명과 크기를 다시 계산해보자.. 


## crop error

