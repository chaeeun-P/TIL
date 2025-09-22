import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# 0) 데이터 불러오기
#    sklearn 내장 breast_cancer 데이터셋 사용
data = load_breast_cancer()
X, y = data.data, data.target # X: 특성, y: 타깃 (0=악성, 1=양성)

# 1) Train/Test 분할
#    랜덤 시드 고정(random_state=42) → 재현성 보장
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 2) 모델 학습
#    solver='liblinear'은 작은 데이터셋에서도 안정적으로 동작
model = LogisticRegression(max_iter=10000, solver='liblinear')
model.fit(X_train, y_train)

# 3) 예측
y_pred = model.predict(X_test)

# 4) 혼동 행렬 출력
cm = confusion_matrix(y_test, y_pred)
print("=== 혼동 행렬 (Confusion Matrix) ===")
print(cm)

# 5) 분류 리포트 출력 (정밀도, 재현율, F1-score 포함)
print("\n=== 분류 리포트 (Classification Report) ===")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# 6) (선택) 결과 해석
print("\n[결과 해석 가이드]")
print("- 혼동 행렬 해석:")
print("  - TN (True Negative): 실제 양성(0)인데 양성(0)으로 맞춤")
print("  - FP (False Positive): 실제 양성(0)인데 악성(1)으로 잘못 예측 -> 불필요한 검사 발생")
print("  - FN (False Negative): 실제 악성(1)인데 양성(0)으로 예측 -> 위험 요소")
print("  - TP (True Positive): 실제 악성(1)인데 악성(1)으로 맞춤")
print()
print("- 재현율(Recall) = TP / (TP + FN)")
print("  -> 실제 악성 환자 중 모델이 악성이라고 올바르게 예측한 비율")
print("  -> 의료 진단에서는 FN(악성인데 놓친 경우)을 최소화하는 것이 가장 중요함.")
print("  -> 따라서 재현율을 핵심 지표로 삼는 것이 타당함.")