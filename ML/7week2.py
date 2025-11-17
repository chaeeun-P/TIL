import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

y_train_original = df_train['Survived']
df_all = pd.concat([df_train.drop('Survived', axis=1), df_test], ignore_index=True)

df_all['Fare'] = df_all['Fare'].fillna(df_all['Fare'].median())
df_all['Embarked'] = df_all['Embarked'].fillna(df_all['Embarked'].mode()[0])

df_all['Title'] = df_all['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
rare_titles = ['Lady', 'Countess','Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona']
df_all['Title'] = df_all['Title'].replace(['Mlle', 'Ms'], 'Miss')
df_all['Title'] = df_all['Title'].replace('Mme', 'Mrs')
df_all['Title'] = df_all['Title'].replace(rare_titles, 'Rare')

df_all['Deck'] = df_all['Cabin'].str[0].fillna('Missing')

df_all['Age'] = df_all.groupby('Title')['Age'].transform(lambda x: x.fillna(x.median()))

df_all = df_all.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1)

categorical_features = ['Pclass', 'Sex', 'Embarked', 'Title', 'Deck']
df_all = pd.get_dummies(df_all, columns=categorical_features, drop_first=True)

X_processed_train = df_all.iloc[:len(df_train)]
X_train_split, X_val, y_train_split, y_val = train_test_split(
    X_processed_train, y_train_original, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_split)
X_val_scaled = scaler.transform(X_val)

models = {
    "Logistic Regression": LogisticRegression(solver='liblinear', random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42, n_estimators=100)
}
results = {}

print("--- 모델별 학습 및 예측 결과 ---")
for name, model in models.items():
    model.fit(X_train_scaled, y_train_split)
    y_pred = model.predict(X_val_scaled)
    accuracy = accuracy_score(y_val, y_pred)
    results[name] = accuracy
    print(f"{name} Accuracy: {accuracy:.4f}")

df_results = pd.DataFrame(results.items(), columns=['Model', 'Accuracy']).sort_values(by='Accuracy', ascending=False)
plt.figure(figsize=(10, 6))
bars = plt.bar(df_results['Model'], df_results['Accuracy'], color=['skyblue', 'lightcoral', 'lightgreen'])
plt.ylabel('Accuracy')
plt.title('Model Performance Comparison (Baseline)')
plt.ylim(0.7, 0.9)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.005, f'{yval:.4f}', ha='center', va='bottom')
plt.show()

X_scaled_full = scaler.fit_transform(X_processed_train)
pca = PCA(n_components=0.9)
X_pca = pca.fit_transform(X_scaled_full)
n_components = X_pca.shape[1]

X_pca_train, X_pca_val, y_pca_train, y_pca_val = train_test_split(
    X_pca, y_train_original, test_size=0.2, random_state=42
)

pca_models = {
    "LogReg (PCA)": LogisticRegression(solver='liblinear', random_state=42),
    "RandForest (PCA)": RandomForestClassifier(random_state=42, n_estimators=100)
}
print(f"\n--- PCA 분석: {X_processed_train.shape[1]}개 특성 -> {n_components}개 주성분으로 축소 ---")

for name, model in pca_models.items():
    model.fit(X_pca_train, y_pca_train)
    y_pred = model.predict(X_pca_val)
    accuracy = accuracy_score(y_pca_val, y_pred)
    print(f"{name} Accuracy: {accuracy:.4f}")

k_clusters = 3
kmeans = KMeans(n_clusters=k_clusters, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_scaled_full)

df_clustered = pd.DataFrame(X_scaled_full, columns=X_processed_train.columns)
df_clustered['Cluster'] = cluster_labels
df_clustered['Survived'] = y_train_original

cluster_survival_rate = df_clustered.groupby('Cluster')['Survived'].agg(['count', 'mean']).rename(columns={'count': 'Count', 'mean': 'Survival Rate'})
print("\n--- K-Means Cluster Analysis (k=3) ---")
print(cluster_survival_rate)
print(f"가장 높은 생존율 클러스터: Cluster {cluster_survival_rate['Survival Rate'].idxmax()}")

pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X_scaled_full)

df_pca = pd.DataFrame(data=X_pca_2d, columns=['PC1', 'PC2'])
df_pca['Cluster'] = cluster_labels
df_pca['Survived'] = y_train_original

plt.figure(figsize=(10, 8))
scatter = plt.scatter(df_pca['PC1'], df_pca['PC2'], c=df_pca['Cluster'], cmap='viridis', s=100, alpha=0.8, edgecolor='k')

for cluster_id in range(k_clusters):
    subset = df_pca[df_pca['Cluster'] == cluster_id]
    plt.scatter(
        subset[subset['Survived'] == 0]['PC1'],
        subset[subset['Survived'] == 0]['PC2'],
        marker='x',
        s=50,
        c=scatter.to_rgba(cluster_id),
        label=f'Cluster {cluster_id} (Died)'
    )
    plt.scatter(
        subset[subset['Survived'] == 1]['PC1'],
        subset[subset['Survived'] == 1]['PC2'],
        marker='o',
        s=50,
        c=scatter.to_rgba(cluster_id),
        label=f'Cluster {cluster_id} (Survived)'
    )

plt.title('K-Means Clusters (k=3) Projected onto 2 PCA Components')
plt.xlabel(f'Principal Component 1 ({pca_2d.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'Principal Component 2 ({pca_2d.explained_variance_ratio_[1]*100:.1f}%)')
plt.legend(handles=scatter.legend_elements()[0], title="K-Means Cluster")
plt.show()