from datasets import load_dataset
from transformers import AutoTokenizer

# Load a sample dataset (IMDb reviews)
dataset = load_dataset("imdb")

# Load a pre-trained tokenizer (DistilBERT)
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# Define a preprocessing function
def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)

# Apply the preprocessing function to the dataset
tokenized_dataset = dataset.map(preprocess_function, batched=True)

from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments

# Load a pre-trained model for sentiment analysis (DistilBERT)
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
)

# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
)

# Train the model
trainer.train()

import numpy as np
from datasets import load_metric
from sklearn.metrics import accuracy_score, classification_report

# Evaluate model performance
eval_results = trainer.evaluate()

# Extract predictions and labels
predictions = trainer.predict(tokenized_dataset["test"])
preds = np.argmax(predictions.predictions, axis=1)  # Convert logits to labels
labels = predictions.label_ids  # True labels

# Compute accuracy
accuracy = accuracy_score(labels, preds)

# Display evaluation results
print(f"Model Evaluation Metrics:")
print(f"Accuracy: {accuracy:.4f}")

# Print a detailed classification report
report = classification_report(labels, preds, target_names=["Negative", "Positive"])
print(report)
