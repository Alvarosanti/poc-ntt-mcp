from pathlib import Path
from fastmcp import FastMCP
from fastmcp.server.apps import ToolUI

mcp = FastMCP("Suma Server")

# UI como resource ui:// (HTML)
@mcp.resource("ui://sum/view.html")
def suma_ui() -> str:
    return Path("./ui/index.html").read_text(encoding="utf-8")

# 1) Launcher: visible al modelo, muestra la UI
@mcp.tool(ui=ToolUI(resource_uri="ui://sum/view.html"))
def abrir_sumadora() -> dict:
    """Abre la UI de la sumadora."""
    return {}  # mantén esto mínimo para que no “ensucie” el chat

# 2) Lógica: solo visible para la UI
@mcp.tool(
    ui=ToolUI(
        resource_uri="ui://sum/view.html",
        visibility=["app"],
    )
)
def suma(a: float, b: float) -> dict:
    """Suma dos números (tool solo para la UI)."""
    return {"resultado": a + b}

if __name__ == "__main__":
    mcp.run()
