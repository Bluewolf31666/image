import os
import sys
import cv2
from datetime import datetime
import time

time_value=str(datetime.now()).replace(" ","").replace(".","_").replace(":","_").replace("-","_")
print(time_value)
# 선택한 사각형을 정의하는 좌표는 select_coords에 저장됩니다.
select_coords = []
# 사각형을 누르고 있는동안, selecting은 True가 됩니다.
selecting = False

def get_square_coords(x, y, cx, cy):
    """
    cx, cy = 사각형 시작  x,y
    x,y 마지막 지점의 x,y

    """

    # 선택한 지점으로부터 마지막으로 드래그한 지점까지의 길이를 계산, 단 음수가 되지 않도록
    a = max(abs(cx-x), abs(cy-y))
    a = min(a, w-cx, cx, h-cy, cy)
    return cx-a, cy-a, cx+a, cy+a


def region_selection(event, x, y, flags, param): 
    """마우스를 클릭할때 시작하는 콜백 함수."""
    global select_coords, selecting, image

    if event == cv2.EVENT_LBUTTONDOWN: 
        # 왼쪽 마우스를 누를때 시작함
        # 시작 지점저장 및 selecting 변수를 True로 저장
        select_coords = [(x, y)]
        selecting = True

    elif event == cv2.EVENT_MOUSEMOVE and selecting:
        # 드래그 및 이동시 사각형 위치 update
        image = clone.copy()
        x0, y0, x1, y1 = get_square_coords(x, y, *select_coords[0]) #가변인자(인자의 개수가 정해지지 않은 함수)로 받는다는 뜻
        #cv2.rectangle(image, (x0, y0), (x1, y1), (0, 255, 0), 2) #사각형 표시

    elif event == cv2.EVENT_LBUTTONUP: 
        # 마우스를 떘을때, 최종적으로 x,y 업데이트 및 false로 변환
        select_coords.append((x, y))
        selecting = False


# path없이 이미지 로딩, 대신 python 실행시 인자값 필요
filename = sys.argv[1]
basename = os.path.basename(filename) #파일 이름 따로 저장
image = cv2.imread(filename)
h, w = image.shape[:2] #자동으로 shape 저장
# 저장되는 이미지 이름 변수 저장
cropped_filename = os.path.splitext(filename)[0]+time_value +'.jpg'
cropped_basename = os.path.basename(cropped_filename)
# 원본 이미지 저장(crop과정에서 변화하지 않도록).
clone = image.copy() 
# 새로운 창을 파일이름으로 실행및 콜백함수 실행.
cv2.namedWindow(basename) 
cv2.setMouseCallback(basename, region_selection)

# c키가 눌리는지 아닌지 확인.
while True: 
    # 원본 이미지 보여주면서 c키를 누르는 것을 대기
    cv2.imshow(basename, image) 
    key = cv2.waitKey(1) & 0xFF
    # c가 눌린다면 while문 탈출
    if key == ord("c"): 
        break

# 지역이 선택되었는지 확인
if len(select_coords) == 2: 
    cx, cy = select_coords[0]
    x, y = select_coords[1]
    x0, y0, x1, y1 = get_square_coords(x, y, cx, cy)
    #crop된 이미지 저장 및 보여주기
    cropped_image = clone[y0:y1, x0:x1]
    cv2.imshow(cropped_basename, cropped_image) 
    cv2.imwrite(cropped_filename, cropped_image)
    # 아무키나 눌려지는것 기다림
    cv2.waitKey(0)

# 끝이므로 모든 창 종료
cv2.destroyAllWindows()