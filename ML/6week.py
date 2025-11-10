import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from matplotlib.lines import Line2D

# 1) 데이터 로드 (1797개 샘플, 8x8 = 64 features)
digits = load_digits()
X = digits.data          # shape: (n_samples, 64)
y = digits.target        # 0~9
target_names = digits.target_names if hasattr(digits, "target_names") else np.unique(y)

print("X shape:", X.shape)
print("y shape:", y.shape)
print("classes:", np.unique(y))

# 2) 데이터 스케일링: 픽셀값(0~16)의 영향이 크지 않지만, PCA 안정성을 위해 표준화 권장
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3) PCA 적용 및 데이터 변환 (주성분 2개)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
explained_var_ratio = pca.explained_variance_ratio_

# 분석 설명: 첫 2개의 주성분이 설명하는 분산 비율 출력
print("\n--- Explained Variance Ratio ---")
print(f'PC1: {explained_var_ratio[0]:.2%}')
print(f'PC2: {explained_var_ratio[1]:.2%}')
print(f'Total Explained Variance by PC1 & PC2: {explained_var_ratio.sum():.2%}')
print("--------------------------------")


# 4) 2D 산점도 시각화
plt.figure(figsize=(10, 8))
scatter = plt.scatter(
    X_pca[:, 0], X_pca[:, 1],
    c=y, s=30, alpha=0.7, edgecolors="k", cmap="tab10"
)

# 범례 설정
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label=str(i),
           markerfacecolor=scatter.to_rgba(i), markersize=8)
    for i in target_names
]
plt.legend(handles=legend_elements, title="Digit Class", loc="upper right")

# 축 레이블에 분산 설명력 포함
plt.xlabel(f"PC1 (주성분 1: {explained_var_ratio[0]*100:.2f}% 분산 설명)")
plt.ylabel(f"PC2 (주성분 2: {explained_var_2[1]*100:.2f}% 분산 설명)")
plt.title("Digits 데이터셋 PCA 시각화 (64차원 -> 2차원)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()


# 5) 누적 분산 곡선 (추가 분석)
pca_full = PCA().fit(X_scaled)
cumulative_variance = np.cumsum(pca_full.explained_variance_ratio_)
n_components = np.arange(1, len(cumulative_variance) + 1)

plt.figure(figsize=(10, 5))
plt.plot(n_components, cumulative_variance, marker='o', linestyle='-', color='indigo')

# 2개의 주성분이 설명하는 분산 지점 표시
plt.axvline(x=2, color='r', linestyle='--', linewidth=1.5, label='n_components = 2')
plt.axhline(y=cumulative_variance[1], color='r', linestyle='--', linewidth=1.5, label=f'{cumulative_variance[1]:.2%} Cumulative Var')
plt.text(2.5, cumulative_variance[1] - 0.03, f'{cumulative_variance[1]:.2%}', color='red', fontsize=10)


plt.xlabel("주성분 개수 (# of Principal Components)", fontsize=12)
plt.ylabel("누적 분산 설명력 (Cumulative Explained Variance)", fontsize=12)
plt.title("주성분 개수에 따른 누적 분산 설명력 곡선", fontsize=14)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()