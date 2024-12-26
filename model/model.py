
from crewai import LLM
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

llm = LLM(
    model="gpt-4o",
    temperature=0.7
)