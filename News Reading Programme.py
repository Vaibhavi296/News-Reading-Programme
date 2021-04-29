# api key 04d45802710049069c130bae207f1530
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for Today")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=04d45802710049069c130bae207f1530"
    news=requests.get(url).text
    news_dict=json.loads(news)
    articles=news_dict['articles']
    for article in articles:
        speak(article['title'])
        speak("Moving to the next news....Listen carefully")

    speak("Thanks for listening")
