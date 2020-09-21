# docker, django 기본 개발환경

- 특별히 환경구축 하지 않고 docker만 설치되어있으면 바로 개발 가능

### 1. docker-compose.yml (일반 실행)

### docker-compose.yml -> services -> django -> command 의 명령어 변경

- docker-compose up 실행
- log 확인을 위해 daemon으로 실행하지 않는다.
- ec2에 올릴 때는 -d 옵션을 추가해준다.

---

---

---

---

---

### 2. docker-compose.vscode.yml (vscode 디버깅 버전 실행)

- vscode extensions - python
- docker-compose -f docker-compose.vscode.yml up -d 실행
- vscode debug-run으로 가서 실행
- degug-run 탭에서 breakpoints - uncaught exceptions 체크 해제
- vscode의 Remote Development extension 설치하고 사용하면 python select interpreter도 가능!! (but 로컬에 환경구축을 추천..)

---
