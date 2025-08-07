from textblob import TextBlob

def detect_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity < -0.3:
        return "sad"
    elif polarity > 0.3:
        return "happy"
    elif "anxious" in text or "worried" in text:
        return "anxious"
    elif "hello" in text or "hi" in text:
        return "greeting"
    else:
        return "default"
