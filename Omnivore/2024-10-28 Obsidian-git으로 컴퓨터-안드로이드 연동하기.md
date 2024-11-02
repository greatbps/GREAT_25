---
id: 80b974b3-728c-4f83-9d2d-4c391375366a
date_saved: 2024-10-28 14:30:12
date_read: 2024-10-29 16:36:42
omnivore_url: https://omnivore.app/me/https-velog-io-rethinking-21-obsidian-git-ec-9-c-bc-eb-a-1-9-c-e-192d19a3890
original_url: https://velog.io/@rethinking21/Obsidian-git%EC%9C%BC%EB%A1%9C-%EC%BB%B4%ED%93%A8%ED%84%B0-%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0
---

# Obsidian-git으로 컴퓨터-안드로이드 연동하기
#Omnivore
 
[Read on Omnivore](https://omnivore.app/me/https-velog-io-rethinking-21-obsidian-git-ec-9-c-bc-eb-a-1-9-c-e-192d19a3890)
[Read Original](https://velog.io/@rethinking21/Obsidian-git%EC%9C%BC%EB%A1%9C-%EC%BB%B4%ED%93%A8%ED%84%B0-%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0)
 
![post-thumbnail](https://proxy-prod.omnivore-image-cache.app/0x0,sbOfwEs-6RAlMnEGB63-iwMyKbk_WZGGtm840uiNAdy4/https://velog.velcdn.com/images/rethinking21/post/280d35fb-796a-4f1e-af25-ba55a255b4cf/image.png)

> 설명이 불친절 할 수 있습니다.. 🤕 틀린 부분 또는 오류가 있다면 알려주세요!

Obsidian sync는 사용하기엔 비싸서 드라이브로 사용하고 있었으나,  
동기화 속도가 느리고 불안정해 github를 사용한 방식인 Obsidian-git 플러그인을 이용해 동기화 시켜주기로 했다. (~~깃허브 자동 잔디심기도 가능하다!~~)

## 💻 컴퓨터에서 해야 할 일

github계정이 있으며,  
git과 Obsidian이 설치되어있다고 가정한다.

## Obsidian Vault를 github에 올리기

### github repository 만들기

![깃허브 페이지](https://proxy-prod.omnivore-image-cache.app/0x0,sQbNVt52WfZOc0MsIKvBXMxFZvRf-sv_lkfld42oyA5g/https://velog.velcdn.com/images/rethinking21/post/4ee5048b-9377-4efd-b11b-71f6a6f90a87/image.png)

Github 로그인 후 Your Profile > Repositories 탭 > New 버튼을 틀릭해 repository를 생성한다.

![New repository](https://proxy-prod.omnivore-image-cache.app/0x0,s6ugkFHCYI9_DTNqEEv68Qo_N0d57yFOgGq43Ahj0bMU/https://velog.velcdn.com/images/rethinking21/post/f1ad02ca-f109-4c7e-a99c-f2468ce3364e/image.png)

저기서 Public/Private 중 원하는 곳을 선택하면 된다.  
개인정보를 실수로 적은 후 Push되어 셀프 유출되는 상황이 싫다면 Private을 추천한다!

그리고 개인적으로 빈 repository를 만드는걸 추천한다.

설정이 완료되었으면 Create repository 를 클릭한다.

### git

공유하고자 하는 Vault 위치로 터미널을 이동한다

```routeros
git init
git config --local user.name "깃허브 아이디 이름"
git config --local user.email "깃허브 이메일 이름"
```

### .gitignore 설정

필요한 .gitignore 설정  
Vault 폴더 안에 `.gitignore` 파일을 만들어 다음과 같이 작성한다  
안드로이드와 컴퓨터 간의 플러그인 설정 파일 충돌을 막는다. [참고](https://github.com/denolehov/obsidian-git/wiki/Tips-and-Tricks#gitignore)

```asciidoc
.obsidian/

.obsidian/workspace-mobile.json
.obsidian/workspace.json
.obsidian/app.json

.trash/
.DS_Store
```

### github에 올리기

공유하고자 하는 Vault 위치로 터미널을 이동한다

```mipsasm
git add .
git commit -m "initial commit"
git branch -M main 
git remote add origin "생성한 깃허브 주소"
git push -u origin main
```

컴퓨터는 ssh나 https 어떤 방식을 사용해도 상관이 없다.

Obsidian을 켠 후 설정(톱니바퀴) 버튼을 누른다.  
그후 Community Plugins에 들어가고, 만약 거기서 Community Plugin이 꺼져있다고 나오면 켠다.  
![](https://proxy-prod.omnivore-image-cache.app/0x0,sTRIf8vkvRDl5ENbmuqMEyD4hEnMZpGyJKx1NmrvIIM0/https://velog.velcdn.com/images/rethinking21/post/66974327-616c-48a2-8cde-fd59b458c9a6/image.png)

Community plugins 에 Browse를 누른 다음, `Obsidian git`를 검색해 플러그인을 설치한다. (설치 후에 Enable를 눌러줘야 한다.)  
![](https://proxy-prod.omnivore-image-cache.app/0x0,s5OKtgXmpILUX6DaCXP3m7ISrur6YLsc5RHwyC5Axm08/https://velog.velcdn.com/images/rethinking21/post/c1efb3cf-2c96-4078-a7f6-49935f805c62/image.png)

Enable과 동시에 github에 동기화된다.

### 설정

![](https://proxy-prod.omnivore-image-cache.app/0x0,sr8lG635_LdV97xjVTfgdoSsvP1lQUe1a-4YMdNhlnSE/https://velog.velcdn.com/images/rethinking21/post/5495caf1-41a3-4855-a0fc-c28fda5b04c4/image.png)

![](https://proxy-prod.omnivore-image-cache.app/0x0,saeUKM9N5Ahpmhj4czHZrC5IwwL2b-GPQbkSRVtcAfYc/https://velog.velcdn.com/images/rethinking21/post/cf3e87c5-6eab-43eb-afe5-26705fb79c6a/image.png)

(공사중..)

### 사용법, 명령어

설정한 시간을 주기로 자동으로 `git pull`과 `git push` 가 실행된다.  
`ctrl + P` 키를 누른다음, Git

## 📱 안드로이드 폰에서 해야 할 일

Obisidian 앱이 설치되어 있다고 가정한다.

## Termux 설치 (다른거 써도 됨)

![공식 문서의 안내문](https://proxy-prod.omnivore-image-cache.app/0x0,s9Pl663V-YqGiiI0nqtfHhLSE_74vGILGu7TblILsLzk/https://velog.velcdn.com/images/rethinking21/post/1aa092ec-00e0-4511-88b4-82d25afa495f/image.png)

찾아보니 termux 사용하라는 방법도 있고 isomorphic-git 사용하라는 곳도 있다. 그 중에서 termux를 이용하기로 했다

[github termux 설치](https://github.com/termux/termux-app/releases)  
들어가서 알맞는 apk 파일을 안드로이드 폰에 설치해준다.

## termux 기본 세팅

현재 설치된 패키지를 업데이트한다. (가끔씩 `Y/n` 입력을 하라고 나온다. Y 누르기)

```routeros
pkg upgrade && pkg update
```

이제 git 을 설치한다.

```cmake
pkg install git
```

파일 접근 권한을 변경해준다 (요청 알림에 승낙하면 된다.)

```arduino
termux-setup-storage
```

## Git clone

![ssh 가 안된데요](https://proxy-prod.omnivore-image-cache.app/0x0,sqp6k0PBuHJUxR6Rh-547qqLjnxKuckJnXwJ_nyH9qRY/https://velog.velcdn.com/images/rethinking21/post/b4183db1-6f03-4bee-ab46-b68c1b3fc762/image.png)  
Obsidian-git에서는 ssh를 지원하지 않기 때문에 https 로 다운을 받아야 한다. [docs](https://publish.obsidian.md/git-doc/Getting+Started#Performance+and+restrictions)

### Github Personal access token 만들기

전에는 비밀번호로 https로 git clone 을 할 수 있었으나, 지금은 Personal access token을 이용해 git clone을 해야 한다.

![Developer Settings에 있는 메뉴들](https://proxy-prod.omnivore-image-cache.app/0x0,sms37cJbDCSH62UFTA6d-EZJwgHK18RqkmW_9CrLJKYs/https://velog.velcdn.com/images/rethinking21/post/29444b63-615c-4b29-8fbc-fc97f5bf4165/image.png)

Github에 로그인하여  
상단 우측 프로필 클릭 > Settings > Developer settings (맨 밑에 있음) > Personal access tokens > Tokens (classic) 을 클릭한다

(classic이 아닌 것으로 token을 받으면 Obsidian-git이 제대로 작동하지 않는 문제가 있기에 classic으로 받아야 한다.)

Generate new token > Generate new token (classic) 를 누른다. (비번 입력 또는 인증 요청이 온다) 

![New personal access token (classic)](https://proxy-prod.omnivore-image-cache.app/0x0,saMEPIDc-j-n6nRq-Dm3SKcN-4W1nKYemMWafCLu5JWQ/https://velog.velcdn.com/images/rethinking21/post/1d7cf622-f2a1-4170-b14a-adb964562854/image.png)

Name에 token 이름을 입력하고, Expiration으로 Token의 유효기간을 설정한다.  
Select Scopes를 통해 Token의 권한을 설정할 수 있는데, 더 자세히 설정할수 있지만 ~~귀찮기에~~ 맨위 repo (private 레포지토리 에 관한 권한)만 체크 표시했다.

이후에 ghp\~ 로 시작하는 토큰이 표시가 되는데 한번 보여주고 다시 찾을땐 변경해주어야 하므로 복사 후 어딘가에 잘 저장해둔다.

### Termux로 git clone하기

Obsidian-git을 이용해서 git clone 하는 방법이 있지만. 매우 느리기에 (그리고 오류 보여주는 것도 친절하진 않다) termux를 켜 직접 git clone을 하기로 한다.

만들고자 하는 위치에 가서 git clone 을 한다.

```bash
cd ~/storage/shared/Documents
git clone "생성한 git repo 주소 (https)"
```

아이디와 비번/토큰 을 입력하라고 나온다. 각각 github 아이디와 토큰을 입력하고 기다리자.

## Obsidian-git 설치

이제 옵시디언 앱을 열어 Vault를 git clone 한 위치로 들어간 준 다음 열어둔다.  
Community plugin을 켠 다음 Obsidian git 에 들어가 밑에 내리다 보면 Authentication/commit Author 라는 곳이 있다.  
Username\~ 과 Password/Personal\~ 이 곳에 각각 github 아이디와 생성한 토큰을 입력한다.

## 🤕 문제 해결

## buffer error

Obsidian-git 에서 업데이트 할 때마다 buffer error가 떠요  
정확한 원인은 모르겠지만 플러그인을 모두 업데이트 하니 해결되었다.

## git conflict

(주로 컴퓨터와 휴대폰을 동시에 옵시디언을 켜고 있을 때) git conflict이 뜨는 경우가 있다.  
termux에 들어가 이를 해결해주는 것을 추천한다.(강제 pull 이라던지..)

출처들  
[Obsidian-git Getting Started](https://publish.obsidian.md/git-doc/Getting+Started#Performance+and+restrictions)  
[Amylo's blog](https://blog.amylo.diskstation.me/obsidian/tutorials/Sync%5FObsidian%5Fwith%5FAndriod%5FPC/)

[![profile](https://proxy-prod.omnivore-image-cache.app/0x0,s28h2h5JRYdIZFFczd-829QgkutZKY1okJacnQOd4juY/https://velog.velcdn.com/images/rethinking21/profile/e2b3ca38-f8ad-4cd1-91c7-4a06ac69b1e8/image.png)](https://velog.io/@rethinking21/posts)

🍵 떠오르는건 많은데 귀찮아요 졸려요

#### 0개의 댓글