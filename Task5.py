import sys
sys.stdout.reconfigure(encoding='utf-8')


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (8, 5)


train_df = pd.read_csv('train.csv')

print("🔹 Dataset Info:\n")
print(train_df.info())
print("\n🔹 First 5 rows:\n")
print(train_df.head())
print("\n🔹 Summary Statistics:\n")
print(train_df.describe())
print("\n🔹 Missing Values:\n")
print(train_df.isnull().sum())


train_df['Age'].fillna(train_df['Age'].median(), inplace=True)  # Fill missing age with median
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)  # Fill missing embarked with mode

print("\n🔹 Missing Values After Handling:\n")
print(train_df.isnull().sum())


categorical_features = ['Sex', 'Embarked', 'Pclass', 'Survived']
for feature in categorical_features:
    print(f"\n🔹 Value counts for {feature}:\n")
    print(train_df[feature].value_counts())

numeric_features = ['Age', 'Fare', 'SibSp', 'Parch']

for feature in numeric_features:
    plt.figure(figsize=(8, 5))
    sns.histplot(train_df[feature].dropna(), kde=True, color='teal', edgecolor='black', bins=30)
    plt.xlabel(f'{feature}', fontsize=12)
    plt.ylabel('Number of Passengers', fontsize=12)
    plt.title(f'Distribution of {feature}', fontsize=14)
    plt.grid(True)
    plt.show()

    print(f"📌 Observation for {feature}:")
    if feature == 'Age':
        print("- Age distribution is slightly right-skewed. Most passengers are between 20 and 40 years old.\n")
    elif feature == 'Fare':
        print("- Fare distribution is heavily right-skewed with many low fares and some very high outliers.\n")
    elif feature == 'SibSp':
        print("- Most passengers traveled alone (0 siblings/spouse) or with one companion.\n")
    elif feature == 'Parch':
        print("- Majority of passengers had no parents/children with them.\n")


numeric_df = train_df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_df.corr()


plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt=".2f")
plt.title('Correlation Heatmap between Features', fontsize=16)
plt.show()

print("📌 Observation from Heatmap:")
print("- Fare and Pclass are moderately negatively correlated (-0.55). Higher class had lower fare.")
print("- Age and Parch have slight positive correlation (older passengers traveled with children/parents).")
print("- SibSp and Parch are somewhat related (families traveling together).")
print("- Survived is positively correlated with Fare and Parch slightly.\n")


selected_features = ['Survived', 'Pclass', 'Age', 'Fare', 'SibSp', 'Parch']
sns.pairplot(train_df[selected_features], hue='Survived', palette='Set1', diag_kind='kde')
plt.suptitle('Pairplot of Selected Features', y=1.02)
plt.show()

print("📌 Observation from Pairplot:")
print("- Survived passengers are concentrated at lower Pclass (1st class) and younger ages.")
print("- Higher Fare values are more common among survivors.")
print("- Most passengers have 0 SibSp and 0 Parch.\n")


for feature in categorical_features:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=train_df, x=feature, palette='pastel')
    plt.title(f'Countplot of {feature}', fontsize=14)
    plt.xlabel(f'{feature}', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.grid(axis='y')
    plt.show()

    print(f"📌 Observation for {feature}:")
    if feature == 'Sex':
        print("- More males (577) than females (314) on board.\n")
    elif feature == 'Embarked':
        print("- Most passengers embarked from port 'S' (Southampton).\n")
    elif feature == 'Pclass':
        print("- Majority of passengers belonged to 3rd class.\n")
    elif feature == 'Survived':
        print("- Around 62% passengers did not survive.\n")


print("\n🎯 Overall Summary of Findings:")
print("- Younger passengers and females had higher survival rates.")
print("- Passengers in 1st class had better chances of survival.")
print("- Higher fare indicates higher survival probability.")
print("- Most passengers embarked from Southampton (S).")
print("- Many passengers traveled alone without siblings/parents.")
print("- Age and Fare distributions are right-skewed.")
print("- Correlation between features indicates relationships between them.")
