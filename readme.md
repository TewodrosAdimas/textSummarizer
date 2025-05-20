
---

# 📝 Bullet Point Summarizer

This is a simple Streamlit app that summarizes long texts into 3–5 concise bullet points using a pre-trained transformer model from Hugging Face.


---

## 🚀 Features

* Summarizes long text into digestible bullet points
* Built with Hugging Face's `facebook/bart-large-cnn` model
* Clean and minimal Streamlit UI
* Fast and efficient — runs locally in seconds

---

## 📦 Installation

1. Create a `requirements.txt` file with the following:

   ```txt
   streamlit
   transformers
   torch
   sentencepiece  # Needed for some tokenizer models
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Run the App

Launch the app using:

```bash
streamlit run app.py
```

---

## ⚙️ How It Works

* Loads the `facebook/bart-large-cnn` model for summarization via the Hugging Face `transformers` pipeline.
* User pastes any long text into the input area.
* On clicking **Summarize**, the model generates a summary.
* The summary is then split into 3–5 bullet points and displayed on the page.

---


---








![alt text](<Screenshot from 2025-05-14 17-08-03.png>)
```


