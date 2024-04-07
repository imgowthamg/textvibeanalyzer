# Sentiment Analyzer Project

## Overview
The Sentiment Analyzer project is a text analysis tool designed to analyze the sentiment of textual data. It employs Natural Language Processing (NLP) techniques to determine the emotional tone of a piece of text, categorizing it as positive, negative, or neutral.

## Features
- **Sentiment Analysis**: The core feature of the project is sentiment analysis, which classifies text into positive, negative, or neutral categories based on its emotional tone.
- **Web Interface**: The project provides a user-friendly web interface where users can input text for sentiment analysis.
- **Visualization**: Sentiment analysis results are visualized using charts and graphs to provide users with a clear understanding of the sentiment distribution.
- **Multiple Language Support**: The project supports multiple languages, including English, Spanish, Hindi, Tamil, and Malayalam.

## Pipeline
The project follows a pipeline architecture, consisting of the following stages:

1. **Input**: Users input text data via the web interface or through API endpoints.
2. **Preprocessing**: Text data undergoes preprocessing, including tokenization, removing stop words, and other normalization techniques.
3. **Sentiment Analysis**: The preprocessed text is fed into the sentiment analysis model, which predicts the sentiment of the text.
4. **Visualization**: Sentiment analysis results are visualized using Matplotlib and presented to the user via the web interface.
5. **Output**: Users can view sentiment analysis results and insights through the web interface or retrieve them programmatically through API endpoints.

## Setup
To set up the project locally, follow these steps:

1. **Clone the repository**: `git clone https://github.com/imgowthamg/sentiment-analyzer.git`
2. **Navigate to the project directory**: `cd sentiment-analyzer`
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Run the Django development server**: `python manage.py runserver`
5. **Access the web interface at**: `http://127.0.0.1:8000/`

## Dependencies
- Django: Web framework for building the user interface
- NLTK: Natural Language Toolkit for text preprocessing
- Scikit-learn: Machine learning library for sentiment analysis
- Matplotlib: Library for data visualization

## Sample input
  ![Screenshot 2024-04-07 130802](https://github.com/imgowthamg/textvibeanalyzer/assets/119653141/50d55d84-7a6a-48ef-af64-3d2269f4b80e)


## Sample output
![Screenshot 2024-04-07 131213](https://github.com/imgowthamg/textvibeanalyzer/assets/119653141/a4529bfb-957f-46b5-865e-5cef62873bce)




