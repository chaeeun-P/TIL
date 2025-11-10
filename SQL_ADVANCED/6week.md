# SQL_ADVANCED 6주차 정규 과제

## **Week 6 : PIVOT / UNPIVOT**

📌**SQL_ADVANCED 정규과제**는 매주 정해진 주제에 따라 **MySQL 공식 문서 또는 한글 블로그 자료를 참고해 개념을 정리한 후, 프로그래머스 SQL 문제 3문제**와 **추가 확인문제**를 직접 풀어보며 학습하는 과제입니다.

이번 주는 아래의 **SQL_ADVANCED_6th_TIL**에 나열된 주제를 중심으로 개념을 학습하고, 주차별 **학습 목표**에 맞게 정리해주세요. 정리한 내용은 GitHub에 업로드한 후, **스프레드시트의 ‘SQL’ 시트에 링크를 제출**해주세요.

**(수행 인증샷은 필수입니다.)**

> 프로그래머스 문제를 풀고 ‘정답입니다’ 문구를 캡쳐해서 올려주시면 됩니다.

------

## **SQL_ADVANCED_6th_TIL**

- MySQL 공식문서에는 `PIVOT / UNPIVOT`에 대한 **전용 문법을 제공하지 않고 있습니다.** 따라서 이번 주차에서는 PIVOT / UNPIVOT에 대한 개념을 이해하고, 이를 `CASE WHEN + GROUP BY` 또는 `UNION ALL` 등의 조합으로 수동 구현할 수 있는 방법을 학습하면 됩니다. 



## **🏁 강의 수강 (Study Schedule)**

| **주차** | **공부 범위**           | **완료 여부** |
| -------- | ----------------------- | ------------- |
| 1주차    | 서브쿼리 & CTE          | ✅             |
| 2주차    | 집합 연산자 & 그룹 함수 | ✅             |
| 3주차    | 윈도우 함수             | ✅             |
| 4주차    | Top N 쿼리              | ✅             |
| 5주차    | 계층형 질의 & 셀프 조인 | ✅             |
| 6주차    | PIVOT / UNPIVOT         | ✅             |
| 7주차    | 정규 표현식             | 🍽️             |

<br>



# 1️⃣ 학습 내용

**참고할 자료를 아래에 같이 첨부합니다.**

<!-- 꼭 아래의 자료를 참고하지 않고, 개인적인 학습 방법으로 진행하셔도 좋습니다. -->

1. **PIVOT / UNPIVOT 개념 학습 Blog**

https://m.blog.naver.com/regenesis90/222205833002

https://blog.naver.com/regenesis90/222205964866

2. **MySQL 로 PIVOT 구현하기**

https://shxrecord.tistory.com/181



<br>

---

# 2️⃣ 학습 내용 정리하기

## 1. PIVOT

```
✅ 학습 목표 :
* MySQL에서 직접적인 `PIVOT` 문법은 없으므로, `CASE WHEN`, `GROUP BY`, `MAX()` 등으로 대체 구현할 수 있다.
* 데이터를 행 → 열 방향으로 전개하는 기본 로직을 이해한다.
```

-----

## 1\. PIVOT (행 $\rightarrow$ 열 전개)

### 💡 PIVOT 이해와 기본 로직

**PIVOT**은 2가지 컬럼($X$축, $Y$축)에 따라 그룹화된 집계 정보($K$)를 $Y$축 컬럼 값을 \*\*가로(열)\*\*로 펼쳐 2차원적인 형태로 조회하는 방법임.

  * **변환 전:** (직책) + (부서) $\rightarrow$ (직원 수) *[여러 행]*
  * **변환 후:** (직책) $\rightarrow$ (부서1 직원 수, 부서2 직원 수, ...) *[한 행]*

### 🛠️ MySQL PIVOT 구현 (IF 함수 사용)

Oracle SQL의 `PIVOT` 문법 대신, MySQL 등에서 `IF()` 함수와 `MAX()` 집계 함수를 조합하여 PIVOT을 구현함.

  * **핵심 원리:** `IF(조건, 참일 때 값, 거짓일 때 값)`을 사용하여 **특정 날짜(ROWNUM)에 해당하는 값만** 특정 컬럼($WORKDAY20$)에 넣고, 나머지는 0이나 '-'로 처리함. 이후 **`MAX()`** 함수로 그룹 내 유일한 참값(피벗된 값)을 추출함으로 구현됨.

