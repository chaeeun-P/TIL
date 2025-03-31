## 수강사진
![사진](/images/KakaoTalk_20250401_012054592.jpg)
---
# 문풀
## 1번 문제 : 포켓몬 중에 type2 가 없는 포켓문의 수를 작성
```
SELECT
  COUNT(id)
FROM basic.pokemon
WHERE type2 IS NOT NULL
```
* NULL 값 있는 것만 원할 땐 : IS NULL
* NULL 값 없는 것만 원할 땐 : IS NOT NULL
* WHERE 여러 개 잇고 싶다면 : AND (둘 다) / OR (하나만) 사용
  * OR 쓸 땐 () or ()

## 2번 문제 : type2가 없는 포켓몬의 type1과, type1의 포켓몬 수를 알려주는 쿼리 작성 + 포켓몬 수 큰 순으로 정렬
```
SELECT
  type1, 
  COUNT(id) as cnt
FROM basic.pokemon
WHERE type2 IS NULL
GROUP BY type1
ORDER BY cnt DESC
```
* 집계함수는 항상 **group by** 와 써야 함! 물론 1번 문제처럼, 특정 칼럼만 계산하는 게 아니라면 쓰지 않아도 되지만, 2번 문제처럼 특정 칼럼만 뽑아낸다면 **group by** 필요
* count 쓴 걸 where 이나 order by 쓸 땐 다른 이름으로 정해주는 게 나음 

## 3번 문제 : type 2 상관 없이 type 1의 포켓몬 수를 알 수 있는 쿼리 작성 
```
SELECT
  type1,
  COUNT(id)
FROM basic.pokemon
GROUP BY type1
```
* 상관 없이 == 말 그대로 상관 없이! 추가적인 조건 X
* DISTINCT 는 value_counts() 야! 중복 없이 보고 싶을 때 ~

## 4번 문제 : 전설 여부 (유니크한 값) 에 따른 포켓몬 수를 알 수 있는 쿼리 작성
```
SELECT
  is_legendary,
  COUNT(id)
FROM basic.pokemon
GROUP BY is_legendary
```
* GROUP BY 1 -> SELECT 의 첫 컬럼을 의미
* order by 1 or 2 도 됨

## 5번 문제 : 동명 이인이 있는 이름은 무엇일까요?
```
SELECT
  name,
  COUNT(name) as cnt
FROM basic.trainer
GROUP BY 1
HAVING cnt >= 2
```
```
SELECT
*
FROM(
  SELECT
    name,
    COUNT(name) as cnt
  FROM basic.trainer
  GROUP BY 1
)
WHERE cnt >= 2
```
* GROUP BY 후에 (집계 후에) 조건을 걸고 싶다면, where 이 아니라 having 을 써야 함!!
* 2번처럼 서브쿼리로도 가능 
## 6번 문제 : trainer 테이블에서 IRIS 트레이너의 정보를 알 수 있는 쿼리 작성
```
SELECT
  *
FROM basic.trainer
WHERE name = "Iris"
```
## 7번 문제 : trainer 테이블에서 iris, whitney, cynthia 트레이너의 정보를 알 수 있는 쿼리를 작성
```
SELECT
  *
FROM basic. trainer
WHERE (name = "Iris")
  OR (name = 'Whitney')
  OR (name = 'Cynthia')
```
```
SELECT
  *
FROM basic. trainer
WHERE name IN ('Iris','Whitney','Cynthia')
```
* 여러 개가 있는지 확인 할 땐 `IN` 사용
## 8번 문제 : 전체 포켓몬의 수는?
```
SELECT
  COUNT(id)
FROM basic.pokemon
``` 
## 9번 문제 : 세대 별로 포켓몬 수가 얼마나 되는지 알 수 있는 쿼리 작성 
```
SELECT
  generation,
  COUNT(id)
FROM basic.pokemon
GROUP BY generation
```
## 10번 문제 : type2가 존재하는 포켓몬의 수는? 
```
SELECT
  COUNT(id)
FROM basic.pokemon
WHERE type2 IS NOT NULL
``` 
* **"특정 칼럼" 의 포켓몬 수를 계산하라고 한 것이 X -> 그냥 전체 기준으로 (집계 안 하고) 포켓몬 수 세면 됨**
## 11번 : type2 가 있는 포켓몬 중에 가장 많은 type1은 무엇인가요?
```
SELECT
  type1,
  COUNT(id)
FROM basic.pokemon as cnt
WHERE type2 IS NOT NULL
GROUP BY type1 
ORDER BY cnt DESC 
```
```
SELECT
  type1,
  COUNT(id)
FROM basic.pokemon as cnt
WHERE type2 IS NOT NULL
GROUP BY type1 
ORDER BY cnt DESC 
LIMIT 1
```
* LIMIT 1 : 가장 위에 하나만 ~
## 12번 : 단일 타입 포켓몬 중 많은 type1은 무엇인가요?
```
SELECT
  type1,
  COUNT(id)
FROM basic.pokemon as cnt
WHERE type2 IS NULL
GROUP BY type1 
ORDER BY cnt DESC 
LIMIT 1
```
## 13번 : 포켓몬의 이름에 "파"가 들어가는 포켓몬?
```
SELECT
  kor_name
FROM basic.pokemon
WHERE kor_name LIKE "%파%"
```
* LIKE : 특정단어가 포함되는 칼럼을 가져오는 단어 (문자열에서!)
  * "%파" : 파로 끝나는 단어
  * "파%" : 파로 시작하는 단어 
  * "%파"%" : 파가 들어가는 단어
