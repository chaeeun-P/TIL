## 수강사진
![사진](/)

## 5-2. join 이해하기

* 그냥 단순히 index 를 나타낼 땐 key 로서 역할 X 
    * 공통값이 key 가 될 수 있음! 
* 데베는 정규화 과정을 거침 -> 개발을 위해 ~ 
    * 정규화는 중복을 최소화하게 데이터를 구조화한 것 

## 5-3. 다양한 조인 방법
![사진](/)
![사진](/)

* inner join
    * 공통 요소만 연결 

* left / right join
    * left / right 테이블 기준으로 붙임 (데이터 X -> null 값으로 둠) 
     * 겹치는 게 없어도 각 테이블에 필요한 데이터가 있을 때... 

* full join
    * 그냥 다 붙여

* cross join 

## 5-4. join 쿼리 작성 

### 쿼리 작성 흐름
1. 테이블 확인
2. 기준 테이블 확인 -> 가장 많이 참고할 기준 테이블 정의 
3. join key 찾기
4. 결과 예상 -> 손, 엑셀로 1차 확인 
5. 쿼리 예상 

### 문법
```
SELECT
    A.col1,
    A.col2,
    B.col1,
    B.col2
FROM table1 AS A
LEFT JOIN table2 AS B
ON A.key = B.key
```
* 테이블 이름이 기니까 약어로 넣어주는 것이 좋음 
* cross join 제외 모두 ON 부분이 필요함 
* key 에는 공통된 칼럼의 이름이 들어감 
    * key 가 되는 칼럼은 SELECT 문에 하나만 써도 됨 (똑같은 게 두 번 나오니까) 

## 5-5. 조인을 처음 공부할 때 헷갈렸던 부분

1. 여러 방법 중 어떤 걸 사용할까?
    1. 보통 left 를 제일 많이 사용
    2. 목적에 맞게 결과 예상해서 사용 
2. 어떤 걸 왼쪽 / 오른쪽?
    1. 기준이 되는 (보고 싶은 데이터가 있는) 테이블을 **왼쪽**에 두기 
3. 여러 테이블 연결 가능?
    1. 가능해용 ㅎㅎ 
    1. 첫 번째 조인 ON 밑에다가 쭉 ~ 쓰면 됨
4. 칼럼 모두 다 선택?
    1. 사용 안 할 거면 ㄴㄴ 

## 5-6~7. 연습 문제

### 1. 트레이너가 보유한 포켓몬들은 얼마나 있는지 알 수 있는 쿼리를 작성해주세요.(보유=status가 Active, Training인 경우를 의미, Released는 방출했다는 것을 의미)

* 쿼리 작성 목표, 확인할 지표: 포켓몬(이름) 얼마나 있는지 알고싶음
* 쿼리 계산 방법: trainer_pokemon+pokemon JOIN -> 그 후 GROUP BY 집계(COUNT)
* 데이터의 기간: X
* 사용할 테이블: trainer_pokemon, pokemon
* Join KEY: trainer_pokemon의 pokemon_id, pokemon의 id
* 데이터 특징: 보유=status가 Active, Training인 경우를 의미, Released는 방출했다는 것을 의미하므로 Released 제외

---

```
SELECT
   kor_name,
   COUNT(tp.id) AS pokemon_cnt
FROM(
    SELECT
        id,
        pokemon_id,
        trainer_id,
        status
    FROM basic.trainer_pokemon
    WHERE status IN ("Active", "Training") 
) AS tp 
LEFT JOIN basic.pokemon AS p
ON tp.pokemon_id = p.id
GROUP BY
    kor_name
ORDER BY
    pokemon_cnt DESC
```
* 만약 필터링한 데이터가 필요한 경우, 필터링 후 -> 조인이 GOOD 
    * 데이터 부담을 줄이기 위해서!
* or 과 in 은 같은 역할이나 in 의 가독성이 더 굿 
* 겹치는 칼럼이 있을 때, 어떤 칼럼인 지 명확하게 써줘야 함 (count 쓸 때) 
    * 칼럼 하나면 p. 안 써도 괜찮음 
* FROM -> JOIN -> WHERE -> GROUP BY 
* WHERE 에 1=1 을 쓰면 그냥 TRUE 의 의미! 모든 행을 반환하겠다는 뜻 

### 2. 각 트레이너가 가진 포켓몬 중 'Grass' 타입의 포켓몬 수를 계산해주세요. (단, 편의를 위해 type1 기준으로 계산)

