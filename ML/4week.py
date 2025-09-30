import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 1. 데이터 불러오기 및 준비
# UCI Wine Quality 데이터: CSV 구분자가 ';' 입니다.
# 파일 경로를 설정합니다. (파일이 현재 폴더에 존재한다고 가정하고 로드합니다.)
PATH_RED    = "winequality-red.csv"
PATH_WHITE = "winequality-white.csv"

# 파일이 존재한다고 가정하고 데이터를 로드합니다.
red = pd.read_csv(PATH_RED, sep=';')
white = pd.read_csv(PATH_WHITE, sep=';')

# 1) 레이블 부여: red=0, white=1
red['target'] = 0
white['target'] = 1

# 2) 합치기 + 섞기
df = pd.concat([red, white], axis=0, ignore_index=True)
df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)


# 3) 특성/타깃 분리
# 오직 'target' 컬럼만 제외하고 모든 컬럼을 X에 포함 (baseline 코드와 동일)
X = df.drop(columns=['target'])
y = df['target']
feature_names = X.columns.tolist()

# 4) 학습/평가 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

print(f"총 샘플 수: {len(X)}")
print(f"학습 데이터 크기: {len(X_train)}")
print(f"테스트 데이터 크기: {len(X_test)}")
print("-" * 30)

# 5) 모델 학습
# 나무의 깊이를 제한하여 가독성을 높입니다. (max_depth=3)
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# 6) 트리 시각화
plt.figure(figsize=(25, 15))
plot_tree(
    clf,
    feature_names=feature_names,
    class_names=['Red (0)', 'White (1)'],
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("와인 타입 분류 결정 나무 (Decision Tree)")
plt.show() # Jupyter Notebook 환경에서 시각화 결과를 보여줍니다.

# 7) 상위 분기 규칙 해석을 위한 정보 추출
tree_ = clf.tree_

# 루트 노드 (Node 0)
root_feature_idx = tree_.feature[0]
root_threshold = tree_.threshold[0]

# 왼쪽 자식 노드 (Node 1) - 샘플 수가 많아 다음 핵심 분기가 일어날 확률이 높음
left_child_node_idx = tree_.children_left[0]
left_child_feature_idx = tree_.feature[left_child_node_idx]
left_child_threshold = tree_.threshold[left_child_node_idx]

# 오른쪽 자식 노드 (Node 2)
right_child_node_idx = tree_.children_right[0]
right_child_feature_idx = tree_.feature[right_child_node_idx]
right_child_threshold = tree_.threshold[right_child_node_idx]


# 와인 타입 분류의 상위 2개 분기 규칙 분석
print("=" * 50)
print("와인 타입 분류를 위한 상위 2개 분기 규칙 분석 결과")
print("=" * 50)

# 규칙 1: 루트 노드 (가장 중요한 분할)
rule_1_feature = feature_names[root_feature_idx]
rule_1_threshold = round(root_threshold, 4)
print(f"1. 루트 분할 규칙 (Rule 1): '{rule_1_feature}' <= {rule_1_threshold}")
print("   - 이 규칙은 전체 데이터를 레드와 화이트로 가장 크게 나누는 핵심 변수입니다.")

# 규칙 2: 다음 단계에서 가장 영향력이 큰 분할 (대부분의 샘플이 이동한 쪽)
# 'quality'가 포함되었으므로, 변수 중요도는 다시 학습됨.

# 임의의 자식 노드(왼쪽 자식)의 분기를 두 번째 규칙으로 채택
rule_2_feature = feature_names[left_child_feature_idx]
rule_2_threshold = round(left_child_threshold, 4)
print(f"2. 주요 자식 분할 규칙 (Rule 2): '{rule_2_feature}' <= {rule_2_threshold}")
print("   - Rule 1로 분리된 집단 내에서 와인 타입을 정교하게 구별하는 다음으로 중요한 규칙입니다.")
print("-" * 50)