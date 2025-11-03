import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, make_scorer

# 1) 데이터 불러오기 및 전처리 (4주차와 동일)
# NOTE: 사용자 환경에 따라 파일 경로를 조정해야 할 수 있습니다.
PATH_RED   = "winequality-red.csv"      # UCI 데이터, 구분자 ';'
PATH_WHITE = "winequality-white.csv"

try:
    red    = pd.read_csv(PATH_RED, sep=';')
    white = pd.read_csv(PATH_WHITE, sep=';')
except FileNotFoundError:
    print("경로에 'winequality-red.csv' 또는 'winequality-white.csv' 파일이 없습니다. 파일을 준비해 주세요.")
    exit()

# 레이블: red=0, white=1
red['target'] = 0
white['target'] = 1

# 합치고 섞기
df = pd.concat([red, white], axis=0, ignore_index=True)
df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)

# 특성/타깃 분리
X = df.drop(columns=['target'])
y = df['target']

# 학습/평가 분할 (동일 분할 유지)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# 2) 실험 준비
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scorers = {
    'acc': make_scorer(accuracy_score),
    'f1m': make_scorer(f1_score, average='macro'),
}
# 이진 분류이므로 multi_class='ovr' 없이 roc_auc_score 사용
try:
    scorers['auc'] = make_scorer(roc_auc_score, needs_proba=True)
except Exception:
    pass

grid_ne = [100, 2000]
grid_mf = ['sqrt', 'log2', None, 0.5] # None은 max_features=n_features와 동일 (sklearn 1.2+ 버전에서는 'sqrt'가 기본)

results = []
feat_imp_by_setting = {}  # 조합별 평균 feature_importances_ 저장

# 3) 8개 조합 교차검증
print("=== 랜덤 포레스트 8개 조합 교차검증 시작 ===")
for ne in grid_ne:
    for mf in grid_mf:
        mf_param = X_train.shape[1] if mf is None else mf # None 처리
        
        rf = RandomForestClassifier(
            n_estimators=ne,
            max_features=mf,
            random_state=42,
            n_jobs=-1
        )
        t0 = time.time()
        out = cross_validate(
            rf, X_train, y_train,
            scoring=scorers, cv=cv, n_jobs=-1,
            return_estimator=True
        )
        
        fit_time = out['fit_time'].mean()
        scores = {m: out[f'test_{m}'].mean() for m in scorers}

        # 각 fold의 feature_importances_ 평균 계산 (일반화된 중요도)
        importances = np.mean([est.feature_importances_ for est in out['estimator']], axis=0)
        feat_imp_by_setting[(ne, mf)] = importances

        results.append({
            'n_estimators': ne,
            'max_features': str(mf),
            'acc': scores.get('acc', np.nan),
            'f1m': scores.get('f1m', np.nan),
            'auc': scores.get('auc', np.nan),
            'cv_fit_time_sec': fit_time,
        })
        print(f"  > NE={ne}, MF={mf}: F1m={scores.get('f1m', np.nan):.4f}, Time={fit_time:.2f}s")

# 결과표 정리 (F1-macro 우선 정렬)
df_res = pd.DataFrame(results).sort_values(['f1m','acc'], ascending=False).reset_index(drop=True)
print("\n=== 8개 조합 결과표 (교차검증 평균) ===")
print(df_res.to_markdown(index=False, floatfmt=".4f"))


# 4) 최고 조합 선택 및 최종 분석
best_row = df_res.iloc[0]
best_ne = int(best_row['n_estimators'])
best_mf = best_row['max_features'] # 문자열 'None' 또는 'sqrt' 등

print(f"\n[선정된 최고 조합] n_estimators={best_ne}, max_features={best_mf}")

# 5) 중요 변수 해석 (Top-10 및 시각화)
best_imp = feat_imp_by_setting[(best_ne, best_mf if best_mf != 'None' else None)]
feat_names = X.columns.to_list()

top_k = 10
idx_sorted = np.argsort(best_imp)[::-1][:top_k]

# 중요 변수 Top-10 출력
print("\n=== 중요 변수 Top-10 (교차검증 평균 기반) ===")
top_importances = pd.DataFrame({
    'Feature': [feat_names[i] for i in idx_sorted],
    'Importance': best_imp[idx_sorted]
})
print(top_importances.to_markdown(index=False, floatfmt=".4f"))

# 시각화 (막대 그래프)
plt.figure(figsize=(10, 6))
plt.bar(top_importances['Feature'], top_importances['Importance'], color='skyblue')
plt.xlabel("와인 특성 변수", fontsize=12)
plt.ylabel("변수 중요도 (Feature Importance)", fontsize=12)
plt.title(f"최적 RandomForest 모델의 변수 중요도 (Top {top_k})\n(NE={best_ne}, MF={best_mf})", fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 6) 해석을 위한 정보 저장 (이후 Markdown 보고서에 사용)
top3_features = top_importances.head(3)