**1. PM\_CALENDAR 피벗 (날짜 헤더 생성 예시):**

```sql
SELECT 
    '' AS USERCD,
    MAX(IF(B.ROWNUM = '20', B.WORKDAY, 0)) AS WORKDAY20,
    -- ... (이하 생략)
FROM (
    -- ROWNUM 키 생성: DATECHAR의 일자 부분(7, 2) 추출
    SELECT 
        CONCAT(SUBSTRING(A.DATECHAR,5,2),'.',SUBSTRING(A.DATECHAR,7,2)) WORKDAY,
        SUBSTRING(A.DATECHAR,7,2) AS ROWNUM
    FROM PM_CALENDAR A
    WHERE A.DATECHAR BETWEEN '20200420' AND '20200430'
) B;
```

**2. PM\_COMMUTE 피벗 (출퇴근 기록 데이터 전개):**
동일한 `ROWNUM` 키를 사용하고, `USERCD`를 기준으로 **`GROUP BY`** 함으로 각 사용자별 출퇴근 기록을 행에서 열로 전개함.

```sql
SELECT 		
    A.USERCD,	
    MAX(IF(ROWNUM = '20', CONCAT(A.TODATE, '<br>/', A.FROMDATE), '-')) AS WORKDAY20,
    -- ... (이하 생략)
FROM (
    -- ROWNUM 키 생성: WORKDAY의 일자 부분(7, 2) 추출
    SELECT   	 
        USERCD,
        SUBSTRING(WORKDAY,7,2) AS ROWNUM,
        IFNULL(DATE_FORMAT(TODATE, '%H:%i'),'') TODATE,		
        IFNULL(DATE_FORMAT(FROMDATE, '%H:%i'),'') FROMDATE
    FROM PM_COMMUTE
    WHERE WORKDAY BETWEEN '20200420' AND '20200430' AND CMPCD = 'P0001'
) A
GROUP BY A.USERCD;
```


## 2. UNPIVOT

```
✅ 학습 목표 :
* UNPIVOT 역시 직접 문법이 없으므로, `UNION ALL`과 `JOIN`, JSON 등의 방법으로 열 → 행 형태로 변환하는 과정을 익힌다.
* `UNION ALL`로 수동 구현 시의 컬럼 이름 통일과 데이터 병합 과정을 익힌다.
```

## 2\. UNPIVOT (열 $\rightarrow$ 행 압축)




### 💡 UNPIVOT 이해와 기본 로직

**UNPIVOT**은 PIVOT의 반대 역할임. 여러 개의 컬럼($Y_1$값, $Y_2$값, ...)으로 나누어져 분포하는 집계 함수 값들을 하나의 컬럼($K$) 아래 행(row)으로 묶어 새로운 구조의 테이블로 변환하는 것임.

  * **변환 전:** (직책), (부서1 직원 수), (부서2 직원 수) *[한 행]*
  * **변환 후:** (직책), (부서), (직원 수) *[여러 행]*

### 🛠️ UNPIVOT 구현 (UNION ALL 사용)

UNPIVOT 문법이 없는 환경에서는 여러 컬럼을 \*\*`UNION ALL`\*\*로 수동 결합하여 하나의 행(Row)으로 만듦.

**1. UNION ALL 기본식:**

```sql
SELECT 컬럼X, '컬럼Y값1' AS 컬럼Y, 컬럼Y1_K AS 컬럼K FROM 테이블A
UNION ALL
SELECT 컬럼X, '컬럼Y값2' AS 컬럼Y, 컬럼Y2_K AS 컬럼K FROM 테이블A
-- ... (모든 컬럼을 개별 SELECT 문으로 변환 후 합치기)
```

**2. 오라클 UNPIVOT 예시 (pivot\_sample 테이블 UNPIVOT):**

```sql
SELECT * FROM pivot_sample
UNPIVOT (
    -- 결과로 만들어질 값 컬럼 이름
    count_employee 
    -- 결과로 만들어질 그룹 컬럼 이름
    FOR department_id IN (
        -- 기존 컬럼명 AS 새 그룹 값
        d10_c AS 10,
        d20_c AS 20,
        -- ... (이하 생략)
    )
);
```

