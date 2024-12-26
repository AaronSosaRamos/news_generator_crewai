from crewai import Crew
from model.model import llm
from agents.agents import AgentManager
from tasks.tasks import TaskManager

def generate_content(topic):

    agent_manager = AgentManager(llm=llm)
    agent_manager.initialize_agents(topic)

    agents = agent_manager.get_agents()

    senior_research_analyst_agent = agents["senior_research_analyst"]
    web_scraper_agent = agents["web_scraper"]
    content_writer_agent = agents["content_writer"]

    task_manager = TaskManager(agents=agents)
    task_manager.initialize_tasks(topic)

    tasks = task_manager.get_tasks()

    research_task = tasks["research_task"]
    web_scraping_task = tasks["web_scraping_task"]
    writing_task = tasks["writing_task"]

    crew = Crew(
        agents=[
            senior_research_analyst_agent,
            web_scraper_agent,
            content_writer_agent
        ],
        tasks=[
            research_task,
            web_scraping_task,
            writing_task
        ],
        verbose=True
    )

    return crew.kickoff(inputs={"topic": topic})