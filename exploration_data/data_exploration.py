import unittest
from typing import Dict

import ijson


class GettingTypesOfValue(unittest.TestCase):
    file_path_all_roads_nbg = r"C:\\TransportDataPlatform\\data\\raw_data\\roadsAllNbg.json"
    file_path_all_poi_nbg = r"C:\TransportDataPlatform\data\raw_data\poiAllNbg.json"
    file_path_all_poi_bg = r"C:\TransportDataPlatform\data\raw_data\poiAllBg.json"
    
    def test_get_type_of_roads(self):

        listRoadsTypes = []
        

        file = open(self.file_path_all_roads_nbg, "rb")

        try:
            for element in ijson.items(file, "elements.item"):

                if (
                    element["type"] == "way"
                    and element.get("tags")
                    and element.get("tags").get("highway")
                ):
                    listRoadsTypes.append(element["tags"].get("highway"))

        finally:
            file.close()

        print(set(listRoadsTypes))
        # {'track', 'platform', 'trunk', 'residential', 'tertiary_link', 'secondary', 'elevator', 'secondary_link', 'path', 'construction', 'tertiary', 'bridleway', 'primary', 'rest_area', 'services', 'primary_link', 'pedestrian', 'footway', 'proposed', 'corridor', 'ladder', 'service', 'unclassified', 'steps', 'living_street', 'cycleway', 'trunk_link'}


    def test_get_type_of_maxspeed(self):

        listMaxSpeed = []

        file = open(self.file_path_all_roads_nbg, "rb")

        try:
            for element in ijson.items(file, "elements.item"):

                if (
                    element["type"] == "way"
                    and element.get("tags")
                    and element.get("tags").get("maxspeed")
                ):
                    listMaxSpeed.append(element["tags"].get("maxspeed"))

        finally:
            file.close()

        print(set(listMaxSpeed))
        # {'50', '100', '30', '10', 'RS:rural', 'RS:living_street', '40', '5', '80', '60', 'RS:urban', '20'}

    def test_get_list_of_tags_roads(self):
        listTags = []

        file = open(self.file_path_all_roads_nbg, "rb")

        try:
            for element in ijson.items(file, "elements.item"):
                if element["type"] == "way" and element.get("tags"):
                    # Add every key inside the tags dictionary to the list
                    for key in element["tags"].keys():
                        listTags.append(key)

        finally:
            file.close()

        print(set(listTags))
