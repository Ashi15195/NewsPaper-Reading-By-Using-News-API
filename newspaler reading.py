import requests  #allow to send http request
import json  #used to send data from server to clint

def speak(str):
    from win32com.client import Dispatch #win is used to convert
    speak =  Dispatch("SAPI.spVoice")  #it is used to convert text to speak
    speak.speak(str)


if __name__ == '__main__':
    speak("news for today...lets begin")
    url = "https://newsapi.org/v2/everything?q=tesla&from=2022-02-04&sortBy=publishedAt&apiKey=8aa979e432064d22b0cd3dd75cea8b01"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']

    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak(article['description'])
        print(article['description'])


        speak("moving to the another news....listen carefully")




    speak("thanks for listening")



