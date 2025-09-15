# SQL_ADVANCED 2주차 정규 과제 

## Week 2 :집합 연산자 & 그룹 함수

📌**SQL_ADVANCED 정규과제**는 매주 정해진 주제에 따라 **MySQL 공식 문서 또는 한글 블로그 자료를 참고해 개념을 정리한 후, 프로그래머스/ Solvesql / LeetCode에서 SQL 3문제**와 **추가 확인문제**를 직접 풀어보며 학습하는 과제입니다. 

이번 주는 아래의 **SQL_ADVANCED_2nd_TIL**에 나열된 주제를 중심으로 개념을 학습하고, 주차별 **학습 목표**에 맞게 정리해주세요. 정리한 내용은 GitHub에 업로드한 후, **스프레드시트의 'SQL' 시트에 링크를 제출**해주세요. 



**👀 (수행 인증샷은 필수입니다.)** 

> 프로그래머스 문제를 풀고 '정답입니다' 문구를 캡쳐해서 올려주시면 됩니다. 



## SQL_ADVANCED_2nd

**1. 집합 연산자**

### 15.2.18. UNION Clause

### 15.2.14. Set Operations with UNION, INTERSECT

- UNION, UNION ALL 중심으로 개념을 정리하고, INTERSECT, EXCEPT는 구문이 어떤 기능을 하는지 간단히만 알아봅니다. EXCEPT와 INTERSECT는 대부분 MySQL 버전에서 공식 지원되지 않기 때문에, **이번주 학습은 `UNION, UNION ALL` 만 집중적으로 정리해주세요.**

**2. 그룹 함수 (집계 함수)**

### 14.19.1. Aggregate Function Descriptions



## 🏁 주차별 학습 (Study Schedule)

| 주차  | 공부 범위               | 완료 여부 |
| ----- | ----------------------- | --------- |
| 1주차 | 서브쿼리 & CTE          | ✅         |
| 2주차 | 집합 연산자 & 그룹 함수 | ✅         |
| 3주차 | 윈도우 함수             | 🍽️         |
| 4주차 | Top N 쿼리              | 🍽️         |
| 5주차 | 계층형 질의와 셀프 조인 | 🍽️         |
| 6주차 | PIVOT / UNPIVOT         | 🍽️         |
| 7주차 | 정규 표현식             | 🍽️         |



### 공식 문서 활용 팁

>  **MySQL 공식 문서는 영어로 제공되지만, 크롬 브라우저에서 공식 문서를 열고 이 페이지 번역하기에서 한국어를 선택하면 번역된 버전으로 확인할 수 있습니다. 다만, 번역본은 문맥이 어색한 부분이 종종 있으니 영어 원문과 한국어 번역본을 왔다 갔다 하며 확인하거나, 교육팀장의 정리 예시를 참고하셔도 괜찮습니다.**



# 1️⃣ 학습 내용 

> 아래의 링크를 통해 *MySQL 공식문서*로 이동하실 수 있습니다.
>
> - 15.2.18. UNION Clause : MySQL 공식문서 
>
> https://dev.mysql.com/doc/refman/8.0/en/union.html
>
> - 15.2.14. Set Operations with UNION, INTERSECT : MySQL 공식문서
>
> https://dev.mysql.com/doc/refman/8.0/en/set-operations.html
>
> (한국어 버전) https://dart-b-official.github.io/posts/mysql-UNION/
>
> - 14.19.1. Aggregate Function Descriptions : MySQL 공식문서
>
> https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html
>
> (한국어 버전) https://dart-b-official.github.io/posts/mysql-aggregate_function/



<!-- 여기까진 그대로 둬 주세요-->

# 2️⃣ 학습 내용 정리하기

## 1. 집합 연산자

~~~
✅ 학습 목표 :
* UNION과 UNION ALL의 차이와 사용법을 이해한다.
* 중복 제거 여부, 컬럼 정렬 조건 등을 고려하여 올바르게 집합 연산자를 사용할 수 있다. 
~~~

1. 집합 연산자: 여러 쿼리 결과를 하나로 합치기

* 집합 연산자는 서로 다른 SELECT 문의 결과를 결합하여 하나의 테이블처럼 보여주는 강력한 도구
* 이 연산자를 사용할 때는 중복을 어떻게 처리할지가 가장 중요한 차이점


