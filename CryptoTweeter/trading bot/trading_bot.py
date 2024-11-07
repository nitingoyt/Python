import os
import time
import hmac
import hashlib
import requests
import schedule
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

WAZIRX_API_URL = 'https://api.wazirx.com/sapi/v1'
API_KEY = os.getenv('WAZIRX_API_KEY')
SECRET_KEY = os.getenv('WAZIRX_SECRET_KEY')

# Function to generate signature
def generate_signature(query_string, secret_key):
    return hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()

# Function to get market data
def get_market_data(symbol):
    try:
        endpoint = f'{WAZIRX_API_URL}/ticker/24hr'
        params = {'symbol': symbol}
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        print(f"Market data for {symbol}: {data}")  # Debugging line
        return data
    except Exception as e:
        print(f"Error fetching market data: {e}")
        return None

# Function to place an order
def place_order(symbol, side, quantity, price):
    try:
        endpoint = f'{WAZIRX_API_URL}/order'
        params = {
            'symbol': symbol,
            'side': side,
            'type': 'LIMIT',
            'timeInForce': 'GTC',
            'quantity': quantity,
            'price': price,
            'recvWindow': 5000,
            'timestamp': int(time.time() * 1000)
        }
        
        # Debugging: Print parameters before signing
        print(f"Order parameters before signing: {params}")

        query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
        signature = generate_signature(query_string, SECRET_KEY)
        params['signature'] = signature

        # Debugging: Print the final URL
        print(f"Placing order with URL: {endpoint}")
        print(f"Parameters: {params}")

        headers = {
            'X-Api-Key': API_KEY
        }

        response = requests.post(endpoint, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        result = response.json()
        print(f"Order response: {result}")  # Debugging line
        return result
    except Exception as e:
        print(f"Error placing order: {e}")
        return None

# Trading strategy (simple example)
def trading_strategy():
    symbol = 'btcusdt'
    print(f"Running trading strategy at {datetime.now()}")  # Debugging line
    data = get_market_data(symbol)
    if data:
        last_price = float(data.get('lastPrice', 0))
        print(f"Last price for {symbol}: {last_price}")

        # Example strategy: buy if price is below a certain value
        if last_price < 30000:
            order_response = place_order(symbol, 'BUY', 0.001, last_price)
            print(f"Placed BUY order: {order_response}")
        elif last_price > 35000:
            order_response = place_order(symbol, 'SELL', 0.001, last_price)
            print(f"Placed SELL order: {order_response}")
        else:
            print("No action taken.")
    else:
        print("No market data available.")

# Schedule the trading strategy to run every minute
def schedule_trading():
    print("Scheduling trading times...")  # Debugging line
    schedule.every(1).minutes.do(trading_strategy)

if __name__ == "__main__":
    print("Starting the trading bot...")
    schedule_trading()
    while True:
        try:
            current_time = datetime.now()
            print(f"Current time: {current_time}")
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("Bot stopped by user.")
            break
