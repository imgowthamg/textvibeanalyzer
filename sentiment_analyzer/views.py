from django.shortcuts import render
from .forms import UserInputForm
from textblob import TextBlob
from wordcloud import WordCloud
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

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment_label = analysis.sentiment.polarity
    sentiment_score = analysis.sentiment.subjectivity
    return sentiment_label, sentiment_score

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    image_stream = BytesIO()
    wordcloud.to_image().save(image_stream, format='PNG')
    image_data = base64.b64encode(image_stream.getvalue()).decode('utf-8')
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
                translated_text = translate_text(user_text, source_lang=selected_language)
                if translated_text:
                    user_text = translated_text
                else:
                    return render(request, 'sentiment_analyzer/translation_failed.html')

            # Perform sentiment analysis
            sentiment_label, sentiment_score = analyze_sentiment(user_text)

            # Generate word cloud based on the original text
            wordcloud_image_url = generate_wordcloud(form.cleaned_data['text'])

            return render(
                request,
                'sentiment_analyzer/result.html',
                {'text': user_text, 'sentiment_label': sentiment_label, 'sentiment_score': sentiment_score, 'wordcloud_image_url': wordcloud_image_url}
            )
    else:
        form = UserInputForm()

    return render(request, 'sentiment_analyzer/analyze_sentiment.html', {'form': form})
