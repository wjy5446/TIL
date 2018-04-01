# Elastic_search Mapping

타입을 제대로 지정하지 않는 다면 Kibana와 같은 시각화 및 분석 할 때 어려움이 있다.



- classesRating_mapping.json

```
{
  "class"{
    "properies" : {
    	"title" : {"type":"string"}
    	"submit_date" : {"type":"date", "format" : "yyyy-MM-dd},
    	"school_location" : {"type":"geo_point"}
    }
  }
}
```



### Create Mapping

- `curl -XPUT 'http://localhost:9200/classes/class/_mapping' -d @classesRating_mapping.json`