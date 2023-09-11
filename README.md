# [S2d] Korean Pronunciation Practice Web Application Study

## Installation
1. install python3.8

2. install packages
```bash
# You can add package names to this requirements.txt
pip install -r requirements.txt
```

## execute web server

```bash
uvicorn fastapi_app.main:app --reload --host 0.0.0.0 --port 8000
```

## connect to web server
http://127.0.0.1:8000

## connect api document
http://127.0.0.1:8000/docs

## file structure
```
.
├── fastapi_app
│   ├── routers # api routers 
│   |   ├── rank.py # 리더보드 관련 api 구현 파일
│   |   ├── speech.py # 음성연습 관련 api 구현 파일
│   ├── utils
│   |   ├── openai_stt_api.py # openai stt api 구현 모듈
│   |   ├── text_diff.py # 문장 비교 알고리즘 구현 모듈
│   ├── views
│   |   ├── home.py # 연습페이지 웹페이지 구현 파일
│   |   ├── ranking.py # 리더보드 웹페이지 구현 파일
│   ├── main.py # main file of fastapi. uwsgi will run this file to start web server.
├── static # static files, you can access files in this directory by http://127.0.0.1:8000/static/css/home.css
│   ├── css # css files
│   ├── img # image files
│   └── js # javascript files
├── templates # html files
│   ├── home.html # 연습 웹페이지
│   ├── ranking.html # 리더보드 웹페이지
├── README.md # this file
├── requirements.txt # python package list
