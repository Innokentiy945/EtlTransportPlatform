from api_client.api_client_osm import OverpassClient

from pathlib import Path
import json


class ExtractPoiAllBg():
    def __init__(self):
        self.client = OverpassClient()

    async def exractPoiAllBgRaw(self):
        file_path = Path("data/raw_data/poiAllBg.json")

        if file_path.is_file() and file_path.stat().st_size > 0:
            print(f"File {file_path} exists. Loading from disk")
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)

        print("The file does not exist or is empty. Extraction started")

        query = """
            [out:json][timeout:90];

            area["ISO3166-2"="RS-00"]->.belgrade;

            (
              nwr["amenity"~"^(restaurant|fast_food|bar|pub|cafe|biergarten|food_court|ice_cream)$"](area.belgrade);
            );

            out center;
            """

        data = await self.client.execute(query)

        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return data