### 🤝 최종 UNION ALL을 통한 데이터 병합

두 개의 피벗된 테이블(`PM_CALENDAR` 피벗 결과와 `PM_COMMUTE` 피벗 결과)을 \*\*`UNION ALL`\*\*로 합침으로, 날짜 헤더 정보와 사용자별 출퇴근 기록이 `WORKDAYxx` 컬럼 아래에 결합된 최종 직관적인 형태의 테이블이 완성됨.

  * **PM\_CALENDAR 피벗**에서 생성된 `WORKDAY` 값(날짜)은 **헤더 행**으로 사용됨.
  * **PM\_COMMUTE 피벗**에서 생성된 `TODATE`/`FROMDATE` 값은 **데이터 행**으로 사용됨.
  * 두 쿼리의 컬럼 이름(`USERCD`, `WORKDAY20`, `WORKDAY21`, ...)과 개수가 **정확히 일치**해야 `UNION ALL`이 가능함.



---

# 3️⃣ 실습 문제

## Leetcode 문제 

https://leetcode.com/problems/reformat-department-table/description/

> LeetCode. Reformat Department Table
>
> 학습 포인트 : MySQL 에서는 PIVOT을 쉽게 구할 수 있는 방법이 없다. 
>
> - 수동으로 구하기 : CASE WHEN + 집계함수 / GROUP BY + 조건 분기 사용



## 문제 인증란

![images](/images/스크린샷%202025-11-10%20221238.png)



## 확인 문제 

### 문제 1

> **🧚지희는 매월 각 매장의 월별 매출 데이터가 담긴 테이블을 가공하려 합니다. 아래와 같은 테이블이 있다고 가정합시다.**

| **branch** | **Jan_sales** | **Feb_sales** | **Mar_sales** |
| ---------- | ------------- | ------------- | ------------- |
| A          | 100           | 120           | 130           |
| B          | 90            | 110           | 140           |

> **Q. 이 테이블을 아래와 같은 형태로 바꾸고 싶습니다. SQL에서 UNION ALL을 활용하여 UNPIVOT 구조를 수동으로 구현해보세요.**

| **branch** | **month** | **sales** |
| ---------- | --------- | --------- |
| A          | Jan       | 100       |
| A          | Feb       | 120       |
| A          | Mar       | 130       |
| B          | Jan       | 90        |
| B          | Feb       | 110       |
| B          | Mar       | 140       |

```
SELECT branch, 'Jan' AS month, Jan_sales AS sales FROM SalesTable
UNION ALL
SELECT branch, 'Feb' AS month, Feb_sales AS sales FROM SalesTable
UNION ALL
SELECT branch, 'Mar' AS month, Mar_sales AS sales FROM SalesTable
ORDER BY branch, month;
```



### 문제 2

> **🧚태연이는 지점별로 월별 매출을 한 눈에 보기 위해, 아래와 같이 매출 데이터가 저장된 데이터를 가공하려고 합니다.**

| **branch** | **month** | **sales** |
| ---------- | --------- | --------- |
| A          | Jan       | 100       |
| A          | Feb       | 120       |
| A          | Mar       | 130       |
| B          | Jan       | 90        |
| B          | Feb       | 110       |
| B          | Mar       | 140       |

> **이 데이터를 아래와 같이 월별 매출 컬럼이 각각 존재하도록 PIVOT 형태로 바꾸고 싶습니다.MySQL에서는 PIVOT 문법이 없기 때문에, CASE WHEN, GROUP BY, MAX() 또는 SUM() 등을 이용해 수동으로 구현해보세요.**

- 원하는 결과 

| **branch** | **Jan_sales** | **Feb_sales** | **Mar_sales** |
| ---------- | ------------- | ------------- | ------------- |
| A          | 100           | 120           | 130           |
| B          | 90            | 110           | 140           |

~~~
SELECT
    branch,
    MAX(CASE WHEN month = 'Jan' THEN sales ELSE NULL END) AS Jan_sales,
    MAX(CASE WHEN month = 'Feb' THEN sales ELSE NULL END) AS Feb_sales,
    MAX(CASE WHEN month = 'Mar' THEN sales ELSE NULL END) AS Mar_sales
FROM 
    SalesData
GROUP BY 
    branch
ORDER BY 
    branch;
~~~







### **🎉 수고하셨습니다.**