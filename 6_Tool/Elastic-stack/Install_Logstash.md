# Install Logstash

- `sudo apt-get install logstash`
- `sudo vi /etc/logstash/conf.d/10-syslog.conf` : configuration file 수정

```
input {
  file {
    type => "syslog"
    path => ["/var/log/messages", "/var/log/*.log"]
  }
}

output {
  stdout {
    codec => rubydebug
  }
  
  elasticsearch {
    hosts => "localhost"
  }
}
```

- elastic search database 안에 모든 파일과 syslog를 저장한다.
- input section : 저장할 포맷과 저장 path를 명시한다.
- output section : 
  - "stdout output" : logstash 디버그 할 때 사용 (/var/log/logstash/logstash.stdout)에서 확인
  - "elasticsearch output" : 실제 log를 elastic search에 저장



### Start Logstash

- `sudo service logstash restart`



### Verify Logstash

- `sudo curl -XGET 'localhost:9200/_cat/indices?v&pretty'`



`health status index uuid pri rep docs.count docs.deleted store.size pri.store.size` 가 나오면 성공 !!