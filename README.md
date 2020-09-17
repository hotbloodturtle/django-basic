# docker, django 기본 개발환경

- 특별히 환경구축 하지 않고 docker만 설치되어있으면 바로 개발 가능

### 1. docker-compose.local.yml (로컬버전 실행)

- vscode extensions - python
- docker-compose -f docker-compose.local.yml up -d 실행
- vscode debug-run으로 가서 실행
- degug-run 탭에서 breakpoints - uncaught exceptions 체크 해제
- vscode의 Remote Development extension 설치하고 사용하면 python select interpreter도 가능!! (but 로컬에 환경구축을 추천..)

---

---

---

---

---

### 2. docker-compose.develop.yml (dev서버 버전 실행)

### docker-compose.yml -> services -> django -> command 의 명령어 변경

- docker-compose -f docker-compose.develop.yml up -d 실행

---

### 로컬에서 언제든지 docker-compose 명령을 바꿔서 local, dev 버전으로 실행할수 있다.