* UNION: 결과 집합을 합치면서 중복된 행을 자동으로 제거
    * UNION은 내부적으로 중복을 확인하고 제거하는 과정을 거치기 때문에, 이 과정이 불필요한 상황에서는 UNION ALL보다 성능이 떨어질 수 O
    * 데이터의 유일성을 보장해야 할 때 유용하게 쓰임 

```
-- 두 테이블에서 중복되는 값 'A'를 한 번만 표시
SELECT name FROM employees
UNION
SELECT name FROM contractors;
```

* UNION ALL: 중복된 행을 제거하지 않고 모든 행을 그대로 합쳐서 반환
    * 중복 제거를 위한 추가적인 연산이 없으므로 UNION보다 훨씬 빠르게 동작
    * 따라서 결과에 중복이 발생하지 않는다는 것을 확실히 알거나, 중복이 허용되는 경우에는 UNION ALL을 사용하는 것이 좋음

```
-- 두 테이블의 모든 값을 중복 여부와 관계없이 합침
SELECT name FROM employees
UNION ALL
SELECT name FROM contractors;
```

* 집합 연산자 사용 시 필수 규칙
    * 컬럼 수와 순서 일치: 결합하려는 모든 SELECT 문은 컬럼의 개수와 순서가 동일해야 함
    * 데이터 타입 호환: 각 컬럼의 데이터 타입이 서로 호환되어야 함 (e.g. CHAR와 VARCHAR는 호환되지만, CHAR와 DATE는 호환되지 않습니다. MySQL은 필요에 따라 자동으로 타입을 변환)
    * 컬럼명: 최종 결과의 컬럼명은 가장 첫 번째 SELECT 문에서 정의한 컬럼 이름을 따름
    * ORDER BY와 LIMIT: 전체 결과에 정렬이나 개수 제한을 적용하려면, UNION 연산자 뒤에 오는 마지막 SELECT 문에 ORDER BY나 LIMIT 절을 추가해야 함

```
-- 두 쿼리 결과를 합친 후 최종적으로 정렬 및 제한
SELECT product_id, product_name FROM products WHERE price > 100
UNION
SELECT product_id, product_name FROM archived_products WHERE stock > 0
ORDER BY product_name ASC
LIMIT 10;
```

## 2. 그룹함수

~~~
✅ 학습 목표 :
* COUNT, SUM, AVG, MAX, MIN 함수의 기본 사용법을 익힌다.
* GROUP BY와 HAVING 절을 적절히 활용할 수 있다.
* NULL과 집계 함수가 어떻게 상호작용하는지 이해한다. 
~~~

2. 그룹 함수: 여러 행을 하나의 값으로 요약
* 그룹 함수는 여러 행의 데이터를 모아 하나의 값으로 요약해주는 함수
* 주로 GROUP BY 절과 함께 사용되며, 특정 기준으로 그룹을 나눈 뒤 각 그룹에 대한 요약 정보를 계산하는 데 필수적

* 주요 그룹 함수
    * COUNT(): 그룹 내의 행 개수를 셈
    * COUNT(*): NULL 값 여부와 관계없이 모든 행의 개수를 반환
    * COUNT(컬럼명): 해당 컬럼의 값이 NULL이 아닌 행의 개수만 셈
    * COUNT(DISTINCT 컬럼명): 해당 컬럼의 고유한 값 개수만 셈 

```
-- 각 부서별 직원 수 계산
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
```
* SUM() & AVG(): 숫자 데이터의 총합과 평균을 계산
    * 이 함수들은 NULL 값을 자동으로 무시하고 계산에 포함 X

```
-- 각 카테고리별 총 매출액과 평균 가격 계산
SELECT category, SUM(sales) AS total_sales, AVG(price) AS average_price
FROM products
GROUP BY category;
```
* MAX() & MIN(): 그룹 내에서 가장 큰 값(MAX)과 가장 작은 값(MIN)을 찾음 
    * 숫자뿐만 아니라 문자열, 날짜/시간 데이터에도 적용할 수 있어 매우 유용

