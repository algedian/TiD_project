# TiD_project
2016-2 Topics in Database Team project

- 환경구성
  - Ubuntu 16.04
  - OpenCV 2.4.13?
  - FFMpeg

- 파이썬 스크립트 사용 방법
  - video2frame.py
    - `--filename, --framefolder` option
      - 현재 상태는 아래와 같이 사용한다
      - `framefolderpath =  "./" + ==framefolder== + "/frames" `
      - ` vidcap = cv2.VideoCapture("./" + ==framefolder== + "/" + ==filename== + ".mp4") `
  - image2video.py
    - 나중에 추가합니다.
