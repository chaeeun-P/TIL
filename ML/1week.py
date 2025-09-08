# 1. 데이터 로딩 (OpenML에서 Boston 데이터셋 불러오기)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.datasets import fetch_openml

boston = fetch_openml(name="boston", version=1, as_frame=True)
df = boston.frame
X = df.drop(columns=["MEDV"])
y = df["MEDV"]
feature_names = X.columns

print("데이터 형태:", X.shape, y.shape)
print("\n데이터 미리보기:")
print(df.head())

# ===========================================================
# 2. 간단 EDA
# ===========================================================
print("\n결측치 확인:")
print(X.isna().sum())

print("\n기본 통계량:")
print(X.describe())

print("\nMEDV(target) 분포 시각화:")
plt.hist(y, bins=30, edgecolor='k')
plt.title("MEDV Distribution")
plt.xlabel("MEDV (Median value of owner-occupied homes in $1000s)")
plt.ylabel("Frequency")
plt.show()

# ===========================================================
# 3. 선형회귀 모델 학습
# ===========================================================
# StandardScaler와 LinearRegression을 Pipeline으로 묶어서 사용
model = make_pipeline(StandardScaler(), LinearRegression())
model.fit(X, y)
print("\n모델 학습 완료")

# ===========================================================
# 4. 회귀계수 확인
# ===========================================================
# Pipeline에서 LinearRegression의 계수(coefficients) 가져오기
coefs = model.named_steps["linearregression"].coef_

# feature와 coef 묶어서 DataFrame으로 정리
coef_df = pd.DataFrame({
    'feature': feature_names,
    'coefficient': coefs
})

# 절댓값이 큰 순서대로 정렬
coef_df['abs_coef'] = np.abs(coef_df['coefficient'])
coef_df_sorted = coef_df.sort_values(by='abs_coef', ascending=False)
print("\n절댓값 기준 회귀계수 정렬:")
print(coef_df_sorted)

# ===========================================================
# 5. 긍정적/부정적 영향 확인
# ===========================================================
# 회귀 계수 가장 큰(긍정적) 특성
most_positive_feature = coef_df_sorted.iloc[0]['feature']
most_positive_coef = coef_df_sorted.iloc[0]['coefficient']
print(f"\n가격 상승에 가장 큰 긍정적 영향: {most_positive_feature} (계수: {most_positive_coef:.4f})")

# 회귀 계수 가장 작은(부정적) 특성
most_negative_feature = coef_df_sorted.iloc[-1]['feature']
most_negative_coef = coef_df_sorted.iloc[-1]['coefficient']
print(f"가격 하락에 가장 큰 부정적 영향: {most_negative_feature} (계수: {most_negative_coef:.4f})")

# ===========================================================
# 6. 시각화
# ===========================================================
plt.figure(figsize=(12, 6))
plt.bar(coef_df_sorted['feature'], coef_df_sorted['coefficient'])
plt.axhline(0, color='red', linewidth=0.8, linestyle='--')
plt.title("Feature Coefficients from Linear Regression")
plt.xlabel("Features")
plt.ylabel("Standardized Coefficient Value")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ===========================================================
# 7. 추가 분석 (선택) - R^2, RMSE 계산
# ===========================================================
from sklearn.metrics import r2_score, mean_squared_error

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(f"\n모델 성능:")
print(f"R-squared: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")