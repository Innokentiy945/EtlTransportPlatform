from etl.extract.common.extract_base import BaseExtraction


class RoadsExtraction(BaseExtraction):
    def extractResidentalRoads(self):
        return self.extractBase(
            inputFilePath="data/raw_data/roadsAllNbg.json",
            outputFilePath="data/extracted_data/residentialRoads.json",
            jsonTypeOfObject="type",
            jsonValueOfObject="way",
            jsonMainNodeType="tags",
            jsonSubNodeType="highway",
            jsonSubNodeValue="residential",
            outputMapping={
                "id": "id",
                "tags": "tags"
            }
        )

    def extractPrimaryRoads(self):
        return self.extractBase(
            inputFilePath="data/raw_data/roadsAllNbg.json",
            outputFilePath="data/extracted_data/primaryRoads.json",
            jsonTypeOfObject="type",
            jsonValueOfObject="way",
            jsonMainNodeType="tags",
            jsonSubNodeType="highway",
            jsonSubNodeValue="primary",
            outputMapping={
                "id": "id",
                "tags": "tags"
            }
        )

    def extractSecondaryRoads(self):
        return self.extractBase(
            inputFilePath="data/raw_data/roadsAllNbg.json",
            outputFilePath="data/extracted_data/secondaryRoads.json",
            jsonTypeOfObject="type",
            jsonValueOfObject="way",
            jsonMainNodeType="tags",
            jsonSubNodeType="highway",
            jsonSubNodeValue="secondary",
            outputMapping={
                "id": "id",
                "tags": "tags"
            }
        )


