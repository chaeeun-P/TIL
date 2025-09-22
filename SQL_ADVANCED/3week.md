# SQL_ADVANCED 3주차 정규 과제 

## Week 3: 윈도우 함수 (Window Functions)

📌**SQL_ADVANCED 정규과제**는 매주 정해진 주제에 따라 **MySQL 공식 문서 또는 한글 블로그 자료를 참고해 개념을 정리한 후, 이번 주차에는 LeetCode SQL 문제 3문제**와 **추가 확인문제**를 직접 풀어보며 학습하는 과제입니다. 

이번 주는 아래의 **SQL_ADVANCED_3rd_TIL**에 나열된 주제를 중심으로 개념을 학습하고, 주차별 **학습 목표**에 맞게 정리해주세요. 정리한 내용은 GitHub에 업로드한 후, **스프레드시트의 'SQL' 시트에 링크를 제출**해주세요. 



**(수행 인증샷은 필수입니다.)** 

> Leet code의 문제를 풀고 '정답입니다' 문구를 캡쳐해서 올려주시면 됩니다. 



## SQL_ADVANCED_3rd

### 14.20.2 Window Function Concepts and Syntax

### 14.20.1 Window Function Description

### 14.19.1 Aggregate Function Descriptions

- 위 문서 중 *14.19.1. Aggregate Function Descriptions* 문서에서 1주차 (집계 함수) 에서 다룬 부분을 제외하고 **OVER( ) 절을 활용한 윈도우 함수 문법과 `RANK( ), DENSE_RANK( ), ROW_NUMBER( ), LAG( ), LEAD( )`등 윈도우 함수 특유의 기능 중심으로 정리해주세요.**



## 🏁 강의 수강 (Study Schedule)

| 주차  | 공부 범위               | 완료 여부 |
| ----- | ----------------------- | --------- |
| 1주차 | 서브쿼리 & CTE          | ✅         |
| 2주차 | 집합 연산자 & 그룹 함수 | ✅         |
| 3주차 | 윈도우 함수             | ✅         |
| 4주차 | Top N 쿼리              | 🍽️         |
| 5주차 | 계층형 질의와 셀프 조인 | 🍽️         |
| 6주차 | PIVOT / UNPIVOT         | 🍽️         |
| 7주차 | 정규 표현식             | 🍽️         |



### 공식 문서 활용 팁

>  **MySQL 공식 문서는 영어로 제공되지만, 크롬 브라우저에서 공식 문서를 열고 이 페이지 번역하기에서 한국어를 선택하면 번역된 버전으로 확인할 수 있습니다. 다만, 번역본은 문맥이 어색한 부분이 종종 있으니 영어 원문과 한국어 번역본을 왔다 갔다 하며 확인하거나, 교육팀장의 정리 예시를 참고하셔도 괜찮습니다.**



# 1️⃣ 학습 내용

> 아래의 링크를 통해 *MySQL 공식문서*로 이동하실 수 있습니다.
>
> - 14.20.2 Window Function Concepts and Syntax : MySQL 공식문서
>
> https://dev.mysql.com/doc/refman/8.0/en/window-functions-usage.html
>
> (한국어 버전) https://dart-b-official.github.io/posts/mysql-Window-Function/
>
> - 14.20.1 Window Function Description : MySQL 공식문서
>
> https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html
>
> (한국어 버전) https://dart-b-official.github.io/posts/mysql-Window-Function(2)/
>
> - 14.19.1 Aggregate Function Descriptions : MySQL 공식문서
>
> https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html
>
> (한국어 버전) https://dart-b-official.github.io/posts/mysql-aggregate_function/
>

<br>



---

# 2️⃣ 학습 내용 정리하기

## 1. 윈도우 함수

~~~
✅ 학습 목표 :
* OVER 절을 통해 행 단위 분석을 가능하게 하는 윈도우 함수의 구조를 이해한다.
* RANK, DENSE_RANK, ROW_NUMBER의 차이를 구분하고 사용할 수 있다.
* 이전 또는 이후 행을 참조하는 LAG, LEAD 함수를 적절히 사용할 수 있다.
~~~

## SQL 윈도우 함수: 기본 개념 및 활용

### 윈도우 함수란?

**윈도우 함수**는 특정 행 집합인 **'윈도우(Window)'** 내에서 계산을 수행하고, 각 행마다 그 결과를 반환함. 일반적인 집계 함수가 여러 행을 하나의 결과로 요약하는 것과 달리, 윈도우 함수는 **원본 행의 개수를 유지하면서** 추가적인 정보를 계산함.

  * **일반 집계 함수**: `GROUP BY`를 사용해 행을 요약함 (예: 전체 수익의 합계).
      * `SELECT SUM(profit) FROM sales;` → **1개 행** 반환
  * **윈도우 함수**: `OVER()` 절을 사용해 원본 행을 유지함 (예: 각 행에 전체 수익을 추가).
      * `SELECT profit, SUM(profit) OVER() FROM sales;` → **여러 행** 반환

### 주요 개념

  * **현재 행 (Current Row)**: 함수 계산의 기준이 되는 행임.
  * **윈도우 (Window)**: 현재 행과 관련된 행들의 집합임.
  * **`OVER()` 절**: 윈도우 함수를 정의하는 핵심 구문임. 괄호 안에 윈도우의 범위를 지정함.
      * `OVER()`: 전체 행을 하나의 윈도우로 간주함.
      * `OVER(PARTITION BY country)`: `country`별로 행을 그룹화하여 각 그룹(파티션) 내에서 계산함.

### 실행 순서

SQL 쿼리 실행 시, 윈도우 함수는 `GROUP BY`와 `HAVING` 절 **이후**, `ORDER BY` 절 **이전**에 실행됨.

