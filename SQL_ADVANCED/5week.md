# SQL_ADVANCED 5주차 정규 과제 

## Week 5 : 계층형 질의 & 셀프 조인

📌**SQL_ADVANCED 정규과제**는 매주 정해진 주제에 따라 **MySQL 공식 문서 또는 한글 블로그 자료를 참고해 개념을 정리한 후, 프로그래머스 SQL 문제 3문제**와 **추가 확인문제**를 직접 풀어보며 학습하는 과제입니다. 

이번 주는 아래의 **SQL_ADVANCED_5th_TIL**에 나열된 주제를 중심으로 개념을 학습하고, 주차별 **학습 목표**에 맞게 정리해주세요. 정리한 내용은 GitHub에 업로드한 후, **스프레드시트의 'SQL' 시트에 링크를 제출**해주세요. 



**(수행 인증샷은 필수입니다.)** 

> 프로그래머스 문제를 풀고 '정답입니다' 문구를 캡쳐해서 올려주시면 됩니다. 



## SQL_ADVANCED_5th

### 15.2.20 WITH (Common Table Expressions)

- **재귀 CTE를 통한 계층형 구조 탐색 방법을 중심으로 학습해주세요.**

> Self Join은 따로 MySQL 공식문서가 없습니다. 다른 블로그나 유튜브 영상을 참고하여 스스로 학습하고, 넣어주세요. 



## 🏁 강의 수강 (Study Schedule)

| 주차  | 공부 범위               | 완료 여부 |
| ----- | ----------------------- | --------- |
| 1주차 | 서브쿼리 & CTE          | ✅         |
| 2주차 | 집합 연산자 & 그룹 함수 | ✅         |
| 3주차 | 윈도우 함수             | ✅         |
| 4주차 | Top N 쿼리              | ✅         |
| 5주차 | 계층형 질의와 셀프 조인 | ✅         |
| 6주차 | PIVOT / UNPIVOT         | 🍽️         |
| 7주차 | 정규 표현식             | 🍽️         |



### 공식 문서 활용 팁

>  **MySQL 공식 문서는 영어로 제공되지만, 크롬 브라우저에서 공식 문서를 열고 이 페이지 번역하기에서 한국어를 선택하면 번역된 버전으로 확인할 수 있습니다. 다만, 번역본은 문맥이 어색한 부분이 종종 있으니 영어 원문과 한국어 번역본을 왔다 갔다 하며 확인하거나, 교육팀장의 정리 예시를 참고하셔도 괜찮습니다.**



# 1️⃣ 학습 내용

> 아래의 링크를 통해 *MySQL 공식문서*로 이동하실 수 있습니다.
>
> - 15.2.20 WITH (Common Table Expressions) : MySQL 공식문서 
>
> https://dev.mysql.com/doc/refman/8.0/en/with.html
>
> (한국어 버전) https://dart-b-official.github.io/posts/mysql-RecursiveWith/



<br>

---

# 2️⃣ 학습 내용 정리하기

## 1. 계층형 질의 (WITH RECURSIVE)

~~~
✅ 학습 목표 :
* 'WITH RECURSIVE' 문법을 활용해 계층형 구조를 탐색할 수 있다.
~~~

## 1\. 계층형 질의: WITH RECURSIVE (재귀 CTE)

### **개념 정의**

재귀적 공통 테이블 표현식 (Recursive CTE)은 **자기 자신의 이름**을 참조하며 **반복적으로 실행**되는 임시 테이블임. 끝없이 이어지는 **계층 구조** (조직도, 트리, 댓글)나 **반복 계산** (수열)을 SQL 내에서 처리할 수 있게 함.

### **핵심 구조 (두 가지 파트의 반복)**

재귀 CTE는 반드시 **`UNION ALL`** 또는 `UNION DISTINCT`로 구분된 **두 부분**으로 구성되며, `WITH RECURSIVE`로 시작함.

| 파트 | 역할 (무엇을 하는가?) | 예시 |
| :--- | :--- | :--- |
| **비재귀 부분 (Anchor, 시작점)** | 재귀의 **시작점** 또는 **초기 값**을 설정함. CTE 이름을 참조하지 않음. | "계산의 **첫 번째 값**은 1로 설정함." |
| **재귀 부분 (Recursive, 반복)** | **직전 단계의 결과**를 참조하여 다음 단계의 결과를 계산함. **종료 조건**에 도달할 때까지 반복됨. | "직전 값에 **1을 더한 값**이 다음 값이 됨." |

### **예시 코드: 1부터 5까지 숫자 만들기 (수열 생성)**

'1'에서 시작하여, 5에 도달할 때까지 계속해서 1을 더해나가는 반복 과정을 보여줌.

```sql
WITH RECURSIVE NumberSeries (n) AS (
    -- 1. 비재귀 (시작점): 초기값 1 설정
    SELECT 1 
    
    UNION ALL
    
    -- 2. 재귀 (반복): 직전 n의 값에 1을 더함
    SELECT n + 1 
    FROM NumberSeries   -- 자기 자신(NumberSeries)을 참조
    WHERE n < 5         -- 종료 조건: n이 5보다 작을 때까지만 반복
)
SELECT * FROM NumberSeries;
```

## 2. 셀프 조인

~~~
✅ 학습 목표 :
* 같은 테이블 내에서 상호 관계를 탐색할 수 있는 셀프 조인의 구조를 이해하고 사용할 수 있다. 
~~~

## 2\. 셀프 조인 (Self Join)

### **개념 정의**

**셀프 조인**은 **하나의 테이블을 두 번** 사용하여, 마치 서로 다른 두 테이블인 것처럼 조인하는 방식임. 주로 테이블 내의 **행들 사이의 1단계 관계** (예: 직원과 그 상사)를 탐색할 때 사용됨.

