import torch
import transformers
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
from sklearn.metrics import accuracy_score, f1_score

# Part 1: Fine-Tuning BERT

# Load dataset (Example: Classifying customer reviews as positive or negative)
dataset = load_dataset("yelp_polarity")

# Load tokenizer
tokenizer = BertTokenizer.from_pretrained("distilbert-base-uncased")

def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)

# Tokenize dataset
tokenized_datasets = dataset.map(preprocess_function, batched=True)

# Load pre-trained BERT variant
model = BertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

# Part 2: Debugging Issues

# Adjust training arguments to avoid overfitting or long training times
training_args = TrainingArguments(
    output_dir="./bert_finetuned",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,  # Adjusted learning rate for improved generalization
    per_device_train_batch_size=8,  # Increased batch size for better performance
    per_device_eval_batch_size=8,
    num_train_epochs=5,  # Fine-tune for more epochs
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=500,
    save_total_limit=3,
    gradient_accumulation_steps=2,  # Helps with memory optimization
    fp16=True,  # Mixed precision training for efficiency
    load_best_model_at_end=True,  # Save best model based on evaluation metric
    metric_for_best_model="accuracy"
)

# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    tokenizer=tokenizer
)

# Fine-tune the model with debugging fixes
trainer.train()

# Save the refined model
# model.save_pretrained("./bert_finetuned")
# tokenizer.save_pretrained("./bert_finetuned")

print("Fine-tuning complete. Model saved.")

# Part 3: Evaluating the Model

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    accuracy = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds, average="weighted")
    return {"accuracy": accuracy, "f1_score": f1}

# Evaluate on test dataset
eval_results = trainer.evaluate()
print("Evaluation Results:", eval_results)

# Run predictions on test data
def predict_on_test():
    test_texts = [
        "The service at this restaurant was amazing!",
        "I had a terrible experience, would not recommend."
    ]
    inputs = tokenizer(test_texts, padding=True, truncation=True, max_length=512, return_tensors="pt")
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    print("Predictions:", predictions.tolist())

predict_on_test()

print("Evaluation complete.")

# Part 4: Creative Application
# Applying the model to classify customer reviews

def classify_review(review_text):
    """Classifies a customer review as positive or negative."""
    inputs = tokenizer([review_text], padding=True, truncation=True, max_length=512, return_tensors="pt")
    outputs = model(**inputs)
    prediction = torch.argmax(torch.nn.functional.softmax(outputs.logits, dim=-1), dim=1).item()
    label = "Positive" if prediction == 1 else "Negative"
    return label

# Test with new customer reviews
new_reviews = [
    "Absolutely love this place, will visit again!",
    "The food was cold and the service was rude."
]

for review in new_reviews:
    print(f"Review: {review}\nPrediction: {classify_review(review)}\n")

print("Real-world application complete.")
