from textblob import TextBlob

def detect_sentiment(text):

    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        return "Positive"

    elif analysis.sentiment.polarity < 0:
        return "Negative"

    return "Neutral"
