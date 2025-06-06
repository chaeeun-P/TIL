# 통계학 4주차 정규과제

📌통계학 정규과제는 매주 정해진 분량의 『*데이터 분석가가 반드시 알아야 할 모든 것*』 을 읽고 학습하는 것입니다. 이번 주는 아래의 **Statistics_4th_TIL**에 나열된 분량을 읽고 `학습 목표`에 맞게 공부하시면 됩니다.

아래의 문제를 풀어보며 학습 내용을 점검하세요. 문제를 해결하는 과정에서 개념을 스스로 정리하고, 필요한 경우 추가자료와 교재를 다시 참고하여 보완하는 것이 좋습니다.

4주차는 `2부. 데이터 분석 준비하기`를 읽고 새롭게 배운 내용을 정리해주시면 됩니다.


## Statistics_4th_TIL

### 2부. 데이터 분석 준비하기
### 10. 데이터 탐색과 시각화



## Study Schedule

|주차 | 공부 범위     | 완료 여부 |
|----|----------------|----------|
|1주차| 1부 p.2~56     | ✅      |
|2주차| 1부 p.57~79    | ✅      | 
|3주차| 2부 p.82~120   | ✅      | 
|4주차| 2부 p.121~202  | ✅      | 
|5주차| 2부 p.203~254  | 🍽️      | 
|6주차| 3부 p.300~356  | 🍽️      | 
|7주차| 3부 p.357~615  | 🍽️      | 

<!-- 여기까진 그대로 둬 주세요-->

# 10. 데이터 탐색과 시각화

```
✅ 학습 목표 :
* EDA의 목적을 설명할 수 있다.
* 주어진 데이터셋에서 이상치, 누락값, 분포 등을 식별하고 EDA 결과를 바탕으로 데이터셋의 특징을 해석할 수 있다.
* 공분산과 상관계수를 활용하여 두 변수 간의 관계를 해석할 수 있다.
* 적절한 시각화 기법을 선택하여 데이터의 특성을 효과적으로 전달할 수 있다.
```
### 데이터 시각화의 궁극적 목적: 분석 결과의 커뮤니케이션

### EDA 

* EDA의 목적
    * 데이터의 형태와 척도가 분석에 알맞는지 확인
    * 데이터의 결측값 & 이상치 파악 및 보완
    * 변수 간의 관계성 파악
    * 분석 목적과 방향성 점검 및 보정 

* EDA 코드
    * 왜도 확인 : df.skew()
    * 첨도 확인 : df.kurtosis()
    * 분포 확인 : sns.distplot(df['칼럼']) 

### 공분산 / 상관계수

* 공분산 : 변수 간의 상관관계 수치화
    * 변수 간의 다른 척도 기준 반영 -> 공분산 값으로 상관성 크기 비교 X (1, 2와의 공분산과 3, 4와의 공분산 비교X)
    * 공분산 코드 : df.cov()
* 상관계수 (피어슨 상관계수) : 공분산을 두 변수가 변하는 전체의 정도로 나눔 (-1~1)
    * 상관계수의 단계    
        ![사진](/images/스크린샷%202025-05-06%20173548.png)    
    * 산점도의 기울기와 상관계수는 관련 X  
        ![사진](/images/스크린샷%202025-05-06%20173752.png)  
    * 상관계수 ↑ -> 예상의 정확도, 설명력 ↑
    * 이상치의 영향을 고려하여 시각화까지 해 볼 것! -> 이상치 영향이 클 경우 제거하는 것이 좋음 
    * 산점도 행렬 시각화 코드  
        ![사진](/images/스크린샷%202025-05-06%20174112.png)  
    * clustermap  
        ![사진](/images/스크린샷%202025-05-06%20175104.png)   
        ![사진](/images/스크린샷%202025-05-06%20175329.png)  

### 추가 시각화 코드
* 피벗  
    ![사진](/images/스크린샷%202025-05-06%20180649.png)  
* 방사형 차트 -> 한 번에 시각화하여 비교도 가능  
    ![사진](/images/스크린샷%202025-05-06%20180856.png)  
* 파이차트 / 도넛차트  
* 트리맵 차트 -> 위계구조까지 표현  
    ![사진](/images/스크린샷%202025-05-06%20181147.png)  
* 공간 시각화  
    ![사진](/images/스크린샷%202025-05-06%20181333.png)  
    * 도트맵 : 데이터 개요 파악에는 유리하지만, 정확한 값은 X 
* 박스 플롯  
    ![사진](/images/스크린샷%202025-05-06%20181547.png)  
<br>
<br>

# 확인 문제

## 문제 1.
> **🧚 공분산과 상관계수의 차이점에 대해 간단히 설명하세요.**

```
공분산은 변수 간의 다른 척도기준이 그대로 반영되어 다른 공분산끼리 절대적으로 비교할 수 없지만, 상관계수는 공분산을 전체 변하는 정도로 나누어 절대적으로 비교할 수 있도록 설정한 지표이다. 
```

## 문제 2.
> **🧚 다음 데이터 분석 목표에 적합한 시각화 방법을 보기에서 모두 골라 연결해주세요.**

> 보기: 산점도, 선그래프, 막대그래프, 히스토그램, 박스플롯

(a) 변수의 분포 확인 
(b) 두 변수 간의 관계 확인   
(c) 집단별 평균 비교   
(d) 시계열 데이터 분석

<!--중복 가능-->

```
(a) : 막대그래프, 히스토그램, 박스플롯   
(b) : 산점도  
(c) : 박스플롯, 막대그래프  
-> 막대그래프가 표시하는 것을 평균으로 설정해서 비교 가능  
(d) : 선그래프      
-> 막대그래프는 범주형 변수, 히스토그램은 연속형 변수 
```


### 🎉 수고하셨습니다.