## 14번 : 뱃지가 6개 이상인 트레이너는 몇 명?
```
SELECT 
  COUNT(id)
FROM basic.trainer
WHERE badge_count >= 6
```
## 15번 : 트레이너가 보유한 포켓몬이 제일 많은 트레이너는?
```
SELECT
  trainer_id,
  COUNT(pokemon_id) as cnt
FROM baisc.trainer_pokemon
GROUP BY trainer_id
ORDER BY cnt DESC
```
## 16번 : 포켓몬을 많이 풀어준 트레이너는?
```
SELECT
  trainer_id,
  COUNT(pokemon_id) as cnt
FROM basic.trainer_pokemon
WHERE status = 'Released'
GROUP BY trainer_id
ORDER BY cnt DESC
```
* 포켓몬을 가지고 있는 것 중에, 풀어준 거니까 (구하는 최종 값은 포켓몬 수, 조건 설정)
## 17번 : 트레이너 별로 풀어준 포켓몬의 비율이 20%가 넘는 포켓몬 트레이너는 누구일까요? 
```
SELECT
  trainer_id,
  COUNT(status = 'Released') as cnt,
  COUNT(pokemon_id) as pkm,
  COUNTIF(status = 'Released')/COUNT(pokemon_id) as rrate
FROM basic.trainer_pokemon
GROUP BY trainer_id
HAVING rrate >= 0.2
```
* COUNTIF(칼럼 = 3) : 칼럼 중 행이 3인 행의 count를 구함 
* COUNT 는 여러 개 쓸 수 있음 (컴마로 이어주기만 하면 됨) 
* AS 로 쓴 건 밑에 WHERE 절에서 쓰는 거임 

### WHERE 써야 할지, HAVING 써야 할지 헷갈리면 알고리즘을 생각해 보자! (그 조건이 집계 후에 와야 하는지, 집계 전에 와야 하는지)
### 이제 GROUP BY ALL 쓰면 뒤에 칼럼 이름 안 써도 돼 ~~

## 총 정리
![사진](/images/스크린샷%202025-04-01%20012035.png)
## 쿼리를 작성하는 흐름 
1. 지표 고민 (어떤 문제를 해결하기 위해 이 데이터가 필요한가?) -> 문제 정의 
2. 지표 구체화 (추상적이지 않고 구체적인 지표 명시) -> 분모, 분자 제대로 확인 / 이름 제대로 표시 (어떤 컬럼은 어떤 VALUE)
3. 지표 탐색 (유사한 문제 해결한 케이스 확인) -> 있다면 해당 쿼리 리뷰 / 없으면 쿼리 작성
4. 쿼리 작성 (테이블 찾기) -> 2개라면 JOIN 고민 
5. 데이터 정합성 확인 (예상한 결과와 동일한지 확인) -> 내가 원하는대로 데이터를 뽑아냈는지!
6. 쿼리 가독성 (확인하기 쉽게 작성해야 함) 
7. 쿼리 저장 (쿼리는 재사용되니까... 문서로 작성) 