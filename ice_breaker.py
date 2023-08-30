import os

# from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
# Load the .env file
# load_dotenv()


from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello Langchain")
    linkedin_profile_url = linkedin_lookup_agent(name="Bill gates")

    summary_template = """
    given the information {information} about a person i want you to create:
    1. A Short summary
    2. Two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )

    print(chain.run(information=linkedin_data))

    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/williamhgates")
    # print(linkedin_data.json())
