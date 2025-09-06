import requests
import json

# Altın fiyatlarını çekiyoruz
url = "https://finans.truncgil.com/today.json"
response = requests.get(url)
data = response.json()

# Sadece gerekli verileri alıyoruz
altin = {
    "gram": {"al": data["Gram Altın"]["Alış"], "sat": data["Gram Altın"]["Satış"]},
    "ceyrek": {"al": data["Çeyrek Altın"]["Alış"], "sat": data["Çeyrek Altın"]["Satış"]},
    "yarim": {"al": data["Yarım Altın"]["Alış"], "sat": data["Yarım Altın"]["Satış"]},
    "ons": {"al": data["Ons"]["Alış"], "sat": data["Ons"]["Satış"]}
}

# altin.json dosyasını güncelle
with open("altin.json", "w", encoding="utf-8") as f:
    json.dump(altin, f, ensure_ascii=False, indent=2)

print("altin.json güncellendi!")
