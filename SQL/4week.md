# 수강 사진
![사진](/images/스크린샷%202025-05-06%20225032.png)

# 4-4. 날짜 및 시간 데이터 이해하기 (2)
* `CURRENT_DATETIME([time_zone])` : 현재 datetime 출력  
    * CURRENT_DATE() → 2025-05-06 (UTC)
    * CURRENT_DATE("Asia/Seoul") → 2025-05-07 (한국 시간이 time zone (기준), 한국은 UTC+9)
    * CURRENT_DATETIME() → 2025-05-06 15:03:22 (UTC)
    * CURRENT_DATETIME("Asia/Seoul") → 2025-05-07 00:03:22 (서울 시간 기준) 
* `EXTRACT(part FROM datetime_expression)` : DATETIME 에서 특정 부분만 추출하고 싶은 경우 (e.g. 월별 주문)
    * 예시 코드  
        ![사진](/images/스크린샷%202025-05-06%20185946.png)  
    * 요일 추출하는 경우 : `EXTRACT(DAYOFWEEK FROM datetime_col) -> 한 주의 첫날이 일요일인 [1,7] 범위의 값을 변환 (e.g. 일요일은 - 1, 월요일은 - 2) 
    * DATE 와 HOUR 만 남기고 싶은 경우 (나머지는 0으로 채워짐) : `DATETIME_TRUNC(datetime_col, HOUR)`  
        ![사진](/images/스크린샷%202025-05-06%20185810.png)
* `PARSE_DATETIME` : 문자열로 저장된 DATETIME 을 DATETIME 타입으로 바꾸고 싶은 경우  
    ![사진](/images/스크린샷%202025-05-06%20190048.png)
* `FORMAT_DATETIME` : DATETIME 타입 데이터를 특정 형태의 문자열 데이터로 변환  
    ![사진](/images/스크린샷%202025-05-06%20190148.png)
* `LAST_DAY` : 마지막 날을 알고 싶은 경우, 자동으로 월의 마지막 값을 계산해서 특정 연산을 할 경우  
    ![사진](/images/스크린샷%202025-05-06%20190403.png)
* `DATETIME_DIFF` : 두 DATETIME의 차이를 알고 싶은 경우  
    ![사진](/images/스크린샷%202025-05-06%20203421.png)


# 4-5. 시간 데이터 연습문

## 1. 트레이너가 포켓몬을 포획할 날짜(catch_date)를 기준으로 2023년 1월에 포획한 포켓몬의 수를 계산
* catch_datetime 이라고 되어 있지만 utc 가 있기에 time stamp 로 보는 것이 맞음 
* date 도 utc 기준인지, kr 기준인지 확인해 봐야 함 
```
SELECT
    id, 
    catch_date,
    DATE(DATETIME(catch_datetime, "Asia/Seoul")) AS catch_datetime_kr_date
FROM basic.trainer_pokemon
WHERE 
```
* 확인하는 방법
```
SELECT
    COUNT(DISTINCT id) AS cnt
FROM basic.trainer_pokemon
WHERE 
    EXTRACT(YEAR FROM DATETIME(catch_datetime, "Asia/Seoul")) = 2023 
    AND EXTRACT(MONTH FROM DATETIME(catch_datetime, "Asia/Seoul")) = 1
```

## 2. 배틀이 일어난 시간(battle_datetime)을 기준으로, 오전 6시에서 오후6시 사이에 일어난 배틀의 수를 계산해주세요.
```
SELECT
    id,
    battle_datetime, 
    DATETIME(battle_timestamp,"Asia/Seoul") AS battle_timestamp_kr
FROM basic.battle
```
```
SELECT
    COUNTIF(battle_datetime = DATETIME(battle_timestamp,"Asia/Seoul")) AS SAME 
FROM basic.battle
```
* 데이터 확인 
```
SELECT
    COUNT(DISTINCT id)
FROM basic.battle
WHERE
    EXTRACT(HOUR FROM battle_datetime) >= 6
    AND EXTRACT(HOUR FROM battle_datetime) <= 18 
```
```
SELECT
    COUNT(DISTINCT id)
FROM basic.battle
WHERE
    EXTRACT(HOUR FROM battle_datetime) BETWEEN 6 and 18
```
* 시간의 경우 숫자형이기 때문에 between 사용 가능 
```
SELECT
    *,
    EXTRACT(HOUR FROM battle_datetime)
FROM basic.battle
```

## 3. 각 트레이너별로 그들이 포켓몬을 포획한 첫 날(catch_date)을 찾고, 그 날짜를 ‘DD/MM/YYYY’ 형식으로 출력해주세요. (2024-01-01 ⇒ 01/01/2024)
```
SELECT
    trainer_id,
    FORMAT_DATE("%d/%m/%Y", min_date) AS new_min
FROM (
    SELECT
        trainer_id,
        MIN(DATE(catch_datetime, "Asia/Seoul")) AS min_date
    FROM basic.trainer_pokemon
    GROUP BY
        trainer_id
)   
ORDER BY
        trainer_id      
```
* 데이터도 숫자가 작을 수록 min 
* order by 는 맨 마지막에 진행 
## 4. 배틀이 일어난 날짜(battle_date)를 기준으로 요일별로 배틀이 얼마나 자주 일어났는지 계산해주세요.
```
SELECT
    day_of_week,
    count(DISTINCT id) AS battle_cnt
FROM(
    SELECT
        *,
        EXTRACT(DAYOFWEEK FROM battle_date) AS day_of_week
    FROM basic.battle
)
GROUP BY
    day_of_week
