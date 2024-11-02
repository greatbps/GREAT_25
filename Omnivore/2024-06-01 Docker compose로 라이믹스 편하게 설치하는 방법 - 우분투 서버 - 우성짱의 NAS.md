---
id: 7a886cfa-cdef-4ca4-8047-e1474fee5221
date_saved: 2024-06-01 17:27:43
date_published: 2020-08-29 22:27:44
date_read: 2024-06-19 15:08:01
omnivore_url: https://omnivore.app/me/docker-compose-nas-18fd2e94a54
original_url: https://www.wsgvet.com/ubuntu/125
---

# Docker compose로 라이믹스 편하게 설치하는 방법 > 우분투 서버 | 우성짱의 NAS
#Omnivore
 
[Read on Omnivore](https://omnivore.app/me/docker-compose-nas-18fd2e94a54)
[Read Original](https://www.wsgvet.com/ubuntu/125)
 
### 본문

[![3232235777_MydWz0eb_578fb1efec1c5be26833d3215085b597a3998c6c.png](https://proxy-prod.omnivore-image-cache.app/843x0,skzzJp0Ew3kfT9dt7AwR9E9v6XEeFBgb7RUPuRvbk87E/https://cdn.wsgvet.com/data/editor/2008//thumb-3232235777_MydWz0eb_578fb1efec1c5be26833d3215085b597a3998c6c_980x653.png)](https://www.wsgvet.com/bbs/view%5Fimage.php?fn=https%3A%2F%2Fcdn.wsgvet.com%2Fdata%2Feditor%2F2008%2F%2F3232235777%5FMydWz0eb%5F578fb1efec1c5be26833d3215085b597a3998c6c.png) 

**들어가며**

Rhymix(라이믹스)는 XE에서 포크되어 오픈소스로 개발되고 있는 국산 CMS입니다.

php, mysql, 웹서버로 구성됩니다.

요새는 SSL 인증서 발급이 필요하고, 자동갱신 설정, ffmpeg 설치 및 redis 설치 등이 기본적으로 필요합니다.

하나하나 설치하는데 시간도 오래걸리고 힘듭니다.

명령어 단 2줄로 설치가 된다면 어떨까요?

바로 도커로 가능합니다.

소스는 깃허브([링크](https://github.com/woosungchoi/docker-rhymix))에 올려뒀습니다.

**준비사항** 

자신의 도메인이 우분투 20.04 서버 또는 센토스8 서버를 가리키게 해야 됩니다.

도메인 뿐만 아니라, [www.도메인,](https://www.wsgvet.com/) port.도메인, pma.도메인까지 가리키게 하는게 중요합니다. (phpmyadmin, portainer 접속용)  

그리고 방화벽은 80, 443 포트를 열어주세요.

**설치하기**

(1) Ubuntu 20.04 LTS

위 명령어로 현재 우분투 패키지의 상태를 최신화하고, curl과 git을 설치하고, 필요없는 패키지를 삭제합니다.

위 명령어 한줄이면 됩니다.

(2) Centos 8

위 명령어로 현재 센토스8 패키지의 상태를 최신화하고, curl과 git을 설치하고, 필요없는 패키지를 삭제합니다.

위 명령어 한줄이면 됩니다.

도메인 주소, 이메일 주소, root DB 비번, DB유저, DB 비번, DB이름 등을 물어보는데 원하는대로 설정 가능합니다.

그후 자동으로 설치됩니다.

SSL 인증서 발급 및 자동 갱신 cron 작업이 되어 있고, ffmpeg도 php에 붙여서 움직이는 GIF 파일도 MP4로 바꿀 수 있습니다.

**로컬이나 SSL 없이 설치하기**

(1) Ubuntu 20.04 LTS users

위 명령을 넣은 후

위 명령을 넣고 설치하면 됩니다.

(2) For Centos 8 users

위 명령을 넣고

위 명령을 넣은 후 설치하면 됩니다.

(3) For Windows 10 WSL2 Ubuntu 20.04 LTS users

WSL2 Ubuntu 20.04 LTS와 docker를 윈도우10에 설치합니다.

<https://www.wsgvet.com/ubuntu/160> , <https://www.wsgvet.com/ubuntu/180>

위 명령어를 넣은 후

위 명령어를 넣으면 됩니다.

처음에 Enter your domain (ex : mydomain.com or localhost) : 이렇게 나옵니다.

로컬에서 설치하기 때문에 localhost 를 넣으면 됩니다. 나머지는 원하는대로 설정할 수 있습니다.

**라이믹스 설정하기**

자신의 도메인 주소로 들어가면 라이믹스 설치화면이 나올 것입니다.

DB : mysql

DB server address : db

DB server port : 3306

DB ID : 설치할때 지정했던 DB유저 이름

DB Password : DB 비밀번호

DB name : DB이름

넣으면 됩니다.

**Redis 캐시 설정하기**

Admin panel(관리자 페이지) -> Configuration(설정) -> System configuration(시스템 설정) -> Advanced configuration(고급설정)

Cache enable(캐시 사용) : redis

Host(호스트) : redis

Port(포트) : 6379

DB number(DB번호) : 1

이렇게 설정하면 됩니다.

**인증메일 설정하기**

구글 SMTP가 제일 편합니다.

<https://www.wsgvet.com/bbs/board.php?bo%5Ftable=home&wr%5Fid=594>

위 링크의 2번에 보시면 앱 비밀번호 생성하기가 있는데, 따라하셔서 16자리 앱비밀번호를 찾습니다.

![3232235777_Um3szY1Z_2e37534da112190b4bb41f0db76a2249861e5857.png](https://proxy-prod.omnivore-image-cache.app/545x0,spoI2nbNlqwxE-aYi7vHYg395Y15hA7Hnw5K4A1wZwPk/https://cdn.wsgvet.com/data/editor/2008//3232235777_Um3szY1Z_2e37534da112190b4bb41f0db76a2249861e5857.png) 

관리자 페이지 -> 설정 -> 시스템 설정 -> 알림 설정에서 위와 같이 설정하면 됩니다. 

이메일 주소는 자신의 gmail 주소를 넣으면 됩니다.

**phpmyadmin과 portainer**

Phpmyadmin : [https://pma.yourdomain.com](https://pma.yourdomain.com/)

Portainer : [https://port.yourdomain.com](https://port.yourdomain.com/)

위와 같은 형식의 주소로 들어가면 들어갈 수 있습니다.

portainer는 웹으로 도커 컨테이너를 관리할 수 있는 좋은 툴입니다.

[Docker를 Web에서 관리하는 Portainer 설치방법](https://www.wsgvet.com/bbs/board.php?bo%5Ftable=ubuntu&wr%5Fid=120) 

위 링크를 참조하세요.  

**도커 이미지 자동 업그레이드 등록**

docker\_upgrade.sh 파일에서 /your/path/to/rhymix/ 부분을 자신의 도커 폴더로 변경합니다.

위와 같이 실행 가능하게 해줍니다.

위 내용에서 /your/path/to/rhymix/ 부분을 자신의 도커 폴더로 변경 후 명령을 내려주면 crontab에 자동으로 들어갑니다.

**기타 실행명령어**

docker-compose.yml 파일이 있는 곳으로 가서

위 명령어를 내리면 전체 도커 컨테이너가 시작됩니다.

위 명령어를 내리면 전체 도커 컨테이너가 정지됩니다.

위 명령어를 내리면 도커 이미지를 최신화하고, 재시작합니다.