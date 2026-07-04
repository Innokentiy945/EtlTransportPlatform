from fastapi import APIRouter

from etl.extract.raw_extract_roads_nbg import RoadNBGRawDataExtractor

router = APIRouter()

extractor = RoadNBGRawDataExtractor()


@router.post("/extract/roads")
async def extract_roads():
    await extractor.extract()
    return {"status": "extracted"}