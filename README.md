# GoEmotions BERT Emotion Classifier

This project uses a BERT-based model fine-tuned on the [GoEmotions dataset](https://github.com/google-research/google-research/tree/master/goemotions) to classify text into 28 emotion categories (27 emotions + Neutral), all running **locally** on your machine.

<img width="782" alt="image" src="https://github.com/user-attachments/assets/0bbef5ab-854b-4672-86b8-411980620cd3" />

## About

- This app is a complete copy of the `logasanjeev/goemotions-bert` HuggingFace project and this repo is only meant for running evaluations on that model locally.
- Multi-label emotion classification
- Simple web UI with Gradio

## Installation

### 1. Clone or download this repository

```bash
git clone https://github.com/tuomax7/affective-computing-ml.git
cd affective-computing-ml
```

### 2. Create a Python virtual environment

```bash
python -m venv goemotions-env
source goemotions-env/bin/activate   # On Windows: goemotions-env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the classifier app

```bash
python goemotions_local.py
```

This will launch the app at [http://localhost:7860](http://localhost:7860) where you can then type in your predictions.
