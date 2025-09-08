# SQL_ADVANCED 1주차 정규 과제 

## Week 1 : 서브쿼리 & CTE

📌**SQL_ADVANCED 정규과제**는 매주 정해진 주제에 따라 **MySQL 공식 문서 또는 한글 블로그 자료를 참고해 개념을 정리한 후, 프로그래머스 SQL 3문제**와 **추가 확인문제**를 직접 풀어보며 학습하는 과제입니다. 

이번 주는 아래의 **SQL_ADVANCED_0th_TIL**에 나열된 주제를 중심으로 개념을 학습하고, 주차별 **학습 목표**에 맞게 정리해주세요. 정리한 내용은 GitHub에 업로드한 후, **스프레드시트의 'SQL' 시트에 링크를 제출**해주세요. 



**👀 (수행 인증샷은 필수입니다.)** 

> 프로그래머스 문제를 풀고 '정답입니다' 문구를 캡쳐해서 올려주시면 됩니다. 



## SQL_ADVANCED_1st_TIL 

### 15.2.15. SubQueries

#### 특히 15.2.15.1 ~ 15.2.15.7 (Scalar, EXISTS, Correlated, Derived 등) 

### 15.2.20 WITH (Common Table Expressions)

- `WITH RECURSIVE`에 대한 내용은 추후에 공부합니다. 해당 링크에서 `WITH`에 해당하는 부분만 정리해보세요. 




## 🏁 주차별 학습 (Study Schedule)

| 주차  | 공부 범위               | 완료 여부 |
| ----- | ----------------------- | --------- |
| 1주차 | 서브쿼리 & CTE          | ✅         |
| 2주차 | 집합 연산자 & 그룹 함수 | 🍽️         |
| 3주차 | 윈도우 함수             | 🍽️         |
| 4주차 | Top N 쿼리              | 🍽️         |
| 5주차 | 계층형 질의와 셀프 조인 | 🍽️         |
| 6주차 | PIVOT / UNPIVOT         | 🍽️         |
| 7주차 | 정규 표현식             | 🍽️         |

<br>


### 공식 문서 활용 팁

>  **MySQL 공식 문서는 영어로 제공되지만, 크롬 브라우저에서 공식 문서를 열고 이 페이지 번역하기에서 한국어를 선택하면 번역된 버전으로 확인할 수 있습니다. 다만, 번역본은 문맥이 어색한 부분이 종종 있으니 영어 원문과 한국어 번역본을 왔다 갔다 하며 확인하거나, 교육팀장의 정리 예시를 참고하셔도 괜찮습니다.**



# 1️⃣ 학습 내용 

> 아래의 링크를 통해 *MySQL 공식문서*로 이동하실 수 있습니다.
>
> - SubQueries : MySQL 공식문서 
>
> https://dev.mysql.com/doc/refman/8.0/en/subqueries.html
>
> (한국어 버전)
> https://dart-b-official.github.io/posts/mysql-subqueries/


> - CTE(공통 테이블 표현식) : MySQL 공식문서
>
> https://dev.mysql.com/doc/refman/8.0/en/with.html
>
> (한국어 버전)
> https://dart-b-official.github.io/posts/mysql-cte/

<br>
<br>
<!-- 여기까진 그대로 둬 주세요-->





# 2️⃣ 학습 내용 정리하기

---

 # 1. 서브쿼리

~~~
✅ 학습 목표 :
* SubQueries에 대한 문법을 이해하고 활용할 수 있다.  
~~~

## SQL 서브쿼리(Subquery) 정리

* 서브쿼리는 하나의 SQL문 안에 포함된 또 다른 SELECT 문을 의미
* SQL 표준에서 정의하는 대부분의 기능을 지원하며, MySQL 고유의 기능도 포함

```
SELECT * FROM t1 WHERE column1 = (
  SELECT column1 FROM t2);
```

* SELECT * FROM t1 ...은 **외부 쿼리(outer query)**, (SELECT column1 FROM t2)는 서브쿼리

### 서브쿼리의 주요 특징

* 구조적 분리: 쿼리를 구조적으로 나누어 각 부분을 쉽게 이해할 수 있게 함
* 유연성: 복잡한 JOIN이나 UNION을 대체할 수 있으며, 많은 사용자들이 복잡한 조인보다 서브쿼리가 더 읽기 쉽다고 느낌 
* 중첩: 서브쿼리는 외부 쿼리 안에 중첩될 수 있으며, 서브쿼리 안에 또 다른 서브쿼리를 넣는 것도 가능
* 괄호 필수: 모든 서브쿼리는 반드시 괄호로 감싸야 함
* 서브쿼리 결과 형태: 서브쿼리의 결과는 반환하는 값의 개수에 따라 다음과 같이 구분
    * Scalar: 단일 값(single value)을 반환 
    * Column: 단일 컬럼(single column)을 반환합니다. 여러 개의 행을 포함
    * Row: 단일 행(single row)을 반환하며, 여러 개의 컬럼을 포함할 수 있음
    * Table: 여러 개의 행과 컬럼을 반환 
