import requests

def get_binance_pairs():
    api_url = "https://api.binance.com/api/v3/ticker/price"

    params = {
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        pairs = response.json()
        return pairs
    else:
        print(f"Errore nella richiesta API: {response.status_code}")
        return None

def print_usdt_pairs(pairs):
    tickers = []
    if pairs:
        for pair in pairs:
            if 'USDT' in pair['symbol']:
                ticker = pair['symbol'].replace('USDT', '')
                if ticker not in tickers:
                    tickers.append(ticker)
                    print(f"{ticker}")
    else:
        print("Nessuna coppia trovata.")

if __name__ == "__main__":
    usdt_pairs = get_binance_pairs()
    print_usdt_pairs(usdt_pairs)
