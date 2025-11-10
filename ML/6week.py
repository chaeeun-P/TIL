# Week 6: PCA on scikit-learn digits (8x8 -> 2D)
# - 목표: 64차원 이미지를 PCA로 2차원 축소 후 산점도 시각화
# - 출력: 2D 산점도, PC1/PC2 분산 설명력(비율) 표시
# - 해석 포인트:
#   * PC1·PC2가 전체 분산의 몇 %를 설명하는지
#   * 2D 평면에서 각 숫자 클래스의 군집/중첩 정도

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1) 데이터 로드 (1797개 샘플, 8x8 = 64 features)
digits = load_digits()
X = digits.data          # shape: (n_samples, 64)
y = digits.target        # 0~9
target_names = digits.target_names if hasattr(digits, "target_names") else np.unique(y)

print("X shape:", X.shape)
print("y shape:", y.shape)
print("classes:", np.unique(y))

# 2) (선택) 스케일링: 픽셀값(0~16)이라 영향이 크지 않지만, PCA 안정성을 위해 표준화 권장
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3) PCA(주성분 2개)


# 4) 2D 산점도 시각화
plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    X_pca[:, 0], X_pca[:, 1],
    c=y, s=18, alpha=0.7, edgecolors="none", cmap="tab10"
)
plt.xlabel(f"PC1 ({explained_var_ratio[0]*100:.2f}% var)")
plt.ylabel(f"PC2 ({explained_var_ratio[1]*100:.2f}% var)")
plt.title("Digits PCA (n_components=2)")

# 범례: 0~9 클래스를 색상에 매핑


# 5) (선택) 누적 분산 곡선: 몇 개의 주성분이 얼마만큼 설명하는지

plt.xlabel("# of Principal Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("Cumulative Explained Variance by #PCs (Digits)")
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()

# --- 주피터 노트북에 서술 가이드 ---
# - PC1/PC2의 분산 설명력(%): 위 print 결과를 인용해, 2D가 원 데이터의 분산을 얼마나 담는지 서술
# - 산점도 해석: 클래스 간 분리 정도, 중첩되는 영역, 특이 클래스(예: 1과 7의 근접 등) 관찰
# - 유의점: PCA는 분류 목적이 아니라 최대 분산 방향을 찾는 선형 축소 → 분리 불완전 가능
#         고차원의 복잡한 구조를 단순화하여 시각적 통찰을 제공한다는 점을 강조