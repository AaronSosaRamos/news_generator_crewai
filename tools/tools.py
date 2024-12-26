from crewai_tools import (
    SerperDevTool,
    ScrapeWebsiteTool
)

search_tool = SerperDevTool(n_results=10)
scrape_website_tool = ScrapeWebsiteTool()