# 데이터 가공을 위한 SQL

## 하나의 값 조작하기

### 데이터를 가공하는 이유

- 데이터의 코드값을 저장 할 때 or 접근 로그를 문자열로 표현할 경우
- 로그 데이터와 업무 데이터를 함께 다루는 경우, 데이터 형식이 일치하지 않는 경우,
- NULL 이 존재하는 경우



### 데이터의 코드값을 실제 값으로 연결

```
select 
	user_id, 
	case
		when register_device = 1 then '데스크톱'
		when register_device = 2 then '스마트폰'
		when register_device = 3 then '애플리'
		else '' # default
	end as device_name
from mst_users
```

`case {} when {} then end`  : case 문 이용.



### url 요소 추출

**referrer**

- 클릭이나 검색이 일어났을 때 주소 뒤에 붙는 또 다른 주소
- 이를 통해 어떤 사이트를 통해, 어떤 클릭을 통해 사이트에 왔는 지 알 수 있음
- 직접 주소를 치거나 sms 링크를 들어온 경우 확인이 어려움

```
select
	stamp,
	substring(referrer from 'https?://([^/]*)') as referrer_host
	
from axxess_log
```

- regex를 이용해 추출 실제 미들웨어에 따라 query가 달라질 수 있다.



```
select
	stamp
	, url
	, substring(url from '//[^/]+([^?#]+)') as path
	, substring(url from 'id=([^&]*)') as id
from access_log
```

`substring(str, start, length)` : 문자열 자르기



- mysql regex
  - `^` : string 시작
  - `$` : string 끝
  - `.` : single character
  - `[...]` : 칸에 있는 어느 값
  - `[^...]` : 칸에 안에 이외의 값
  - `*` : 0 or more
  - `+` : 1 or more
  - `p1|p2|p3` : or
  - `{n}` : n번 가능
  - `{m,n}` : m에서 n 번 가능
  - `[:alnum:] or [0-9a-z]` : alpha + numeric
  - `[:digit:]` : digits

- `where name REGEXP'^..pp'`으로 서칭



### 문자열 배열로 분해

```
select
	stamp
	, url
	, split_part(substring(url from '//[^/]+([^?#]+)', '/', 2)) as path1
	, split_part(substring(url from '//[^/]+([^?#]+)'), '/', 3)) as path2
from access_log
```



### 현재 날짜와 타임스탬프 추출

```
select
	current_date as dt
	, current_timestamp as stamp
;
```



### 지정한 값 날짜/시간 추출

```
select
	cast('2016-01-01' as date) as dt
	, cast('2016-01-01 12:00:00' as timestamp) as stamp
```



### 연도, 월, 일 추출

```
select 
	year(stamp) as year
	, month(stamp) as month
	, day(stamp) as day
from
;
```

```
# 문자열로 추출시

select
	stamp
	, substring(stamp, 1, 4) as year
	, substring(stamp, 6, 2) as month
	, substring(stamp, 9, 2) as day
from
;
```



### 결손 값 디폴트 값으로 대체

```
select 
	purchase_id
	, amount
	, coupon
	amount - coalesce(coupon, 0) as discount
from 
	purchase_log_with_coupon
```

`coalesce(exp1, 0)`: exp1이 null일 때 0으로 대체