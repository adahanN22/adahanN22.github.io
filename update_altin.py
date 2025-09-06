import requests
import json

# Altın fiyatlarını çekeceğimiz API
url = "https://finans.truncgil.com/today.json"

try:
    response = requests.get(url)
    data = response.json()

    altin_data = {
        "gram": {"al": data["Gram Altın"]["Alış"], "sat": data["Gram Altın"]["Satış"]},
        "ceyrek": {"al": data["Çeyrek Altın"]["Alış"], "sat": data["Çeyrek Altın"]["Satış"]},
        "yarim": {"al": data["Yarım Altın"]["Alış"], "sat": data["Yarım Altın"]["Satış"]},
        "ons": {"al": data["Ons"]["Alış"], "sat": data["Ons"]["Satış"]}
    }

    # altin.json dosyasına yaz
    with open("altin.json", "w", encoding="utf-8") as f:
        json.dump(altin_data, f, ensure_ascii=False, indent=2)

    print("altin.json başarıyla güncellendi!")

except Exception as e:
    print("Hata oluştu:", e)
