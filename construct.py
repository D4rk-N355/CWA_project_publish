from service.config import DATABASE_PATH
from service.init_db_set import loadpulse_init_db
print(DATABASE_PATH)
loadpulse_init_db(DATABASE_PATH)
