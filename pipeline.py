import shutil
import json
from config import DATA_RAW, DATA_PROCESSED

def run_pipeline():
    img = load_apod()
    result = twist_filter(img)

    # kopiujemy obraz jako latest.jpg
    shutil.copy(img, DATA_RAW + "latest.jpg")

    # zapisujemy wynik twist-filter
    with open(DATA_PROCESSED + "twist.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Pipeline result:", result)
