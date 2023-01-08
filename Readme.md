# Django로 restful api 서버 만들기

## REST(REpresentational State Transfer)

자원을 이름으로 구분해서 해당 자원의 상태를 주고 받는 것을 의미한다.

HTTP프로토콜을 그대로 사용해 웹의 장점을 활용할수 있는 아키텍쳐 스타일이며 client와 server사이의 통신 방식중 하나이다.



### 통신 방식

- GET - Read : 정보요청, URI가 가진 정보를 검색하기 위해 서버에 요청한다.

- POST - Create : 정보 입력, 클라이언트에서 서버로 전달하려는 정보를 보낸다.
- PUT - Update : 정보 업데이트, 주로 내용을 갱신하기 위해 사용한다.(데이터 전체를 바꿀 때)
- PATCH - Update : 정보 업데이트, 주로 내용을 갱신하기 위해 사용한다.(데이터 일부만 바꿀 때)
- DELETE - Delete : 정보 삭제



### 요청, 응답의 DATA Type

JSON, XML, TEXT, RSS 등이 있지만 **일반적인 방법은 JSON, XML** 이다..



### API(Application Programming Interface)

응용프로그램에서 사용할 수 있도록 운영체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스이다.

REST특징을 기반으로 서비스api를 구현하여 REST Data Type에 맞게 요청을 하고 받아오는 작업이다.





---

Restful의 특징

1. URI는 정보의 자원을 표현해야 한다.
2. CRUD(post, get, put, delete) 를 호출할 때 방식을 하나로 통일하자.



RESTful이란?

**REST 설계 규칙**을 잘 지키서 만든 API를 RESTful api라고 한다.



## 개발환경 

파이참, 파이썬





