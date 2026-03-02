import sqlite3
from service.config import DATABASE_PATH
db_path = DATABASE_PATH
def loadpulse_init_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # 1. 建立靜態站點資訊表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Stations_Info (
            StationId TEXT PRIMARY KEY,
            StationName TEXT,
            CityName TEXT,
            DistrictName TEXT,
            Lat_WGS84 REAL,
            Lon_WGS84 REAL,
            Altitude REAL
        )
    ''')

    # 2. 建立動態觀測紀錄表
    # 使用 StationId + ObsTime 作為聯合唯一鍵，防止重複
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Weather_Logs (
            station_id TEXT,
            obs_time TIMESTAMP,
            temp REAL,
            humid REAL,
            pressure REAL,
            rain REAL,
            wind_speed REAL,
            day_high REAL,
            day_low REAL,
            PRIMARY KEY (station_id, obs_time),
            FOREIGN KEY (station_id) REFERENCES Stations_Info (StationId)
        )
    ''')
    
    
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_time ON Weather_Logs (obs_time)')
    conn.commit()  
    conn.close()   
    print("---complete---")

loadpulse_init_db(db_path)