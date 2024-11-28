import pandas as pd
from files import read_datasets, read_gt
#from wiki_data import wiki_repl_url
from llms import llm
from eval import eval




def main():
    dataframes, fn = read_datasets()
    print(len(dataframes), len(fn))
    gt = read_gt()
    print(len(gt))
    print(gt)
    

    llm_list = llm(dataframes, fn, gt)


    acc = eval(gt,llm_list)
    print(acc)


    
                

    















if __name__ == "__main__":
    main()


