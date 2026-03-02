📄 README.md (CWA_Project_Publish - Alpha v1.0)
🌡️ LoadPulse: 全台氣象與電力負載數據分析專案
本專案旨在自動化擷取 CWA（中央氣象署）全台 835 觀測站數據，進行標準化清洗後存入 SQLite 資料庫，為後續電力負載相關性分析提供基礎。


📂 1. 專案目錄結構
---------------------------------------------------------
CWA_project/
├── data/               # 原始數據存放區
│   └── raw_json/       # 備份的 .json.gz 檔案
├── database/           # 資料庫存放區
│   └── load_pulse.db   # 核心 SQLite 資料庫
├── service/            # 核心邏輯函式庫
│   ├── config.py       # 絕對路徑與配置
│   ├── init_fetch.py   # API 請求邏輯
│   └── data_washing.py # 清洗與 SQL 寫入邏輯
├── .env                # 環境變數 (API_KEY) - [不可上傳至 Git]
├── main.py             # 主執行程式
└── requirements.txt    # 必要的 Python 套件清單
---------------------------------------------------------


🛠️ 2. 伺服器環境建置步奏

Step 1: 複製專案與建立環境
---------------------------------------------------------
# 進入專案目錄
cd CWA_project

# 建議建立虛擬環境 (Virtual Environment)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
---------------------------------------------------------


Step 2: 安裝必要套件
--------------------------------------------------------
pip install -r requirements.txt
主要依賴：requests, python-dotenv, certifi, pathlibs
--------------------------------------------------------



Gemini 說了
這是一個非常專業的作法！在將程式碼部署到伺服器之前，一份清晰的 README.md 能幫助你（或未來的合作夥伴）快速重建開發環境，並確保 API 金鑰等敏感資訊不會外洩。

這是一份為你的 LoadPulse (CWA_Project) 量身打造的測試版 README：

📄 README.md (CWA_Project_Publish - Alpha v1.0)
🌡️ LoadPulse: 全台氣象與電力負載數據分析專案
本專案旨在自動化擷取 CWA（中央氣象署）全台 835 觀測站數據，進行標準化清洗後存入 SQLite 資料庫，為後續電力負載相關性分析提供基礎。

📂 1. 專案目錄結構
Plaintext
CWA_project/
├── data/               # 原始數據存放區
│   └── raw_json/       # 備份的 .json.gz 檔案
├── database/           # 資料庫存放區
│   └── load_pulse.db   # 核心 SQLite 資料庫
├── service/            # 核心邏輯函式庫
│   ├── config.py       # 絕對路徑與配置
│   ├── init_fetch.py   # API 請求邏輯
│   └── data_washing.py # 清洗與 SQL 寫入邏輯
├── .env                # 環境變數 (API_KEY) - [不可上傳至 Git]
├── main.py             # 主執行程式
└── requirements.txt    # 必要的 Python 套件清單
🛠️ 2. 伺服器環境建置步奏
Step 1: 複製專案與建立環境
Bash
# 進入專案目錄
cd CWA_project

# 建議建立虛擬環境 (Virtual Environment)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
Step 2: 安裝必要套件
Bash
pip install -r requirements.txt
主要依賴：requests, python-dotenv, certifi, pathlib

Step 3: 配置環境變數
在根目錄建立 .env 檔案，並填入你的 CWA API Key：

Plaintext
API_KEY=你的中央氣象署API金鑰
🚀 3. API 呼叫與環境測試
在正式運行大規模清洗前，請執行測試腳本確認 API 通訊與路徑權限。

測試重點：
連線測試：確認 requests 是否能通過 SSL 驗證 (使用 certifi)。

路徑測試：確認 pathlib 產生的絕對路徑在伺服器環境（Linux/Win）是否正確。

權限測試：確認 data/ 與 database/ 目錄具備寫入權限。



💾 4. 資料儲存規範
原始檔：存於 data/raw_json/，以時間戳命名並進行 gzip 壓縮以節省空間。

資料庫：

Stations_Info: 靜態站點資料（不重複寫入）。

Weather_Logs: 每 10 分鐘 835 站的批次觀測紀錄（使用 executemany）。


