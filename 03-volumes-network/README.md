# 03. 볼륨 & 네트워크

## 볼륨 (Volume)

컨테이너는 종료되면 데이터가 사라짐.
볼륨을 사용하면 컨테이너가 종료돼도 데이터 유지 가능!

---

## 네트워크 (Network)

컨테이너끼리 서로 통신할 수 있게 연결해주는 것.
같은 네트워크에 있어야 컨테이너끼리 접근 가능!

---

## docker-compose.yml 구조
```yaml
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root1234
      MYSQL_DATABASE: testdb
    ports:
      - "3306:3306"
    volumes:
      - db-data:/var/lib/mysql  # 볼륨 연결
    networks:
      - my-network              # 네트워크 연결

  app:
    build: ../01-basics/hello-docker
    ports:
      - "8000:8000"
    networks:
      - my-network              # 같은 네트워크 연결

volumes:
  db-data:                      # 볼륨 생성

networks:
  my-network:                   # 네트워크 생성
```

---

## 볼륨 없으면 vs 있으면

볼륨 없으면:
컨테이너 종료 -> DB 데이터 전부 사라짐

볼륨 있으면:
컨테이너 종료 -> 볼륨에 데이터 유지 -> 재실행해도 데이터 그대로!

---

## 네트워크 없으면 vs 있으면

네트워크 없으면:
app 컨테이너 -> db 컨테이너 접근 불가

네트워크 있으면:
app 컨테이너 -> db 컨테이너 접근 가능
= 실제 서비스처럼 앱이 DB에 접근 가능!

---

## 실무 연결

백엔드 앱 -> DB에 데이터 저장/조회
= 네트워크로 연결 + 볼륨으로 데이터 유지