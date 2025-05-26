from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import gradio as gr

# Load the tokenizer and model
MODEL_NAME = "logasanjeev/goemotions-bert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# GoEmotions labels (27 emotions + neutral)
labels = [
    "admiration", "amusement", "anger", "annoyance", "approval", "caring", "confusion",
    "curiosity", "desire", "disappointment", "disapproval", "disgust", "embarrassment",
    "excitement", "fear", "gratitude", "grief", "joy", "love", "nervousness", "optimism",
    "pride", "realization", "relief", "remorse", "sadness", "surprise", "neutral"
]

# Main function to classify text input
def classify_emotions(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.sigmoid(logits)[0]
    threshold = 0.3
    results = {labels[i]: float(probs[i]) for i in range(len(labels)) if probs[i] > threshold}
    return results if results else {"neutral": 1.0}

# Optional Gradio UI
gr.Interface(fn=classify_emotions, inputs="text", outputs="label", title="GoEmotions BERT Emotion Classifier").launch()
