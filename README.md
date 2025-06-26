

# Stocker AI

## Overview

**Stocker AI** is an automated stock market analysis tool designed to provide users with comprehensive insights and forecasts in the financial market. The application integrates several innovative features, utilizing advanced technologies to enhance user experience and decision-making in stock trading.

---

## Steps To Run the Code

### 1. Clone the Repository
First, clone the Stocker AI repository to your local machine by running the following command in your terminal:

```bash
git clone https://github.com/VaibhavKothe/stockerAI.git
cd stockerAI
```

### 2. Install the Required Packages
Next, install the necessary Python packages using the following command:

```bash
pip install -r requirements.txt
```

### 3. Run the Application
Finally, start the Stocker AI application by executing the command:

```bash
streamlit run app.py
```

---

## Features

### 1. Get the Latest News from the Market
This feature scrapes the latest news from the **Moneycontrol** website and presents it in a Streamlit DataFrame format. The DataFrame includes:

- **Summary of the news**
- **Headlines**
- **Sentiment analysis** for both the summary and headlines
- **Pie charts** displaying the sentiment distribution for the summary and headlines

> **Note:** Users can read the complete articles on the Moneycontrol website, and links are provided in the Stocker app itself under the news section.

![News Summary Screenshot](https://github.com/user-attachments/assets/7fb9cf0a-250a-478e-b227-20c2510e575d)
![Sentiment Analysis Screenshot](https://github.com/user-attachments/assets/d73e9d6d-2a14-4380-89b8-205669b6d3c3)

---

### 2. News Analysis Chatbot
Users can interact with a chatbot to retrieve insights from the scraped news without reading the articles. The chatbot can answer queries like:

- Stocks recommended to buy
- Which stocks received investments, etc.

This functionality is powered by **MongoDB Atlas** for vector search, **CosmoCloud** as the backend layer, and **Gemini AI** as the language model.

![Chatbot Screenshot](https://github.com/user-attachments/assets/0fe6d8a1-c841-46e8-a7c3-10c34c6d54d7)

---

### 3. Stock Charts
Stocker AI provides various stock charts, including:

- Candlestick charts
- Line charts
- Daily returns
- Volume charts

These charts are available for **1,965 companies** listed on the **NSE** and are generated using **Plotly** and **yfinance**.

![Stock Chart Screenshot 1](https://github.com/user-attachments/assets/0dc7d52f-62d8-4c54-8bb5-121c9a06eb63)
![Stock Chart Screenshot 2](https://github.com/user-attachments/assets/6a77853f-d149-4ae2-a354-9eeee91abbbf)

---

### 4. Chat with Graph
This unique feature uses the **Gemini-1.5-pro-latest model** to perform direct analyses on stock charts based on user queries. Users no longer need to manually analyze the charts, as this chatbot automates the process.

![Chat with Graph Screenshot](https://github.com/user-attachments/assets/396ae378-00a6-4352-80d3-959f0af40b4c)

---

### 5. Indicators Recommendations
Stocker AI provides clear recommendations based on technical indicators in the market. This includes insights from oscillators, moving averages, and other indicators to guide users in their trading decisions.

![Indicators Recommendations Screenshot](https://github.com/user-attachments/assets/22334740-4214-40ae-a964-9edf750ac0af)

---

### 6. Forecast
The application offers forecasts for the upcoming months based on user specifications. This feature employs the **Facebook Prophet** model to generate reliable predictions.

![Forecast Screenshot](https://github.com/user-attachments/assets/e0d35fc9-a282-4ade-bd3f-ebc212bf0002)

---

## Getting Started

To get started with Stocker AI, clone the repository and follow the instructions in the installation section.

```bash
git clone https://github.com/VaibhavKothe/stockerAI.git
cd stockerAI
```
