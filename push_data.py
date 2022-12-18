# Import the libraries we need
from pymongo import MongoClient
import requests
from read_conn_string import read_conn_string

conn_string = read_conn_string()

# Connect to the database with the connection string we got from Atlas, replacing user and password.
client = MongoClient(conn_string)

# Next we define the database we are using.
# It does not have to exist first, like with relational databases.
db = client.get_database('coin_markets')

# Now, we make the API call and prices the results to the terminal.
prices = requests.get('https://api.coingecko.com/api/v3//coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')
prices = prices.json()
print(prices)

# We define the collection we will store this data in,
# which is created dynamically like the database,
# and insert the data into the collection.
db_prices = db.get_collection('prices')
inserted = db_prices.insert_many(prices)
# Print a count of documents inserted.
print(str(len(inserted.inserted_ids)) + " documents inserted")