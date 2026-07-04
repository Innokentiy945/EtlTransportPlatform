import asyncio

from etl.extract.extract_road_types import RoadsExtraction
from etl.extract.raw_extract_roads_nbg import RoadNBGRawDataExtractor


async def main():
    allRoadsExtract = RoadNBGRawDataExtractor()
    await allRoadsExtract.extract()

    RoadsExtraction().extractResidentalRoads()
    RoadsExtraction().extractPrimaryRoads()
    RoadsExtraction().extractSecondaryRoads()


if __name__ == "__main__":
    asyncio.run(main())