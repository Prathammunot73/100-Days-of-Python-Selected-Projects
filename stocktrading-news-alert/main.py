import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"

#Get yesterday's closing stock price.
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,
}
response=requests.get(STOCK_ENDPOINT,params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference= float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down=None
if difference>0:
    up_down="🔺"
else:
    up_down="🔻"

# % difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent= abs((difference/float(yesterday_closing_price))*100)
print(diff_percent)


#use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent)>3:
    news_params={
        "apiKey":NEWS_API_KEY,
        "q":COMPANY_NAME,
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles=news_response.json()["articles"]

    #Use Python slice operator to create a list contain first 3 articles.
    three_articles=articles[:3]
    print(three_articles)

    #Created a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in three_articles
    ]
    #Send each article as a separate message via Twilio.
    client=Client(TWILIO_SID,TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message=client.messages.create(
            body=article,
            from_="YOUR_TWILIO_PHONE_NUMBER",
            to="YOUR_NUMBER",
        )



