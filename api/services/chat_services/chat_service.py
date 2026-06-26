from dotenv import load_dotenv
from api.services.ai_service import response_for_conversions
from api.exceptions import custom_exception as exc
import httpx
import os


load_dotenv()

API_KEY = os.environ.get("API_KEY_AWESOME")


async def conversions_api_get(conversions: object) -> dict:

    currency_pair = f"{conversions.convert_currency.strip().upper()}-{conversions.converted.strip().upper()}"

    URL = f"https://economia.awesomeapi.com.br/json/last/{currency_pair}"

    headers = {}

    if API_KEY:
        headers["x-api-key"] = API_KEY

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(URL, headers=headers)

            if response.status_code == 404:
                raise exc.ConversionError()

            if response.status_code != 200:
                raise exc.ResponseError()

            data_conversion = response.json()

            response_ai = response_for_conversions(data_conversion=data_conversion)

            return response_ai

        except httpx.RequestError:
            raise exc.ResponseError()