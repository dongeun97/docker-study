01. 도커 기본 개념 & 첫 실습
? 도커란?
앱 실행에 필요한 **모든 것(코드, 라이브러리, 환경설정)**을 하나의 컨테이너에 담아서, 어디서든 똑같이 실행되게 해주는 기술.

"내 컴퓨터에서는 되는데 서버에서는 왜 안 되지?" → 이 문제를 해결해준다!


? 핵심 개념 3가지
1. Image (이미지) ? ? 설계도

컨테이너를 만들기 위한 읽기 전용 템플릿
Docker Hub에서 남이 만든 이미지를 가져다 쓸 수 있음
예: nginx, python:3.11, ubuntu 등

2. Container (컨테이너) ? ? 실행 중인 인스턴스

이미지를 실제로 실행한 것
이미지 1개로 컨테이너를 여러 개 만들 수 있음
VM(가상머신)보다 훨씬 가볍고 빠름

3. Dockerfile ? ? 레시피

이미지를 어떻게 만들지 적어놓은 텍스트 파일
예: "Ubuntu 깔고 → Python 설치하고 → 내 코드 복사해"


? VM vs Docker
가상머신 (VM)도커 (Container)크기수 GB수 MB시작 속도수 분수 초OS 포함? (OS 전체)? (호스트 OS 공유)격리 수준완전 격리프로세스 격리

?? 기본 명령어
bash# 이미지 받아서 컨테이너 실행
docker run <이미지명>

# 백그라운드 실행 + 포트 연결
docker run -d -p 호스트포트:컨테이너포트 <이미지명>

# 실행 중인 컨테이너 목록
docker ps

# 모든 컨테이너 목록 (종료된 것 포함)
docker ps -a

# 컨테이너 중지
docker stop <컨테이너ID>

# 컨테이너 삭제
docker rm <컨테이너ID>

# 이미지 목록
docker images

# 이미지 삭제
docker rmi <이미지명>

? 실습 1 ? Hello World
bashdocker run hello-world
동작 과정:

로컬에 hello-world 이미지 없음 확인
Docker Hub에서 자동으로 이미지 다운로드
다운받은 이미지로 컨테이너 생성
컨테이너 실행 → Hello from Docker! 출력 후 종료


? 실습 2 ? nginx 웹서버 띄우기
bashdocker run -d -p 8080:80 nginx

-d : 백그라운드 실행 (터미널이 안 막힘)
-p 8080:80 : 내 컴퓨터 8080포트 → 컨테이너 80포트 연결

브라우저에서 http://localhost:8080 접속 → nginx 웹서버 확인 ?

? 알게 된 것

Docker Hub = 이미지 저장소 (npm 같은 개념)
docker run 하면 이미지가 없을 경우 자동으로 다운받아줌
-d 옵션으로 백그라운드 실행, -p로 포트 연결
hello-world는 실행 후 바로 종료 (?), nginx는 계속 실행 중 (?)
Jenkins + Docker 조합: Jenkins가 코드 변경을 감지 → Docker 이미지 빌드 → 서버에 배포