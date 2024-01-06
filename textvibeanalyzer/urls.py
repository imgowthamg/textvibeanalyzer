# textvibeanalyzer/urls.py
from django.contrib import admin
from django.urls import path, include
from sentiment_analyzer.views import analyze_sentiment

urlpatterns = [
    path('', analyze_sentiment, name='analyze_sentiment'),
    path('admin/', admin.site.urls),
    path('sentiment/', include('sentiment_analyzer.urls')),
]
