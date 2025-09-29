# Exchange Rate MCP Server

A Model Context Protocol (MCP) server that provides currency conversion functionality using the ExchangeRate-API.

## Features

- Convert amounts between different currencies using real-time exchange rates
- Support for about 161 currencies currently
- Error handling for invalid currency codes, API errors, and network issues

## Setup

### Prerequisites

- Python 3.12+
- `uv` package manager 
- ExchangeRate-API key (free tier available)

### Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Copy the `.env.example` file into your `.env`:
   ```
   cp .env.example .env
   ```
4. Replace `your_api_key` in the `.env` with your actual API key. 

   >You can get your free API key from [ExchangeRate-API](https://exchangerate-api.com/)

### Configuration

Copy and paste this in the `claude_desktop_config.json` file:

```json
{
  "mcpServers": {
    "exchange-rate-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/exchange-rate-mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

## Usage

Once configured, you can use the `convert_currency` tool in Claude to convert between currencies:

- `convert_currency(100, "USD", "EUR")` - Convert 100 USD to EUR
- `convert_currency(50, "GBP", "JPY")` - Convert 50 GBP to JPY

## Troubleshooting

- **"uv: command not found"**: Make sure `uv` is installed and the full path is specified in the configuration
- **"Invalid API key"**: Check that your `.env` file contains a valid ExchangeRate-API key