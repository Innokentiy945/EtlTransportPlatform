from etl.transform.common.transform_geo_base import TransformGeoBase


class SpatialJoinPoiRoadsNbg(TransformGeoBase):
    def spatialCafesResidentialRoadsNbg(self):
        TransformGeoBase.spatialJoin(
            self,
            "data/extracted_data/cafesNbg.json",
            "data/extracted_data/residentialRoadsNbg.json",
        "data/transformed_data/cafesResidentialRoadsSpatial.json")