# 'source:name', 'colour:arrow', 'footway', 'old_name:sr-Latn', 'note', 'cycleway:surface', 'motor_vehicle', 'destination', 'maxheight:signed', 'tourism', 'source:hgv', 'razed:frequency', 'maxspeed:practical:forward', 'width:lanes', 'traffic_calming', 'crossing_ref', 'vehicle', 'floating', 'lane_markings', 'sidewalk:left:surface', 'name:ru', 'name:1947-1951', 'check_date:ramp', 'parking:condition:right', 'turn:lanes:backward', 'cycleway:right:lane', 'name:1956-2016', 'colour:text', 'bridge', 'alt_name:sr-Latn', 'wikipedia', 'source:width', 'razed:electrified', 'fixme', 'junction', 'nat_ref', 'bus_bay:right:access', 'maxheight', 'change:lanes:forward', 'psv:lanes', 'parking:lane:left:perpendicular', 'parking', 'check_date:footway:surface', 'parking:left:taxi', 'short_name:sr-Latn', 'name:1946-1956', 'alt_name:en', 'ramp:stroller', 'name', 'seasonal', 'destination:symbol', 'maxspeed:backward:conditional', 'sidewalk:right:surface', 'alt_name', 'maxweightrating:hgv', 'shoulder', 'zone:maxspeed', 'cycleway:left', 'destination:ref:to', 'trolley_wire', 'destination:forward', 'int_ref', 'source', 'maxspeed:type', 'side', 'level', 'indoor', 'name:etymology:wikipedia', 'change:lanes:backward', 'wikidata', 'bin', 'cycleway:right', 'parking:both:orientation', 'parking:right:orientation', 'conveying', 'parking:lane:right:parallel', 'check_date:handrail', 'lit', 'parking:both:fee', 'parking:both:restriction', 'oneway:bicycle', 'wheelchair', 'handrail:right', 'parking:left:markings', 'opening_date', 'gauge', 'source:maxspeed:mapillary', 'source:destination', 'location', 'frequency', 'lanes:psv', 'foot:right', 'emergency', 'proposed:highway', 'proposed', 'temporary', 'parking:left:orientation', 'destination:colour:arrow', 'horse', 'destination:lang:sr-Latn', 'busway:right', 'alt_name:sr', 'parking:right:access', 'taxi', 'ref:RS:ulica', 'elevator', 'unofficial', 'width', 'source:destination:mapillary', 'name:1935-1942', 'parking:lane:both', 'maxspeed:forward', 'crossing:island', 'ramp:luggage', 'highway', 'old_ref', 'postal_code', 'parking:both:capacity', 'source:geometry', 'traffic_signals:sound', 'name:en', 'crossing:signals', 'destination:colour:text', 'mapillary', 'parking:left:fee:conditional', 'parking:right:maxstay', 'turn:lanes', 'access', 'int_name', 'short_name', 'parking:left', 'alt_name:int_name', 'destination:lanes', 'sidewalk:right', 'motor_vehicle:lanes', 'handrail:center', 'bench', 'destination:lang:sr:lanes', 'step_count', 'ramp', 'parking:right:fee:conditional', 'sidewalk:both', 'foot', 'oneway', 'noname', 'destination:lang:int:lanes', 'bicycle_road', 'railway', 'lanes:backward', 'name:sr-Latn', 'service', 'parking:left:capacity', 'cycleway', 'parking:condition:both', 'check_date:sidewalk', 'layer', 'usage', 'maxspeed:practical:backward', 'cutting', 'lanes:both_ways', 'destination:lang:sr:forward', 'traffic_signals:vibration', 'parking:left:restriction', 'supervised', 'embedded_rails:lanes', 'destination:lang:sr-Latn:backward', 'maxspeed:conditional', 'parking:left:maxstay', 'short_name:int_name', 'tourist_bus', 'covered', 'bus_bay', 'destination:lang:la', 'lanes', 'tactile_paving', 'motor_vehicle:conditional', 'parking:right:fee', 'parking:right:capacity', 'incline', 'cycleway:right:oneway', 'electrified', 'crossing:markings', 'parking:lane:left', 'parking:left:fee', 'steps', 'sidewalk:both:surface', 'parking:right:taxi', 'check_date:surface', 'bus', 'parking:both:markings', 'passenger_information_display', 'maxweightrating', 'button_operated', 'check_date', 'lanes:psv:backward', 'source:sign', 'source:url', 'destination:colour:back', 'bus:lanes:backward', 'motorcycle', 'description', 'place', 'name:etymology:wikidata', 'parking:right:restriction', 'shelter', 'bus:lanes', 'smoothness', 'start_date', 'overtaking', 'check_date:lit', 'dog', 'maxweight', 'parking:right', 'colour:back', 'parking:lane:right', 'ref', 'sidewalk:left', 'ramp:wheelchair', 'traffic_signals:direction', 'destination:lang:sr-Latn:lanes', 'old_name:sr', 'maxweight:conditional', 'lanes:psv:forward', 'image', 'parking:lane:left:parallel', 'voltage', 'short_name:sr', 'colour', 'placement:forward', 'cycleway:both', 'destination:lang:sr:backward', 'surface', 'razed:voltage', 'embankment', 'bridge:structure', 'change:lanes', 'fee', 'old_name', 'source:maxspeed', 'sac_scale', 'destination:lang:sr', 'destination:ref', 'placement', 'lanes:psv:conditional', 'parking:right:markings', 'man_made', 'sidewalk', 'handrail', 'razed:railway', 'name:1942-1946', 'maxweight:signed', 'disused:railway', 'public_transport', 'maxspeed:backward', 'parking:condition:left', 'parking:both:fee:conditional', 'segregated', 'destination:int_ref:to', 'parking:lane:both:perpendicular', 'old_name:en', 'turn:lanes:forward', 'cycleway:left:oneway', 'tracktype', 'disused', 'opening_hours', 'lanes:forward', 'handrail:left', 'source:cycleway:width', 'destination:backward', 'check_date:smoothness', 'hgv', 'motorroad', 'psv', 'parking:left:access', 'embedded_rails', 'footway:surface', 'destination:lang:sr-Latn:forward', 'ramp:bicycle', 'survey:date', 'busway', 'name:sr', 'toilets', 'parking:lane:right:perpendicular', 'cycleway:width', 'parking:both', 'tourist_bus:lanes', 'informal', 'parking:lane:both:diagonal', 'destination:int_ref', 'maxspeed', 'bicycle', 'maxspeed:practical', 'construction', 'alt_name:ru', 'priority', 'parking:both:maxstay', 'sur', 'crossing', 'tunnel', 'parking:right:restriction:taxi'}


    def test_get_list_amenities(self):
        listAmenities=[]
        
        file = open(self.file_path_all_poi_nbg, "rb")

        try:
            for element in ijson.items(file, "elements.item"):
                # 1. Access tags dictionary safely
                tags = element.get("tags")

                # 2. Check if type is node and tags exists, and if 'amenity' is inside tags
                if element.get("type") == "node" and tags and "amenity" in tags:
                    # 3. Directly append the value of the amenity (e.g., "hospital")
                    listAmenities.append(tags.get("amenity"))

        finally:
            file.close()

        print(set(listAmenities))
