### Sistemas de multi-agentes de inteligencias artificiais

# Biblioteca
from crewai_tools import tool
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

# Modelo LLM - Llama3 70B
llm = ChatGroq(temperature=0.7,
               groq_api_key='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',
               model_name='llama3-70b-8192')

# Ferramentas - Busca na internet com DuckDuckGo
@tool('DuckDuckGoSearchRun')
def search_tool(search_query: str):
  ''' Search the web for infotmation on a given topic'''
  return DuckDuckGoSearchRun().run(search_query)

# Topico do blog
topic = "Queimadas no Mato Grosso"

# Agentes
researcher = Agent(
    role = "Senior Researcher",
    goal = f"Pesquisar noticias sobre {topic}.",
    backstory = "Um pesquisador experiente que tem muito engajamento e curiosidade no estado de mato grosso",
    verbose = True,
    tools = [search_tool],
    llm = llm,
)

writer = Agent(
    role = "Top Writer",
    goal = f"Cria noticias sobre o  {topic}. ",
    backstory = "Escritor renomado que escreve noticias para o jornal",
    verbose = True,
    tools = [search_tool],
    llm = llm,
)

# Tarefas
research_task = Task(
    description = f"Investigue sobre o {topic}.",
    expected_output = "Escreva em 3 paragrafos em portugues brasil",
    tools = [search_tool],
    agent = researcher,
)

write_task = Task(
    description = f"escreva sobre o {topic}, falando as principais causas.",
    expected_output = f"Escreva sobre o {topic}, em 3 paragrafos",
    tools = [search_tool],
    agent = researcher,
    output_file = "queimadasmt"
)

# Orquestrador
crew = Crew(
    agents=[researcher, writer],
    tasks = [research_task, write_task]
)

result = crew.kickoff(
    inputs = {"topic": topic}
)