* 서브쿼리에서 허용되는 요소: 서브쿼리는 일반적인 SELECT 문에 사용되는 대부분의 요소를 포함할 수 있음 
    * DISTINCT, GROUP BY, ORDER BY, LIMIT 
    * JOIN, 인덱스 힌트, UNION 
    * 함수, 주석 등 

----

1. 스칼라 서브쿼리 (Scalar Subquery)
* 가장 단순한 형태의 서브쿼리로, 단일 값을 반환
* 스칼라 서브쿼리는 단일 컬럼 값이나 리터럴이 허용되는 거의 모든 곳에서 사용 가능

```
SELECT (SELECT s2 FROM t1);
```
* 위 예시에서 서브쿼리는 t1 테이블의 s2 컬럼에서 단일 값을 반환
* 서브쿼리 결과의 NULL 가능성은 원본 컬럼의 NOT NULL 제약조건과 무관
    * e.g. 예를 들어, t1 테이블이 비어 있다면 s2가 NOT NULL이더라도 결과는 NULL
* 사용 제한
    * LIMIT나 LOAD DATA와 같이 리터럴 값만 허용하는 구문에는 스칼라 서브쿼리를 사용할 수 X

2. 서브쿼리를 이용한 비교 연산
* 서브쿼리는 비교 연산자의 오른쪽 피연산자로 가장 흔하게 사용

```
non_subquery_operand comparison_operator (subquery) 
```

* 비교 연산자
    * `=`,`>`, `<`, `>=`, `<=`, `<>`, `!=`, `<=>` 
    * MySQL은 또한 LIKE (subquery)와 같은 구문도 허용
* 중요 사항
    * 스칼라 값과 비교하려면, 서브쿼리는 반드시 단일 값을 반환
    * Row Constructor와 비교하려면, 서브쿼리는 Row 서브쿼리여야 하고, 반환하는 값의 개수가 Row Constructor와 동일해야 함

3. ANY, IN, SOME 서브쿼리

* 이 키워드들은 비교 연산자 뒤에 오며, 서브쿼리에서 반환된 값들과 조건을 비교

    * ANY: 서브쿼리에서 반환된 값 중 하나라도 조건을 만족하면 TRUE를 반환합니다. 
    * IN: = ANY의 별칭입니다. 두 구문은 동일한 결과를 반환합니다. 하지만 IN은 표현식 리스트를 받을 수 있는 반면, = ANY는 서브쿼리만 사용할 수 있다는 차이점이 있습니다. 
    * SOME: ANY의 또 다른 별칭입니다. 혼동을 줄이기 위해 NOT IN이나 NOT ALL 대신 사용하면 의미를 더 명확히 전달할 수 있습니다. 

4. ALL 서브쿼리

* ALL 키워드는 비교 연산자 뒤에 오며, 서브쿼리에서 반환된 모든 값에 대해 비교 결과가 TRUE일 때 TRUE를 반환합니다. 

* 빈 테이블과 NULL 값 처리: `> ALL`과 같은 조건에서 서브쿼리가 빈 테이블을 반환하면 TRUE가 됩니다. 
* 서브쿼리 결과에 NULL이 포함되면 전체 결과가 NULL이 됩니다. NOT IN은 `<> ALL`의 별칭입니다. 

5. 행 서브쿼리 (Row Subquery)

* ROW 서브쿼리는 하나의 행을 반환하며, 이 행은 여러 개의 컬럼 값을 포함할 수 있습니다. 
* ROW 서브쿼리를 사용할 때, 서브쿼리가 두 개 이상의 행을 반환하면 오류가 발생합니다. 
* ROW 서브쿼리와 비교하려면, 행 생성자(Row Constructor)를 사용해야 하며, 반환되는 값의 개수가 일치해야 합니다. 

```
SELECT * FROM t1
  WHERE (col1, col2) = (SELECT col3, col4 FROM t2 WHERE id = 10);
```

6. EXISTS 또는 NOT EXISTS 서브쿼리

* EXISTS: 서브쿼리가 한 행이라도 반환하면 TRUE를 반환합니다. 
* NOT EXISTS: 서브쿼리가 아무 행도 반환하지 않으면 TRUE를 반환합니다. 
* EXISTS 서브쿼리에서는 SELECT *, SELECT 5, SELECT column1 등 어떤 SELECT 리스트를 사용하든 결과에 영향을 미치지 않습니다. MySQL은 EXISTS 서브쿼리의 SELECT 절을 무시합니다. 

7. 상관 서브쿼리 (Correlated Subquery)
* 상관 서브쿼리는 서브쿼리 안에서 외부 쿼리(outer query)에 있는 테이블을 참조하는 경우를 말합니다. 

```
SELECT * FROM t1
  WHERE column1 = ANY (
    SELECT column1 FROM t2
    WHERE t2.column2 = t1.column2
  );
```
* 위 예시에서 서브쿼리는 외부 쿼리의 t1 테이블을 참조하고 있습니다. 

* 성능 최적화: 상관 서브쿼리는 외부 쿼리의 행마다 실행될 수 있어 성능에 영향을 줄 수 있습니다. 



