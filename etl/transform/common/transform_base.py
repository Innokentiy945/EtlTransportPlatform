import json
import os
from typing import Dict

import ijson


class TransformBase:

    def baseTransform(self, inputFilePath: str, outputFilePath: str, fieldsToAdd: list[Dict]):
        file = open(inputFilePath, "rb")
        os.makedirs(os.path.dirname(outputFilePath), exist_ok=True)
        out = open(outputFilePath, "w", encoding="utf8")

        try:
            for element in ijson.items(file, "elements.item"):
                for field in fieldsToAdd:
                    element.update(field)

                # FIX 1: Use your existing 'out' file instead of reopening 'file'
                # FIX 2: Pass 'element' to json.dump instead of 'element.update'
                json.dump(element, out, indent=4)

        except Exception as e:
            print(f"Data were not transformed: {e}")

        finally:
            file.close()
            out.close()