# {'waste_disposal',
# 'veterinary_pharmacy',
# 'table',
# 'prep_school',
# 'taxi',
# 'parcel_locker',
# 'payment_centre',
# 'kindergarten',
# 'fountain',
# 'music_school',
# 'compressed_air',
# 'courthouse',
# 'post_office',
# 'vacuum_cleaner',
# 'drinking_water',
# 'bar',
# 'veterinary',
# 'clinic',
# 'vehicle_inspection',
# 'research_institute',
# 'ferry_terminal',
# 'restaurant',
# 'shelter',
# 'bus_stop',
# 'language_school',
# 'ice_cream',
# 'events_venue',
# 'hookah_lounge',
# 'car_wash',
# 'cinema',
# 'shower',
# 'bicycle_repair_station',
# 'bicycle_parking',
# 'warehouse',
# 'dressing_room',
# 'bicycle_rental',
# 'college',
# 'school',
# 'recycling',
# 'fuel',
# 'doctors',
# 'cafe',
# 'currency_exchange',
# 'pharmacy', 'library', 'dancing_school', 'medical_laboratory', 'driving_school', 'bank', 'vending_machine', 'theatre', 'bureau_de_change', 'food_court', 'security_booth', 'telephone', 'atm', 'townhall', 'dentist', 'parking', 'charging_station', 'university', 'gambling', 'fast_food', 'casino', 'social_facility', 'office', 'fire_station', 'waste_basket', 'childcare', 'lounger', 'dojo', 'hospital', 'police', 'studio', 'marketplace', 'pub', 'parking_entrance', 'animal_boarding', 'place_of_worship', 'boat_sharing', 'boat_rental', 'car_rental', 'bench', 'toilets', 'nightclub', 'arts_centre', 'clock', 'community_centre', 'bbq'}

    def test_get_list_coisens(self):
        listCouisens=[]

        file = open(self.file_path_all_poi_bg, "rb")

        try:
            for element in ijson.items(file, "elements.item"):
                tags = element.get("tags")

                if element.get("type") == "node" and tags and "cuisine" in tags:
                    listCouisens.append(tags.get("cuisine"))

        finally:
            file.close()

        print(set(listCouisens))















