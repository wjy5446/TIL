# Install Kibana

- `sudo apt-get install kibana`


- `sudo vi /etc/kibana/kibana.yml` : kibana 설정

  ```
  server.port : 5601
  server.host : "localhost"
  # server.host : "0.0.0.0" 어디서든 접속할 때 사용
  elasticsearch.url: "http://localhost:9200"
  ```



### Start kibana

- `sudo service kibana start`



### Setting Kibana index pattern

- Management -> index pattern
  - "index pattern"을 생성하는 이유는 logstash가 모은 로그를 읽어드리기 위해서 이다. 기본 속성은 매일 모든 데이터를 받는다.

