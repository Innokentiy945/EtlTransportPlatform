import unittest
import ijson


class GettingTypesOfValue(unittest.TestCase):

    def test_get_type_of_roads(self):

        list = []
        file_path = "C:\\TransportDataPlatform\\data\\raw_data\\roadsAllNbg.json"

        file = open(file_path, "rb")

        try:
            for element in ijson.items(file, "elements.item"):

                if (
                    element["type"] == "way"
                    and element.get("tags")
                    and element.get("tags").get("highway")
                ):
                    list.append(element["tags"].get("highway"))

        finally:
            file.close()

        print(set(list))
        # {'track', 'platform', 'trunk', 'residential', 'tertiary_link', 'secondary', 'elevator', 'secondary_link', 'path', 'construction', 'tertiary', 'bridleway', 'primary', 'rest_area', 'services', 'primary_link', 'pedestrian', 'footway', 'proposed', 'corridor', 'ladder', 'service', 'unclassified', 'steps', 'living_street', 'cycleway', 'trunk_link'}


    def test_get_type_of_maxspeed(self):

        list = []
        file_path = "C:\\TransportDataPlatform\\data\\raw_data\\roadsAllNbg.json"

        file = open(file_path, "rb")

        try:
            for element in ijson.items(file, "elements.item"):

                if (
                    element["type"] == "way"
                    and element.get("tags")
                    and element.get("tags").get("maxspeed")
                ):
                    list.append(element["tags"].get("maxspeed"))

        finally:
            file.close()

        print(set(list))
        # {'50', '100', '30', '10', 'RS:rural', 'RS:living_street', '40', '5', '80', '60', 'RS:urban', '20'}













