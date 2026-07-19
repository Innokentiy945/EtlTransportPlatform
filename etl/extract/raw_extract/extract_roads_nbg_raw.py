import json
from pathlib import Path

from api_client.api_client_osm import OverpassClient


from pathlib import Path
import json

class RoadNBGRawDataExtractor:

    def __init__(self):
        self.client = OverpassClient()

    async def extractRoadsRaw(self):

        file_path = Path("data/raw_data/roadsAllNbg.json")

        if file_path.is_file() and file_path.stat().st_size > 0:
            print(f"File {file_path} exists. Loading from disk")

            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)

        print("The file does not exist or is empty. Extraction started")


        query = """
        [out:json][timeout:120];

        (
          way["highway"](44.785,20.360,44.840,20.450);
        );

        out geom;
        """

        data = await self.client.execute(query)


        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        return data

