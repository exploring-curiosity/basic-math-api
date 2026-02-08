import asyncio
import pytest
from dedalus_mcp.client import MCPClient

MCP_SERVER_URL = "http://127.0.0.1:8000/mcp"

async def test_list_tools():
    """Verify exactly 5 tools are registered."""
    client = await MCPClient.connect(MCP_SERVER_URL)
    tools = await client.list_tools()
    await client.close()
    assert len(tools) == 5, f"Expected 5 tools, got {len(tools)}"

async def test_tool_schemas():
    """Each tool has name + description."""
    client = await MCPClient.connect(MCP_SERVER_URL)
    tools = await client.list_tools()
    await client.close()
    for tool in tools:
        assert "name" in tool, f"Tool missing name: {tool}"
        assert "description" in tool, f"Tool missing description: {tool}"

async def test_addnumbers():
    """Call addnumbers with sample args and verify string return."""
    client = await MCPClient.connect(MCP_SERVER_URL)
    result = await client.call_tool("addnumbers", {"a": 5, "b": 3})
    await client.close()
    assert isinstance(result, str), f"Expected string result, got {type(result)}"

async def test_dividenumbers():
    """Call dividenumbers with sample args and verify string return."""
    client = await MCPClient.connect(MCP_SERVER_URL)
    result = await client.call_tool("dividenumbers", {"a": 10, "b": 2})
    await client.close()
    assert isinstance(result, str), f"Expected string result, got {type(result)}"

async def test_healthcheck():
    """Call healthcheck and verify string return."""
    client = await MCPClient.connect(MCP_SERVER_URL)
    result = await client.call_tool("healthcheck", {})
    await client.close()
    assert isinstance(result, str), f"Expected string result, got {type(result)}"

async def test_multiplynumbers():
    """Call multiplynumbers with sample args and verify string return."""
    client = await MCPClient.connect(MCP_SERVER_URL)
    result = await client.call_tool("multiplynumbers", {"a": 4, "b": 5})
    await client.close()
    assert isinstance(result, str), f"Expected string result, got {type(result)}"

async def test_subtractnumbers():
    """Call subtractnumbers with sample args and verify string return."""
    client = await MCPClient.connect(MCP_SERVER_URL)
    result = await client.call_tool("subtractnumbers", {"a": 8, "b": 3})
    await client.close()
    assert isinstance(result, str), f"Expected string result, got {type(result)}"

async def main():
    """Run all test functions."""
    await test_list_tools()
    await test_tool_schemas()
    await test_addnumbers()
    await test_dividenumbers()
    await test_healthcheck()
    await test_multiplynumbers()
    await test_subtractnumbers()
    print("All tests passed!")

if __name__ == "__main__":
    asyncio.run(main())