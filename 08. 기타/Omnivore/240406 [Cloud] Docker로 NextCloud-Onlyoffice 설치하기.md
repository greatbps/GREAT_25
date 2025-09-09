---
id: 1fd1a5d3-a80f-4a43-a286-f22f50daf9f2
---

# [Cloud] Docker로 NextCloud-Onlyoffice 설치하기
#Omnivore
 
[Read on Omnivore](https://omnivore.app/me/cloud-docker-next-cloud-onlyoffice-18eb2c8b993)
[Read Original](https://velog.io/@ysy3285/AWS-Docker%EB%A1%9C-NextCloud-Onlyoffice-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)
 
![post-thumbnail](https://proxy-prod.omnivore-image-cache.app/0x0,stGoEhz8OAHj0LbF4ZI3oU7PklS7KUPIjFS8qbLmtqHs/https://velog.velcdn.com/images/ysy3285/post/6a361552-d2f4-4ade-8a2d-6bfbcdd517a9/image.png)

## 0\. 개요

![](https://proxy-prod.omnivore-image-cache.app/0x0,s-wsgJjuA0YtiXkau1BxXHM9a5bLd2lTF4ArU2QzqCtk/https://velog.velcdn.com/images/ysy3285/post/e4cd4541-80fb-4261-89da-cb65cd8df798/image.png)  
오늘은 온프레미스 방식이 아닌 Docker-Compoese를 활용해서 Nextcloud 및 OnlyOffice를 설치해보겠습니다.

## 1\. 준비

먼저 Docker와 Docker-compose를 설치해주세요  
[Docker 설치](https://velog.io/@ysy3285/Docker-%EC%9A%B0%EB%B6%84%ED%88%AC%EC%97%90-%EB%8F%84%EC%BB%A4-%EC%84%A4%EC%B9%98-%ED%95%98%EA%B8%B0)  
[Docker-compose 설치](https://velog.io/@ysy3285/Docker-Docker-Compose-%EC%84%A4%EC%B9%98)

## 1) git clone

```crmsh
git clone https://github.com/ONLYOFFICE/docker-onlyoffice-nextcloud
```

## 2) 해당 디렉토리로 이동

```bash
cd docker-onlyoffice-nextcloud
```

디렉토리는 아래와 같이 구성되어 있고  
![](https://proxy-prod.omnivore-image-cache.app/0x0,s7xUF_2y8M-Sy_6dsvUHE1uRr7FIyhGr5tg623fsFPL0/https://velog.velcdn.com/images/ysy3285/post/269f42fb-f7eb-46e2-ac5d-89c6a6facd12/image.png)

## 3) docker-compose.yml 수정

```css
vi docker-compose.yml
```

저는 DB를 MariDB를 사용할 예정이므로 아래와 같이 db부분을 추가해줍니다.

```yaml
version: '3'
services:
  db:
    container_name: mariadb-server
    image: mariadb
    command: --transaction-isolation=READ-COMMITTED --binlog-format=ROW
    restart: always
    ports:
      - 3306:3306
    volumes:
      - mysql_data:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD={패스워드}
      - MYSQL_PASSWORD={패스워드}
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
  app:
    container_name: app-server
    image: nextcloud:fpm
    restart: always
    expose:
      - '80'
      - '9000'
    volumes:
      - app_data:/var/www/html
  onlyoffice-document-server:
    container_name: onlyoffice-document-server
    image: onlyoffice/documentserver:latest
    restart: always
    expose:
      - '80'
      - '443'
    volumes:
      - document_data:/var/www/onlyoffice/Data
      - document_log:/var/log/onlyoffice
  nginx:
    container_name: nginx-server
    image: nginx
    restart: always
    ports:
      - 80:80
      - 443:443
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - app_data:/var/www/html
volumes:
  document_data:
  document_log:
  app_data:
  mysql_data:
```

## 4) docker-compose 실행

```ebnf
docker-compose up -d
```

## 3\. Nextcloud 설치

## 1) 사용자 생성 및 DB 설정

**[http://IP](http://ip/)**로 접속하면 아래와 같은 창이 뜹니다.  
![](https://proxy-prod.omnivore-image-cache.app/0x0,sfkzanXL1xRaoU7Xs6oYVUKUUOAbcnkxEBmcVOFsgZOA/https://velog.velcdn.com/images/ysy3285/post/616b0fe7-c15c-493e-87df-cd363f80c06a/image.png)  
원하는 사용자 이름 암호를 입력하고  
데이터 베이스 설정은 MySQL/MariaDB로 선택후

> \[데이터베이스 사용자\] nextcloud  
> \[데이터베이스 암호\] docker-compose.yml에서 설정한 암호  
> \[데이터베이스 이름\] nextcloud  
> \[mariaDB컨테이너 이름\] mariadb-server

설치 완료 버튼을 클릭합니다.

localhost로 입력할 경우 아래와 같은 오류가 발생합니다.  
"관리자 생성을 시도하는 동안 오류가 발생했습니다: 데이터베이스에 연결하지 못했습니다: 드라이버에서 예외가 발생했습니다: SQLSTATE\[HY000\]\[2002\] 연결이 거부되었습니다."  
"Error while trying to create admin user: Failed to connect to the database: An exception occured in driver: SQLSTATE\[HY000\]\[2002\] Connection refused"

## 2) Nextcloud 설치 완료

아래와 같은 화면이 나온다면 설치 완료 입니다.  
![](https://proxy-prod.omnivore-image-cache.app/0x0,sSgnOTN5tzO7w6VklafZaQL89EInU2US2YUG6_LyibYw/https://velog.velcdn.com/images/ysy3285/post/dca1e68d-c7c1-476e-86af-d7fff8425735/image.png)

## 4\. Onlyoffice 설치

다시 프로젝트 폴더로 이동해 아래 스크립트를 실행합니다.

```jboss-cli
cd docker-onlyoffice-nextcloud
bash set_configuration.sh
```

이제 Nextcloud에서 OnlyOffice를 활용할 수 있습니다.  
![](https://proxy-prod.omnivore-image-cache.app/0x0,sJRHlK7VZ4B56xHKxlKMlimrGsPdv8hZoZzKcbT5a5I8/https://velog.velcdn.com/images/ysy3285/post/c562a1d8-4793-4075-bc7f-5fca2a6f148c/image.png)

[![profile](https://proxy-prod.omnivore-image-cache.app/0x0,smXI5VeXopIlOf3kdDR4jtMzmjn_bmXcfX3MMtIb1VM0/https://velog.velcdn.com/images/ysy3285/profile/8c5704ad-e447-4cbe-aed3-88a2ee6a9536/%EB%AF%B8%EB%AA%A8%ED%8B%B0%EC%BD%98.png)](https://velog.io/@ysy3285/posts)

#### 0개의 댓글