## 오류를 바라보는 관점

**오류는 길잡이의 역할**
![사진]()
### bigquery error

#### syntax error
* 번역기 돌려보기
* 구글에 검색해 보기 
* 빨간색 체크표시 된 곳 혹은 그 위에가 오류일 경우 多

## 데이터 타입과 데이터 변환

### 데이터 타입

* 숫자 : 1, 2, 3, 4
* 문자 : "나", "데이터"
* 시간, 날짜 : 2024-01-01
* 부울 : 참/거짓 

### 데이터 변환

**보이는 것과 저장된 것의 차이 존재**  
*e.g. 1이어도 문자일 수도 있음 -> 우리가 원하는 타입으로 변환해야 함*

`CAST` : 자료 타입 변경 함수 
`SAFE_` : 조금 더 안전한 변경 함수수
---
```
SELECT
    CAST(1 AS STRING) # 숫자 1을 문자 1로 변경 
```
```
SELECT
    SAFE_CAST("카일스쿨" AS INT64) # 변환 실패 -> NULL 값 반환 
```
<br>

* 수학 함수 (외울 필요 X)
    * tip. 나누기를 할 경우 x/y 대신 SAFE_DIVIDE 함수 사용
    ```
    SAFE_DIVIDE(x,y) # x, y 중 하나라도 0인 경우 그냥 나누면 zero error 발생
    ```
<br>


* 문자열 함수 -> 이 5개를 한 번에 같이 쓸 수 있음!
    ![사진]()  
    * `CONCAT` (문자열 붙이기) : 이 코드는 데이터나 숫자를 데이터셋 안에 직접 넣음 -> FROM 없어도 실행 
        ```
        SELECT 
            CONCAT("안녕", "하세요", "!") AS result
        ```
    * `SPILT` (문자열 분리) : SPILT(문자열 원본, 나눌 기준이 되는 문자)  
        => **배열로 저장됨!**
        ``` 
        SELECT
            SPILT("가, 나, 다, 라", ",") AS result # 쉼표 기준으로 나눠라 -> 여기는 쉼표 뒤에 띄어쓰기 있어서 "가", " 나" 로 됨 
        ```
    * `REPLACE` (특정 단어 수정) : REPLACE(문자열 원본, 찾을 단어, 바꿀 단어)
        ```
        SELECT
            REPLACE("안녕하세요", "안녕", "실천") AS result
    * `TRIM` (문자열 자르기) : TRIM(문자열 원본, 자를 단어)
        ```
        SELECT
            TRIM("안녕하세요","하세요") AS result
        ```
    * `UPPER` (영어 소문자 -> 대문자) : UPPER(문자열 원본)
        ```
        SELECT
            UPPER("abc") AS result
        ```
<br>

### 날짜 및 시간 데이터
**우리가 어떤 행위를 할 때, 시간의 흐름에 따라 진행하므로 시간을 다루는 게 중요함**

* 시간 데이터 다루기
    * `DATE` : DATE만 표시하는 데이터 (e.g. 2023-12-31)
    * `DATETIME` : DATE와 TIME까지 표시하는 데이터, Time Zone 정보 X (2023-12-31 14:00:00)
        * `Time zone` : GMT (영국 근처), UTC (국제 표준 시간), `TIMESTAMP` (UTC부터 경과한 시간을 나타내는 값, e.g. 2023-12-31 14:00:00 UTC) => Time Zone 정보 O -> UTC 로 나옴! (UTC 에서 이만큼 지났다~)
    * `TIME` : 날짜와 무관하게 시간만 표시 (23:59:59:00)
    * `millisecond` (1000ms==1초) : millisecond -> timestamp -> datetime 으로 변경해서 사용 (빠른 반응이 필요한 분야에서 사용) 
    * `microsecond` : 1/1000ms, 1/1000000초  
        ![사진](/)

**많은 회사의 table에 시간이 timestamp로 저장된 경우가 많음 (혹은 datatime)**  
**-> timestamp <-> datetime 변환을 할 수 있어야 함**
