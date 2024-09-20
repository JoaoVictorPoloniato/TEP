```python
from typing import Union

from langchain_core.tools import Tool
from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langflow.base.langchain_utilities.model import LCToolComponent
from langflow.inputs import SecretStrInput, MultilineInput, IntInput
from langflow.schema import Data


class TavilySearchAPIComponent(LCToolComponent):
    display_name = "Tavily Search API"
    description = "Call Tavily Search API."
    name = "TavilySearchAPI"

    inputs = [
        SecretStrInput(name="tavily_api_key", display_name="Tavily API Key", required=True),
        MultilineInput(
            name="input_value",
            display_name="Input",
        ),
        IntInput(name="max_results", display_name="Max Results", value=5, required=True),
    ]

    def run_model(self) -> Union[Data, list[Data]]:
        wrapper = self._build_wrapper()
        results = wrapper.run(self.input_value)
        data = [Data(data=result, text=result["content"]) for result in results]
        self.status = data
        return data

    def build_tool(self) -> Tool:
        wrapper = self._build_wrapper()
        return Tool(
            name="tavily_search",
            description="Search Tavily for recent results.",
            func=wrapper.run,
        )

    def _build_wrapper(self):
        try:
            from langchain_community.tools.tavily_search import TavilySearchResults
            from langchain.utilities.tavily_search import TavilySearchAPIWrapper
            tavilySearchAPIWrapper = TavilySearchAPIWrapper(tavily_api_key=self.tavily_api_key)
        except ImportError:
            raise ImportError("Please install langchain to use TavilySearchAPIWrapper.")
        return TavilySearchResults(api_wrapper=tavilySearchAPIWrapper)
```


