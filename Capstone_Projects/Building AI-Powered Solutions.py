# User Story 2: Clustering for Student Grouping 

# As a teacher, I want to group students into different categories based on their learning styles so that I can tailor my teaching methods to each group. 

# Solution: Apply K-means clustering to student performance data to identify different learning groups (e.g., fast learners, struggling students). 

# Implementation Plan 
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib


# Phase 1: Data Collection & Preparation 
# Gather data for student performance, study habits, and exam results. 
# Collect image data for training the GAN. 
def load_and_preprocess_student_data(file_path):
    df = pd.read_csv(file_path)
    features = ["exam_score", "study_hours", "attendance_rate", "homework_completion"]
    df = df[features]
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    return df, df_scaled, scaler

file_path = "C:/Users/user/Downloads/student_data.csv"  # Update with actual dataset path
df, df_scaled, scaler = load_and_preprocess_student_data(file_path)

# Phase 2: Model Development 
# Develop the supervised learning model to predict exam performance. 
# Implement the K-means clustering algorithm to group students. 
# Train the GAN model on existing artwork for generation tasks. 
def train_exam_performance_model(df):
    X = df.drop(columns=["exam_score"])
    y = df["exam_score"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model, X_test, y_test

exam_model, X_test, y_test = train_exam_performance_model(df)


def apply_kmeans_clustering(df_scaled, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(df_scaled)
    return kmeans, clusters

kmeans_model, clusters = apply_kmeans_clustering(df_scaled)

# Phase 3: Model Evaluation and Tuning 
# Evaluate the classification model and clustering output. 
# Fine-tune hyperparameters to improve accuracy. 
def evaluate_kmeans(df_scaled, kmeans_model):
    return silhouette_score(df_scaled, kmeans_model.labels_)

silhouette_score_value = evaluate_kmeans(df_scaled, kmeans_model)

# Phase 4: Application Development 
# Integrate models into an interactive Python application. 
# Create a simple interface for students, teachers, and digital artists to interact with the system. 
st.title("Student Clustering & Exam Performance Prediction")

# Display student clusters
st.subheader("K-Means Clustering Results")
st.write(f"Silhouette Score: {silhouette_score_value:.2f}")

# User input for predicting exam performance
st.subheader("Predict Exam Performance")
st.write("Enter student details to predict exam score:")
study_hours = st.number_input("Study Hours", min_value=0, max_value=10, value=5)
attendance_rate = st.number_input("Attendance Rate (%)", min_value=0, max_value=100, value=80)
homework_completion = st.number_input("Homework Completion (%)", min_value=0, max_value=100, value=90)

if st.button("Predict Score"):
    student_input = np.array([[study_hours, attendance_rate, homework_completion]])
    student_input_scaled = scaler.transform(student_input)
    predicted_score = exam_model.predict(student_input_scaled)[0]
    st.write(f"Predicted Exam Score: {predicted_score:.2f}")

# Cluster visualization
st.subheader("Cluster Visualization")
fig, ax = plt.subplots()
sns.scatterplot(x=df["study_hours"], y=df["exam_score"], hue=clusters, palette="viridis", ax=ax)
ax.set_xlabel("Study Hours")
ax.set_ylabel("Exam Score")
st.pyplot(fig)

st.write("Application ready for teachers and students to interact with clustering and predictions.")

# Phase 5: Testing and Deployment 
# Test the system with real data to ensure predictions and grouping are accurate. 
# Deploy the application for use by students and teachers. 
# Save models for deployment
joblib.dump(exam_model, "exam_performance_model.pkl")
joblib.dump(kmeans_model, "kmeans_clustering_model.pkl")
joblib.dump(scaler, "scaler.pkl")

st.write("Models saved for deployment. Application is now ready for real-world testing with student data.")