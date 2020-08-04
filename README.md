# docker, django 기본 개발환경
- 특별히 환경구축 하지 않고 docker만 설치되어있으면 바로 개발 가능


### vscode 로 실행 방법 (디버깅가능)
- vscode extensions - python, docker 설치
- docker-compose up -d   (명령어 입력)
- vscode debug-run으로 가서 실행
- docker extension 설치 후 docker 탭에서 실행중인 container 우클릭 open in browser
- degug-run 탭에서 breakpoints - uncaught exceptions 체크 해제

---
---

### 일반 실행방법 (디버깅 불가...)
### services -> django -> command 의 명령어 변경

before
```
    command: 
      - bash
      - -c
      - |
        python manage.py migrate
        pip install debugpy -t /tmp && python /tmp/debugpy --wait-for-client --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:8000 --nothreading
```

after
```
    command: 
      - bash
      - -c
      - |
        python manage.py migrate
        python manage.py runserver 0:8000
```

