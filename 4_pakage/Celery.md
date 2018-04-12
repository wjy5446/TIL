### Celery

Python에서 비동기 작업 큐을 관리해 주는 패키지

-> I/O의 Iddle 타임이 긴 작업들을 처리할 때 매우 효율 적이다.



### Message Queue

CPU 연산 처리전에 잠시 저장하는 공간

-> 여기서는 Redis를 이용해 저장



### Broker와 worker의 차이

- Broker : 여러 작업을 전달하는 역활
- Worker : 분배된 작업을 동시 다발적으로 처리하는 역활



### Redis(Remote Dictionary Sever)

`키-값` 구조의 데이터를 저장하는 NoSQL 일종, 모든 데이터를 메모리로 불러와서 처리하는 메모리 기반 DBMS



### 설치

- `https://github.com/MSOpenTech/redis/releases`에서 msi 파일 다운로드
- `C:\ProgramFiles/Redis> redis-cli.exe` 실행
- `shutdwon`
- `C:\ProgramFiles\Redis> redis.server.exe`



- `conda install -c conda-forge celery==3.1.25`
- `conda install -c conda-forge redis-py`



### Redis 실행

`import redis`

`r=redis.StricRedis(host='localhost', port=6379, db=0)`

- port 번호 : 6379
- `result = r.set("foo", "bar")` : foo에 bar 저장, 반환 값으로 set 완료에 대한 boolean 값 반환
- `r.get("foo")`: foo 값 가져오기, binary 값 반환
- `result.decod("ascii")` : ascii 값으로 변형



### Celeary 실행

- 비동기화할 함수 .py로 제작

`from celery import Celery`

```
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
app = Celery('task', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)

@app.task
def add(a,b):
	return a+b
```

`celery -A task worker -l info Window`



- task.py 실행

```
import task

result = task.add.delay(2,3)
result.ready() # 실행 결과 확인
result.get() # 실행 결과 가져오기
```

