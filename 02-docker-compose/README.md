# 02. Docker Compose

## Docker Compose란?

여러 컨테이너를 한번 관리하는 도구
docker run을 여러번 할 필요 없이 docker-compose.yml 파일 하나로 한번에 실행/종류 가능


---

## 기존 방식 vs Docker Compose

기존 방식:
docker run -d -p 8080:80 nginx
docker run -p 8000:8000 my-app

Docker Copose 방식:
docker-compose up

## docker-compose.yml 구조
```yaml
services:
  web:
    image: nginx        # Docker Hub에서 이미지 가져옴
    ports:
      - "8080:80"       # 내 컴퓨터 8080 -> 컨테이너 80
  app:
    build: ../01-basics/hello-docker  # Dockerfile로 직접 빌드
    ports:
      - "8000:8000"     # 내 컴퓨터 8000 -> 컨테이너 8000
```

---


## image vs build 차이

image: nginx   -> Docker Hub에서 남이 만든 이미지 가져올 때
build: 경로    -> 내가 만든 Dockerfile로 직접 빌드할 때

---

## 포트 설정이 두 곳에 있는 이유

app.py 안의 포트  -> 컨테이너 안에서 열어놓는 방 번호
docker-compose 포트 -> 외부(브라우저)에서 접근할 수 있게 연결

둘 다 설정해야 브라우저에서 접근 가능!

---

## 주요 명령어

docker-compose up      # 전체 컨테이너 실행
docker-compose down    # 전체 컨테이너 종료
docker-compose up -d   # 백그라운드로 실행

---

## Docker Compose vs 쿠버네티스

Docker Compose  = 내 컴퓨터에서 여러 컨테이너 관리
쿠버네티스      = 실제 서버에서 여러 컨테이너 관리 (자동 복구, 자동 확장)