```
## 5. 트레이너가 포켓몬을 처음으로 포획한 날짜와 마지막으로 포획한 날짜의 간격이 큰 순으로 정렬하는 쿼리를 작성해주세요.
```
SELECT
    *,
    DATETIME_DIFF(max_date, min_date, DAY) AS diff
DATETIME_DIFF()
FROM(
    SELECT
        trainer_id,
        MIN(DATETIME(catch_datetime,"Asia/Seoul")) AS min_date,
        MAX(DATETIME(catch_datetime,"Asia/Seoul")) AS max_date
    FROM basic.battle
    GROUP BY
        trainer_id
)
ORDER BY
    diff DESC
```
# 4-6. 조건문

* `CASE WHEN`  
    * 작성 방법  
        ```
        SELECT
            CASE
                WHEN 조건 1 THEN 조건1이 참일 경우 결과
                WHEN 조건 2 THEN 조건2가 참일 경우 결과
            ELSE 그 외 조건일 경우 결과
        END AS 새로운 칼럼 이름 
        ```
    * 예시 문제  
        ![사진](/images/스크린샷%202025-05-06%20220430.png)  
    * 두 when 에 다 겹치면, 앞선 순서를 따른다는 것을 명심! 
* `IF` : 단일 조건일 때
    * 작성 방법  
        ```
        IF(조건문, true 일 때 값, FALSE 일 때 값) AS 새로운 칼럼 이름 
        ```

# 4-7. 조건문 연습 문제

## 1. 포켓몬의 ‘Speed’가 70이상이면 ‘빠름’, 그렇지 않으면 ‘느림’으로 표시하는 새로운 칼럼 ‘Speed_Category’를 만들어주세요.
```
SELECT
    id,
    kor_name,
    speed,
    IF(speed >= 70, "빠름", "느림") AS Speed_Category
FROM basic.pokemon
```
## 2. 포켓몬의 type1에 따라 water, fire, electric 타입은 각각 물, 불, 전기로 그 외 타입은 기타로 분류하는 새로운 컬럼 type_korean을 만들어 주세요.
```
SELECT
    id,
    kor_name,
    type1,
    CASE
        WHEN type1 = 'Water' THEN '물'
        WHEN type1 = 'Fire' THEN '불'
        WHEN type1 = 'Electric' THEN '전기'
    ELSE "기타"
    END AS type_korean
FROM basic.pokemon
```
## 3. 각 포켓몬의 총점(total)을 기준으로, 300 이하면 ‘low’, 301에서 500 사이면 ‘medium’, 501이상이면 ‘high’로 분류해주세요.
```
SELECT 
    *
FROM(
SELECT
    id,
    kor_name,
    total,
    CASE
        WHEN total <= 300 THEN 'low'
        WHEN total BETWEEN 300 AND 500 THEN 'medium'
    ELSE "high"
    END AS total_pokemon
FROM basic.pokemon
)
WHERE 
    total_pokemon = 'low'
```
* 사이에 있다면 BETWEEN 사용 ~ 
* total_pokemon 칼럼을 쓰고 싶다면, 서브쿼리 해서 그 칼럼이 실행한 다음 가져와야 됨 
## 4. 각 트레이너의 배지 개수를 기준으로 5개 이하면 beginner, 6개에서 8개 사이면 Intermediate, 그 이상이면 advanced로 분류해주세요.
```
SELECT
    id,
    name,
    badge_count,
    CASE
        WHEN badge_count <= 5 THEN 'beginner'
        WHEN badge_count BETWEEN 6 and 8 THEN 'Intermediate'
    ELSE 'advanced'
    END AS badge_level 
FROM basic.trainer 
```
## 5. 트레이너가 포켓몬을 포획한 날짜(catch_date)가 ‘2023-01-01’ 이후이면 recent, 그렇지 않으면 old로 분류해주세요.
```
SELECT
    id,
    trainer_id,
    pokemon_id,
    catch_datetime,
    IF(DATE(catch_dateimte, "Asia/Seoul") >= "2023-01-01", "recent", "old") AS recent 
FROM basic.trainer_pokemon
```
```
SELECT
    id,
    trainer_id,
    pokemon_id,
    catch_datetime,
    IF(DATE(catch_dateimte, "Asia/Seoul") >= "2023-01-01", "recent", "old") AS recent,
    "recent" AS recent_all
FROM basic.trainer_pokemon
```
* 모든 칼럼에 동일한 값을 추가하고 싶다면!
## 6. 배틀에서 승자(winner_id)가 player1_id와 같으면 player 1 wins, player2_id와 같으면 player2wins, 그렇지 않으면 draw로 결과가 나오게 해주세요.
```
SELECT
    id, 
    winner_id,
    player1_id,
    player2_id,
    CASE
        WHEN winner_id = player1_id THEN "player 1 wins"
        WHEN winner_id = player2_id THEN "player 2 wins"
    ELSE "draw"
    END AS battle_result 
FROM basic.battle 
``` 
# 4-8. 정리
**데이터 타입 변환, 조건문은 다 SELECT 문에서 이루어짐!** 

# 4-9. 빅쿼리 공식 문서 확인 (필요할 때 찾아보려고) 
* 기술을 어떻게 사용하는지에 대한 문서
* “기술명” + documentation 으로 검색
* google sql == big query
* 어떻게 쓰는지 모를 때, [bigquery 특정 행위] 검색
    * i want to change string to int in bigquery
    * stackoverflow 에서 찾아봥 
* 가장 최근 문서 찾아서 확인해라 ~ 
* slack Rss Feed : 새로운 소식 나오면 알려줌 ~!~!!! 