### **핵심 구조 (별칭을 이용한 구분)**

같은 테이블을 두 번 `FROM` 절에 사용하면서, 반드시 별칭(Alias)을 붙여서 **어떤 역할을 하는지** 명확히 구분해야 함.

  * **테이블 1 (별칭 E):** 직원(Employee) 역할
  * **테이블 2 (별칭 M):** 상사(Manager) 역할

### **예시 코드: 직원 이름 옆에 상사 이름 붙이기**

`employees` 테이블 하나에 `id`와 `manager_id` 정보가 함께 들어있다고 가정함.

| id | name | manager\_id |
| :--- | :--- | :--- |
| 101 | **김철수** | 100 |
| 102 | 이영희 | 101 |
| 100 | **박사장** | NULL |

```sql
SELECT
    E.name AS 직원_이름,
    M.name AS 상사_이름
FROM
    employees AS E  -- E: 현재 직원 정보를 가져올 테이블
JOIN
    employees AS M  -- M: 상사 정보를 가져올 테이블
ON
    E.manager_id = M.id; -- 조인 조건: '직원' 테이블의 상사 ID = '상사' 테이블의 ID
```


### **차이점**

| 구분 | WITH RECURSIVE (재귀 CTE) | 셀프 조인 (Self Join) |
| :--- | :--- | :--- |
| **관계 깊이** | **N단계 깊이** (전체 계층) 처리 | **1단계 깊이** (직속 관계) 처리 |
| **목적** | 전체 조직 경로 찾기, 수열 생성 등 **반복 처리**에 적합함 | 직속 상사/부하 등 **직계 관계** 파악에 용이함 |
| **특징** | 자기 자신을 **반복적**으로 참조하는 것이 가능함 | 자기 자신을 **단순히 두 역할**로 나눠 조인하는 것임 |


<br>

<br>

---

# 3️⃣ 실습 문제

## 문제 

- https://leetcode.com/problems/employees-earning-more-than-their-managers/ 

> LeetCode 181. Employees  Earning More Than Their Managers
>
> 학습 포인트 : 동일 테이블을 두 번 조인 (왜 동일 테이블을 JOIN 해야하는 문제일까)

- https://leetcode.com/problems/tree-node/description/

> LeetCode 608. Tree Node 
>
> 학습 포인트 : id, parent_id 기반의 트리 구조에서 **부모 ~ 자식 관계 재귀 탐색**
>
> Hint : (문제 해석) 
>
> - 어떤 노드가 Root Node 이려면, 부모노드가 존재하지 않아야 한다. 
> - 어떤 노드가 Inner Node 이려면, 나를 부모로 가지는 노드가 하나 이상 존재하여야 한다.
>   - 그 외네는 모두 Leaf Node 이다. --> (CASE 문을 사용하는 것을 추천드립니다.)

- https://school.programmers.co.kr/learn/courses/30/lessons/144856

> 프로그래머스 : 저자 별 카테고리 별 매출액 집계하기 
>
> 학습 포인트 : 카테고리와 서브카테고리 계층 구조를 분석하는 로직, SELF JOIN / CTE를 다 활용할 수 있다.
>
> - 위에 2가지의 문제를 풀어보고 난 이후, 더 편리한 방법으로 문제를 풀어보세요.

---

## 문제 인증란

![iamge](/images/스크린샷%202025-11-03%20203456.png)
![iamge](/images/스크린샷%202025-11-03%20203613.png)
![iamge](/images/스크린샷%202025-11-03%20203709.png)



---

# 확인문제

## 문제 1

> **🧚윤서는 어떤 기업의 조직 구조를 분석하는 SQL 쿼리를 작성하고 있습니다. 각 직원은 상위 관리자 ID(manager_id)를 가지며, 조직도는 같은 Employees 테이블 내에서 계층적으로 연결됩니다. 윤서는 최상위 관리자부터 각 사원까지의 계층 깊이(depth)를 계산하고자 다음과 같은 SELF JOIN 기반 쿼리를 시도했습니다.** 

~~~sql
SELECT e1.id, e1.name, e2.name AS manager_name
FROM Employees e1
LEFT JOIN Employees e2 ON e1.manager_id = e2.id;
~~~

> **쿼리를 잘 작성했다고 생각을 했지만, 막상 실행을 해보니 1단계 매니저까지만 추적할 수 있어 계층 구조의 전체를  표현하는데 한계가 존재했습니다. 이에 여러분에게 다음과 같은 미션을 요청합니다. WITH RECURSIVE를 활용하여  최상위 관리자부터 시작해 각 직원까지의 조직 구조 계층 깊이(depth)를 구하고, 결과를 depth가 높은 순으로 정렬하는 쿼리를 작성하세요.**



~~~
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT 
        id, 
        name, 
        manager_id, 
        1 AS depth
    FROM 
        Employees
    WHERE 
        manager_id IS NULL

    UNION ALL

    SELECT 
        E.id, 
        E.name, 
        E.manager_id, 
        EH.depth + 1 AS depth
    FROM 
        Employees AS E
    INNER JOIN 
        EmployeeHierarchy AS EH
    ON 
        E.manager_id = EH.id
)
SELECT 
    id,
    name,
    depth
FROM 
    EmployeeHierarchy
ORDER BY 
    depth DESC,
    id ASC;
~~~



---

### 참고자료

<!--셀프조인에 대해 학습하시기에 도움이 되도록 참고할말한 잘 설명된 블로그들을 같이 첨부하겠습니다. -->

https://step-by-step-digital.tistory.com/101



<br>

### 🎉 수고하셨습니다.