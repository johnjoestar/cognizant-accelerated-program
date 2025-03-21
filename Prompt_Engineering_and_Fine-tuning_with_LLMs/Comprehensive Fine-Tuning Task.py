import pandas as pd
import random

categories = [
    "Technical Issue",
    "Billing",
    "General Inquiry",
    "Account Access",
    "Cancellation Request",
    "Product Feedback"
]

# Sample queries for each category
samples = {
    "Technical Issue": [
        "the app crashes every time i try to open it",
        "i can't upload my files to the cloud",
        "the website keeps freezing on the login page",
        "my screen goes black when i launch the app",
        "i get a 404 error when clicking on dashboard",
    ],
    "Billing": [
        "i was charged twice this month",
        "how can i get a refund?",
        "my invoice is incorrect",
        "i need a receipt for last month's payment",
        "can i change my billing date?"
    ],
    "General Inquiry": [
        "what does the premium plan include?",
        "is there a student discount available?",
        "how do i update my profile picture?",
        "do you offer support on weekends?",
        "can i use the app on multiple devices?"
    ],
    "Account Access": [
        "i forgot my password",
        "how can i change my email address?",
        "my account was locked",
        "i can’t receive the verification code",
        "how do i enable two-factor authentication?"
    ],
    "Cancellation Request": [
        "i want to cancel my subscription",
        "please terminate my account",
        "how do i opt out of auto-renewal?",
        "cancel my free trial immediately",
        "i no longer need the service"
    ],
    "Product Feedback": [
        "i love the new interface!",
        "it would be great to have a dark mode",
        "please add more export options",
        "i wish the app loaded faster",
        "the recent update improved performance a lot"
    ]
}

# Generate 35 examples per category by repeating and varying slightly
data = []
for label in categories:
    base_samples = samples[label]
    for i in range(35):
        sample = random.choice(base_samples)
        data.append({"text": sample, "label": label})

# Convert to DataFrame and shuffle
df = pd.DataFrame(data)
df = df.sample(frac=1).reset_index(drop=True)

# Display a portion of the dataset
import ace_tools as tools; 
tools.display_dataframe_to_user(name="Customer Support Classification Dataset", dataframe=df)

from transformers import AutoModelForSequenceClassification, AutoTokenizer
model_name = "distilbert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
tokenizer = AutoTokenizer.from_pretrained(model_name)

from datasets import load_dataset
dataset = load_dataset("Customer Support Classification Dataset")
def preprocess_function(examples):
    return tokenizer(examples['text'], truncation=True, padding=True)
tokenized_dataset = dataset.map(preprocess_function, batched=True)

from transformers import Trainer, TrainingArguments
training_args = TrainingArguments(
output_dir="./results", eval_strategy="epoch",
learning_rate=2e-5, per_device_train_batch_size=16,
num_train_epochs=3, weight_decay=0.01,
)
trainer = Trainer(
model=model, args=training_args,
train_dataset=tokenized_dataset["train"],
eval_dataset=tokenized_dataset["test"],
)

trainer.train()

# model.save_pretrained("./fine_tuned_model")
# tokenizer.save_pretrained("./fine_tuned_model")

results = trainer.evaluate()
print(results)

from sklearn.metrics import classification_report
predictions = trainer.predict(tokenized_dataset["test"])
y_pred = predictions.predictions.argmax(axis=1)
y_true = tokenized_dataset["test"]["label"]
print(classification_report(y_true, y_pred))