# 2. CTE

~~~
✅ 학습 목표 :
* CTE에 대한 문법을 이해하고 활용할 수 있다. 
~~~

## 공통 테이블 표현식(CTE) 정리
공통 테이블 표현식(CTE, Common Table Expression)은 하나의 SQL 문장 내에서만 존재하는 임시적인 이름 있는 결과 집합입니다. 복잡한 쿼리를 구조적으로 분리하고 가독성을 높이는 데 유용합니다.

1. 일반 CTE (Common Table Expressions)

* 구문 
    * WITH 절을 사용하여 하나 이상의 CTE를 정의할 수 있습니다. 각 CTE는 서브쿼리의 결과 집합에 이름을 부여하며, 이후의 SELECT 문에서 마치 일반적인 테이블처럼 해당 이름을 참조하여 사용할 수 있습니다.

```
WITH
  cte1 AS (SELECT a, b FROM table1),
  cte2 AS (SELECT c, d FROM table2)
SELECT b, d FROM cte1 JOIN cte2
WHERE cte1.a = cte2.c;
```
* 구문 규칙
    * WITH 절은 SELECT, UPDATE, DELETE 문 앞에 위치해야 합니다. 또한 INSERT, REPLACE, CREATE TABLE/VIEW, DECLARE CURSOR, EXPLAIN 문에서도 사용할 수 있습니다.
    * 하나의 SQL 문장에는 단 하나의 WITH 절만 허용됩니다.
    * 여러 개의 CTE를 정의할 때는 쉼표(,)로 구분하여 나열해야 합니다.
    * CTE의 이름은 해당 문장 내에서 유일해야 합니다.
    * 이름 해석 순서는 서브쿼리 > CTE > 기본 테이블/뷰 순서입니다.
    * CTE 정의 시 컬럼 이름을 지정할 수 있습니다. 지정하지 않으면 첫 번째 SELECT 문의 select list에서 컬럼 이름을 가져옵니다.

<br>

<br>

---

# 3️⃣ 실습 문제

**두 문제 중에서 한 문제는 SubQuery와 CTE를 사용한 방법을 각각 활용해서 2개의 답변을 제시해주세요**

## 프로그래머스 문제 

https://school.programmers.co.kr/learn/courses/30/lessons/131123

> 즐겨찾기가 가장 많은 식당 정보 출력하기 (GROUP BY, SubQuery) : Lev 3

https://school.programmers.co.kr/learn/courses/30/lessons/131115

> 가격이 제일 비싼 식품의 정보 출력하기 (SUM, MAX, MIN, SubQuery) : Lev 2



---

## 문제 인증란

![사진](/)



---


## 문제 1

> **🧚예린이는 최근 여러 주문 데이터를 분석하는 업무를 맡게 되었습니다. 특정 고객의 주문 이력을 분석하기 위해, 다음과 같이 최근 30일간 주문만 필터링한 CTE를 사용해 쿼리를 작성했습니다.**

~~~sql
WITH RecentOrders AS (
  SELECT *
  FROM Orders
  WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
)
SELECT customer_id, COUNT(*) AS recent_order_count
FROM RecentOrders
GROUP BY customer_id;
~~~

> **그런데 예린이는 "이 쿼리를 WITH 없이, 서브쿼리 방식으로 바꿔서 실행해보라" 는 피드백을 받았고, 서브쿼리로 작성해보려 했지만 익숙하지 않아 SQL_ADVANCED를 듣는 학회원분들에게 도움을 요청하고 있습니다. 예린이의 쿼리를 WITH 없이 서브쿼리로 변환해보세요. 그리고 두 방식의 차이점을 설명해보고, 각각의 장단점을 정리해보세요**



~~~
```
SELECT
    customer_id,
    COUNT(*) AS recent_order_count
FROM
    (SELECT *
     FROM Orders
     WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)) AS RecentOrders
GROUP BY
    customer_id;
```
CTE는 복잡한 쿼리를 논리적으로 분할하여 가독성을 높이고, 한 번 정의한 중간 결과를 여러 번 재사용할 수 있는 장점이 있습니다. 반면 서브쿼리는 직관적으로 사용할 수 있지만, 쿼리가 복잡해질수록 가독성이 떨어지고 동일한 코드를 여러 번 중복해서 사용해야 하는 단점이 있습니다.
~~~



## 참고자료

서브쿼리를 사용하는 이유가 너무 어려우신 분들을 위해 참고자료를 첨부합니다. 아래 블로그를 통해서 더욱 쉽게 공부해보시고 문제를 풀어보세요.

1. [SQL] 서브쿼리는 언제 쓰는걸까? 
   https://project-notwork.tistory.com/38

2. [SQLD] 서브 쿼리 (SubQeury) 개념 및 종류
   https://bommbom.tistory.com/entry/%EC%84%9C%EB%B8%8C-%EC%BF%BC%EB%A6%ACSub-Query-%EA%B0%9C%EB%85%90-%EB%B0%8F-%EC%A2%85%EB%A5%98


### 🎉 수고하셨습니다.