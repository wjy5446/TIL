# Spark Core 실행

### Spark 실행 절차

1) spark-submit에서 application 제출

2) spark-submit은 driver program을 실행해 main 함수 호출

3) driver program은 cluster manager에게 executor 리소스 요청

4) cluster manager가 executor 실행

5) task를 나누어서 executor 전송

6) executor가 task 실행

7) application 종료시 cluster manager 리소스 반납



### Spark 실행 모드

- Local 멀티쓰레드 환경 설정 - client mode
- Cluster 분산 환경 설정 - cluster mode



### driver - multi thread 모드로 실행

- ` ./bin/spark-shell --master local[*]`

- `jps` 실행시 `SparkShell` 확인



### driver - cluster 모드로 실행

- `./sbin/start-master.sh` : 마스터 실행
- `./sbin/start-slave.sh spark://CentOS7-14:7077` : 워커 실행
- `./bin/spark-shell --master spark://CentOS7-14:7077` : spark-shell 실행



- jps 실행시, `master`, `worker`, `sparksubmit` 동작



### Spark Submit

Cluster Manager에게 Spark Application을 제출하는 툴

`./bin/spark-submit`

- `--master` : master URL
- `--deploy-mode` : Driver Program이 실행되는 곳
- `--class` : main함수가 들어가 있는 Entry Point 클래스
- `--executor-memory` : Executor가 사용할 메모리
- `--driver-memory` : Driver가 사용할 메모리
- `<application-jar>` : application을 실행하는 코드 (Dependency lib 포함)



- **Deploy mode**
  - Client 모드 : spark-submit 일부에서 실행, driver의 출력을 콘솔 일부에서 확인 가능, application 실행도안 worker node에 연결
  - Cluster 모드 : driver program이 worker node 중 하나에서 실행,  python, r 지원하지 않음.
- **master URL**
  - local : 하나의 worker 실행
  - local[K] : k개의 worker 실행
  - local[*] : 될수있는 한 많은 worker 실행
  - Spark://HOST:7077 : spark standalone 이용
  - Mesos://HOST:5050 : mesos 이용
  - yarn : YARN 이용
  - K8s://HOST : kubernetes 이용



#### Deploy Mode - client

- `./sbin/start-master.sh` : master 실행
- `./sbin/start-slave.sh spark://CentOS7-14:7077` : slave 실행



- `./bin/spark-submit --master spark://CentOS7-14:7077 --class org.apache.spark.examples.SparkPi /kikang/spark-2.3.1-bin-hadoop2.7/examples/jars/spark-examples_2.11-2.3.1.jar 3000 ` : jar 실행



- jps 확인, `master`, `slave`, `CoarseGrainedExecutorBackend`, `SparkSubmit` 실행



#### Deploy Mode - cluster

- `./bin/spark-submit --deploy-mode cluster --master spark://CentOS7-14:7077 --class org.apache.spark.examples.SparkPi /kikang/spark-2.3.1-bin-hadoop2.7/examples/jars/spark-examples_2.11-2.3.1.jar 3000` : jar 실행

- REST API 이용, spark://CentOS7-14:7077 -> 6066
  - 6066 이용시, 안정하게 동작 



- Jsp 확인시, `master`, `slave`, `SparkSubmit`, `DriverWrapper` 실행



#### Deploy Mode - core, memory config

- `--total-executor-cores 1 --executor-memory 512M --driver-memory 512M`

- `--supervise` : Driver가 죽어도 다시 살아나는 모드



#### History server 실행

실제 spark 실행시 동작할 때만, 동작여부 확인이 가능하므로, spark 동작 이외에도 log를 확인하기 위해 history server 실행

- `./conf/spark-defaults.conf`에서 

  - `spark.eventLog.enabled true`
  - `spark.evenKog.dir spark/history`
  - `spark.history.fs.logDirectory spark/history`
