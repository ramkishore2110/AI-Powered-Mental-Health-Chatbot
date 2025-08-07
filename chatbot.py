import random
from nlp_utils import detect_emotion

responses = {
    "greeting": ["Hi there!", "Hello!", "Hey! How are you feeling today?"],
    "sad": ["I'm here for you. Want to talk about it?", "You're not alone. It's okay to feel down."],
    "anxious": ["Try taking a deep breath. Would you like a guided meditation link?"],
    "happy": ["That's great to hear! Keep smiling!"],
    "default": ["I’m here to listen. Please tell me how you’re feeling."]
}

def get_bot_response(user_input):
    emotion = detect_emotion(user_input)
    return random.choice(responses.get(emotion, responses['default']))
