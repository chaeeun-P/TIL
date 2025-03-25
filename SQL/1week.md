## 수강사진
![사진](/images/스크린샷%202025-03-25%20014655.png)
---

### select

**SELECT** col1 **as** new_name  
**FROM** 데이터셋  
**WHERE** 조건  

* as : select 문 내에서 칼럼 이름 따로 설정 (따옴표X)
* * : 전체 행을 불러오는 건데, 보통 잘 X
* * EXCEPT A : 전체에서 어떤 칼럼 제외하고
* -- : 주석 
* ; : 끝냈다 ~  

### select 연습문제
#### 1번
```
SELECT  
  *
FROM basic.trainer
```
#### 2번
```
SELECT  
  name
FROM `basic.trainer`
```
#### 3번
```
SELECT  
  name, age
FROM `basic.trainer`
```
#### 4번
```
SELECT
  name, age, hometown
FROM basic.trainer
WHERE id = 3
```
#### 5번
```
SELECT
  hp, attack
FROM basic.trainer
WHERE kor_name = "피카츄"
```
### 요약 (집계, 그룹화, 정렬) 
```
SELECT
    집계함수 (COUNT, MAX, MIN)
FROME table
GROUP BY 집계할 때 사용하는 칼럼
```
![사진](/images/)
* 특정 조건 해당 row count

```
SELECT
    집계할 때 사용하는 칼럼 (그냥 한 번 더 씀),
    COUNT(DISTINCT 칼럼)
FROME table
GROUP BY 집계할 때 사용하는 칼럼 
```
**, 꼭 붙여주기!!!!!!!!!**
**GROUPBY 로 집계할 칼럼을 무조건 SELECT 문에 작성해 주어야 함**
```
SELECT
    DISTINCT 칼럼
FROME table
GROUP BY 
HAVING
```

* DISTINCT : 고유값을 알고 싶은 경우 (value_counts)
* groupby 후에는 where 말고 having 써야 함~ 
    * 정 where 쓰고 싶으면 서브쿼리로 groupby 끝난 다음 써야 함! (근데 이렇게 하는 게 그냥 having이랑 똑같다... 걍 having ㄱ) groupby 나온 이후에 조건 쓰려면 무조건 having
* 서브쿼리 : select 문 안에 select

```
SELECT
    col
FROM
LIMIT 10
ORDER BY 칼럼순서
```
* 순서 : DESC(내림차순), OSC(오름차순 - default)
* 보통 order by 를 가장 맨 마지막에 씀
* LIMIT : 쿼리문 결과의 행 수 제한 

### 요약 연습 문제
#### 1번
```
SELECT  
  count(id)
FROM basic.pokemon
```
#### 2번
```
SELECT
  generation,
  COUNT(id)
FROM basic.pokemon
GROUP BY generation
```
#### 3번
```
SELECT
  type1
  count(id)
FROM basic.pokemon
GROUP BY type1
HAVING type 1 > 10
ORDER BY type1 DESC
```
