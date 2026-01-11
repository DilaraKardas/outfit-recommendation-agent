from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    print("HATA: API Key bulunamadı!")
    exit()

client = genai.Client(api_key=api_key)

print("--- HESABINDAKI TÜM MODELLER ---")

# Hiçbir özellik kontrolü yapmadan (hata riskini sıfıra indirmek için)
# sadece isimleri yazdırıyoruz.
try:
    for model in client.models.list():
        # Sadece isminde "gemini" geçenleri görelim ki liste çok uzamasın
        if "gemini" in model.name.lower():
            print(f"- {model.name}")
            
except Exception as e:
    print(f"Bir hata oluştu: {e}")

print("-" * 30)