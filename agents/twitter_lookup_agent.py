from langchain import PromptTemplate
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from tools.tools import get_profile_url
def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
       given the name {name_of_person} I want you to find a link/URL to their official Twitter profile page, and then extract their twitter username from the URL /link 
       Final answer must have person's username only"""
    tools_for_agent_twitter = [
        Tool(
            name="Crawl Google 4 Twitter profile page",
            func=get_profile_url,
            description="useful for when you need to get the username from Twitter Page URL",),
    ]
    agent = initialize_agent(
        tools_for_agent_twitter,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True)
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template)
    twitter_username = agent.run(prompt_template.format_prompt(name_of_person=name))
    return twitter_username