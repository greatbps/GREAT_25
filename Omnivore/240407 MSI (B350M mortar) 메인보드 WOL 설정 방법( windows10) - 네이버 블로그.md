---
id: e6074ca5-4d0b-4423-8a0f-97663b4eae47
---

# MSI (B350M mortar) 메인보드 WOL 설정 방법( windows10) : 네이버 블로그
#Omnivore
 
[Read on Omnivore](https://omnivore.app/me/https-m-blog-naver-com-post-view-nhn-blog-id-kj-63-is-https-redi-18eb6750d07)
[Read Original](https://m.blog.naver.com/PostView.nhn?blogId=kj63&isHttpsRedirect=true&logNo=222180437017)
 
MSI (B350M mortar) 메인보드 WOL 설정 방법( windows10)

여러번 시도끝에 어렵게 성공해서 메모해둡니다.

**​**

BIOS에서 SETTING-> Advanced -> Wake Up Event Setup -> Resume By PCI-E Device 옵션을 Enabled로 변경

전원쪽 옵션에서 ErP Ready 옵션 Disabled

​

Windows 10에서 realtek 최신버전 드라이버 설치

(아래 설정은 realtek 기준이라 intel의 경우 다를 수 있음)

Wake on magic packet when system : 사용

WOL 및 종료 링크 속도: 10Mbps 먼저

네트워크 주소: 원한다면 MAC 변경해도 상관없음. 만약 변경했다면 WOL신호 보낼때는 변경한 MAC으로 해야함.

매직 패킷 웨이크 온: 사용

웨이크 온 랜 종료: 사용

패턴 일치 웨이크 온: 사용

​

가장 중요한 설정!

제어판 -> 전원 단추 작동 설정 -> "현재 사용할 수 없는 설정 변경" 클릭 후 "빠른 시작 켜기(권장)" 체크해제 해야함. 

만약 체크된 상태라면 컴퓨터 꺼졌을때 링크가 down됨.(원래 컴퓨터가 꺼지면 10Mbps/half로 링크 up이 정상임.)