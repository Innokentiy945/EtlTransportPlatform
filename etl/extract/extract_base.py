import json
import os
from collections.abc import MutableMapping

import ijson


class BaseExtraction:

    def extractBase(
        self,
        inputFilePath,
        jsonTypeOfObject,
        jsonValueOfObject,
        jsonMainNodeType,
        jsonSubNodeType,
        jsonSubNodeValue,
        outputMapping,
        outputFilePath
    ):
        file = open(inputFilePath, "rb")

        os.makedirs(os.path.dirname(outputFilePath), exist_ok=True)
        out = open(outputFilePath, "w", encoding="utf8")

        try:
            for element in ijson.items(file, "elements.item"):

                if (
                    element[jsonTypeOfObject] == jsonValueOfObject
                    and element.get(jsonMainNodeType)
                    and element[jsonMainNodeType].get(jsonSubNodeType) == jsonSubNodeValue
                ):
                    result = {}

                    for key, value in outputMapping.items():
                        result[key] = element.get(value)

                    json.dump(result, out, ensure_ascii=False)
                    out.write("\n")

        finally:
            file.close()
            out.close()