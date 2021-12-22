# 프로젝트명 : 백수탈출
<div align=center>
<img src="https://github.com/teraglass/Baeksu/blob/main/manual/home.png" width="500" height="375">

DDIT 'AI 기술을 활용한 소프트웨어 엔지니어링' 중간프로젝트<br/>

프로젝트 기간 : 2021-04-07 ~ 2021-04-21 <br/>

구현한 화면은 사용자 메뉴얼(ppt)을 통해 확인해주세요 : <a href="https://github.com/teraglass/Baeksu/blob/main/manual/baeksu_manual.pptx">![manual](https://img.shields.io/badge/Manual-47A248?style=flat&logo=Matrix&logoColor=white)</a>
</div>

---

#### 사용한 기술

- 서버 : Python, Flask
- DB 및 DB 연결 라이브러리 : Oracle, mybatis
- 게시판 페이지 : HTML, CSS, Jquery, JavaScript
- 프로젝트 버전 관리 : SVN (이클립스 내), RedMine (관련 문서 작성 및 보고)

#### 맡은 역할

- DB 개념적, 논리적 설계
- 전체 화면 레이아웃 
- 면접 후기 게시판과 건의사항 게시판 DB 연결 및 화면 구현

---
#### 개인적으로 변경한 사항

- calendar 관련 파일 오타 리팩토링
- github에 기록용으로 남기기 위해 database 관련 정보들을 다 공개로 올렸지만 현실의 사이트를 배포할 때는 보안상 데이터베이스 정보와 API Key 등을 공개하지 않는다는 점에서 key를 암호화
  - key.xml 
    ```
      <?xml version="1.0" encoding="UTF-8" ?>

      <resources>
          <string name="secret_key">mykey</string>
          <string name="db_address">baeksu/비밀번호@{ip-address}/xe</string>
      </resources>
    ```
  - elemTree 사용
    ```
    app = Flask(__name__, static_url_path='', static_folder='static')

    keyXml = elemTree.parse('keys.xml')
    secretKey = keyXml.find('string[@name="secret_key"]').text
    app.config['SECRET_KEY'] = secretKey
    ```
- 흩어져 있던 xml, py 파일들을 mapper, dao 폴더로 그룹화
- 
#### 개인적으로 추가, 변경하고 싶은 사항
- 배포 👉  AWS는 배포까지 완료해도 주어진 주소로 연결이 안됨.
- 카카오맵 수정 👉 API key 문제인지 화면에서 클릭하면 버튼만 표시되고 지도는 표시되지 않

