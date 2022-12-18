# Import the only library we need.
from pymongo import MongoClient
from read_conn_string import read_conn_string

conn_string = read_conn_string()

# Connect to the MongoDB database using our connection string.
client = MongoClient(conn_string)

# Connect to the coin_markets database and the prices collection.
db = client.get_database('coin_markets')
db_prices = db.get_collection('prices')

# Search for records where the price_change_24h value is greater than 1,
# loop the results, and print them to the terminal.
for doc in db_prices.find({"price_change_24h": {"$gt": 1} }):
    print(doc)