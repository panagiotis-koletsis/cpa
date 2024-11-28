from langchain_community.tools import DuckDuckGoSearchRun
import time

import wikipedia

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from promptTemplates import PROMPT_TEMPLATE_TYPO

def web_search(table):
    search = DuckDuckGoSearchRun()
    time.sleep(3)
    res = search.invoke(table['col0'][0])

    




    return res


def wikipedia_search(table):
    cor = correction(table['col0'][0])
    

    res = wikipedia.summary(cor)
    return res

model = "qwen2:7b"
def correction(text):
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE_TYPO)
    prompt = prompt_template.format(text=text)
    llm = OllamaLLM(model=model)

    res = f"""{llm.invoke(prompt)}"""
    return res 
