from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv("exemplo_env.env")

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB_NAME")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION")

if not MONGO_URI:
    raise Exception("❌ MONGO_URI não carregou do .env")

print("✅ Variáveis carregadas com sucesso")

client = MongoClient(
    MONGO_URI,
    connectTimeoutMS=5000,
    serverSelectionTimeoutMS=5000
)

mongo_db = client[DB_NAME]
text_collection = mongo_db[COLLECTION_NAME]

# Teste de conexão
try:
    client.admin.command("ping")
    print("✅ MongoDB conectado!")
    print("📦 Banco:", mongo_db.name)
    print("📁 Coleção:", text_collection.name)
except Exception as e:
    print("❌ Erro MongoDB:", e)
