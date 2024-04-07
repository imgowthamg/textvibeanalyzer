from django.shortcuts import render
from .forms import UserInputForm
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from googletrans import Translator

def translate_text(text, source_lang, target_lang='en'):
    try:
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang).text
        return translated_text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None

def analyze_sentiment_score(text):
    analysis = TextBlob(text)
    sentiment_polarity = analysis.sentiment.polarity
    sentiment_score = abs(sentiment_polarity)
    return sentiment_polarity, sentiment_score

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()  # Ensures that the word cloud is not clipped
    wordcloud_image = BytesIO()
    plt.savefig(wordcloud_image, format='png')
    wordcloud_image.seek(0)
    wordcloud_image_base64 = base64.b64encode(wordcloud_image.getvalue()).decode('utf-8')
    plt.close()  # Close the plot to prevent overlapping images
    return wordcloud_image_base64

def analyze_sentiment(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data['text']
            selected_language = request.POST.get('language', 'en')

            # Translate the text to English if necessary
            if selected_language != 'en':
                translated_text = translate_text(user_text, source_lang=selected_language, target_lang='en')
            else:
                translated_text = user_text

            # Perform sentiment analysis on the translated text
            sentiment_polarity, sentiment_score = analyze_sentiment_score(translated_text)

            # Generate word cloud based on the original text
            wordcloud_base64 = generate_wordcloud(user_text)

            return render(
                request,
                'sentiment_analyzer/result.html',
                {'original_text': user_text, 'translated_text': translated_text, 'sentiment_label': sentiment_polarity, 'sentiment_score': sentiment_score, 'wordcloud_image': wordcloud_base64}
            )
    else:
        form = UserInputForm()

    return render(request, 'sentiment_analyzer/analyze_sentiment.html', {'form': form})
