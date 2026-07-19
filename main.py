import asyncio
import uvicorn
from fastapi import FastAPI

import asyncio
from fastapi import FastAPI

from etl.data_orhestration.controller import router


app = FastAPI(
    title="Transport Data Platform"
)

app.include_router(router)


print("MAIN ROUTER:")
print(router.routes)
print(len(router.routes))

print("APP ROUTES:")
for route in app.routes:
    print(route.path)


async def main():
    pass


if __name__ == "__main__":
    asyncio.run(main())

    # await RoadNBGRawDataExtractor().extractRoadsRaw()
    # await  PoiNBGRawDataExtractor().extractPoiRaw()
    # RoadsExtractionNbg().extractResidentalRoads()
    # RoadsExtractionNbg().extractPrimaryRoads()
    # RoadsExtractionNbg().extractSecondaryRoads()