## Weather Bot API Project

### 프로젝트 세팅
```
# 가상 환경 생성
python3 -m venv .venv
source .venv/bin/activate

# 패키지 설치
pip install -r requirements.txt
```

### 서버 시작
```
cd src
uvicorn main:app --reload
```

### api_key 삽입
```
src > config.py에서 EXTERNAL_WEATHER_API_KEY에 노션 문서에 기록된 외부 날씨 요청용 api_key를 삽입해주세요.
```

### 테스트 실행
```
# weather-bot/src

pytest
```

### API 문서
- [Swagger](http://127.0.0.1:8000/docs)
- [Redoc](http://127.0.0.1:8000/redoc)
