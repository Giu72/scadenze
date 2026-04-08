from datetime import datetime, timedelta

# 1. La nostra lista di scadenze (per ora la scriviamo a mano)
scadenze = [
    {"titolo": "Revisione Ascensore", "data": "2024-05-20"},
    {"titolo": "Rata Assicurazione", "data": "2024-06-15"},
    {"titolo": "Manutenzione Caldaia", "data": "2024-05-10"}
]

oggi = datetime.now()

print("--- CONTROLLO SCADENZE IN CORSO ---")

for item in scadenze:
    data_scadenza = datetime.strptime(item["data"], "%Y-%m-%d")
    giorni_mancanti = (data_scadenza - oggi).days
    
    if 0 <= giorni_mancanti <= 15:
        print(f"⚠️ AVVISO: '{item['titolo']}' scade tra {giorni_mancanti} giorni!")
    elif giorni_mancanti < 0:
        print(f"❌ SCADUTO: '{item['titolo']}' è scaduto da {-giorni_mancanti} giorni!")