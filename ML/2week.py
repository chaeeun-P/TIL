import numpy as np
import pandas as pd
import statsmodels.api as sm

# 1. `statsmodels`를 사용한 회귀모델 생성

# 전제: X와 y 변수가 이미 준비되어 있다고 가정
# X: 독립 변수(features) DataFrame
# y: 종속 변수(target) Series 또는 ndarray

# 안전장치: y를 1차원으로 변환
y = np.asarray(y).ravel()

# X 변수에 상수항 추가 (sm.add_constant)
X_const = sm.add_constant(X)

# OLS(최소제곱법) 모델 적합
# sm.OLS(종속변수, 독립변수).fit()
model = sm.OLS(y, X_const)
result = model.fit()


# 2. 리포트 출력 및 해석

print(result.summary())

# ----- 요약 리포트 해석 가이드 -----

print("\n[리포트 핵심 항목 해석]")

# 각 변수의 p-value (P>|t| 열)
print("1. p-value (P>|t|):")
print("- 유의수준(일반적으로 0.05)보다 작은 변수는 통계적으로 유의미합니다.")
print("- 이는 해당 변수가 종속변수를 예측하는 데 의미 있는 영향을 미친다는 것을 의미합니다.")

# R-squared (결정계수)
print("\n2. R-squared (결정계수):")
print(f"- 값: {result.rsquared:.4f}")
print("- 모델이 종속 변수(y)의 분산을 얼마나 설명하는지 나타냅니다.")
print("- 0과 1 사이의 값으로, 1에 가까울수록 모델이 데이터를 잘 설명합니다.")

# Adj. R-squared (수정 결정계수)
print("\n3. Adj. R-squared (수정 결정계수):")
print(f"- 값: {result.rsquared_adj:.4f}")
print("- 독립 변수의 개수를 고려하여 R-squared를 보정한 값입니다.")
print("- 불필요한 변수가 추가되면 값이 감소할 수 있어, 여러 모델을 비교할 때 더 신뢰할 수 있는 지표입니다.")

# 추가적으로 pandas DataFrame으로 정리하여 유의미한 변수 확인
summary_df = pd.DataFrame({
    "coef": result.params,
    "p_value": result.pvalues,
    "R-squared": result.rsquared,
    "Adj. R-squared": result.rsquared_adj
})

# p-value 기준 유의미 변수 확인
alpha = 0.05
summary_df["significant"] = summary_df["p_value"] < alpha

print("\n--- 각 변수의 통계적 유의성 ---")
print(summary_df.drop(index="const", errors="ignore"))