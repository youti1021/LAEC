import cv2
import numpy as np
import pyautogui
import time

template_paths = ['./pic/play.png', './pic/next.png', './pic/skip.png']

try:
    while True:
        # 화면을 캡처하여 numpy 배열로 변환
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)

        # OpenCV를 사용하여 BGR에서 RGB로 변환 (스크린샷은 기본적으로 RGB 포맷이므로 BGR로 변환 불필요)
        screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        for template_path in template_paths:
            # 템플릿 이미지를 읽어오기
            template = cv2.imread(template_path, cv2.IMREAD_COLOR)

            # 템플릿 이미지가 3채널 BGR 형식인지 확인
            if template.shape[2] == 4:  # 템플릿이 4채널인 경우
                template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)  # 3채널로 변환

            # 매칭 메소드 (여기서는 TM_CCOEFF_NORMED를 사용)
            result = cv2.matchTemplate(screenshot_rgb, template, cv2.TM_CCOEFF_NORMED)

            # 결과에서 최대 매칭값 및 그 위치를 찾기
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            threshold = 0.68  # 나머지 이미지들은 68% 이상 매칭될 때

            if max_val >= threshold:
                template_height, template_width = template.shape[:2]

                # 이미지가 발견된 위치의 중앙으로 좌표 계산
                center_x = max_loc[0] + template_width // 2
                center_y = max_loc[1] + template_height // 2

                pyautogui.click(center_x, center_y)
                print(f"'{template_path}' 이미지 발견! 클릭 위치: ({center_x}, {center_y})")
            else:
                # 매칭값이 임계값보다 낮을 경우 메시지 출력
                print(f"'{template_path}' 이미지를 찾을 수 없습니다.")

        # 잠시 대기 후 다시 시도 (예: 1초 대기)
        time.sleep(5)

except KeyboardInterrupt:
    print("프로그램이 사용자의 요청으로 종료되었습니다.")
