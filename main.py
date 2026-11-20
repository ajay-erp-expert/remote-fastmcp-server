from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("remote-mcp-server")


# MCP tool: this is what Claude (or any MCP client) can actually call
@mcp.tool
def hello(name: str = "World") -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"


# Plain HTTP route (NOT an MCP tool): handy as a health check
@mcp.custom_route("/health", methods=["GET"])
async def health(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")


if __name__ == "__main__":
    # MCP endpoint will be at http://<host>:8000/mcp
    mcp.run(transport="http", host="0.0.0.0", port=8000)
