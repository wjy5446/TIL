# SQLAchemy

### ORM (Object-Relational Mapping)

데이터 베이스와 객체 지향 프로그래밍 언어 간에 데이터를 변환하는 프로그래밍 기법, 즉, 가상의 객체 데이터 베이스를 구축하는 방법이다.

##### 대표적인 패키지 : SQLAlchemy



### DB 엔진에 연결

`engine = sqlalchemy.create_engine("mysql+mysqldb://root:<pw>@13.124.123.82/db_name")`



### Mapping class 생성

- declarative_base()를 상속받아서 사용
- row 하나 하나를 의미 한다.

```
Base = declarative_base()

class User(Base):
	__tablename__ = "user2"
	
	user_id = column(Integer, primary_key=True)
	name = Columns(String(2))
	age = Columns(Integer)
	
	def __init__(self, name, age):
		self.name = name
		self.age = aage
	
	def __repr__(self):
		return "<User {}, {}>".format(self.name, self.age)
```



### Engine에 연결된 데이터 베이스 테이블 생성

`Base.metadata.create_all(engine)`



### Session 

DB와 Object간의 통로 역활

`Session = sessionmaker(bind=engine)` : Session 열기

`session.close()` : session 닫기



### Insert in session

session에 user object 추가

`User = User('jin', 'jin@gmail.com', '27', '2016-02-21')`

`session.add(user)` : session에 정보 추가

`session.add_all(users)` : session multi object



### Commit & rollback

- `session.commit()` : 실제 데이터 베이스에 추가
- `session.rollback()` : 최근에 add했던 정보 제거



### Select

`result = session.query(User).all()` : 모든 data형식 반환

### filter

- 부등식

`result = session.query(User).filter(User.name == 'jin')`

- like

`result = session.query(User).filter(User.email.like("%gmail%"))` : SQL like (User 앞에 `~` 사용시 아닌 애들만 가져온다.)

- in

`result = session.query(User).filter(User.name.in_(["alice", "andy"]))` 

- and_, or_

`from sqlalchemy import and_, or_`

`result = session.query(User).filter(and_(User.age < 30, User.email.like("%gmail%")))`

- order_by

`result = session.query(User).order_by(User.age.desc())` : 내림차순으로 정렬

- count

`result = session.query(User).count()`



### Update

`jin = session.query(User).filter(User.name == "jin").one()` : 하나만 가져오기

`jin.age = 30` 



### Delete

`session.query(User).filter(User.name == "jin").delete()` : 내용 삭제