```
-- 각 상품별로 가장 최근에 판매된 날짜와 최고 판매 금액 찾기
SELECT product_id, MAX(sale_date) AS latest_sale, MIN(price) AS min_price
FROM sales
GROUP BY product_id;
```
* GROUP_CONCAT(): 그룹 내 여러 행에 있는 문자열 값들을 하나의 긴 문자열로 합쳐줌
    * EPARATOR 옵션으로 값들 사이에 , 외의 다른 구분자를 넣을 수 있고, ORDER BY로 연결 순서를 지정할 수도 있음

```
-- 각 학생이 수강하는 과목들을 쉼표로 구분하여 나열
SELECT student_name, GROUP_CONCAT(subject_name SEPARATOR ', ') AS subjects
FROM student_courses
GROUP BY student_name;
```
* 룹 함수 사용 시 유의점
    * GROUP BY 절: SELECT 절에 그룹 함수가 아닌 다른 컬럼이 포함되면, 반드시 그 컬럼을 GROUP BY 절에 명시
        * GROUP BY가 없으면 전체 결과가 하나의 그룹으로 간주
    * HAVING 절: 그룹 함수를 사용한 결과에 조건을 적용하여 필터링하고 싶을 때는 WHERE 절 대신 HAVING 절을 사용
        * WHERE 절은 그룹화가 이루어지기 전에 개별 행에 조건을 적용

```
-- 전체 평균 평점보다 높은 평점을 가진 영화 카테고리만 조회
SELECT category, AVG(rating) AS avg_rating
FROM movies
GROUP BY category
HAVING AVG(rating) > (SELECT AVG(rating) FROM movies);
```

<br><br>

---

# 3️⃣ 실습 문제

https://leetcode.com/problems/customers-who-never-order/

> LeetCode 183. Customers Who never Order
>
> 학습 포인트 : 주문 내역이 없는 고객을 찾기 위한 패턴 익히기  

https://leetcode.com/problems/department-highest-salary/description/

> LeetCode 184. Department Highest Salary
>
> 학습 포인트 : 부서별 최고 연봉자 추출을 위한 **그룹별 정렬 / 필터링** 방식 이해하기

---

## 문제 인증란

![사진](/images/스크린샷%202025-09-15%20215102.png)
![사진](/images/스크린샷%202025-09-15%20215303.png)

---

# 확인문제

## 문제 1

> **🧚동혁이는 SQL 문제를 풀면서 `UNION과 UNION ALL`의 차이를 명확히 이해하지 못해 중복된 값이 생기거나 누락되는 문제를 계속 겪고 있습니다.** 아래는 동혁이가 작성한 쿼리입니다.

~~~sql
SELECT name FROM member
UNION
SELECT name FROM blackList;
~~~

> **그런데 예상과 달리 blacklist에만 있는 이름이 결과에 안 나오거나, 중복된 이름이 사라져서 헷갈리고 있습니다. UNION과 UNION ALL의 차이를 설명하고, 중복 포함 여부에 따라 어떤 경우에 어떤 쿼리를 써야 하는지 예시와 함께 설명해주세요**

<br>

~~~
UNION과 UNION ALL의 차이는 중복 처리 방식  

* UNION: 두 쿼리 결과를 결합하며 중복 행을 제거하는 방식
* UNION ALL: 두 쿼리 결과를 결합하며 중복 행을 모두 포함하는 방식  

따라서 데이터 유일성이 중요할 때는 UNION을, 성능을 고려하며 모든 행이 필요할 때는 UNION ALL을 사용해야 함
~~~

## 참고자료
그룹 함수가 많아서 중요하게 많이 쓰이는 함수들을 정리해놓은 참고자료를 첨부합니다. 아래 블로그를 통해서 더욱 쉽게 공부해보시고 문제를 풀어보세요.
1. [SQL 10] 그룹 함수, GROUP BY 절, HAVING 절
https://keep-cool.tistory.com/37

또한, MySQL 문서 이외에 Oracle 함수에서 사용하는 그룹함수에 대한 소개도 같이 첨부합니다. SQLD 시험 준비하시는 분이 있다면 이 자격증 시험에서는 Oracle 언어를 기반으로 문제가 출제하오니 아래 블로그도 같이 공부해보세요. (선택사항입니다.)
2. 그룹 함수 (Group FUNCTION)
https://dkkim2318.tistory.com/48

<br>

### 🎉 수고하셨습니다.