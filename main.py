import os
import httpx
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("Exchange Rate MCP Server")

EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
if not EXCHANGE_RATE_API_KEY:
    raise EnvironmentError("EXCHANGE_RATE_API_KEY is not set in environment variables.")


@mcp.tool
async def convert_currency(amount: float, base_curr: str, target_curr: str) -> str:
    """Convert an amount from one currency to another using current exchange rates."""

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{base_curr.upper()}/{target_curr.upper()}/{amount}")
            response.raise_for_status()
            data = response.json()

            if data.get("result") == "error":
                error_type = data.get("error-type", "unknown")
                if error_type == "unknown-code":
                    raise Exception(f"Unknown currency code: {base_curr} or {target_curr}")
                elif error_type == "malformed-request":
                    raise Exception("Invalid request format")
                elif error_type == "invalid-key":
                    raise Exception("Invalid API key")
                elif error_type == "inactive-account":
                    raise Exception("API account inactive")
                elif error_type == "quota-reached":
                    raise Exception("API quota exceeded")
                else:
                    raise Exception(f"API error: {error_type}")
        
            return f"{amount} {base_curr.upper()} = {data.get('conversion_result'):.2f} {target_curr.upper()} (Rate: {data.get('conversion_rate')})"
        
    except httpx.HTTPStatusError as e:
        raise Exception(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        raise Exception(f"Request error occurred: {str(e)}")
    except Exception as e:
        raise Exception(f"Unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    mcp.run()
