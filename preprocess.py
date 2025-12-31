import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
import os

# Load data
df = pd.read_csv('cleaned_iris.csv')

# Features and target
X = df.drop('target', axis=1)
y = df['target']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save to data
os.makedirs('data', exist_ok=True)
with open('data/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X.columns)
X_train_scaled_df['target'] = y_train.values
X_train_scaled_df.to_csv('data/processed_iris.csv', index=False)

print('Preprocessing completed')