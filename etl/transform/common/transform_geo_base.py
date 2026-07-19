import json
import os
from typing import Dict
import geopandas
import ijson
from shapely.geometry import Point, LineString


class TransformGeoBase:

    def spatialJoin(self, inputPathOne: str, inputPathTwo: str, outputResult: str):
        try:
            points = self.__loadGeoJson(inputPathOne)
            roads = self.__loadGeoJson(inputPathTwo)

            points = points.to_crs(3857)
            roads = roads.to_crs(3857)

            result = geopandas.sjoin_nearest(
                points, roads, how="left", distance_col="distance_m"
            )

            result = result.to_crs(4326)
            os.makedirs(os.path.dirname(outputResult), exist_ok=True)
            result.to_file(
                outputResult,
                driver="GeoJSON",
                encoding="utf-8"
            )
            self.__removeAllNullValues(outputResult)

        except Exception as e:
            print(e)

    @staticmethod
    def __loadGeoJson(inputPath: str):
        with open(inputPath, "r", encoding="utf-8") as f:
            data = json.load(f)

        rows = []

        for item in data:
            row = {
                "id": item.get("id"),
                **item.get("tags", {})
            }

            if "lat" in item and "lon" in item:
                row["geometry"] = Point(item["lon"], item["lat"])
            elif "geometry" in item:
                row["geometry"] = LineString(
                    [(point["lon"], point["lat"]) for point in item["geometry"]]
                )

            rows.append(row)

        return geopandas.GeoDataFrame(
            rows,
            geometry="geometry",
            crs="EPSG:4326"
        )

    @staticmethod
    def __removeAllNullValues(inputPath: str):
        with open(inputPath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for feature in data.get('features', []):
            properties = feature.get('properties', {})

            keys_to_delete = []
            for key, value in properties.items():
                if value is None:
                    keys_to_delete.append(key)

            for key in keys_to_delete:
                del properties[key]

        with open(inputPath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return inputPath





