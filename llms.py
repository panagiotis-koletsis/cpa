from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from promptTemplates import PROMPT_TEMPLATE, PROMPT_TEMPLATE_STRUCTURING
from content import web_search, wikipedia_search

model = "gemma2:9b"
def llm(dataframes, fn, gt):
    distinct_values = gt['url'].unique()
    print("--------------",len(distinct_values))
    llm_gt = []
    for i in range(len(dataframes)):
        table = dataframes[i]

        #web_search 
        #cont = web_search(table)
        #cont = wikipedia_search(table)


        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(table=table,distinct_values=distinct_values)
        #print(prompt)
        #prompt = prompt_template.format(table=table)
        llm = OllamaLLM(model=model)
        res = f"""{llm.invoke(prompt)}"""
        print(table)
        print("---res",res)
        print_gt(gt,fn[i])
        # Find the position of the last "|"
        last_pipe_pos = res.rfind('|')
        # Extract everything up to (but not including) the last "|"
        res = res[:last_pipe_pos].strip()
        # print("--TABLE\n",table,"----")
        #print(res)
        try:
            llm_list = llmLlist(res)
        except IndexError:
            print("IndexError1")
            try:
                res = structuringLlm(res)
                llm_list = llmLlist(res)
            except IndexError:
                print('IndexError2')
                res = []

        llm_list = processList(llm_list,fn[i])
        llm_gt.append(llm_list)
        #print(llm_list)
    #print(llm_gt)
    return llm_gt    


def print_gt(gt,fn):
    for i in range(len(gt)):
        if gt['table_id'][i] == fn:
            print("++++++++++++++++",gt['column_1'][i],gt['column_2'][i],gt['url'][i])



model_structuring = "qwen2:7b"
def structuringLlm(res):
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE_STRUCTURING)
    prompt = prompt_template.format(res=res)
    llm = OllamaLLM(model=model)
    res = f"""{llm.invoke(prompt)}"""
    return res



def processList(llm_list,table_id):
    llm_list = [[item.replace('col', '') for item in sublist] for sublist in llm_list]
    for i in range(len(llm_list)):
        llm_list[i].insert(0,table_id)
        temp = llm_list[i][2]
        llm_list[i][2] = llm_list[i][3]
        llm_list[i][3] = temp
    return llm_list    



def llmLlist(res):
    # Split the text into lines and remove the header and delimiter lines
    lines = res.strip().split('\n')

    # Initialize the result list
    llm_list = []

    # Process each line to extract elements
    for line in lines:  # Skip the header line
        elements = line.strip('|').split('|')
        # Add the relation in the expected order
        llm_list.append([elements[0].strip(), elements[1].strip(), elements[2].strip()])

    if llm_list[0][0] == 'col':
        llm_list.pop(0)
    if llm_list[0][0] == '---':
        llm_list.pop(0)


    return llm_list