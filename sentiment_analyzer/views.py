# sentiment_analyzer/views.py
from django.shortcuts import render
from .forms import UserInputForm
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def analyze_sentiment(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data['text']
            # Perform sentiment analysis using TextBlob
            analysis = TextBlob(user_text)
            sentiment_label = analysis.sentiment.polarity
            sentiment_score = analysis.sentiment.subjectivity

            # Generate word cloud
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(user_text)

            # Convert word cloud to image
            image_stream = BytesIO()
            wordcloud.to_image().save(image_stream, format='PNG')
            image_data = base64.b64encode(image_stream.getvalue()).decode('utf-8')
            wordcloud_image_url = f"data:image/png;base64,{image_data}"

            return render(
                request,
                'sentiment_analyzer/result.html',
                {'user_text': user_text, 'sentiment_label': sentiment_label, 'sentiment_score': sentiment_score, 'wordcloud_image_url': wordcloud_image_url}
            )
    else:
        form = UserInputForm()

    return render(request, 'sentiment_analyzer/analyze_sentiment.html', {'form': form})
