### vscode 로 실행 방법
- docker-compose up -d
- vscode debug-run으로 가서 실행
- docker extension 설치 후 docker 탭에서 실행중인 container 우클릭 open in browser
- degug-run 탭에서 breakpoints - uncaught exceptions 체크 해제

---
---

### 일반 실행방법
docker-compose.yml 파일 수정




```
pip install debugpy -t /tmp && python /tmp/debugpy --wait-for-client --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:8000 --nothreading
```

# 위부분 바꾸기

```
python manage.py runserver
```

