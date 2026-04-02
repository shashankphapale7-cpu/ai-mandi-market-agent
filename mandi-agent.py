import requests
import json
import subprocess
import pandas as pd

# ================= CONFIGURATION =================
API_KEY = "YOUR_ACTUAL_API_KEY_HERE" 
BASE_CITY = "Ahmednagar"
OLLAMA_MODEL = "llama3.1"
# This is the verified 2026 Resource ID for Agmarknet Daily Prices
RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070" 
# =================================================

def get_mandi_data(params):
    """Universal fetcher with proper headers for 2026 security."""
    url = f"https://api.data.gov.in/resource/{RESOURCE_ID}"
    combined_params = {
        "api-key": API_KEY,
        "format": "json",
        **params
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, params=combined_params, headers=headers)
        if response.status_code != 200:
            print(f"❌ API Error {response.status_code}: {response.text}")
            return None
        return response.json()
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return None

def main():
    print("🌾 Initializing Mandi-Master for Ahilyanagar...")
    
    # Step 1: Get unique commodities specifically for Maharashtra
    # We increase limit to 200 to ensure we see all crops
    data = get_mandi_data({"filters[state]": "Maharashtra", "limit": "200"})
    
    if not data or 'records' not in data:
        print("❌ Could not load data. Check if your API Key is verified in your email.")
        return

    records = data['records']
    commodities = sorted(list(set(r['commodity'] for r in records)))

    print("\nAvailable Commodities in Maharashtra Today:")
    for i, name in enumerate(commodities, 1):
        print(f"{i}. {name}")
    
    try:
        choice = int(input("\nSelect a commodity number: "))
        selected = commodities[choice - 1]
    except:
        return

    # Step 2: Filter specifically for the selected crop
    print(f"📡 Analyzing {selected}...")
    # Use the filtered records we already fetched to save API calls
    crop_data = [r for r in records if r['commodity'] == selected]
    
    if not crop_data:
        print("No specific price data found.")
        return

    # Step 3: Llama 3.1 Analysis
    df = pd.DataFrame(crop_data)
    json_summary = df[['market', 'district', 'modal_price']].to_json(orient='records')
    
    prompt = f"Act as an Ahilyanagar Agri-Trader. Analyze this {selected} data: {json_summary}. Find the highest price market vs {BASE_CITY} and give a 1-sentence WhatsApp alert."
    
    print("🧠 Running Llama 3.1 on RTX 4050...")
    process = subprocess.Popen(['ollama', 'run', OLLAMA_MODEL], 
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    stdout, _ = process.communicate(input=prompt)
    
    print("\n" + "="*40 + "\n" + stdout + "\n" + "="*40)

if __name__ == "__main__":
    main()
