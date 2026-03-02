import os
import certifi
import requests
from dotenv import load_dotenv
from service.config import ENV_PATH
dotenv_path_config = ENV_PATH
load_dotenv(dotenv_path=dotenv_path_config)
api_key = os.getenv("API_KEY")
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
os.environ['SSL_CERT_FILE'] = certifi.where()

def loadpulse_init_fetch():
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001"
    params = {
        "Authorization": api_key, 
        "format": "JSON",
    }
    
    try:
        res = requests.get(url, params=params, verify = True)
        print("json fetched!!")
        json_data = res.json()
        return json_data
            
    except requests.exceptions.JSONDecodeError:
        print("❌ JSON 解析失敗！回傳的可能不是標準 JSON 格式。")
        print(f"實際內容為: {res.text}")
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
    


#json_fetched = loadpulse_fetch_station_list()


