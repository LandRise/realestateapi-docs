# Real Estate API MCP Server - Connection Guide

This guide explains how to connect to the Real Estate API MCP (Model Context Protocol) server using your API key. Our MCP server is built with FastMCP and supports standard MCP connections.

## Authentication

The Real Estate API MCP server requires an API key for authentication. You can provide this key in two ways:
- **URL Parameter**: `x-api-key=YOUR_API_KEY`
- **HTTP Header**: `x-api-key: YOUR_API_KEY`

## Connection Methods

### 1. Claude Desktop & MCP-Compatible Applications

For applications that support MCP configuration files (like Claude Desktop), add the following to your configuration:

```json
{
  "mcpServers": {
    "realestateapi-mcp": {
      "url": "https://mcp.realestateapi.com/sse",
      "headers": {
        "x-api-key": "YOUR_API_KEY"
      }
    }
  }
}
```

**Configuration file locations:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### 2. Programmatic Integration (Claude API)

When building applications that call the Claude API with MCP server support, use the following configuration:

```javascript
const mcpServers = [
  {
    type: "url",
    url: "https://mcp.realestateapi.com/sse?x-api-key=YOUR_API_KEY",
    name: "realestateapi-mcp",
    tool_configuration: {
      enabled: true
    }
  }
]
```

Then pass this configuration when making API calls to Claude.

### 3. Other MCP-Compatible Clients

Our MCP server works with any client or application that implements the Model Context Protocol standard. Simply use either:
- **URL with parameter**: `https://mcp.realestateapi.com/sse?x-api-key=YOUR_API_KEY`
- **Base URL with headers**: Configure the client to send the `x-api-key` header if supported

## Quick Start

1. Obtain your API key from the RealEstateAPI dashboard
2. Choose your connection method based on your use case
3. Replace `YOUR_API_KEY` with your actual API key
4. For desktop applications, restart the app after updating configuration
5. Test the connection by querying real estate data through the MCP tools

## Compatibility

This MCP server is compatible with:
- Claude Desktop
- Applications using the Anthropic API with MCP support
- Any MCP-compliant client or framework
- Custom applications implementing the MCP protocol

## Support

For additional help or to report issues, please visit our documentation at [your-support-url] or contact our support team.