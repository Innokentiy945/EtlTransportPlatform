from etl.extract.common.extract_node import ExtractNode


class PoiCafesExtractingNbg(ExtractNode):
    def extractPoiCafeNbg(self):
        return self.extractNode(
            inputFilePath="data/raw_data/poiAllNbg.json",
            outputFilePath="data/extracted_data/cafesNbg.json",
            jsonTypeOfObject="type",
            jsonValueOfObject="node",
            jsonMainNodeType="tags",
            jsonSubNodeType="amenity",
            jsonSubNodeValue="cafe",
            outputMapping={
                "id": "id",
                "lat": "lat",
                "lon": "lon",
                "tags": "tags"
            }
        )

class PoiAllFoodPoiBG(ExtractNode):
    def extractAllFoodPoi(self):
        return self.extractSpecificPoi(
            inputFilePath="data/raw_data/poiAllBg.json",
            outputFilePath="data/extracted_data/poiAllFoodBG.json",
            jsonTypeOfObject="type",
            jsonValueOfObject="node",
            jsonMainNodeType="tags",
            allowed_amenities=["cafe", "restaurant", "fast_food", "bar", "pub", "biergarten", "food_court"],
            allowed_cuisine=["balkan", "bar_and_grill", "barbecue", "burger", "chicken", "european", "fish", "fish_and_chips", "french", "greek", "grill", "gyros", "local", "national", "regional", "russian", "sandwich", "sausage", "seafood", "serbian", "shawarma", "spanish", "steak", "steak_house", "traditional", "wings", "домаћа"],
            outputMapping={
                "id": "id",
                "lat": "lat",
                "lon": "lon",
                "tags": "tags"
            }
        )