`FROM` → `WHERE` → `GROUP BY` → `HAVING` → **`WINDOW FUNCTION`** → `ORDER BY` → `LIMIT`

-----

### 윈도우 함수로 사용 가능한 함수들

윈도우 함수는 크게 두 가지로 나눌 수 있음.

#### 1\. 집계 함수 (Aggregate Functions)

`OVER` 절이 추가되면 일반 집계 함수가 윈도우 함수로 동작함.

  * `SUM()`: 합계
  * `AVG()`: 평균
  * `COUNT()`: 개수
  * `MAX()`, `MIN()`: 최댓값, 최솟값

#### 2\. 비집계 전용 윈도우 함수 (Non-Aggregate Functions)

`OVER()` 절이 반드시 필요한 함수들임. 주로 **순위, 행 번호, 이동 평균** 등에 사용됨.

| 함수 | 설명 |
| :--- | :--- |
| **`ROW_NUMBER()`** | 파티션 내 고유한 일련번호를 부여함. 동점 행에도 다른 번호를 부여함. |
| **`RANK()`** | 순위를 매기되, 동점일 경우 같은 순위를 부여하고 다음 순위는 건너뜀 (예: 1, 2, 2, 4). |
| **`DENSE_RANK()`** | 순위를 매기되, 동점일 경우 같은 순위를 부여하고 다음 순위를 건너뛰지 않음 (예: 1, 2, 2, 3). |
| **`CUME_DIST()`** | 누적 분포 값 (현재 행 이하의 값 비율)을 반환함. 0에서 1 사이의 값임. |
| **`NTILE(N)`** | 전체 행을 N개의 그룹으로 나눈 후, 각 행에 그룹 번호(1\~N)를 부여함. |
| **`LAG()`** | 현재 행을 기준으로 N행 **이전**의 값을 가져옴. |
| **`LEAD()`** | 현재 행을 기준으로 N행 **이후**의 값을 가져옴. |
| **`FIRST_VALUE()`** | 프레임 내 첫 번째 행의 값을 반환함. |
| **`LAST_VALUE()`** | 프레임 내 마지막 행의 값을 반환함. |

-----

### `OVER` 절의 구성

`OVER` 절을 사용하면 윈도우의 범위를 세밀하게 조정할 수 있음.

**`OVER (PARTITION BY ... ORDER BY ... ROWS BETWEEN ... AND ...)`**

  * **`PARTITION BY`**: 윈도우 함수를 적용할 그룹을 지정함 (예: 국가별, 연도별).
  * **`ORDER BY`**: 파티션 내에서 행의 순서를 정함 (`RANK`, `ROW_NUMBER` 등의 순위 함수에 필수적임).
  * **`ROWS/RANGE BETWEEN ... AND ...`**: \*\*프레임(Frame)\*\*을 정의함. 현재 행을 기준으로 윈도우에 포함될 행의 범위를 설정함.
      * `ROWS UNBOUNDED PRECEDING`: 파티션의 첫 행부터 현재 행까지.
      * `ROWS 1 PRECEDING AND 1 FOLLOWING`: 현재 행을 기준으로 이전 행 1개와 이후 행 1개.

---

# 3️⃣ 실습 문제

## LeetCode 문제 

https://leetcode.com/problems/department-top-three-salaries/

> LeetCode 185. Department Top Three Salaries 
>
> 학습 포인트 : DENSE_RANK( ) + PARTITION BY 사용으로 그룹 내 상위 N개 추출

https://leetcode.com/problems/consecutive-numbers/

> LeetCode 180. Consecutive Numbers 
>
> 학습 포인트 : LAG( ) 함수로 이전 값과 비교하여 연속 데이터 탐지 

https://leetcode.com/problems/last-person-to-fit-in-the-bus/

> LeetCode 2481. Last Person to Fit in the Bus 
>
> 학습 포인트 : SUM( ) OVER (ORDER BY ...) 로 누적 합계 계산 후 조건 필터링 



문제를 푸는 다양한 방법이 존재하지만, **윈도우 함수를 사용하여 해결하는 방식에 대해 고민해주시길 바랍니다.** 

---

## 문제 인증란

![사진](/images/스크린샷%202025-09-22%20210934.png)
![사진](/images/스크린샷%202025-09-22%20211115.png)
![사진](/images/스크린샷%202025-09-22%20211221.png)

---

# 확인문제

## 문제 1

> **🧚예린이는 고객별로 얼마나 많은 주문을 하는지 분석하기 위해, 고객의 주문 목록에 주문 순서를 표시하는 쿼리를 작성해보았습니다. 이때 주문일 순서대로 각 고객의 주문 번호를 매기기 위해 윈도우 함수를 활용했습니다.**

~~~sql
SELECT customer_id, order_id, order_date,
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS order_rank
FROM Orders;
~~~

> **이번에는 예린이에게 "윈도우 함수를 쓰지 않고 동일한 결과를 만들어보라"는 미션을 받았습니다. 예린이는 이 작업을 어떻게 해야할지 막막합니다. 예린이를 도와 ROW_NUMBER() 윈도우 함수 없이 동일한 결과를 서브쿼리나 JOIN을 사용해서 작성해보세요.**

~~~
```
SELECT
    o1.customer_id,
    o1.order_id,
    o1.order_date,
    (SELECT COUNT(*)
     FROM Orders o2
     WHERE o2.customer_id = o1.customer_id AND o2.order_date <= o1.order_date) AS order_rank
FROM
    Orders o1
ORDER BY
    o1.customer_id, o1.order_date;
```
~~~



<br>

### 🎉 수고하셨습니다.