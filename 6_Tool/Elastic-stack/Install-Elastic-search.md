# Install Elasticsearch on Ubuntu 16.04 

### 1. Apk-get update, upgrade

- `sudo apt-get update`
- `sudo apt-get upgrade`



### 2. Install JAVA 8 

- `sudo apt-get install default-jre`





### 3.Install Elastic search

- `wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -`

- `sudo apt-get install apt-transport-https`

- `echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list

  sudo apt-get update`

  ​

- `sudo apt-get install elasticsearch`

  ​


### 4. Config Elasticsearch

- 설치 경로 : '/usr/share/elasticsearch'
- Config : '/etc/elasticsearch'
- Init script : '/etc/init.d/elasticsearch'



- `vi /etc/elasticsearch/elasticsearch.yml`
  - `newwork.host : "localhost"`
  - `http.port : 9200`
- `vi /etc/default/elasticsearch `
  - `START_DAEMON = True`
- `vi /etc/elasticsearch/jvm.optuins` : heap size 문제 일시

  - `-Xms512m, -Xmx512m` 로 변경


### 5. START & STOP & CHECK

- `sudo systemctl enable elasticsearch.service` : 부팅시 자동 실행
- `sudo service elasticsearch start` : 시작
- `sudo service elasticsearch stop` : 종료
- `curl -XGET 'localhost:9200'` : check run




### 6. Trouble Shooting

- 5.0 -> 6.0 update시 문제 : https://discuss.elastic.co/t/elasticsearch-service-wont-start-after-full-cluster-upgrade-from-5-4-to-6-0/108048/5