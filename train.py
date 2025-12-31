import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load processed data
df = pd.read_csv('data/processed_iris.csv')
X_train = df.drop('target', axis=1)
y_train = df['target']

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model
with open('data/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print('Training completed')