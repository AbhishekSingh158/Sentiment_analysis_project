import nltk # from pip install nltk
from textblob import TextBlob #from pip install textblob
nltk.download('vader_lexicon') #ensures the VADER lexicon is downloaded, which is useful for sentiment analysis.

# List of words which we are using to define the sentiment in the sentence
#you can add more words according to your usage

positive_words = ["joyful", "glad", "delighted", "cheerful", "ecstatic", "content", "pleased", "amused", "thrilled", "excited"]
negative_words = ["sorrowful", "unhappy", "dejected", "grieving", "mournful", "melancholy", "distressed", "disappointed", "heartbroken","sad"]
neutral_words = ["indifferent", "serene", "neutral", "objective", "impartial", "unemotional", "apathetic"]

# Function to detect sentiment using TextBlob 
def detect_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    #if else condition for the sentiment analysis
    if sentiment > 0:
        return "Positive😊"
    elif sentiment < 0:
        return "Negative😔"
    else:
        return "Neutral😐"

# Get input from the user 
text = input("Enter your text here: ")
sentiment = detect_sentiment(text)
print(f"The sentiment of the text is: {sentiment} in nature")

# Function to detect sentiment using custom word lists
#Determines the sentiment based on the highest count
def detect_sentiment_custom(text):
    words = text.split()
    happy_count = sum(1 for word in words if word in positive_words)
    sad_count = sum(1 for word in words if word in negative_words)
    neutral_count = sum(1 for word in words if word in neutral_words)
    
    if happy_count > sad_count and happy_count > neutral_count:
        return "Positive"
    elif sad_count > happy_count and sad_count > neutral_count:
        return "Negative"
    else:
        return "Neutral"

