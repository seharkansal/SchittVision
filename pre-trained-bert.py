import torch
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load your CSV file into a DataFrame
df = pd.read_csv('path_to_your_data.csv')  # Update with your actual file path

# Ensure your columns are named 'text' and 'emotion'
texts = df['text'].tolist()
emotions = df['emotion'].tolist()

# Encode emotions (labels) as integers
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(emotions)

# Tokenization
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Custom Dataset class
class EmotionDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        text = self.texts[item]
        label = self.labels[item]
        encoding = self.tokenizer.encode_plus(
            text, 
            add_special_tokens=True, 
            max_length=self.max_len, 
            return_token_type_ids=False, 
            padding='max_length', 
            truncation=True, 
            return_attention_mask=True, 
            return_tensors='pt'
        )
        
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'label': torch.tensor(label, dtype=torch.long)
        }

# Split dataset into train and validation sets
train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2)

# Create Dataloaders with smaller batch sizes
train_dataset = EmotionDataset(train_texts, train_labels, tokenizer, max_len=128)
val_dataset = EmotionDataset(val_texts, val_labels, tokenizer, max_len=128)

train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True, num_workers=2)
val_dataloader = DataLoader(val_dataset, batch_size=8, num_workers=2)

# Load Pre-trained BERT model (you can use DistilBERT for better memory efficiency)
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(label_encoder.classes_))

# Optimizer and Loss Function
optimizer = AdamW(model.parameters(), lr=2e-5)
device = torch.device("cpu")  # Switch to CPU if GPU memory is an issue
model = model.to(device)

# Training Loop with Gradient Accumulation
accumulation_steps = 4  # Accumulate gradients over 4 mini-batches
for epoch in range(3):
    model.train()
    optimizer.zero_grad()
    for i, batch in enumerate(train_dataloader):
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['label'].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()

        if (i + 1) % accumulation_steps == 0:
            optimizer.step()
            optimizer.zero_grad()

    print(f"Epoch {epoch + 1} finished.")

# Evaluation
model.eval()
predictions, true_labels = [], []

with torch.no_grad():
    for batch in val_dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['label'].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits

        predictions.extend(torch.argmax(logits, dim=-1).cpu().numpy())
        true_labels.extend(labels.cpu().numpy())

accuracy = accuracy_score(true_labels, predictions)
print(f"Validation Accuracy: {accuracy}")
