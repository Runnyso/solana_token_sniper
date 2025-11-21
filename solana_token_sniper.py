import requests, time

def snipe_new_tokens():
    print("Solana new token sniper (pump.fun + dexscreener)")
    seen = set()
    while True:
        r = requests.get("https://api.pump.fun/new")
        for token in r.json().get("tokens", []):
            mint = token["mint"]
            if mint in seen: continue
            seen.add(mint)
            if token["market_cap"] < 5000:  # under 5k FDV
                print(f"SNIPED!\n"
                      f"{token['symbol']} (${token['market_cap']:,.0f} FDV)\n"
                      f"Mint: {mint}\n"
                      f"https://pump.fun/{mint}\n"
                      f"https://dexscreener.com/solana/{mint}\n"
                      f"{'-'*50}")
        time.sleep(3)

if __name__ == "__main__":
    snipe_new_tokens()
