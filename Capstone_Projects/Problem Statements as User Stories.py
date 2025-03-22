# User Story 1: Personalized Chatbot for Customer Service 

# As a business owner, I want to create a personalized chatbot that can assist customers with frequently asked questions (FAQs) so that I can provide quick responses and improve customer satisfaction.  
# Solution: Use a pre-trained LLM like GPT and fine-tune it with customer interaction data to generate accurate and contextually relevant responses. 
# User Story 2: Summarization for Research Papers 

# As a researcher, I want an AI tool that can summarize lengthy research papers, allowing me to quickly grasp key findings and save time on reading, so that I can focus on analysis.  
# Solution: Use prompt engineering to guide an LLM to extract summaries from research papers, tuning the model for better accuracy and relevance. 
#  User Story 3: Text-Based Sentiment Analysis for Social Media Monitoring 

# As a social media manager, I want to analyse customer sentiment based on user comments on social platforms so that I can adjust marketing strategies accordingly.  
# Solution: Fine-tune an LLM to classify sentiment in social media posts and optimize prompt design to enhance sentiment classification accuracy. 
#  Implementation Plan 

#  Phase 1: Data Collection & Preparation 

# Task 1: Gather customer service interaction data, research papers, and social media posts for training and fine-tuning. 
# Task 2: Preprocess data to align with the input format for tokenization and embedding.

import pandas as pd
from datasets import Dataset

# Load sample dataset (Replace with actual dataset)
df = pd.read_csv("C:\Users\user\Downloads\IMDB Dataset.csv\IMDB Dataset.csv")

# Standardize labels (e.g., positive = 1, negative = 0, neutral = 2)
label_map = {"positive": 1, "negative": 0, "neutral": 2}
df['label'] = df['label'].map(label_map)

# Convert to Hugging Face Dataset format
dataset = Dataset.from_pandas(df)

# Save cleaned dataset
df.to_csv("cleaned_imdb.csv", index=False)

# Phase 2: Model Development 

# Task 1: Fine-tune an existing LLM (e.g., GPT) on your domain-specific data (e.g., customer service chats, research papers). 
# Task 2: Develop a custom prompt engineering strategy to guide the model's output for each use case (e.g., summarization, sentiment analysis). 
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
from datasets import load_dataset

# Load dataset
dataset = load_dataset("csv", data_files="cleaned_imdb.csv")

# Load tokenizer
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Tokenize dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Split into train/test sets
train_test_split = tokenized_dataset["train"].train_test_split(test_size=0.2)
train_dataset = train_test_split["train"]
test_dataset = train_test_split["test"]

# Load model with sentiment classification head
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
)

# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Train the model
trainer.train()

# Save fine-tuned model
model.save_pretrained("./fine_tuned_sentiment_model")
tokenizer.save_pretrained("./fine_tuned_sentiment_model")

# Phase 3: Model Evaluation and Tuning 

# Task 1: Evaluate the model’s performance on unseen data (testing data) using appropriate metrics like accuracy, precision, recall, etc. 
# Task 2: Fine-tune the model further based on evaluation results. 
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import numpy as np

# Define evaluation function
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    preds = np.argmax(predictions, axis=1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average="weighted")
    acc = accuracy_score(labels, preds)
    
    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }

# Run evaluation
eval_results = trainer.evaluate()
print(eval_results)

# Phase 4: Application Development 

# Task 1: Build a simple web-based application or tool where users can input text and receive model predictions. 
# Task 2: Integrate the LLM into the application to provide responses or summaries based on prompts. 
import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load fine-tuned sentiment analysis model
model_path = "./fine_tuned_sentiment_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Label map
label_map = {0: "Negative", 1: "Positive", 2: "Neutral"}

# Streamlit UI
st.title("Sentiment Analysis for Social Media")
st.subheader("Enter a social media post to analyze sentiment!")

# User input
user_input = st.text_area("Type a tweet or comment here...")

if st.button("Analyze Sentiment"):
    if user_input:
        # Tokenize input
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)

        # Predict sentiment
        with torch.no_grad():
            outputs = model(**inputs)
            prediction = torch.argmax(outputs.logits, dim=1).item()
        
        sentiment = label_map[prediction]
        
        # Display result
        st.success(f"Predicted Sentiment: **{sentiment}**")
    else:
        st.warning("Please enter a comment or tweet.")

# Phase 5: Testing and Deployment 

# Task 1: Conduct usability testing with real users to ensure the system meets the needs of customers, researchers, or social media managers. 
# Task 2: Deploy the application for production use, ensuring it can scale to handle multiple users.
# Learning Outcomes 
