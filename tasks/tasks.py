from crewai import Task

class TaskManager:
    def __init__(self, agents):
        self.agents = agents
        self.tasks = None

    def initialize_tasks(self, topic):
        self.tasks = {
            "research_task": Task(
                description=(f"""
                    1. Conduct comprehensive research on {topic} including:
                        - Recent developments and news
                        - Key industry trends and innovations
                        - Expert opinions and analyses
                        - Statistical data and market insights
                    2. Evaluate source credibility and fact-check all information
                    3. Organize findings into a structured research brief
                    4. Include all relevant citations and sources
                """),
                expected_output="""A detailed research report containing:
                    - Executive summary of key findings
                    - Comprehensive analysis of current trends and developments
                    - List of verified facts and statistics
                    - All citations and links to original sources
                    - Clear categorization of main themes and patterns
                    Please format with clear sections and bullet points for easy reference.""",
                agent=self.agents["senior_research_analyst"]
            ),
            "web_scraping_task": Task(
                description=("""
                    Using the sources provided by the Senior Research Analyst:
                    1. Scrape content from the provided URLs.
                    2. Extract relevant and structured information such as:
                        - Key data points
                        - Relevant quotes and statistics
                        - Summary of critical ideas
                    3. Filter out irrelevant or redundant content.
                    4. Organize the scraped data into a clean, structured format.
                """),
                expected_output="""A structured dataset or summary containing:
                    - Key data points extracted from sources
                    - Relevant quotes and their context
                    - Organized themes and subtopics for further content creation
                    - All original source URLs for reference""",
                agent=self.agents["web_scraper"]
            ),
            "writing_task": Task(
                description=("""
                    Using the research brief and scraped data provided:
                    1. Create an engaging blog post that:
                        - Transforms technical information into accessible content
                        - Maintains all factual accuracy and citations from the research
                    2. Includes:
                        - Attention-grabbing introduction
                        - Well-structured body sections with clear headings
                        - Compelling conclusion
                    3. Preserves all source citations in [Source: URL] format.
                    4. Includes a References section at the end.
                """),
                expected_output="""A polished blog post in markdown format that:
                    - Engages readers while maintaining accuracy
                    - Contains properly structured sections
                    - Includes inline citations hyperlinked to the original source URL
                    - Presents information in an accessible yet informative way
                    - Follows proper markdown formatting, using H1 for the title and H3 for the sub-sections.""",
                agent=self.agents["content_writer"]
            )
        }

    def get_tasks(self):
        if self.tasks is None:
            raise ValueError("Tasks have not been initialized. Call 'initialize_tasks(topic)' first.")
        return self.tasks
