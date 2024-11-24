---
id: 3b0b8d3c-f15e-4a27-aaaf-9b5f23f15f33
---

# 디지털 월세 절약하기: Ollama로 나만의 AI 비서 만드는 법
#Omnivore
 
[Read on Omnivore](https://omnivore.app/me/https-eopla-net-magazines-22793-192eb4b5715)
[Read Original](https://eopla.net/magazines/22793)
 
#아이템 선정 #사업전략 #프로덕트 

 디지털 월세 절약하기: Ollama로 나만의 AI 비서 만드는 법

![](https://proxy-prod.omnivore-image-cache.app/0x0,s7e3BCYFPYFmv1Cwoq_RAi9H32vXXXo6HH5UpZohGxyg/https://cdn.maily.so/dywbx3lpm0gwevjiymbpei068izh)

“다들 디지털 월세 얼마나 내시나요?”

최근 월 구독제 서비스의 증가로 '디지털 월세'라는 말이 유행하고 있습니다.

자연어 처리(NLP, Natural Language Processing)가 가능한 거대 언어 모델(LLM, Large Language Model)들이 공격적으로 출시되면서, ChatGPT를 시작으로 Claude, Gemini, Ollama 등 다양한 생성형 AI 제품이 쏟아져나오고 있습니다.

![](https://proxy-prod.omnivore-image-cache.app/0x0,sXDf_7MAwtO6cABZp6Ggxet97tO_ekX05yPR_JoIy6bg/https://cdn.maily.so/mreybwcd2el6tpq6bi5hsgs7o0yn)

Open WebUI를 활용한 무료 AI 화면

이로 인해 월 구독제에 대한 부담이 커졌죠. 최근에는 Cursor가 시장 점유율을 높여나갔고, Github Copilot에 Claude 3.5 모델이 탑재된다고 합니다. 생성형 AI 모델뿐만 아니라 AI Wrapper라 불리는 ChatGPT나 Claude 모델을 활용한 서비스나 제품이 더욱 보편화될 것으로 예상됩니다.

![](https://proxy-prod.omnivore-image-cache.app/0x0,sIR6_4B_25o4shREC-ewcfsXCA9fR97gKh7YgChppiHI/https://cdn.maily.so/p6l7xk2is7bvj2d7y09z29ebyfba)

첨부파일을 읽고 요약하는 기능도 훌륭하다.

주요 AI 서비스 월 구독료 예시 :

ChatGPT Plus: $20/월

Claude 3.5 sonnet : $20/월

Cusor Pro : $20/월

Midjourney: $10/월

Github Copilot: $10/월

연간 총액: 약 $960 (한화 약 130만원 이상)

오늘은 Ollama를 내 PC에 그것도 한글 버전을 설치하고 사용하는 방법에 대해서 소개해드리려고 해요. 요즘 같이 디지털 월세라 불리는 월 구독료가 높아지는 때, 나만의 개인 비서로 Ollama를 구축하고자 하신다면 아래 아티클이 도움되시리라 믿습니다. 

---

## **Step 1\. Ollama 설치하기**

링크 : <https://ollama.com/download>

![](https://proxy-prod.omnivore-image-cache.app/0x0,sCeSwaG5tI6oINOQEBWO52FobYOEzGkRlzrIAt2X6mPM/https://cdn.maily.so/4ev60hjs90giittadw4cxzqw8q03)

---

Ollama는 로컬 PC에서 대규모 언어 모델(LLM)을 실행할 수 있게 해주는 오픈 소스 도구입니다. 일반적으로 AI 모델을 사용하려면 인터넷을 통해 클라우드 서버에 접속해야 하지만, Ollama를 사용하면 인터넷 연결 없이도 내 컴퓨터에서 직접 AI 모델을 실행할 수 있습니다.

주요 특징:

로컬 실행: 인터넷 없이도 AI 모델을 사용할 수 있어 데이터 프라이버시가 강화됩니다.

다양한 모델 지원: Llama 2, Mistral 등 다양한 오픈 소스 LLM을 지원합니다.

사용 편의성: 간단한 명령어로 모델을 설치하고 실행할 수 있어 접근성이 높습니다.

왜 Ollama를 사용해야 할까요?

디지털 월세 부담을 줄이고, 데이터 보안을 강화하기 위해 로컬에서 AI 모델을 실행하는 것이 유리합니다. Ollama는 이러한 요구를 충족시켜 주는 도구로서, 개인용 PC나 노트북에서 AI 비서를 구축하고자 하는 분들에게 적합합니다.

---

![](https://proxy-prod.omnivore-image-cache.app/0x0,s_6KhPk6oG7WPhWFkRDJf91_FGqV_gjBqB-iVExjmGXk/https://cdn.maily.so/jxuz4pdarbau41jn05nfa5lgapgz)

먼저 <https://ollama.com/download> 링크로 접속하신 뒤 다운로드를 클릭합니다.

![](https://proxy-prod.omnivore-image-cache.app/0x0,sbXQZj5j3l7Q0mGkC8HfmACwRAuFp5HYoYmg5L91Cstc/https://cdn.maily.so/i557wxp3rbdcrau188zhv2ju2o37)

MacOS / Linux / Windows 각 운영체제에 맞게 다운로드 하시면 됩니다. 참고로 저는 Mac을 쓰기 때문에 이제부터 설치과정과 입력과정은 Mac 기반으로 예시를 보여드리려고 합니다.

![](https://proxy-prod.omnivore-image-cache.app/0x0,spYWrG2oEO9by-Mbwaq9qri2dCfDqeol3Zp_OSqw7h5U/https://cdn.maily.so/maqibztekqtqd3tb6i7b55fbd2tr)

압축폴더를 해제하시면 위와 같이 귀여운 양이 나오는 설치 화면이 나타납니다.

![](https://proxy-prod.omnivore-image-cache.app/0x0,speLqPDejmvz4l4AXaYVvVavuVTv2-3KDW-94l_g4Z8I/https://cdn.maily.so/006gi813x4hfecze3wix15fb722v)

저는 이미 설치를 했기 때문에 Install 후에 바로 아래와 같은 설치화면이 나타납니다.

![](https://proxy-prod.omnivore-image-cache.app/0x0,sjapWIhkw8wCxY7vMMUIp9-ewLbHjOAcj7Dk6je7swl4/https://cdn.maily.so/92cqdjkfxzztol54p1ez1uak7gwa)

터미널에 위와 같이 ollama run llama3.2를 입력해주시면 됩니다. 옆에 복사하기 버튼을 클릭하셔서 바로 Ctrl + V 하셔도 됩니다.

참고로 터미널이 모르시는 분을 위해서,

윈도우는 키보드에 윈도우 단축키를 누르신 후 CMD를 입력하시고, 맥북은 Command키 + Space Bar를 누르신 다음, Terminal이라고 작성해주시면 됩니다.

![](https://proxy-prod.omnivore-image-cache.app/0x0,slHMePDBMv2qUC5NT57dcz5Ms9QjDzbjo5yoyvswMumM/https://cdn.maily.so/qcxkl5o9125wbs7ofq5nemytmpeh)

그러면 위와 같이 상호작용이 가능합니다. 하지만 아쉽게도 한글을 입력하면 다음과 같이 나와요.

![](https://proxy-prod.omnivore-image-cache.app/0x0,sB3ZFJZeTuUkBQbUXmJnHFAY5D8iwupr5rqLL3PurLgM/https://cdn.maily.so/yjztvqwzem7fy961ryl1nlyapccp)

한글로 입력 할 경우 베트남어인지, 태국어인지, 몽골어인지 모를 희귀한 언어로 상호작용을 하게 됩니다. 아무래도 거대 언어 모델이라 불리는 LLM의 학습 기반이 영어이기 때문에 어쩔 수 없는 부분입니다.

터미널로 상호작용하는 건 상당히 불편하죠. 그래서 GUI(그래픽 유저 인터페이스)로 사용이 가능하도록 차근차근 알려드리도록 할게요.

---

## **Step 2\. Docker 설치하기**

링크 : <https://www.docker.com/>

![](https://proxy-prod.omnivore-image-cache.app/0x0,slVowvO_3cfxvBIrr8gXXPHNKn1BePE5gcY0vloew9Ts/https://cdn.maily.so/ju0nq1at2g90jy7n3gmdriaxq90g)

---

### **📌 Docker란 무엇인가요?**

Docker는 애플리케이션을 컨테이너(Container)라는 단위로 패키징하여 어디서나 동일한 환경에서 실행할 수 있게 해주는 플랫폼입니다. 쉽게 말해, 애플리케이션과 그 실행에 필요한 모든 환경을 하나로 묶어 다른 시스템에서도 동일하게 실행할 수 있도록 합니다.

주요 특징:

환경 일관성 유지: 개발 환경과 운영 환경의 차이로 인한 문제를 최소화합니다.

배포 용이성: 컨테이너 이미지를 통해 애플리케이션 배포가 간편해집니다.

리소스 효율성: 가상 머신보다 가볍고 효율적으로 시스템 리소스를 사용합니다.

왜 Docker가 필요한가요?

Ollama와 Open WebUI를 원활하게 실행하기 위해서는 필요한 환경을 구성해야 합니다. Docker를 사용하면 복잡한 환경 설정 없이도 필요한 애플리케이션을 컨테이너로 실행할 수 있어 설치 및 관리가 편리합니다.

---

![](https://proxy-prod.omnivore-image-cache.app/0x0,s75sbTNk7FruZpPp9Jru2QnIvrlg7LTKyV5eZOSxu-5I/https://cdn.maily.so/m4agq739ras685st66pqx29ykiy4)

도커를 설치하기 위해서, Download Docker Desktop을 눌러 설치환경에 맞게 파일을 다운로드 해주시면 됩니다.

도커를 설치한 후 실행하시면 아래와 같은 화면이 뜨실 거에요. 저는 구동중인 Image가 있어서 애플리케이션이 실행중이지만 처음 설치하시면 빈 화면이 출력됩니다.

![](https://proxy-prod.omnivore-image-cache.app/0x0,seLbknPB9tNW37rakdAB2d975k7cx19-rVDP8WiOP1Wk/https://cdn.maily.so/le1pxabiqbd7nsxa2ox8wnpozfbe)

Docker는 가상환경에서 운영체제에 상관없이 여러 오픈소스나 서비스를 구동할 수 있습니다.

이제 도커에서 Ollama 모델을 실행하기 위해 Open WebUI를 설치하러 가보도록 할게요.

---

## **Step 3\. Open WebUI 설치하기**

링크 : <https://openwebui.com/>

![](https://proxy-prod.omnivore-image-cache.app/0x0,sLkWfMHUed9kv0k4fnUEecNomxONclRDTe-lvUsYN3_E/https://cdn.maily.so/iz8u7ehza8n2thvfy5fhydzhq1q6)

---

### **📌 Open WebUI란 무엇인가요?**

Open WebUI는 웹 브라우저를 통해 AI 모델과 상호작용할 수 있도록 도와주는 웹 인터페이스입니다. 터미널 명령어에 익숙하지 않은 사용자도 GUI 환경에서 쉽게 AI 모델을 사용할 수 있게 해줍니다.

주요 특징:

사용자 친화적 인터페이스: 웹 브라우저를 통해 접근하므로 별도의 설치나 복잡한 설정이 필요 없습니다.

다양한 모델 지원: 여러 가지 AI 모델을 손쉽게 선택하고 전환할 수 있습니다.

확장성: 플러그인이나 추가 기능을 통해 기능을 확장할 수 있습니다.

왜 Open WebUI를 사용해야 할까요?

Ollama를 통해 AI 모델을 로컬에서 실행하더라도, 터미널에서 명령어를 입력하는 것은 다소 불편할 수 있습니다. Open WebUI를 사용하면 웹 브라우저에서 그래픽 인터페이스를 통해 AI 모델과 대화할 수 있어 사용성이 크게 향상됩니다.

---

![](https://proxy-prod.omnivore-image-cache.app/0x0,scDedszBhLoL5159Xm4Y8bqO2G6NHqeDDxzGLlj_CxUg/https://cdn.maily.so/7eo3cuamuthidt0lcsfceejbcft1)

위에 전달해드린 링크로 들어가신 다음 “Get Open WebUI”를 클릭하셔야 해요. 그러면 아래와 같이 Github 레파지토리로 이동하게 됩니다.

여기서 잠깐,

1\. GitHub (깃허브)란?

GitHub는 소스코드 관리와 협업을 위해 사용하는 온라인 플랫폼입니다. (예: 개발자들이 프로젝트를 공유하고 협력하는 공간)

2\. GitHub Repository (레포지토리)란?

레포지토리(Repository)는 프로젝트 파일과 히스토리를 저장하는 공간으로, 코드와 문서를 관리하는 폴더 같은 개념입니다. (예: 하나의 앱 개발 프로젝트를 위한 코드 모음)

![](https://proxy-prod.omnivore-image-cache.app/0x0,skKBOgKuNEPDxMMb93Y2C8epaKpfLejfzwLmuJh-r3uk/https://cdn.maily.so/e97wvxnm53iccvn315ij5yjvd58t)

일단은 아무것도 클릭하지 마시고 스크롤을 좀더 내리시면 다음 항목에 주목해주셔야 합니다.

바로 How to Install이라는 부분이에요. Github에 올라온 대부분의 레파지토리는 처음 배포자가 친절하게 안내사항에 대해 소개를 하고 있어요.

![](https://proxy-prod.omnivore-image-cache.app/0x0,sTDduYlZz0-h_fse6SdEqyNs45sz00Ojn-Ga7Rl6OnFE/https://cdn.maily.so/0oooqmtfvcviyi42hzp6zbcbxw6g)

여기서 우리는 Docker를 설치했기 때문에, 파이썬 패키지를 통한 설치가 아닌 Docker 내에서 실행하려고 해요.

아래 화면을 보시면, 맨 첫번째 줄에 있는 명령어를 사용하면 됩니다.

“If Ollama is on your computer, use this command : ” ← 라고 적힌 맨 첫줄을 봐주셔야 해요.

이미 위에서 Ollama를 설치하고 왔으니 해당 부분의 명령어를 실행해주셔야 합니다.

![](https://proxy-prod.omnivore-image-cache.app/0x0,s2-AjjVR6ZMcwC7EAnqR_C0mDSjfR8ipH-J4-MiLKKYQ/https://cdn.maily.so/522u4cnt067ofnxa6ka6cg0qpjlv)

해당 명령어를 Command(Mac - Terminal / Windows - CMD)

> docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main

정상적으로 설치가 완료되었다면 로컬에서 Open WebUI를 사용할 수 있게 됩니다.

[Https://localhost:3000](https://localhost:3000/) \~ 8080 포트 내에 접속이 가능합니다.

여기서 잠깐,

1\. 로컬호스트 ([localhost](http://localhost/))란?

로컬호스트는 자기 자신의 컴퓨터를 가리키는 주소로, 네트워크 없이 내 PC에서 서버를 테스트할 때 사용합니다. (예: [localhost](http://localhost/)는 항상 127.0.0.1 IP 주소를 의미해요.)

2\. 포트(Port)란?

포트는 컴퓨터가 네트워크를 통해 데이터를 주고받을 때 사용하는 출입구 같은 번호입니다. (예: 웹사이트 접속은 80번 포트, 메일 전송은 25번 포트를 사용해요.)

컴퓨터에 여러 프로그램이 동시에 네트워크를 쓸 때 어떤 프로그램과 연결해야 할지 포트 번호로 구분합니다.

![](https://proxy-prod.omnivore-image-cache.app/0x0,sGvFICdnqKMeNFz5NydhxQXYySjpCpQ_T3V-bTlVtSvY/https://cdn.maily.so/vx3ngrjya5bj7wg5e202fm5drxfw)

Open WebUI의 장점은 OpenAI의 API키와 Anthropic의 API키를 활용해 다양한 모델을 로컬에서 사용가능한 장점이 있습니다.

만약, 챗지피티와 클로드 사용량이 많지 않다면 API키를 활용해서 Open WebUI로 로컬에서 사용하는 방법도 괜찮은 대안이 될 수 있어요.

이미 저는 다양한 모델을 불러왔기 때문에 아마 처음에는 Ollama 3.2b 모델이 검색 되실 겁니다!

![](https://proxy-prod.omnivore-image-cache.app/0x0,s0-oGoXwMxIsfzK6Hl-GfOQHeK1S5BqnenoewNpaNoFQ/https://cdn.maily.so/l520vb2ra41e1r23vqalhp7p7asa)

하지만 llama 모델은 한국어 지원 능력이 떨어져요. 가끔 외계어를 남발하기도 하고 당최 무슨 말인지 이해 못할 문맥도 생성해주죠.

그래서 한국어 모델로 파인 튜닝(미세조정) 된 모델을 사용하는 걸 추천드려요. 지식 스타트업 Teddysum에서 개발하는 Bllossom 모델을 사용하시면 한글로 파인튜닝 된 llama 최신 모델을 사용 가능합니다.

---

## **마무리**

이번 아티클에서는 Ollama를 활용하여 로컬 AI 비서를 구축하는 방법을 단계별로 살펴보았습니다. 디지털 월세에 대한 부담을 줄이고, 데이터 보안을 강화할 수 있는 좋은 대안이 될 것입니다. 직접 시도해 보시고, 업무나 개인 프로젝트에 활용해 보세요.

여러분의 성공적인 AI 비서 구축을 응원합니다!

---

> **다음 뉴스레터 예고**

다음 호에서는 한국어 지원 모델의 심화 활용법과 Open WebUI에서의 웹 검색 기능 활성화 방법, 그리고 ChatGPT나 Claude 3.5 모델의 API 적용 방법에 대해 자세히 알아보겠습니다. 많은 기대 부탁드립니다!

---

## **FAQ**

### **Q1\. Ollama를 사용하려면 고사양의 컴퓨터가 필요한가요?**

A1\. 모델의 크기와 복잡도에 따라 다르지만, 일반적으로 충분한 RAM(최소 8GB 이상)과 저장 공간이 필요합니다. 고성능을 원한다면 더 나은 사양의 컴퓨터를 사용하는 것이 좋습니다.

### **Q2\. Ollama는 무료인가요?**

A2\. 네, Ollama는 오픈 소스로 제공되어 무료로 사용할 수 있습니다. 다만, 추가로 사용하는 모델에 따라 라이선스가 다를 수 있으니 확인이 필요합니다.

### **Q3\. 설치 중 문제가 발생하면 어떻게 해야 하나요?**

A3\. 공식 문서나 GitHub 이슈 페이지를 참고하시거나, 커뮤니티에 질문하여 해결 방법을 찾을 수 있습니다.

### **Q4\. 다른 언어 모델을 추가로 사용할 수 있나요?**

A4\. 네, Ollama는 다양한 오픈 소스 언어 모델을 지원하며, 필요에 따라 추가로 다운로드하여 사용할 수 있습니다.

### **Q5\. 기업 환경에서 사용해도 되나요?**

A5\. Ollama와 사용하고자 하는 모델의 라이선스를 확인한 후, 기업 환경에서도 사용할 수 있습니다.

---

## **참고 자료**

Ollama 공식 사이트: <https://ollama.ai/>

Docker 공식 사이트: <https://www.docker.com/>

Open WebUI GitHub 레포지토리: <https://github.com/open-webui/open-webui>

---

✅ 엉클잡스 스레드 : <https://www.threads.net/@unclejobs.ai>

🔥 엉클잡스 뉴스레터 : <https://maily.so/unclejobs> 

📌 엉클잡스 오픈채팅방 : <https://open.kakao.com/o/grJDbcOg>

[ ![](https://proxy-prod.omnivore-image-cache.app/16x0,s4J0XB6Y8Mcdi-WZgP91oCg69ol40ExAgUrersHIsttE/https://eopla.net/images/icons/upvote-finger.png) ](#) 2 

  
[ ![](https://proxy-prod.omnivore-image-cache.app/0x0,sgFaVhTsuCryUuwQ1-CWnjgDyqWeDlmosh9tI9VMfzac/https://eo-server.s3.ap-northeast-2.amazonaws.com/uploads/profile_thumb_406554f8-8e5c-4c1d-8292-fda4270bef412.png.png?X-Amz-Expires=600&X-Amz-Date=20241102T042411Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYOZYIPJSGDMGXHR3%2F20241102%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=12557302a4492b9acb10bccea411a8264fd971380aaeb0b498cb35b3baeff1ea) ](https://eopla.net/users?user=%EC%97%89%ED%81%B4%EC%9E%A1%EC%8A%A4%24543541) 

추천 아티클

[ ![](https://proxy-prod.omnivore-image-cache.app/0x0,syCN6orG-ZUzp1nkRubqdqLZN936wUN-wvVHzOao_LQ0/https://eo-server.s3.ap-northeast-2.amazonaws.com/uploads/youtube_9f3b9bd1-f138-4d4b-bf58-db4e2c81f545thumb.png.png?X-Amz-Expires=600&X-Amz-Date=20241102T042411Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYOZYIPJSGDMGXHR3%2F20241102%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=443fd7c98bf3d05831a3497edfd8c3805f2804663118570e39deceb07295ee97) ](https://eopla.net/magazines/19475)

[ ![](https://proxy-prod.omnivore-image-cache.app/0x0,saHAUuoelF6WSkQtyRFaK2s2kpSnkMHgOaBp3hsRUAmY/https://eo-server.s3.ap-northeast-2.amazonaws.com/uploads/youtube_50a4bdb0-a093-4119-8f82-94ff08b2bfbbsam-altmany-combinator_1200xx5760-3240-0-300.jpg.jpg?X-Amz-Expires=600&X-Amz-Date=20241102T042411Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYOZYIPJSGDMGXHR3%2F20241102%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=cc18e897a5fe77ac5fcf0989e7740251f8025d38c6b7ea825bba3c09073760e6) ](https://eopla.net/magazines/2566)

[ ![](https://proxy-prod.omnivore-image-cache.app/0x0,sRM2JwHCFVfLIxmNYCQ5H8YXaZlZpyvgSdWphiqGAT0E/https://eo-server.s3.ap-northeast-2.amazonaws.com/uploads/profile_thumb_e7a1c808-69a5-48ba-b2c8-ca4deee3fb9bimage__1_.png.png?X-Amz-Expires=600&X-Amz-Date=20241102T042411Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYOZYIPJSGDMGXHR3%2F20241102%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=1440b08bd454aab47274d4dc39828de5d6d76026af4643e3e489dad17d6d5b9d) ](https://eopla.net/users?user=%EA%B9%80%EC%A7%80%EC%9C%A4%24246024) [  김지윤 ](https://eopla.net/users?user=%EA%B9%80%EC%A7%80%EC%9C%A4%24246024)  에디터  1년 이상 전 

[ ![](https://proxy-prod.omnivore-image-cache.app/0x0,snL3c8Oo39Iei-R4l23BPhhROLAJJ9neICGz8Oygv9Pc/https://eo-server.s3.ap-northeast-2.amazonaws.com/uploads/youtube_46f6abea-eb32-440d-8422-fe9df06205d55eab9e4a-2626-4ac6-8e91-b0bd0780695bimage__2_.png.png.png?X-Amz-Expires=600&X-Amz-Date=20241102T042411Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYOZYIPJSGDMGXHR3%2F20241102%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=d8a12bcdab042e6f722c71ad00668e7c1e92a90ca47d2d6b209e252cef13d568) ](https://eopla.net/magazines/62)

[ ![](https://proxy-prod.omnivore-image-cache.app/0x0,s-QxqEKe_SYoT_RTlzrEdwuIrfURzR5iKK74XRzTxAnQ/https://eo-server.s3.ap-northeast-2.amazonaws.com/uploads/profile_thumb_040d93c8-c37a-47e0-9041-10149fea8b8b257fd44c-40c7-470d-bd37-c036ee8fd96f71488903_24427217225081418_1432608860094332928_n.jpg.jpg.jpg?X-Amz-Expires=600&X-Amz-Date=20241102T042411Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYOZYIPJSGDMGXHR3%2F20241102%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=099beeafad9418afdcfced6bfcea611f8c99f1c6360272759eb2fd6a06df0f0b) ](https://eopla.net/users?user=%ED%83%9C%EC%9A%A9%2468) [  태용 ](https://eopla.net/users?user=%ED%83%9C%EC%9A%A9%2468)  2년 이상 전 