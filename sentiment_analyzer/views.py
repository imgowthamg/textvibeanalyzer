from django.shortcuts import render
from .forms import UserInputForm
from textblob import TextBlob
from wordcloud import WordCloud
import base64
from io import BytesIO

def generate_word_cloud(user_text):
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(user_text)

    # Convert the word cloud to an image
    image_stream = BytesIO()
    wordcloud.to_image().save(image_stream, format='PNG')

    # Encode the image as base64
    image_data = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    # Construct the URL for the image
    wordcloud_image_url = f"data:image/png;base64,{image_data}"

    return wordcloud_image_url

def analyze_sentiment(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data['text']
            selected_language = request.POST.get('language', 'en')

            # Perform translation if the selected language is not English
            if selected_language != 'en':
                try:
                    blob = TextBlob(user_text)
                    translated_blob = blob.translate(to='en')
                    user_text = str(translated_blob)
                except Exception as e:
                    print(f"Translation failed: {e}")
                    # Handle translation failure gracefully

            # Perform sentiment analysis
            analysis = TextBlob(user_text)
            sentiment_label = analysis.sentiment.polarity
            sentiment_score = analysis.sentiment.subjectivity

            # Generate word cloud
            wordcloud_image_url = generate_word_cloud(user_text)

            # Return the result
            return render(
                request,
                'sentiment_analyzer/result.html',
                {'text': user_text, 'sentiment_label': sentiment_label, 'sentiment_score': sentiment_score, 'wordcloud_image_url': wordcloud_image_url}
            )
    else:
        form = UserInputForm()

    return render(request, 'sentiment_analyzer/analyze_sentiment.html', {'form': form})
