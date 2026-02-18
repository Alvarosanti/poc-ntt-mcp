from pathlib import Path
from fastmcp import FastMCP
from fastmcp.server.apps import ToolUI

mcp = FastMCP("Suma Server")

# Registrar la UI
@mcp.resource("ui://sum/view.html")
def suma_ui() -> str:
    return Path("./ui/index.html").read_text()

# Tool solo visible para la App
@mcp.tool(
    ui=ToolUI(
        resource_uri="ui://sum/view.html",
        visibility=["app"]
    )
)
def suma(a: float, b: float) -> dict:
    return {"resultado": a + b}

if __name__ == "__main__":
    mcp.run()
