# 📈 Stock Trading News Alert

A Python project that monitors daily stock price changes and automatically fetches the latest news articles when the stock price changes significantly.

## 🚀 Features

* Fetches daily stock prices using the Alpha Vantage API.
* Calculates the percentage change between the last two trading days.
* Detects significant stock price movements.
* Retrieves the latest news articles using the News API.
* Sends the top news headlines and descriptions via SMS using Twilio.

## 🛠️ Technologies Used

* Python 3
* Requests
* Alpha Vantage API
* News API
* Twilio API

## 📁 Project Structure

```text
StockTrading_NewsAlert/
│── main.py
│── .gitignore
│── README.md
```

## ⚙️ Setup

1. Clone the repository.

```bash
git clone https://github.com/Prathammunot73/StockTrading_NewsAlert.git
```

2. Install the required package.

```bash
pip install requests twilio
```

3. Replace the placeholder values in `main.py` with your own credentials:

* Alpha Vantage API Key
* News API Key
* Twilio Account SID
* Twilio Auth Token
* Twilio Phone Number
* Your Phone Number

4. Run the project.

```bash
python main.py
```

## 📲 How It Works

1. Retrieves the latest daily stock prices.
2. Calculates the percentage change from the previous trading day.
3. If the price change exceeds the configured threshold, the program:

   * Fetches the latest news related to the company.
   * Selects the top three news articles.
   * Sends each article as an SMS notification.

## 📚 What I Learned

* Working with REST APIs
* HTTP requests using the Requests library
* Using list comprehensions
* Integrating multiple APIs in one project
* Sending SMS notifications with Twilio

## Attribution

This project was developed as part of my learning journey through the **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.
