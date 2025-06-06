# 통계학 3주차 정규과제

📌통계학 정규과제는 매주 정해진 분량의 『*데이터 분석가가 반드시 알아야 할 모든 것*』 을 읽고 학습하는 것입니다. 이번 주는 아래의 **Statistics_3rd_TIL**에 나열된 분량을 읽고 `학습 목표`에 맞게 공부하시면 됩니다.

아래의 문제를 풀어보며 학습 내용을 점검하세요. 문제를 해결하는 과정에서 개념을 스스로 정리하고, 필요한 경우 추가자료와 교재를 다시 참고하여 보완하는 것이 좋습니다.

2주차는 `2부-데이터 분석 준비하기`를 읽고 새롭게 배운 내용을 정리해주시면 됩니다.


## Statistics_3rd_TIL

### 2부. 데이터 분석 준비하기
### 08. 분석 프로젝트 준비 및 기획
### 09. 분석 환경 세팅하기



## Study Schedule

|주차 | 공부 범위     | 완료 여부 |
|----|----------------|----------|
|1주차| 1부 p.2~56     | ✅      |
|2주차| 1부 p.57~79    | ✅      | 
|3주차| 2부 p.82~120   | ✅      | 
|4주차| 2부 p.121~202  | 🍽️      | 
|5주차| 2부 p.203~254  | 🍽️      | 
|6주차| 3부 p.300~356  | 🍽️      | 
|7주차| 3부 p.357~615  | 🍽️      |  

<!-- 여기까진 그대로 둬 주세요-->

# 08. 분석 프로젝트 준비 및 기획

```
✅ 학습 목표 :
* 데이터 분석 프로세스를 설명할 수 있다.
* 비즈니스 문제를 정의할 때 주의할 점을 설명할 수 있다.
* 외부 데이터를 수집하는 방법에 대해 인식한다.
```

### 데이터 분석 프로세스 

**데이터 분석의 목적: 효과적인 결정을 할 수 있도록 하는 것**
**-> 정확하게 목표 설정을 하는 것이 가장 중요함**
* 데이터 분석의 과정  
![사진](/images/스크린샷%202025-04-02%20135407.png)

* 데이터 분석 방법론
    1. CRISP-DM 방법론  
    ![사진](/images/스크린샷%202025-04-02%20135606.png)  
    ![사진](/images/스크린샷%202025-04-02%20135614.png)
    2. SAS SEMMA 방법론  
    ![사진](/images/스크린샷%202025-04-02%20135720.png)  
    ![사진](/images/스크린샷%202025-04-02%20135727.png)  
    ![사진](/images/스크린샷%202025-04-02%20135747.png)

*초반부에는 비즈니스 문제와 해결방향 명확히 정의 + 데이터 탐색 -> 중반부에는 데이터를 문적에 맞게 수집 및 가공 (필요에 따라 머신러닝 사용) -> 후반부에는 분석 결과 검토 및 검증 -> 환경에 적용 => 이 모든 과정을 양방향으로 모니터링하며 보완해야 함*

* MECE 방식 : 세부 정의들이 서로 겹치지 않고, 전체를 합쳤을 땐 빠진 것 없이 전체를 이루는 것  
![사진](/images/스크린샷%202025-04-02%20140230.png)  
-> 세부 항목이 중복 X 지만 다 합치면 추진 과제가 되도록 

### 비즈니스 문제 정의 

**비즈니스 문제는 현상에 대한 설명 X 본질적인 문제가 함께 전달되어야 함!**  
![사진](/images/스크린샷%202025-04-02%20140647.png)  
-> e.g. 통신사의 약정이 끝난 고객들이 타 통신사로 이탈 (현상 설명)  
-> e.g. 고객들이 이탈하여 수익이 감소 (비즈니스 문제)  
![사진](/images/스크린샷%202025-04-02%20140810.png)

**초기 EDA에서의 상관관계/데이터 특성/시각화 적극 활용 -> 커뮤니케이션에 활용**  
-> 또한, EDA 진행하며 분석 목적을 바꿔야 하는 경우에는 빠른 커뮤니케이션을 통해 빠르게 변경해야 함 

### 외부 데이터 수집
![사진](/images/스크린샷%202025-04-02%20141349.png)
* 외부 데이터 수집 방법
    1. 데이터 구매 / mou를 통한 공유
    2. 오픈 데이터 수집 -> 가공 
    3. 웹에 있는 데이터 크롤링

#### 크롤링

* 법적 이슈를 주의하여, robots.txt 르르 확인하여 수집 가능한 데이터를 확인해야 함 
* 크롤링 : 웹 페이지 내의 링크들을 따라가면서 **모든 내용** 가져오기
    * 스크래핑 : 웹 페이지에서 **자신이 원하는 부분의 내용**만 가져옴 (e.g. 날씨 정보 사이트에서 날씨 데이터만 수집) 

# 09. 분석 환경 세팅하기

```
✅ 학습 목표 :
* 데이터 분석의 전체적인 프로세스를 설명할 수 있다.
* 테이블 조인의 개념과 종류를 이해하고, 각 조인 방식의 차이를 구분하여 설명할 수 있다.
* ERD의 개념과 역할을 이해하고, 기본 구성 요소와 관계 유형을 설명할 수 있다.
```
*cf. 프로그램 비교*  
![사진](/images/스크린샷%202025-04-02%20142237.png)

