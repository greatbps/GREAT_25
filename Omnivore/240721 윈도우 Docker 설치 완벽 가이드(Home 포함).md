---
id: 1d964713-f262-42e2-9777-35d0f3bb981b
---

# 윈도우 Docker 설치 완벽 가이드(Home 포함)
#Omnivore
 
[Read on Omnivore](https://omnivore.app/me/https-www-lainyzine-com-ko-article-a-complete-guide-to-how-to-in-190c9583668)
[Read Original](https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/)
 
[Docker](https://www.lainyzine.com/ko/article/docker/)는 같은 이름의 회사에서 개발하고 있는, 경량 가상화 기술 [리눅스 컨테이너](https://www.lainyzine.com/ko/article/linux-container/)를 구현하는 애플리케이션입니다. VirtualBox나 VMWare 같은 [가상머신](https://www.lainyzine.com/ko/article/virtual-machine/)에서는 등을 활용해 하드웨어부터 에뮬레이션합니다만, Docker를 사용하면 실행하고자하는 프로세스만 격리된 환경에서 실행하는 것이 가능합니다. 이를 이용해 손쉽게 프로세스를 격리할 수 있을 뿐만아니라, 격리된 환경을 이미지로 만들어서 Docker만 돌아간다면 어디서든 똑같이 동작하는 컨테이너를 만들 수 있습니다.

[리눅스 컨테이너](https://www.lainyzine.com/ko/article/linux-container/)라는 이름에서 알 수 있듯이 [Docker](https://www.lainyzine.com/ko/article/docker/)는 리눅스를 기반으로 동작하는 애플리케이션입니다. 따라서 윈도우에서는 이전부터 Docker를 사용하는 게 비교적 까다로웠습니다만, Docker 사에서는 이러한 불편함을 해소하기 위해 Docker Desktop를 공개해 Windows와 Mac 환경에서 Docker를 손쉽게 사용할 수 있도록 도와주고 있습니다.

이 글에서는 Windows Home과 Windows Pro를 기준으로 Docker Desktop을 설치하는 방법에 대해서 소개합니다. macOS, [Linux](https://www.lainyzine.com/ko/article/linux/), [Synology DSM](https://www.lainyzine.com/ko/article/synology-dsm/) 등 다른 환경에서 Docker를 설치하는 방법에 대해서는 다음 글에서 소개합니다: [운영체제 별 Docker 설치 방법 총 정리](https://www.lainyzine.com/ko/article/a-summary-of-docker-installation-methods-by-operating-system/).

* [Windows Home과 Pro에서 Docker 설치 차이 이해하기](#windows-home%EA%B3%BC-pro%EC%97%90%EC%84%9C-docker-%EC%84%A4%EC%B9%98-%EC%B0%A8%EC%9D%B4-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0)
* [WSL2를 설치하고 활성화하는 방법](#wsl2%EB%A5%BC-%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0-%ED%99%9C%EC%84%B1%ED%99%94%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)
* [Docker Desktop 다운로드 및 설치 방법](#docker-desktop-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-%EB%B0%8F-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95)
* [Docker 설치 확인 및 간단한 nginx 서버 예제 실행해보기](#docker-%EC%84%A4%EC%B9%98-%ED%99%95%EC%9D%B8-%EB%B0%8F-%EA%B0%84%EB%8B%A8%ED%95%9C-nginx-%EC%84%9C%EB%B2%84-%EC%98%88%EC%A0%9C-%EC%8B%A4%ED%96%89%ED%95%B4%EB%B3%B4%EA%B8%B0)
* [부록: Hyper-V 기반 Docker Engine 사용하는 방법(Windows 10 Pro)](#%EB%B6%80%EB%A1%9D-hyper-v-%EA%B8%B0%EB%B0%98-docker-engine-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95windows-10-pro)
* [추천 문서](#%EC%B6%94%EC%B2%9C-%EB%AC%B8%EC%84%9C)

## Windows Home과 Pro에서 Docker 설치 차이 이해하기[#](#table-of-contents) 

먼저 Windows에서 Docker를 설치하기에 앞서서 본인이 사용중인 Windows가 어떤 에디션인지 확인할 필요가 있습니다. Windows + S를 입력하고, 검색 창에서 PC 정보를 검색합니다.

* 관련 글: [Windows 10 에디션, 버전, 빌드 정보 확인하는 방법](https://www.lainyzine.com/ko/article/how-to-check-windows-10-edition-version-build-information/)

![PC 정보 설정을 실행합니다](https://proxy-prod.omnivore-image-cache.app/1500x539,shZZE0qAwtkJohnVq7dgRyEugvr-DlsNko5ZY1XKAzng/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/80F9C2A0-6395-4947-BF02-8866EF8A1589.png) 

오른쪽의 정보 창에서 스크롤해서 내려가면 Windows 10 에디션을 확인할 수 있습니다. 예시의 이미지에서는 Windows 10 Pro를 사용중인 것을 알 수 있습니다.

![현재 사용중인 Windows 에디션을 확인합니다](https://proxy-prod.omnivore-image-cache.app/1500x849,sBS6JYrslcW1AQfqfDyPOWgspYhr-Kq3jwQ-8FX0ItUw/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/598AF8FE-626E-4930-B156-F65A8799E352.png) 

Docker를 사용할 때 Windows Home Edition과 Windows Pro Edition의 가장 큰 차이는 Hyper-V 기능의 지원여부입니다.

> Hyper-V는 Windows Pro, Enterprise 및 Education 64비트 버전에서 사용할 수 있습니다. Home 버전에서는 사용할 수 없습니다. – [Windows 10의 Hyper-V 소개 | Microsoft Docs](https://docs.microsoft.com/ko-kr/virtualization/hyper-v-on-windows/about/)

Docker Desktop은 기본적으로 Hyper-V 기능을 사용하기 때문에 Windows Pro 에디션에서만 사용할 수 있었습니다. Home 에디션에서는 Docker Toolbox(boot2docker)가 대안으로 이야기되곤 했었습니다만, 현재는 공식적으로 지원이 종료된 상태입니다.

희소식은 2020년 5월 [Windows 10 May 2020 Update(20H1) 업데이트](https://blogs.windows.com/windowsexperience/2020/05/27/whats-new-in-the-windows-10-may-2020-update/)가 릴리스되면서 WSL2가 정식 릴리스되었다는 점입니다. WSL2는 Windows Home에서도 사용할 수 있으며 Docker Desktop의 발빠른 지원으로 현재는 WSL2를 기반으로 Docker Desktop을 사용하는 것이 가능합니다. 정리하면 다음과 같습니다.

* Windows 10/11 Professional / Education / Enterprise 에디션  
   * WSL2 기반 Docker Engine 사용 가능  
   * Hyper-V 기반 Docker Engine 사용 가능
* Windows 10/11 Home 에디션  
   * WSL2 기반 Docker Engine 사용 가능

WSL은 Windows Subsystem for Linux 2의 줄임말로 윈도우에서 리눅스를 사용할 수 있게 해주는 기능입니다. Home 에디션의 경우 Docker를 사용하려면 WSL2가 필수이며, Pro 사용자의 경우 WSL2를 사용하지 않더라도 Hyper-V 기반 가상화를 사용해 Docker Engine을 사용하는 것이 가능합니다.

이 글에서는 Home과 Pro 공통으로 사용할 수 있고, 좀 더 안정적으로 동작하는 WSL2 방식을 중점적으로 소개합니다. Hyper-V를 사용하는 방법은 부록으로 소개하겠습니다.

## WSL2를 설치하고 활성화하는 방법[#](#table-of-contents) 

Windows에서 WSL2를 설치하는 방법에 대해서는 다음 글에서 자세히 소개하고 있습니다. 아래에서 `wsl` 명령어가 없거나 문제가 있는 경우 다음 글을 참고해주시기 바랍니다.

* 관련 글: [Windows WSL2 설치하고 리눅스 사용하는 방법](https://www.lainyzine.com/ko/article/how-to-install-wsl2-and-use-linux-on-windows-10/)

여기서는 WSL2를 설치하는 방법을 빠르게 살펴보고자 합니다. 윈도우 10 버전 2004(빌드 19041 이상)이나 윈도우 11에는 기본적으로 `wsl` 명령어가 포함되어있습니다. 파워셸을 관리자 모드로 열고 다음 명령어를 실행해주세요.

```ada
$ wsl --install
```

설치가 끝나고 다음 명령어를 실행해, WSL 버전 기본값을 2로 변경해줍니다.

```gams
$ wsl --set-default-version 2
```

WSL2로 리눅스를 사용하고자 하는 경우, 리눅스 배포판 설치하는 등 추가 설정이 필요합니다만, Docker만 사용하는 경우 여기까지만 셋업하면 됩니다. 그럼 이제 Docker Desktop을 설치해보겠습니다.

## Docker Desktop 다운로드 및 설치 방법[#](#table-of-contents) 

WSL2 준비가 끝났으니 이제 본격적으로 Docker Desktop을 설치해보겠습니다.

1\. 다음 페이지로 이동해서 Download for Windows를 클릭해 Docker Desktop for Windows를 다운로드 받습니다. 2023년 7월 현재 최신 버전은 4.21.1입니다(버전에 따라 조금 다를 수 있으나 설치 과정은 대동소이합니다).

* [Docker Desktop for Mac and Windows | Docker](https://www.docker.com/products/docker-desktop)

![Docker Desktop을 다운로드 합니다](https://proxy-prod.omnivore-image-cache.app/1430x1000,smhMg4lHDoA-coPxbagexfSUqBxvSsECWvI3l8mGEy48/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/264412A4-7882-4AA1-905D-068D19F23CEA.png) 

2\. 다운로드 받은 `Docker Desktop Installer.exe`를 실행하면 사용자 계정 컨트롤이 나타납니다. 설치를 진행하려면 ’예’를 클릭합니다.

![설치를 계속하려면 사용자 계정 컨트롤 팝업에서 예를 클릭합니다](https://proxy-prod.omnivore-image-cache.app/1500x782,sibpDkIu3lTl9sSFovyEKibSpvzeA6gEILWGchHdqqzc/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/2B773043-AEDD-479E-9C30-39A139B1B532.png) 

3\. 안내에 따라 설치를 진행합니다. 설치 중간에 Configuration이 나타납니다. 둘 다 체크하고 설치를 진행합니다(첫 번째 옵션은 WSL 관련, 2번째 옵션은 바탕화면에 아이콘 추가할지 여부입니다).

![설치 과정에서 필요한 Configuration을 진행합니다](https://proxy-prod.omnivore-image-cache.app/1500x865,sNVa0o3mjHg8at0757Hk1u_wouFgdwYjM-kgm549ah-M/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/33B87151-BEBF-4923-8778-DEFB9674455A.png) 

4\. Docker Desktop 설치가 진행됩니다. 몇 분 정도 시간이 걸리니 완료될 때까지 기다립니다.

![Docker가 설치됩니다. 몇 분 정도 시간이 걸립니다](https://proxy-prod.omnivore-image-cache.app/1500x876,sPUh887Lii76SP2TAfhaRgP_87W_i5mOzbHKtIJsImaE/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/A36851DA-CA26-4605-A0DB-4AD7DDBD8390.png) 

5\. 설치가 끝나면 Installation succeeded 메시지가 나타납니다. 시스템 상태에 따라서 재시작이나 로그아웃을 해야하는 경우도 있습니다. Close 버튼을 클릭해 인스톨러를 종료합니다.

![Docker Desktop 설치가 완료되었습니다](https://proxy-prod.omnivore-image-cache.app/1500x900,s3DO-L3Ax24XGd35t3siyVGxrmtD2m4s2MbaCWiWt64Q/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/78A2A923-AE4E-42D6-A710-7821182FBCAD.png) 

6\. 이제 바탕화면의 Docker Desktop 아이콘이나 Windows + S로 Docker를 검색해서 Docker Desktop을 실행할 수 있습니다. Docker Desktop을 실행합니다.

![Docker Desktop을 실행합니다](https://proxy-prod.omnivore-image-cache.app/1500x837,sLWL5kFitxWJ0ESUZ2RqqMw1xwSs4AO6c6vO1AsDGG6s/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/6DB95404-662D-4AA1-8CF5-12C653AD69F7.png) 

7\. 시스템에 WSL2가 활성화되어있다면 Docker는 기본적으로 WSL2를 백엔드로 Docker Engine을 실행합니다. 초기 셋업에는 몇 분 정도의 시간이 걸립니다. 성공적으로 Docker가 실행되면 Tutorial이 나타납니다.

![Docker가 처음 실행되면 Tutorial 안내 페이지가 나타납니다](https://proxy-prod.omnivore-image-cache.app/1500x882,s4Jsx70b-_IWvJyk6wHeyJgnBBzMLn2NJqcCMPMo7pjM/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/EFEE116E-21A4-4E09-BFFC-9865ED16FC3E.png) 

8\. Docker Desktop은 시스템 트레이에 숨겨져있습니다. 숨겨진 아이콘을 활성화하고 고래 모양 아이콘에서 오른쪽 버튼을 누르면 상태를 Docker Desktop을 관리할 수 있습니다. 여기서 About Docker Desktop을 클릭합니다.

![Windows 시스템 트레이의 Docker 메뉴](https://proxy-prod.omnivore-image-cache.app/1252x736,s9kMIEvXeo3fj1N1NbHCYWl8WyMOi1Ve3yZvTF0Gi6RI/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/06B91789-27A7-496A-9F9A-A6614DF313A7.png) 

현재 설치된 Docker Desktop과 관련된 도구들의 버전을 여기서 확인할 수 있습니다.

![About Docker Desktop에서 Docker 관련 도구의 버전을 확인할 수 있습니다](https://proxy-prod.omnivore-image-cache.app/1436x1000,s8Pvdd0KDQcLVuaGzUpLeORi9xpRGo2cyB2A2gVkH6a0/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/6EEEE460-4B25-446C-B5C6-4E6C7B1E0EDD.png) 

9\. 다음으로 WSL2 설정이 잘되어있는지 확인하고 WSL 통합 설정을 진행하겠습니다. Docker 아이콘에서 오른쪽 버튼을 눌러 Settings를 선택합니다. 먼저 General 설정에서 ’Use the WSL 2 based engine’에 체크가 되어있는지 확인합니다. 미리 체크가 되어있을 텐데, 혹시 되어있지 않다면 체크하고 오른쪽 아래의 Apply & Restart 버튼을 클릭합니다.

![WSL2 based engine 사용 여부가 체크되어있는지 확인합니다](https://proxy-prod.omnivore-image-cache.app/1500x848,sMwNpB7scaZn6sIvH4U1aYzrqlF2Bo-JqD2JX3T-rVIw/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/31977517-27DE-49C6-AD83-7F36CE823496.png) 

10\. 다음으로 왼쪽 사이드바에서 Resource > WSL Integration 메뉴로 이동합니다. ’Enable Integration with my default WSL distro’에 체크되어있는지 확인합니다. 체크가 되어있지 않을 텐데 체크하고 오른쪽 아래의 Apply & Restart 버튼을 클릭해주면 도커 엔진이 재실행됩니다.

![WSL2 통합 기능이 활성화 되어있는지 확인해봅니다](https://proxy-prod.omnivore-image-cache.app/1500x850,sI6ykFfSoQUwJ8i4-Ke8N1jPhxh_mqGCH-5Xv5gy-fsw/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/844BA629-59ED-45A2-88BD-7798B497FB94.png) 

Docker가 재실행되면 WSL2 기반 Docker 설치는 모두 완료되었습니다!

## Docker 설치 확인 및 간단한 nginx 서버 예제 실행해보기[#](#table-of-contents) 

Docker가 처음이시라면, 튜토리얼을 따라하면서 배워보는 걸 추천합니다.

* 관련 글: [따라하면서 배우는 Docker 입문 튜토리얼](https://www.lainyzine.com/ko/article/docker-tutorial/)

여기서는 [Windows Terminal](https://www.lainyzine.com/ko/article/how-to-install-windows-terminal-powershell-wsl2/)을 열어서 정상 동작하는지 간단하게 테스트 해보겠습니다. PowerShell 탭을 하나 열고 `wsl` 명령어로 Docker 전용 머신이 실행중인 것을 확인할 수 있습니다.

```angelscript
$  wsl -l -v
NAME                   STATE           VERSION
* docker-desktop         Running         2
  docker-desktop-data    Running         2
```

[wsl](https://www.lainyzine.com/ko/article/comprehensive-guide-to-using-wsl/)로 docker-desktop 리눅스에 명령어를 실행해볼 수 있습니다. docker-desktop은 [BusyBox](https://www.lainyzine.com/ko/article/busybox/)가 포함된 LinuxKit 기반의 경량 리눅스인 것을 확인해볼 수 있습니다.

```angelscript
$ wsl -d docker-desktop busybox
BusyBox v1.29.3 (2019-01-24 07:45:07 UTC) multi-call binary.
...
```

`docker version` 명령으로 Docker 서버와 클라이언트 정보를 확인해봅니다.

```yaml
$ docker version
Client:
Cloud integration: 1.0.17
Version:           20.10.7
API version:       1.41
...

Server: Docker Engine - Community
Engine:
Version:          20.10.7
API version:      1.41 (minimum version 1.12)
...
```

`docker ps`로 실행중인 컨테이너를 확인해봅니다.

```cmake
$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

아직 아무것도 실행중이지 않은 것을 확인할 수 있습니다. 여기서부터는 nginx 이미지로 간단한 서버 테스트를 해보겠습니다. 먼저 웹 브라우저를 열어 127.0.0.1:4567에 접속해봅니다. 다음과 같이 사이트에 접속을 할 수 없는 상태인 것을 확인합니다.

![4567 포트로 접속해도 아무것도 나타나지 않습니다](https://proxy-prod.omnivore-image-cache.app/1500x964,sTsschq3X-hO1foV1DJJrUW_w88I3GQd1M4az2YaHCT8/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/67296D0F-FE7A-4017-BF06-CB2E3DAB40D3.png) 

`docker run` 명령어로 nginx 이미지 기반 컨테이너를 하나 실행해봅니다.

```vim
$ docker run -p 4567:80 -d nginx:latest
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
b4d181a07f80: Pull complete
edb81c9bc1f5: Pull complete
b21fed559b9f: Pull complete
03e6a2452751: Pull complete
b82f7f888feb: Pull complete
5430e98eba64: Pull complete
Digest: sha256:47ae43cdfc7064d28800bc42e79a429540c7c80168e8c8952778c0d5af1c09db
Status: Downloaded newer image for nginx:latest
5909b49c4a0e677fae0146846bdf4feca1ef869ece4cc46499f58d00f311e3d1
```

Docker에서는 이미지를 자동으로 다운로드 받고 실행해줍니다. `docker ps`로 실행한 컨테이너를 확인합니다.

```angelscript
$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                  PORTS                                   NAMES
5909b49c4a0e   nginx:latest   "/docker-entrypoint.…"   1 second ago   Up Less than a second   0.0.0.0:4567->80/tcp, :::4567->80/tcp   musing_allen
```

다시 웹 브라우저에서 127.0.0.1:4567에 접속해보면, 이제 ‘Welcome to nginx!’ 메시지가 나타납니다.

![4567 포트로 nginx 서버가 실행중인 것을 확인할 수 있습니다](https://proxy-prod.omnivore-image-cache.app/1500x966,stR-BUBkU6jas_6vMXvqyHjzHA17Gf1eBRBH3L6jY4n4/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/124C60EB-AD14-4D80-8F5B-8B677BE1E8EF.png) 

사용하지 않는 컨테이너는 `docker rm` 명령어로 삭제해줍니다. `5909b49c4a0e`는 `docker ps`에서 확인할 수 있는 컨테이너 ID입니다.

```angelscript
$ docker rm -f 5909b49c4a0e
```

이제 Docker를 활용하기만 하면 됩니다.

## 부록: Hyper-V 기반 Docker Engine 사용하는 방법(Windows 10 Pro)[#](#table-of-contents) 

Windows 10에서는 Hyper-V로 Docker를 사용하는 게 가능합니다. Hyper-V는 Intel CPU의 VT-c를 지원하는 CPU/메인보드에서만 동작합니다. 먼저 메인보드 설정을 확인해 Intel 가상화 기능을 활성화해야합니다. 먼저 다음 글을 참고해서, 윈도우의 Hyper-V 기능을 호라성화해주세요.

* 관련 글: [윈도우에서 Hyper-V 활성화하는 방법](https://www.lainyzine.com/ko/article/how-to-enable-hyper-v/)

Docker Desktop을 설치하는 방법은 앞에서 다룬 내용과 동일합니다.

WSL2이 활성화되어있고 WSL2 기반 Docker Engine으로 Docker가 실행중인 경우 Settings 페이지를 열어 ’Use the WSL 2 based engine’을 체크 해제하고 오른쪽 하단의 Apply & Restart 버튼을 클릭하면 Hyper-V 기반 Docker Engine이 실행됩니다.

![Hyper-V 기반 Docker Engine 설정을 위해 WSL2 기능을 비활성화합니다](https://proxy-prod.omnivore-image-cache.app/1500x848,sMwNpB7scaZn6sIvH4U1aYzrqlF2Bo-JqD2JX3T-rVIw/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/31977517-27DE-49C6-AD83-7F36CE823496.png) 

WSL2가 활성화되지 않은 상태에 Docker Desktop을 처음 실행하는 경우 에러가 발생하는 경우가 있습니다. 이는 Docker Desktop의 기본 설정이 WSL2로 잡혀있는데 WSL2가 없어서 발생하는 문제로 보입니다.

![WSL2가 비활성화해서 Docker 시작에 실패한 경우 Hyper-V을 사용합니다](https://proxy-prod.omnivore-image-cache.app/1500x850,skPPE4n21vy-4WazZR5p0rOc-1DnLdSqI-Ri1PglPdqw/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/BC1327E7-FA72-4572-9626-86B309191D7B.png) 

이 경우 에러가 발생하다가 Hyper-V 기반 Docker Engine을 활성화할 수 있는 팝업 창이 나타납니다. ‘Use Hyper-V’ 버튼을 클릭해주면 됩니다.

이러게 해도 제대로 동작하지 않는 경우 Docker 메뉴에서 강제로 재시작을 해보거나,

![Hyper-V 사용에 문제가 있다면 Docker를 강제로 재시작해봅니다](https://proxy-prod.omnivore-image-cache.app/1252x736,s9kMIEvXeo3fj1N1NbHCYWl8WyMOi1Ve3yZvTF0Gi6RI/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/06B91789-27A7-496A-9F9A-A6614DF313A7.png) 

Troubleshoot 메뉴에서 ‘Reset to fatory defaults’ 기능으로 완전 초기화를 해봅니다.

![계속 문제가 있다면 Docker 앱을 완전히 초기화해봅니다](https://proxy-prod.omnivore-image-cache.app/1500x847,s20OKH5fR22SpTDODavGJuSJSnSRuL_SYPP-D8OzuRSQ/https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/assets/1878BDB2-78D3-4199-8E0B-BE36078A6CE4.png) 

Docker Desktop에서도 WSL2를 기본 옵션으로 사용하는 것으로 보여서 특별한 이유가 없다면 Hyper-V보다는 WSL2 기반으로 사용하는 것을 추천합니다. Hyper-V를 다시 비활성화하는 방법은 다음 글에서 소개합니다.

* 관련 글: [Windows - Hyper-V 비활성화하는 방법](https://www.lainyzine.com/ko/article/how-to-disable-hyper-v-in-windows-10/)

## 추천 문서[#](#table-of-contents) 

Docker Desktop을 최신 버전으로 업데이트하는 방법에 대해서는 다음 글에서 소개합니다

* [Docker Desktop 최신 버전으로 업데이트하는 방법](https://www.lainyzine.com/ko/article/how-to-update-to-the-latest-version-of-docker-desktop/)

Docker Desktp은 WSL을 백엔드로 사용하지만, 기본적으로 윈도우에서 Docker를 사용할 수 있도록 도와주는 애플리케이션입니다. WSL 리눅스 머신에서 직접 Docker를 설치하고 사용할 수도 있습니다. 다음 글에서 소개합니다.

* [윈도우 WSL에서 Docker 설치하는 방법](https://www.lainyzine.com/ko/article/how-to-install-docker-on-wsl/)

Docker 셋업이 완료되었다면, 이제 본격적으로 Docker를 활용해볼 차례입니다. Docker 사용법을 다룬 글들은 다음 페이지에 모아두었습니다.

* [개발자를 위한 Docker 사용법 총 정리](https://www.lainyzine.com/ko/article/summary-of-how-to-use-docker/)

윈도우에서 도커를 설치하면, 리눅스 환경으로 활용할 수 있습니다. 하지만 제대로 된 리눅스 환경이 필요하다면, WSL이나 가상 머신을 활용하는 방법도 있습니다. 윈도우에서 리눅스를 사용할 수 있는 다양한 방법들에 대해서는다음 글에서 소개합니다.

* [윈도우에서 리눅스를 사용하는 방법들](https://www.lainyzine.com/ko/article/how-to-use-linux-on-windows/)