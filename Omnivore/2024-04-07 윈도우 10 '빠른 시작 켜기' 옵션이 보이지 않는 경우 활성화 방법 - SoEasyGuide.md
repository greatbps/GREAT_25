---
id: 952bcd68-bf7b-4a75-b025-dc58ba436439
date_saved: 2024-04-07 11:48:47
date_published: 2022-03-23 17:56:08
date_read: 2024-04-07 11:54:00
omnivore_url: https://omnivore.app/me/https-iboxcomein-com-enable-the-turn-on-fast-startup-option-in-w-18eb6754c16
original_url: https://iboxcomein.com/enable-the-turn-on-fast-startup-option-in-windows-10/
---

# 윈도우 10 '빠른 시작 켜기' 옵션이 보이지 않는 경우 활성화 방법 - SoEasyGuide
#Omnivore
 
[Read on Omnivore](https://omnivore.app/me/https-iboxcomein-com-enable-the-turn-on-fast-startup-option-in-w-18eb6754c16)
[Read Original](https://iboxcomein.com/enable-the-turn-on-fast-startup-option-in-windows-10/)
 
윈도우에서는 **빠른 시작 켜기**라는 옵션이 존재 합니다. 이 옵션이 활성화 된 경우 컴퓨터 종료 전 사용 하던 프로그램을 부팅 후 자동으로 빠르게 다시 실행 되도록 해 줍니다.

![빠른_시작_켜기_옵션이_보이지_않는다](https://proxy-prod.omnivore-image-cache.app/816x633,szwgUgY7uJJVBKYDMvZxNswta-7oGKDGZv1NcR7gpitc/https://iboxcomein.com/wp-content/uploads/2022/03/003756-%EB%B9%A0%EB%A5%B8_%EC%8B%9C%EC%9E%91_%EC%BC%9C%EA%B8%B0_%EC%98%B5%EC%85%98%EC%9D%B4_%EB%B3%B4%EC%9D%B4%EC%A7%80_%EC%95%8A%EB%8A%94%EB%8B%A4.webp "빠른 시작 켜기 옵션이 보이지 않는다")

빠른 시작 켜기 옵션이 보이지 않는다

그런데 이 옵션을 변경하기 위해 종료 설정으로 이동 하면 기본적으로 있어야 할 **빠른 시작 켜기** 항목이 보이지 않는 경우가 있습니다.

이는 기본적으로 하드웨어 자체적으로 빠른 시작 켜기 기능을 지원하는 않거나 전원 시스템 설정 옵션이 비활성화 된 경우 나타나는 증상입니다.

기능을 지원하지 않는 것은 하드웨어 구성을 변경하지 않는 이상 별다른 방법이 없습니다. 그런데 기능은 지원하지만 옵션 만 비활성화 되어 있는 경우 최대 절전 모드를 활성화 하거나 전원 레지스트리를 편집하면 다시 활성화 할 수 있습니다.

그래서 오늘은 **윈도우 10에서 '빠른 시작 켜기' 옵션이 보이지 않는 경우 이를 다시 활성화하는 방법**에 대해서 알아 봅니다.

---

해당 포스트는 충분한 테스트 및 검증 후 작성 되었지만 이것이 내용의 정확성이나 신뢰성에 대해 보증을 하는 것은 아니니 **단순 하게 참고**용으로 봐주시길 바랍니다.

튜토리얼 환경 : 윈도우 10 (빌드: 19044.1586)

## **최대 절전 모드 활성화**

명령 프롬프트를 관리자 권한으로 실행 후 powercfg 의 h 옵션을 사용해 최대 절전 모드를 활성화하면 '빠른 시작 켜기(권장)' 옵션이 활성화 되는 경우가 있습니다.

### **관리자 권한으로 명령 프롬프트 실행**

![명령_프롬프트_관리자_권한으로_실행](https://proxy-prod.omnivore-image-cache.app/1024x683,ssKrAdQg2nQG70ehQMFkM4v2_4quwmf1HAnGDpATbmz0/https://iboxcomein.com/wp-content/uploads/2022/03/003759-%EB%AA%85%EB%A0%B9_%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8_%EA%B4%80%EB%A6%AC%EC%9E%90_%EA%B6%8C%ED%95%9C%EC%9C%BC%EB%A1%9C_%EC%8B%A4%ED%96%89-1024x683.webp "명령 프롬프트 관리자 권한으로 실행")

명령 프롬프트 관리자 권한으로 실행

1. 아래 절차로 _명령 프롬프트_ 를 관리자 권한으로 실행 합니다. 아래 방법 외에 [명령 프롬프트를 실행하는 다른 방법들](https://comeinsidebox.com/how-to-run-command-prompt/#more-13468)도 있으니 필요한 경우 확인합니다.  
   1. 윈도우 작업 표시줄의 검색 필드에 _명령 프롬프트_ 등으로 입력 합니다.  
   2. 검색 결과의 '가장 정확' 항목에 _명령 프롬프트_ 가 검색 되면, 오른쪽 하위 실행 옵션에서 **_관리자 권한으로 실행_** 을 클릭 합니다.

![사용자_계정_컨트롤](https://proxy-prod.omnivore-image-cache.app/900x470,ssE4eOuG79rneDmQq3Un14OKkhXTdLHzttHQH3cP9Rw0/https://iboxcomein.com/wp-content/uploads/2022/03/003802-%EC%82%AC%EC%9A%A9%EC%9E%90_%EA%B3%84%EC%A0%95_%EC%BB%A8%ED%8A%B8%EB%A1%A4.webp "사용자 계정 컨트롤")

사용자 계정 컨트롤

1. 만약 _사용자 계정 컨트롤_ 패널이 뜨는 경우 안내하는 내용을 확인 합니다. 그래도 계속 진행 하고 싶다면 _예_ 버튼을 클릭 하고 매번 뜨는 것이 불편 한 경우 [사용자 계정 컨트롤을 비활성화](https://comeinsidebox.com/%ec%82%ac%ec%9a%a9%ec%9e%90-%ea%b3%84%ec%a0%95-%ec%bb%a8%ed%8a%b8%eb%a1%a4-uac/#more-6882) 할 수 있습니다.

### **명령어 작성하기**

![최대_절전_모드_활성화_명령어_입력](https://proxy-prod.omnivore-image-cache.app/900x318,sLZo9QOVr-10xrRAW6tpZA8LNjrpI_ZFe-mk_VLzagU0/https://iboxcomein.com/wp-content/uploads/2022/03/003804-%EC%B5%9C%EB%8C%80_%EC%A0%88%EC%A0%84_%EB%AA%A8%EB%93%9C_%ED%99%9C%EC%84%B1%ED%99%94_%EB%AA%85%EB%A0%B9%EC%96%B4_%EC%9E%85%EB%A0%A5.webp "최대 절전 모드 활성화 명령어 입력")

최대 절전 모드 활성화 명령어 입력

_관리자:명령 프롬프트_ 에서 아래 커맨드를 작성 후 Enter 키를 눌러 주면 옵션을 활성화 할 수 있습니다. 명령어를 복사 후 마우스 오른쪽 버튼으로 입력 줄을 클릭 하면 간단하게 붙여넣기할 수 있습니다.

```applescript
powercfg -h on
```

만약 비활성화 하고 싶은 경우 아래 명령을 사용합니다.

```nginx
powercfg -h off
```

### **적용하기**

변경한 내용을 적용하기 위해 윈도우 시스템을 한 차례 재 부팅 합니다.

## **레지스트리 편집기를 활용하는 방법**

위 과정으로 활성화 되지 않는 다면 레지스트리 편집기에서 Power 키를 수정해 _빠른 시작 켜기_ 를 활성화 할 수 있습니다.

주의: [레지스트리 의 수정 과 편집](https://comeinsidebox.com/%eb%a0%88%ec%a7%80%ec%8a%a4%ed%8a%b8%eb%a6%ac-registry%eb%9e%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%a0%88%ec%a7%80%ec%8a%a4%ed%8a%b8%eb%a6%ac-%ed%8e%b8%ec%a7%91%ea%b8%b0%eb%a5%bc-%ec%82%ac/#more-6014)은 운영체제의 변경을 가하는 것으로 잘못 진행 할 경우 시스템 손상이 발생 할 수 있습니다. 작업 전에 [레지스트리를 백업](https://comeinsidebox.com/%eb%a0%88%ec%a7%80%ec%8a%a4%ed%8a%b8%eb%a6%ac-registry%eb%a5%bc-%eb%b0%b1%ec%97%85-%ed%95%98%eb%8a%94-%eb%b0%a9%eb%b2%95-%ec%95%88%eb%82%b4/#more-6065) 하거나 [윈도우 시스템을 백업](https://iboxcomein.com/windows-11-backup-and-recovery/#ftoc-heading-11) 하길 권장합니다.

### **레지스트리 편집기 실행**

각자 편한 방식으로 '레지스트리 편집기' 를 활성화 합니다. 설명에서는 '실행' 창으로 진행합니다.

![레지스트리_편집기_실행](https://proxy-prod.omnivore-image-cache.app/802x397,s2T_OI9QgZj8djWSaa2bsj4KtufEF8FzRGLRFSki65j0/https://iboxcomein.com/wp-content/uploads/2022/03/003806-%EB%A0%88%EC%A7%80%EC%8A%A4%ED%8A%B8%EB%A6%AC_%ED%8E%B8%EC%A7%91%EA%B8%B0_%EC%8B%A4%ED%96%89.webp "레지스트리 편집기 실행")

레지스트리 편집기 실행

1. 실행 (단축키 : Win \+ R ) 도구를 활성화 합니다. 처음 사용 하는 경우 [실행창 기본 사용 방법](https://comeinsidebox.com/windows-run-command) 에서 추가적인 내용을 확인 할 수 있습니다.
2. _열기(O):_ 옆 텍스트 필드에 `regedit` 이라고 입력 후 _확인_ 버튼을 클릭 하거나 Enter 키를 눌러 줍니다.

![사용자_계정_컨트롤](https://proxy-prod.omnivore-image-cache.app/900x468,supTyCfMp02WbCOEXyUp2fU3Af_1CcbU0ljZLO8GaWTw/https://iboxcomein.com/wp-content/uploads/2022/03/003808-%EC%82%AC%EC%9A%A9%EC%9E%90_%EA%B3%84%EC%A0%95_%EC%BB%A8%ED%8A%B8%EB%A1%A4.webp "사용자 계정 컨트롤")

사용자 계정 컨트롤

1. 사용 하는 계정의 권한 수준에 따라 _사용자 계정 컨트롤_ 패널이 보여질 수 있습니다.  
   * 이 경우 안내하는 내용을 확인 합니다. 그래도 계속 진행 하고 싶다면 _예_ 버튼을 클릭 하면 됩니다.  
   * 만약 매번 보여지는 팝업이 불편 한 경우 [사용자 계정 컨트롤을 비활성화](https://comeinsidebox.com/%ec%82%ac%ec%9a%a9%ec%9e%90-%ea%b3%84%ec%a0%95-%ec%bb%a8%ed%8a%b8%eb%a1%a4-uac) 할 수도 있습니다.

### **Power 키 폴더 이동**

![레지스트리_편집기에서_Power_키_이동](https://proxy-prod.omnivore-image-cache.app/920x715,ssHihuDdjsqxds0a6fJUERNsJ3ganDKMd4o795nZSVqQ/https://iboxcomein.com/wp-content/uploads/2022/03/003810-%EB%A0%88%EC%A7%80%EC%8A%A4%ED%8A%B8%EB%A6%AC_%ED%8E%B8%EC%A7%91%EA%B8%B0%EC%97%90%EC%84%9C_Power_%ED%82%A4_%EC%9D%B4%EB%8F%99.webp "레지스트리 편집기에서 Power 키 이동")

레지스트리 편집기에서 Power 키 이동

아래 올려둔 경로를 통해 **_Power_**  로 이동 합니다. '레지스트리 편집기' 상단 주소창 A 에 경로를 그대로 붙여넣기 ( Ctrl \+ V ) 하면 빠르게 이동 할 수 있습니다.

```taggerscript
\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power
```

### **HiberbootEnabled 값 편집**

![HiberbootEnabled_값_수정](https://proxy-prod.omnivore-image-cache.app/920x715,sKXQII9mANDY9ltNGydMFiV4u9J6Se3FVHhUNSCw8KwE/https://iboxcomein.com/wp-content/uploads/2022/03/003812-HiberbootEnabled_%EA%B0%92_%EC%88%98%EC%A0%95.webp "HiberbootEnabled 값 수정")

HiberbootEnabled 값 수정

1. Power 키에서 `HiberbootEnabled` 값을 찾아 수정 하기 위해 마우스로 두 번 클릭 하거나 컨텍스트 메뉴[1](#easy-footnote-bottom-1-5596)의 _수정(M)_ 메뉴를 통 해 값 편집 창을 실행합니다.

![DWORD_값_데이터_편집](https://proxy-prod.omnivore-image-cache.app/750x350,sTmYiU0eF5HQ35_b-77LR7mwNyKbTsu7ZWEu-KZZiE1g/https://iboxcomein.com/wp-content/uploads/2022/03/003816-DWORD_%EA%B0%92_%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%8E%B8%EC%A7%91.webp "DWORD 값 데이터 편집")

DWORD 값 데이터 편집

1. 'DWORD(32비트)값 편집' 창에서 _값 데이터(V)_ 를 **_1_**  로 지정 후 _확인_ 버튼을 눌러 줍니다.  
   * **값 데이터 1**: 빠른 시작 켜기 활성 상태  
   * **값 데이터 0**: 빠른 시작 켜기 비활성화 상태

### **적용**하기

변경 내용을 적용 하기 위해 아래 중 한 가지를 수행 후 윈도우 키와 조합 되는 단축키가 모두 비활성화 되었는지 확인 합니다.

* [작업 관리자를 실행](https://iboxcomein.com/task-manager) 후 '세부 정보' 탭 의 _explorer.exe_ [프로세스를 다시 시작](https://iboxcomein.com/restart-the-file-explorer-process/)
* 윈도우 시스템을 **재부팅** (권장)

### 결과 확인

![빠른_시작_켜기_활성화_완료](https://proxy-prod.omnivore-image-cache.app/946x745,sOgrdZqChEfSlpVSBTDTboRp9Uo_8miDdjYuzKY4kAok/https://iboxcomein.com/wp-content/uploads/2022/03/005541-%EB%B9%A0%EB%A5%B8_%EC%8B%9C%EC%9E%91_%EC%BC%9C%EA%B8%B0_%ED%99%9C%EC%84%B1%ED%99%94_%EC%99%84%EB%A3%8C.webp "빠른 시작 켜기 활성화 완료")

빠른 시작 켜기 활성화 완료

위와 같이 정상적으로 _빠른 시작 켜기(권장)_ 옵션이 활성화 된 것을 볼 수 있습니다.

## **마무리**

이렇게, **윈도우 10에서 '빠른 시작 켜기(권장)' 옵션이 보이지 않는 경우 이를 다시 활성화하는 두 가지 방법**에 대해 알아 보았습니다.

'빠른 시작 켜기' 옵션은 일종의 **깊은 절전 모드**라고 보면 됩니다. 하지만 컴퓨터를 종료 하고 연결 된 전원 까지 모두 차단 하는 사용 패턴을 가진 경우 '빠른 시작 켜기' 옵션이 무의미 하기 때문에 비활성화 해 두는 것이 좋습니다.

이와 반대로 '빠른 시작 켜기' 기능을 사용 하고 싶은데 옵션이 보이지 않아 난감한 경우 위 내용으로 간단하게 다시 활성화 할 수 있으니 적용 해서 사용해 보시길 바랍니다.

## **참고**

* [윈도우 11 전원 종료 버튼에서 절전 메뉴가 안 보이는 경우 해결 방법](https://comeinsidebox.com/sleep-menu/)
* [윈도우 10 및 11 인터넷 다운로드 속도가 느린 경우 체크 사항](https://iboxcomein.com/windows-internet-download-speed-improvement/)
* [윈도우 11 컴퓨터의 스피커 소리가 한쪽만 재생되는 경우 해결 방법](https://eazymanual.com/how-to-fix-windows-11-speaker-sound-playing-only-one-error/)
* [윈도우 파일 탐색기 가 작동을 하지 않거나 보이지 않는 경우 찾거나 복구 하는 방법](https://iboxcomein.com/how-to-repair-windows-file-explorer-error/)