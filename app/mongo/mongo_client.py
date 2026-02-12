from pymongo import MongoClient

MONGO_URI = "mongodb+srv://vendas_db_user:vendas_projeto_2026@vendas.stspuvx.mongodb.net/?retryWrites=true&w=majority&appName=vendas"

client = MongoClient(
    MONGO_URI,
    connectTimeoutMS=5000,
    serverSelectionTimeoutMS=5000
)

mongo_db = client["sales_texts"]
text_collection = mongo_db["texts"]