### 데이터 처리 프로세스
![사진](/images/스크린샷%202025-04-02%20142306.png)
* 데이터의 흐름 
    * OLTP : 실시간으로 데이터를 트랜잭션 단위로 수집, 분류, 저장하는 시스템 (데이터 생성/저장되는 처음 단계) 
    * DW : 데이터 창고, 사용자 관점에서 주제 별로 통합해 데이터를 쉽게 넣고 뺄 수 있도록 저장해 놓은 DB (여러 시스템에 산재되어 있던 데이터를 한 곳으로 취합)
        * ODS : DW 에 저장하기 전에 임시로 데이터 보관하는 중간 단계  
        -> DW : 전체 히스토리 데이터 보관, ODS : 최신 데이터 반영
    * DM : 사용자 목적에 맞게 가공된 일부 데이터 저장 (집단에 맞게 가공된 개별 데이터 저장소) 
<br>

* 데이터 처리 프로세스 (ETL)  
    ![사진](/images/스크린샷%202025-04-02%20142820.png)
    * Extract (추출) -> Transform (변환) -> Load (불러내기)

<br>

### 분산데이터
* 분산데이터 처리 : 여러 컴퓨터가 일 한 다음 결과 합치기 
    * scale up : 하나의 컴퓨터의 용량 up, 더 빠른 프로세서 탑재 (하나의 컴퓨터가 진행) / scale out : 분산데이터 처리 방식 (여러 컴퓨터가 병렬적으로 처리)
<br>

* 분산처리 방법
    * HDFS (분산처리 방법)
    * 맵리듀스 : HDFS 에 저장된 데이터를 효과적으로 처리하는 방법  
        ![사진](/images/스크린샷%202025-04-02%20151055.png)
        * 관련된 데이터끼리 묶어서 임시의 집합 만듦 (맵 단계) -> 필터링, 정렬을 통해 데이터 추출 (리듀스 단계) 
        * key-value 쌍으로 데이터를 처리함 (자동차-car)  

    * 하둡  
    ![사진](/images/스크린샷%202025-04-02%20151424.png)
<br>

* 분산 시스템 구조  
![사진](/images/스크린샷%202025-04-02%20151509.png)

### 테이블 조인과 ERD

#### 테이블 조인
* 조인의 기본 개념 : 두 테이블이 겹치는 부분을 기준으로 연결 
* left / right join
    * 왼쪽/오른쪽 테이블을 기준으로 다른 테이블 결합
    * 왼쪽/오른쪽 테이블은 그대로 유지하면서 겹치는 것 기준으로 왼쪽/오른쪽 테이블 데이터만 추가함
    * 만약 일치하는 키 값 X -> 행은 살리되 결측값으로 표현됨 (왼쪽/오른쪽의 데이터만 덩그러니 남게 됨!)
    * 겹치는 거 2개면 2개 다 씀! (다른 행으로) 
* inner join : 겹치는 부분의 행만 가져옴 (안 겹치면 행 자체가 사라짐!)
* full join : 모든 행을 살림 (겹치는 코드 X -> 행은 살리고 결측값으로 표현)
* Cross join  
    ![사진](/images/스크린샷%202025-04-02%20153457.png)
    * 고객 별로 각 차량의 구매확률 구하기 (고객 1명 당 차량 5개의 확률 테이블)  

<br>

*메타데이터 관리 시스템 : 데이터가 어디에 어떻게 저장되어 있는지, 데이터를 어떻게 사용할 것인지 이해할 수 있도록 데이터에 대한 정보를 관리하는 시스템*
#### ERD (Entity Relationship Diagram)  
**ERD 를 보고 DB 구조 파악!**
* 각 테이블의 구성 정보와 테이블 간 관계를 도식으로 표현한 그림 형태  
![사진](/images/스크린샷%202025-04-02%20154022.png)

* ERD 의 핵심, key
    * 기본 키 : 테이블에서 유일하게 구분되는 칼럼 (중복 X, 결측값 X)
    * 왜래 키 : 테이블 간에 연결을 위한 칼럼 (중복 O, 결측값 O)
    * 슈퍼 키 : 테이블에서 행을 유일하게 식별할 수 있는 하나의 키 혹은 조합된 키
    * 후보 키 : 기본키 조건의 유일성과 최소성 만족 but 기본키 X   
**테이블 간에는 1:1 / 1:N / N:N 매칭 등 다양함 -> 테이블 간의 관계를 ERD 를 통해서 정확히 파악하여 데이터를 다뤄야 함**  
![사진](/images/스크린샷%202025-04-02%20154022.png)

<br>
<br>

# 확인 문제

## 문제 1.

> **🧚 아래의 테이블을 조인한 결과를 출력하였습니다. 어떤 조인 방식을 사용했는지 맞춰보세요.**

> 사용한 테이블은 다음과 같습니다.

![TABLE1](https://github.com/ejejbb/Template/raw/main/File/2.6.PNG)|![TABLE2](https://github.com/ejejbb/Template/raw/main/File/2.7.PNG)
---|---|

> 보기: INNER, LEFT, RIGHT 조인

<!-- 테이블 조인의 종류를 이해하였는지 확인하기 위한 문제입니다. 각 테이블이 어떤 조인 방식을 이용하였을지 고민해보고 각 테이블 아래에 답을 작성해주세요.-->

### 1-1. 
![TABLE](https://github.com/ejejbb/Template/raw/main/File/2-1.PNG)
```
LEFT join
```

### 1-2. 
![TABLE](https://github.com/ejejbb/Template/raw/main/File/2-3.PNG)
```
inner join
```

### 1-3. 
![TABLE](https://github.com/ejejbb/Template/raw/main/File/2-2.PNG)
```
RIGHT join
```

### 🎉 수고하셨습니다.