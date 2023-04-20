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

