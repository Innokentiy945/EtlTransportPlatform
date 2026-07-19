from etl.extract.common.extract_way import ExtractWay


class RoadsExtractionNbg(ExtractWay):
    def extractResidentalRoads(self):
        return self.extractWay(
            inputFilePath="data/raw_data/roadsAllNbg.json",
            outputFilePath="data/extracted_data/residentialRoadsNbg.json",
            jsonTypeOfObject="type",
            jsonValueOfObject="way",
            jsonMainNodeType="tags",
            jsonSubNodeType="highway",
            jsonSubNodeValue="residential",
            outputMapping={
                "id": "id",
                "tags": "tags",
                "geometry": "geometry"
            }
        )

    def extractPrimaryRoads(self):
        return self.extractWay(
            inputFilePath="data/raw_data/roadsAllNbg.json",
            outputFilePath="data/extracted_data/primaryRoadsNbg.json",
            jsonTypeOfObject="type",
            jsonValueOfObject="way",
            jsonMainNodeType="tags",
            jsonSubNodeType="highway",
            jsonSubNodeValue="primary",
            outputMapping={
                "id": "id",
                "geometry": "geometry",
                "tags": "tags"
            }
        )

    def extractSecondaryRoads(self):
        return self.extractWay(
            inputFilePath="data/raw_data/roadsAllNbg.json",
            outputFilePath="data/extracted_data/secondaryRoadsNbg.json",
            jsonTypeOfObject="type",
            jsonValueOfObject="way",
            jsonMainNodeType="tags",
            jsonSubNodeType="highway",
            jsonSubNodeValue="secondary",
            outputMapping={
                "id": "id",
                "geometry": "geometry",
                "tags": "tags"
            }
        )


