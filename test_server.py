import asyncio
import json
from typing import Any
import pytest
from dedalus_mcp.client import MCPClient

async def test_list_tools():
    """Verify exactly 5 tools are registered."""
    async with await MCPClient.connect("http://127.0.0.1:8000/mcp") as client:
        tools = await client.list_tools()
        assert len(tools) == 5, f"Expected 5 tools, got {len(tools)}"

async def test_tool_schemas():
    """Each tool has name + description."""
    async with await MCPClient.connect("http://127.0.0.1:8000/mcp") as client:
        tools = await client.list_tools()
        for tool in tools:
            assert "name" in tool, f"Tool missing name: {tool}"
            assert "description" in tool, f"Tool missing description: {tool}"

async def test_addnumbers():
    """Call tool 'addnumbers' with sample args."""
    async with await MCPClient.connect("http://127.0.0.1:8000/mcp") as client:
        result = await client.call_tool("addnumbers", {"a": 5, "b": 3})
        assert isinstance(result, str)
        data = json.loads(result)
        assert "result" in data, f"Unexpected response: {result}"

async def test_dividenumbers():
    """Call tool 'dividenumbers' with sample args."""
    async with await MCPClient.connect("http://127.0.0.1:8000/mcp") as client:
        result = await client.call_tool("dividenumbers", {"a": 10, "b": 2})
        assert isinstance(result, str)
        data = json.loads(result)
        assert "result" in data, f"Unexpected response: {result}"

async def test_healthcheck():
    """Call tool 'healthcheck' with sample args."""
    async with await MCPClient.connect("http://127.0.0.1:8000/mcp") as client:
        result = await client.call_tool("healthcheck", {})
        assert isinstance(result, str)
        data = json.loads(result)
        assert "status" in data, f"Unexpected response: {result}"

async def test_multiplynumbers():
    """Call tool 'multiplynumbers' with sample args."""
    async with await MCPClient.connect("http://127.0.0.1:8000/mcp") as client:
        result = await client.call_tool("multiplynumbers", {"a": 4, "b": 5})
        assert isinstance(result, str)
        data = json.loads(result)
        assert "result" in data, f"Unexpected response: {result}"

async def test_subtractnumbers():
    """Call tool 'subtractnumbers' with sample args."""
    async with await MCPClient.connect("http://127.0.0.1:8000/mcp") as client:
        result = await client.call_tool("subtractnumbers", {"a": 8, "b": 3})
        assert isinstance(result, str)
        data = json.loads(result)
        assert "result" in data, f"Unexpected response: {result}"

async def main():
    """Run all tests."""
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