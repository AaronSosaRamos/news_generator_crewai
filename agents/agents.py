from crewai import Agent
from tools.tools import (
    search_tool,
    scrape_website_tool
)

class AgentManager:
    def __init__(self, llm):
        self.llm = llm
        self.agents = None

    def initialize_agents(self, topic):
        self.agents = {
            "senior_research_analyst": Agent(
                role="Senior Research Analyst",
                goal=f"Research, analyze, and synthesize comprehensive information on {topic} from reliable web sources",
                backstory="You're an expert research analyst with advanced web research skills. "
                          "You excel at finding, analyzing, and synthesizing information from "
                          "across the internet using search tools. You're skilled at "
                          "distinguishing reliable sources from unreliable ones, "
                          "fact-checking, cross-referencing information, and "
                          "identifying key patterns and insights. You provide "
                          "well-organized research briefs with proper citations "
                          "and source verification. Your analysis includes both "
                          "raw data and interpreted insights, making complex "
                          "information accessible and actionable.",
                allow_delegation=False,
                verbose=True,
                tools=[search_tool],
                llm=self.llm
            ),
            "web_scraper": Agent(
                role="Web Scraper",
                goal="Extract and organize relevant content from the websites retrieved by the Senior Research Analyst",
                backstory="A highly efficient and accurate web scraping agent designed to collect, clean, and structure "
                          "valuable content from online sources identified by the Senior Research Analyst. This agent ensures "
                          "data integrity by filtering out irrelevant or redundant information and presenting it in a usable format. "
                          "It specializes in extracting structured and unstructured data, preserving context, and highlighting key points "
                          "to aid in the Content Writer’s task of creating engaging posts.",
                allow_delegation=False,
                verbose=True,
                tools=[scrape_website_tool],
                llm=self.llm
            ),
            "content_writer": Agent(
                role="Content Writer",
                goal="Transform research findings into engaging blog posts while maintaining accuracy",
                backstory="You're a skilled content writer specialized in creating "
                          "engaging, accessible content from technical research. "
                          "You work closely with the Senior Research Analyst and the Web Scraper to ensure a smooth flow of "
                          "information and excel at maintaining the perfect balance between informative and entertaining writing, "
                          "while ensuring all facts and citations from the research are properly incorporated. You have a talent for making "
                          "complex topics approachable without oversimplifying them.",
                allow_delegation=False,
                verbose=True,
                llm=self.llm
            )
        }

    def get_agents(self):
        if self.agents is None:
            raise ValueError("Agents have not been initialized. Call 'initialize_agents(topic)' first.")
        return self.agents