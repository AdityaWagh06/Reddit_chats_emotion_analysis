# Reddit Emotion Analysis

This project focuses on analyzing emotional content from Reddit posts to better understand mental health trends and emotional expression online. It involves collecting, cleaning, and fine-tuning an emotion classification model using real-world Reddit data.

## 📌 Features

- 🔍 Scrapes posts from subreddits related to mental health using Reddit API
- 🧹 Cleans and preprocesses text data
- 🤗 Fine-tunes transformer-based models for emotion classification
- 📊 Visualizes emotion trends and distributions
- 📁 Includes datasets like:
  - `cleaned_reddit_data.csv`
  - `depression_posts.csv`
  - `mental_health_dataset.csv`


## 🛠️ Tech Stack

- Python
- Transformers (HuggingFace)
- Scikit-learn
- Pandas, NumPy, Matplotlib
- Reddit API (PRAW)

## 🧠 Model Training

The model is fine-tuned using a cleaned dataset of Reddit mental health posts. It predicts emotions such as *joy*, *anger*, *fear*, *sadness*, and *neutral*.

## 📤 Data Source

All Reddit data was scraped using the [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/en/stable/). We ensured compliance with Reddit’s API policies and anonymized all post content.

## 📈 Visualization

Emotions are visualized over time and across different subreddits to show patterns and trends using `visualize_results.ipynb`.

---

**Note:** This project is for academic and research purposes only and does not provide medical advice.
