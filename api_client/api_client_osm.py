import asyncio
import httpx


class OverpassClient:
    URL = "https://overpass-api.de/api/interpreter"

    async def execute(self, query: str, retries: int = 3) -> dict:

        for attempt in range(retries):
            try:
                async with httpx.AsyncClient(timeout=300) as client:
                    response = await client.post(
                        self.URL,
                        data={"data": query},
                        headers={"User-Agent": "BelgradeRoadETL/1.0"}
                    )

                    response.raise_for_status()
                    return response.json()

            except httpx.HTTPStatusError as e:
                if e.response.status_code == 504:
                    wait = 5 * (attempt + 1)
                    print(f"Overpass timeout, retry in {wait}s...")
                    await asyncio.sleep(wait)
                else:
                    raise

        raise Exception("Overpass API failed after retries")