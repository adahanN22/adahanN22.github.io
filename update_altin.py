import requests, json

url = "https://finans.truncgil.com/today.json"
res = requests.get(url)
data = res.json()

altin_data = {
    "gram": {"al": data["Gram Altın"]["Alış"], "sat": data["Gram Altın"]["Satış"]},
    "ceyrek": {"al": data["Çeyrek Altın"]["Alış"], "sat": data["Çeyrek Altın"]["Satış"]},
    "yarim": {"al": data["Yarım Altın"]["Alış"], "sat": data["Yarım Altın"]["Satış"]},
    "ons": {"al": data["Ons"]["Alış"], "sat": data["Ons"]["Satış"]}
}

with open("altin.json", "w", encoding="utf-8") as f:
    json.dump(altin_data, f, ensure_ascii=False, indent=2)
