"""Interface for tools."""
from typing import Optional

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.tools.base import BaseTool, Tool, tool


class InvalidTool(BaseTool):
    """Tool that is run when invalid tool name is encountered by agent."""

    name = "invalid_tool"
    description = "Called when tool name is invalid."

    def _run(
        self, tool_name: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        return f"""{tool_name} is not a valid tool, choose a valid tool and use this schema:
Thought: I want to use the tool *tool_name*
Action: *tool_name*
Action Input: *input for the tool ....*
"""

    async def _arun(
        self,
        tool_name: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        return f"""{tool_name} is not a valid tool, choose a valid tool and use this schema:
Thought: I want to use the tool *tool_name*
Action: *tool_name*
Action Input: *input for the tool ....*
"""


__all__ = ["InvalidTool", "BaseTool", "tool", "Tool"]
