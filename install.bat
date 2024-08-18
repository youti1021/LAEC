@echo off
setlocal

REM GitHub 리포지토리 ZIP 파일 URL 설정
set "REPO_URL=https://github.com/youti1021/LAEC/archive/refs/heads/main.zip"
set "OUTPUT_ZIP=LAEC-main.zip"
set "EXTRACT_DIR=LAEC-main"

REM 현재 스크립트의 경로를 변수로 저장
set "SELF_DELETE_CMD=del /q /f %~f0"

REM ZIP 파일 다운로드
echo Downloading LAEC repository...
powershell -Command "Invoke-WebRequest -Uri %REPO_URL% -OutFile %OUTPUT_ZIP%"

REM ZIP 파일 압축 해제
echo Extracting the ZIP file...
powershell -Command "Expand-Archive -Path %OUTPUT_ZIP% -DestinationPath . -Force"

REM 압축 해제된 디렉터리로 이동
cd %EXTRACT_DIR%

REM 필요한 Python 패키지 설치
echo Installing required Python packages...
python -m pip install pillow pyscreeze pyautogui numpy opencv-python

REM Python 스크립트 실행
echo Running index.py...
python -m index.py

REM 배치 파일 삭제
echo Deleting the batch file...
start /b "" cmd /c "%SELF_DELETE_CMD%"

endlocal
