from fastapi import APIRouter

from etl.extract.raw_extract.extract_poi_all_bg_raw import ExtractPoiAllBg
from etl.extract.raw_extract.extract_poi_nbg_raw import PoiNBGRawDataExtractor
from etl.extract.raw_extract.extract_roads_nbg_raw import RoadNBGRawDataExtractor
from etl.extract.speсific_extract.extract_poi_types_nbg import PoiCafesExtractingNbg, PoiAllFoodPoiBG
from etl.extract.speсific_extract.extract_road_types_nbg import RoadsExtractionNbg
from etl.transform.create_poi_roads_set import SpatialJoinPoiRoadsNbg

router = APIRouter()

@router.post("/extract/roadsNbgRaw")
async def extract_roads_nbg_raw():
    await RoadNBGRawDataExtractor().extractRoadsRaw()

@router.post("/extract/poiCafeNbgRaw")
async def extract_poi_cafe_nbg_raw():
    await PoiNBGRawDataExtractor().extractPoiNbgRaw()

@router.post("/extract/poiAllBgRaw")
async def extract_poi_all_bg_raw():
    await ExtractPoiAllBg().exractPoiAllBgRaw()

@router.post("/extract/allFoodPoiBG")
def extract_all_food_poi_bg():
    PoiAllFoodPoiBG().extractAllFoodPoi()

@router.post("/extract/residentialRoadsNbg")
def extract_residential_roads_nbg():
    RoadsExtractionNbg().extractResidentalRoads()

@router.post("/extract/primaryRoadsNbg")
def extract_primary_roads_nbg():
    RoadsExtractionNbg().extractPrimaryRoads()

@router.post("/extract/secondaryRoadsNbg")
def extract_secondary_roads_nbg():
    RoadsExtractionNbg().extractSecondaryRoads()

@router.post("/extract/poiCafesNbg")
def extract_poi_cafes_nbg():
    PoiCafesExtractingNbg().extractPoiCafeNbg()

@router.post("/transform/cafesRoadsSpatialNbg")
def transform_cafes_roads_spatial_nbg():
    SpatialJoinPoiRoadsNbg().spatialCafesResidentialRoadsNbg()
