import requests
import os
from datetime import date
from datetime import timedelta
from twilio.rest import Client

my_SE_key = os.environ.get("API_SE_KEY")
my_NEWS_key = os.environ.get("API_NEWS_KEY")
account_sid = os.environ.get("API_TWILIO_KEY")
auth_token = os.environ.get("API_TWILIO_TOKEN")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla" #"Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

dzisiaj = date.today()
wczoraj = dzisiaj - timedelta(days = 1)
six_months_ago = dzisiaj - timedelta(days = 180)
month_ago = dzisiaj - timedelta(days = 30)

print("Yesterday was: ", wczoraj)
przedwczoraj = dzisiaj - timedelta(days = 2)
print("The day before yesterday was: ", przedwczoraj)

def get_percent_change(kurs_z_wczoraj, kurs_z_przedwczoraj):
    if kurs_z_wczoraj == kurs_z_przedwczoraj:
        return 100.0
    try:
        return (abs(kurs_z_wczoraj - kurs_z_przedwczoraj) / kurs_z_przedwczoraj) * 100.0
    except ZeroDivisionError:
        return 0
    
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

SE_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED", # I want to use this function
    "symbol": STOCK_NAME, # I want data of the company
    "outputsize": "compact", # "full" returns full history (20 years), "compact" returns 100 entries
    "datatype": "json", # "json" is default, can be "csv" as well
    "apikey": my_SE_key
    }

SE_response = requests.get(STOCK_ENDPOINT, params=SE_parameters)
SE_response.raise_for_status()
company_data = SE_response.json()

kurs_z_wczoraj = float(company_data["Time Series (Daily)"][str(wczoraj)]["4. close"])
print(f"Wczorajszy kurs Tesli: {kurs_z_wczoraj}")

#TODO 2. - Get the day before yesterday's closing stock price

kurs_z_przedwczoraj = float(company_data["Time Series (Daily)"][str(przedwczoraj)]["4. close"])
print(f"Przedwczorajszy kurs Tesli: {kurs_z_przedwczoraj}")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

price_diff = round(abs(kurs_z_wczoraj-kurs_z_przedwczoraj), 2)
print(f"Różnica cen: {price_diff}")

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

perc_change = round(get_percent_change(kurs_z_wczoraj, kurs_z_przedwczoraj), 2)
print(f"Procentowa różnica: {perc_change}%")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if perc_change > 0.05:
    print("Get news")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    NEWS_parameters = {
    "q": COMPANY_NAME, # I want to find news about the company
    "from": month_ago, # I want data from last six months
    "language": "en",
    "sortBy": "publishedAt",
    "apikey": my_NEWS_key
    }

    NEWS_response = requests.get(NEWS_ENDPOINT, params=NEWS_parameters)
    NEWS_response.raise_for_status()
    company_news = NEWS_response.json()


    # print(company_news)
    # for _ in range(3):
    #     news = f"News {_+1} \n" +\
    #         "Published at: " + \
    #         str(company_news["articles"][_]["publishedAt"]) + \
    #         ", \n" + \
    #         "Source: " + \
    #         company_news["articles"][_]["source"]["name"] +\
    #         ", \n" + \
    #         "Title: " + \
    #         company_news["articles"][_]["title"] +\
    #         ", \n" + \
    #         "Content: " + \
    #         company_news["articles"][_]["content"] +\
    #         "\n"
    #     print(news)
    #     client = Client(account_sid, auth_token)

    #     message = client.messages \
    #                     .create(
    #                         body=news,
    #                         from_='+16812069655',
    #                         to='+48609688960'
    #                     )

    #     print(message.status)
        

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
'''
See above step
'''
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 
'''
See above step
'''

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

news_list = [[f"News {i+1}: \n" +\
            "Published at: " + \
            str(company_news["articles"][i]["publishedAt"]) + \
            ", \n" + \
            "Source: " + \
            company_news["articles"][i]["source"]["name"] +\
            ", \n" + \
            "Title: " + \
            company_news["articles"][i]["title"] +\
            ", \n" + \
            "Content: " + \
            company_news["articles"][i]["content"] +\
            "\n"] \
            for i in range(3)]
print(news_list)

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

