# Weather Prediction Project with Decision Trees
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score

# Part 1: Building the Decision Tree
data = pd.read_csv('C:/Users/user/Downloads/seattle-weather.csv')
#print(data)

df = pd.DataFrame(data)
print(df)

print(df.describe(include="all"))

# cleaning data
print(df.info())

# check for missing values
print(df.isna().sum())

# drop date column
df_updated = df.drop(columns=['date'])

# normalize numerical features
scaler = StandardScaler()
df_updated[['precipitation', 'temp_max', 'temp_min', 'wind']] = scaler.fit_transform(df_updated[['precipitation', 'temp_max', 'temp_min', 'wind']])

# encode categorical target variable
label_encoder = LabelEncoder()
df_updated['weather'] = label_encoder.fit_transform(df_updated['weather'])

# split into training and testing sets
X = df_updated.drop(columns=['weather'])
y = df_updated['weather']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the decision model
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# making predictions
y_pred = dt_model.predict(X_test)

# Part 2: Debugging Issues

# check for underfitting/overfitting
train_accuracy = accuracy_score(y_train, dt_model.predict(X_train))

print(f"Training Accuracy: {train_accuracy:.2f}")

# adjust hyperparameters: tree depth or sample size
adjusted_dt_model = DecisionTreeClassifier(max_depth=5, min_samples_split=10, random_state=42)
adjusted_dt_model.fit(X_train, y_train)

# making predictions with new model
adjusted_y_pred = adjusted_dt_model.predict(X_test)

adjusted_train_accuracy = accuracy_score(y_train, dt_model.predict(X_train))

print(f"Adjusted Training Accuracy: {adjusted_train_accuracy:.2f}")

# Part 3: Evaluating the Model

# regular predictions
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)
print("Classification Report:")
print(report)

# accuracy, precision, recall score, confusion matrix
test_accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Test Accuracy: {test_accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(conf_matrix)


# adjusted predictions
adjusted_report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)
print("Adjusted Classification Report:")
print(adjusted_report)

# adjusted accuracy, precision, recall score, confusion matrix
adjusted_test_accuracy = accuracy_score(y_test, adjusted_y_pred)
adjusted_precision = precision_score(y_test, adjusted_y_pred, average='weighted')
adjusted_recall = recall_score(y_test, adjusted_y_pred, average='weighted')
adjusted_conf_matrix = confusion_matrix(y_test, adjusted_y_pred)

print(f"Adjusted Test Accuracy: {test_accuracy:.2f}")
print(f"Adjusted Precision: {precision:.2f}")
print(f"Adjusted Recall: {recall:.2f}")
print(adjusted_conf_matrix)