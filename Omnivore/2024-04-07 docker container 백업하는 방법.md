---
id: bf04a049-e39b-4ed7-803f-41abe7357c69
date_saved: 2024-04-07 08:47:53
omnivore_url: https://omnivore.app/me/docker-container-18eb5cfb884
original_url: https://velog.io/@nohsangwoo/docker-container-%EB%B0%B1%EC%97%85%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95
---

# docker container 백업하는 방법
#Omnivore
 
[Read on Omnivore](https://omnivore.app/me/docker-container-18eb5cfb884)
[Read Original](https://velog.io/@nohsangwoo/docker-container-%EB%B0%B1%EC%97%85%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)
 
Docker에서 현재 실행 중인 컨테이너의 모든 내용을 다른 컴퓨터로 복사하는 방법은 크게 두 가지가 있습니다.

첫 번째 방법은 Docker 이미지를 사용하는 것입니다. 현재 실행 중인 컨테이너에서 Docker 이미지를 만든 다음, 이 이미지를 다른 컴퓨터로 전송하여 컨테이너를 실행하는 것입니다. 이 방법은 컨테이너의 내용을 완전히 복제할 수 있지만, 이미지 크기가 크다는 단점이 있습니다.

1. 현재 실행 중인 컨테이너의 ID를 확인합니다. 이를 위해서는 docker ps 명령어를 사용합니다.

```angelscript
$ docker ps
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS     NAMES
05e5ce57f548   nginx:latest    "/docker-entrypoint.…"   5 seconds ago    Up 4 seconds    80/tcp    webserver
```

1. 현재 실행 중인 컨테이너에서 Docker 이미지를 만듭니다. 이를 위해서는 docker commit 명령어를 사용합니다.

```llvm
$ docker commit 05e5ce57f548 my-nginx
sha256:3e7c4c4e7124adad9fb6efb1e7e328f191e4f7d998c0d3f7c4d4b4ad7c0f7393
```

이 명령어는 05e5ce57f548 ID를 가진 컨테이너를 기반으로 my-nginx라는 새로운 Docker 이미지를 만듭니다. sha256:3e7c4c4e7124adad9fb6efb1e7e328f191e4f7d998c0d3f7c4d4b4ad7c0f7393는 새로 만든 이미지의 ID입니다.

1. 새로 만든 Docker 이미지를 파일로 저장합니다. 이를 위해서는 docker save 명령어를 사용합니다.

```applescript
$ docker save -o my-nginx.tar my-nginx
```

이 명령어는 my-nginx 이미지를 my-nginx.tar 파일로 저장합니다.

1. 파일을 다른 컴퓨터로 전송합니다.
2. 다른 컴퓨터에 Docker 이미지를 로드합니다. 이를 위해서는 docker load 명령어를 사용합니다.

```applescript
$ docker load -i my-nginx.tar
```

이 명령어는 my-nginx.tar 파일에서 Docker 이미지를 로드합니다.

6.다른 컴퓨터에서 컨테이너를 실행합니다. 이를 위해서는 docker run 명령어를 사용합니다.

```angelscript
$ docker run -d -p 80:80 my-nginx
```

이 명령어는 my-nginx 이미지를 기반으로 container를 실행하는 방법입니다.

[![profile](https://proxy-prod.omnivore-image-cache.app/0x0,sWwXEq38YYIZvdK-wJUXpMQq03PGES7tnv4iImUFjYfk/https://velog.velcdn.com/images/nohsangwoo/profile/33e8750f-8348-4143-aee9-ca76bd5bf71a/social.jpeg)](https://velog.io/@nohsangwoo/posts)

#### 1개의 댓글