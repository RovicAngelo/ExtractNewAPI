
import requests

try:
    base_url = "https://extract-news.p.rapidapi.com/v0/article"
    user_inputs = input('[ Enter a news URL: ]')
 
    print()
    querystring = {"url": str(user_inputs)}

    headers = {
        "X-RapidAPI-Key": "dccee04285msh4bc1d3616458017p1712b2jsn6a45a55e8573",
        "X-RapidAPI-Host": "extract-news.p.rapidapi.com"
    }
# getting the url, parameter,and API key
    response = requests.get(base_url, params=querystring, headers=headers)
    data = response.json()

# accessing the attributes in the dictionary
    news_url = (data['article']['source_url'])
    published_date = (data['article']['published'])
    published_guess_accuracy = (data['article']['published_guess_accuracy'])
    title = (data['article']['title'])
    text = (data['article']['text'])

    # printing the attributes
    print("News Url        : ", news_url)
    print("Published Date  : ", published_date)
    print("Published Guess : ", published_guess_accuracy)
    print("Title           : ", title)
    print("Text            : ", text)

except:
    print('|                                       [ERROR] Something went wrong, Please try again!!!                   '
          '                                  |')
