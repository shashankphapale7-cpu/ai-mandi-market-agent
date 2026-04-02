# ai-mandi-market-agent
Mandi-Master is a high-utility AI agent designed for agricultural traders and farmers in the Ahilyanagar (Ahmednagar) region. It automates the process of finding "Profit Gaps" between different agricultural markets (Mandis) across Maharashtra.

By combining real-time government data with local LLM intelligence (Llama 3.1 via Ollama), the agent identifies where a commodity is selling for the highest price and calculates if the trip is worth the effort.

🚀 Core Features
Real-time Data: Connects directly to the Data.gov.in (Agmarknet) API for live market rates.

Agentic Intelligence: Uses Llama 3.1 to act as a "Virtual Trader" to analyze market spreads.

Local Execution: Runs entirely on your local machine (Ubuntu/Nvidia) for maximum data privacy and zero API costs for the LLM.

Profit Alerts: Generates ready-to-use WhatsApp messages for immediate trade execution.

🛠 Prerequisites
Before running the agent, ensure your Ubuntu system is ready:

Python 3.10+

Ollama installed and running (ollama serve).

Llama 3.1 Model: Downloaded via ollama run llama3.1.

Data.gov.in API Key: Get your free key here.

📥 Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/shashankphapale7-cpu/mandi-master.git
cd mandi-master
2. Set Up Virtual Environment (Recommended)
Bash
python3 -m venv mandivenv
source mandivenv/bin/activate
3. Install Dependencies
Bash
pip install requests pandas
🚦 How to Run the Agent
Configure your API Key:
Open mandi_agent.py and replace "YOUR_ACTUAL_API_KEY_HERE" with your unique key from the government portal.

Execute the Script:

Bash
python3 mandi_agent.py
Select Commodity:
The agent will display a live list of crops being traded today (e.g., Soybean, Onion, Cotton). Enter the corresponding number.

View Report:
The agent will output a Strategy Report comparing your base (Ahilyanagar) with other districts.

🧠 How It Works (The Logic)
Data Extraction: The script pulls the last 200 records from the Ministry of Agriculture's real-time feed.

Filtering: It isolates trades happening within Maharashtra to ensure regional relevance.

LLM Reasoning: * The raw JSON data is passed to Llama 3.1.

The AI identifies the Modal Price (most common trading price).

It compares the price in Ahmednagar against hubs like Vashi (Mumbai), Pune, and Nashik.

Action Output: The agent doesn't just show a table; it provides a WhatsApp Alert drafted with professional trading terminology.

📈 Roadmap (Future God-Level Features)
[ ] Transport Cost Integration: Auto-calculate diesel and toll costs between cities.

[ ] Historical Trends: Predict if prices will rise or fall based on the last 7 days.

[ ] Multi-State Support: Expand arbitrage to neighboring states like Karnataka and Gujarat.

📄 License
Distributed under the MIT License. See LICENSE for more information.

Author: [Shashank Phapale]

Location: Ahilyanagar, Maharashtra, India.
