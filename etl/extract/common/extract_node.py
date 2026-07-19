import json
import os
from decimal import Decimal

import ijson
from typing import Dict


class ExtractNode:

    def extractNode(self,
                    inputFilePath: str,
                    outputFilePath: str,
                    jsonTypeOfObject: str,
                    jsonValueOfObject: str,
                    jsonMainNodeType: str,
                    jsonSubNodeType: str,
                    jsonSubNodeValue: str,
                    outputMapping: Dict[str, str]):

        file = open(inputFilePath, "rb")

        os.makedirs(os.path.dirname(outputFilePath), exist_ok=True)
        out = open(outputFilePath, "w", encoding="utf8")

        results_list = []

        try:
            for element in ijson.items(file, "elements.item"):

                if (
                    element[jsonTypeOfObject] == jsonValueOfObject
                    and element.get(jsonMainNodeType)
                    and element[jsonMainNodeType].get(jsonSubNodeType) == jsonSubNodeValue
                ):
                    result = {}

                    for key, value in outputMapping.items():
                        result[key] = self._convert(element.get(value))

                    print(result["tags"])
                    # 2. Append the dictionary to the list
                    results_list.append(result)

            # 3. Write the entire valid JSON array at once
            json.dump(results_list, out, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f"Data were not extracted!: {e}")

        finally:
            file.close()
            out.close()

    def _convert(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, dict):
            return {k: self._convert(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._convert(v) for v in obj]
        return obj

    def extractSpecificPoi(self,
                           inputFilePath: str,
                           outputFilePath: str,
                           jsonTypeOfObject: str,
                           jsonValueOfObject: str,
                           jsonMainNodeType: str,
                           allowed_amenities: list,
                           allowed_cuisine: list,
                           outputMapping: Dict[str, str]):
        file = open(inputFilePath, "rb")

        os.makedirs(os.path.dirname(outputFilePath), exist_ok=True)
        out = open(outputFilePath, "w", encoding="utf8")

        results_list = []

        try:
            for element in ijson.items(file, "elements.item"):

                if (
                        element[jsonTypeOfObject] == jsonValueOfObject
                        and element.get(jsonMainNodeType)
                ):

                    tags = element.get(jsonMainNodeType, {})
                    current_amenity = tags.get("amenity")
                    current_cuisine = tags.get("cuisine")

                    if current_amenity in allowed_amenities and current_cuisine in allowed_cuisine:
                        result = {}

                        result["amenity"] = current_amenity
                        result["cuisine"] = current_cuisine


                        for key, value in outputMapping.items():
                            result[key] = self._convert(element.get(value))

                        print(result["tags"])
                        results_list.append(result)

            json.dump(results_list, out, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f"Data were not extracted!: {e}")

        finally:
            file.close()
            out.close()