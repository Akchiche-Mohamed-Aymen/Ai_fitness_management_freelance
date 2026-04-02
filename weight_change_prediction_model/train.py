from pandas import read_csv
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.utils.class_weight import compute_class_weight
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load cleaned data
data = read_csv('weightlifting_cleaned.csv')
#replace -2.5 with -2.0
data["delta_weight"] = data["delta_weight"].replace(-2.5, -2.0)
data["delta_weight"] = data["delta_weight"].replace(2.5, 2.0)

classes = data["delta_weight"].unique()

weights = compute_class_weight(
    class_weight="balanced",
    classes=classes,
    y=data["delta_weight"]
)
class_weights = dict(zip(classes, weights))

X , y = data.drop(columns=["delta_weight"]), data["delta_weight"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    stratify=y,
    test_size=0.2,
    random_state=42
)
model = RandomForestClassifier(class_weight=class_weights , random_state=42 , n_estimators=15)

# Cross-validation for first 3 metrics
accuracy_cv = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
precision_cv = cross_val_score(model, X_train, y_train, cv=5, scoring='precision_weighted')
recall_cv = cross_val_score(model, X_train, y_train, cv=5, scoring='recall_weighted')
print(f"Accuracy (CV): \n {accuracy_cv.mean():.4f}")
print(f"Precision (CV): \n {precision_cv.mean():.4f}") 
print(f"Recall (CV): \n {recall_cv.mean():.4f}")
# Train on full training data and evaluate F1 on test set
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
print(f"Accuracy (CV): {accuracy:.4f}")
print(f"Precision (CV): {precision:.4f}")
print(f"Recall (CV): {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

import os
import pickle

# Create the folder if it doesn't exist
os.makedirs('../models', exist_ok=True)

# Save the model
with open('../models/weight_change_model.pkl', 'wb') as f:
    pickle.dump(model, f)