* 쿼리 작성 목표, 확인할 지표: 트레이너가 보유한 포켓몬 중 Grass 타입 포켓몬의 수
* 쿼리 계산 방법: 트레이너가 보유한 포켓몬 조건->Grass 타입으로 WHERE 조건 걸어서 COUNT
* 데이터의 기간: X
* 사용할 테이블: trainer_pokemon, pokemon
* Join KEY: trainer_pokemon.pokemon_id = pokemon.id
* 데이터 특징: 1번과 동일
* group by 추가 고민  
    ![사진](/) 
--- 
```
SELECT
    p.type1
    COUNT(tp.id) AS pokemon_cnt
FROM(
    SELECT
        id,
        pokemon_id,
        trainer_id,
        status
    FROM basic.trainer_pokemon
    WHERE status IN ("Active", "Training") 
) AS tp 
LEFT JOIN basic.pokemon AS p
ON tp.pokemon_id = p.id
WHERE
    p.type1 = "Grass"
GROUP BY
    type1 
ORDER BY
    2 DESC
```
* 2 : 두 번째 칼럼 

### 3. 트레이너의 고향(hometown)과 포켓몬을 포획한 위치(location)을 비교하여, 자신의 고향에서 포켓몬을 포획한 트레이너의 수를 계산해주세요. (status와 상관없이 구해주세요.)

* 쿼리 작성 목표, 확인할 지표: 트레이너 고향과 포켓몬 포획 위치가 같은 트레이너 수 계산
* 쿼리 계산 방법: trainer(hometown), trainer_pokemon(location) JOIN -> hometown=location -> 트레이너 수 COUNT
* 데이터의 기간: X
* 사용할 테이블: trainer, trainer_pokemon
* Join KEY: trainer.id = trainer_pokemon.trainer_id
* 데이터 특징: status 상관없이 구하기

---
```
SELECT
    COUNT(DISTINCT tp.trainer_id) 
FROM basic.pokemon basic.trainer_pokemon AS tp
LEFT JOIN basic.trainer_pokemon AS p
ON tp.id = p.trainer_id
WHERE
    tp.location IS NOT NULL
    AND tp.hometown = p.location 
ORDER BY
    2 DESC
```
* 메타데이터가 있는 것을 left 가 있으면 헷갈릴 수 있음...
* NULL 값 있는지 확인 (데이터 손실 위해) 

### 4. Master 등급인 트레이너들은 어떤 타입의 포켓몬을 제일 많이 보유하고 있을까요?

* 쿼리 작성 목표, 확인할 지표: Master 등급의 트레이너들이 가장 많이 보유하고 있는 타입
* 쿼리 계산 방법: trainer+pokemon+trainer_pokemon (앞에 두 개가 조인키가 없어서 얘가 조인키 역할 대신 해줌) -> Master 조건 설정 (WHERE) -> type1 GROUP BY + COUNT
* 데이터의 기간: X
* 사용할 테이블: trainer, pokemon, trainer_pokemon
* Join KEY: trainer.id = trainer_pokemon.trainer_id, pokemon.id = trainer_pokemon.pokemon_id

---
```
SELECT
    type1, 
    COUNT(tp.id) AS cnt
FROM(
    SELECT
        id,
        pokemon_id,
        trainer_id,
        status
    FROM basic.trainer_pokemon
    WHERE status IN ("Active", "Training") 
) AS tp
LEFT JOIN basic.pokemon AS p
ON tp.pokemon_id = p.id
LEFT JOIN basic.trainer AS t
ON tp.trainer_id = t.id 
WHERE
    t.achievement_level = "Master"
GROUP BY
    type1
ORDER BY
    2 DESC
```

### 5. Incheon 출신 트레이너들은 1세대, 2세대 포켓몬을 각각 얼마나 보유하고 있나요?

* 쿼리 작성 목표, 확인할 지표: Incheon 출신 트레이너들이 보유한 포켓몬 세대 구분
* 쿼리 계산 방법: trainer+pokemon+trainer_pokemon -> Incheon 조건(WHERE) -> 세대(generation)로 GROUP BY COUNT
* 데이터의 기간: X
* 사용할 테이블: trainer, pokemon, trainer_pokemon
* Join KEY: trainer.id = trainer_pokemon.trainer_id, pokemon.id = trainer_pokemon.pokemon_id

--- 
```
SELECT 
    generation,
    COUNT(tp.id) AS cnt 
FROM(
    SELECT
        id,
        pokemon_id,
        trainer_id,
        status
    FROM basic.trainer_pokemon
    WHERE status IN ("Active", "Training") 
) AS tp
LEFT JOIN basic.trainer AS t
ON tp.pokemon_id = p.id
LEFT JOIN basic.pokemon AS p 
ON tp.trainer_id = t.id 
WHERE
    t.hometown = "Incheon"
GROUP BY
    generation
```
* 코드를 지속적으로 사용하기 위해서는 미래의 데이터 변화를 확인하여 코드를 짜야 함 ~! 