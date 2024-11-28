import re

def eval(gt, llm_list):

    gt, llm_list = preprocess(gt,llm_list)

    set1 = set(tuple(sublist) for sublist in llm_list)
    #print("-----------set1",set1)
    set2 = set(tuple(sublist) for sublist in gt)
    #print("*******set2",set2)
    # Calculate intersection and union
    matches = set1.intersection(set2)
    #print("matches", matches)
    total_unique = set1.union(set2)
    
    # Calculate accuracy
    #accuracy = len(matches) / len(total_unique)
    accuracy = len(matches) / len(llm_list)
    return accuracy


def preprocess(gt,llm_list):
    llm_list = [item for sublist in llm_list for item in sublist]
    #print(llm_list)
    for i in range(len(llm_list)):
        llm_list[i][3] = llm_list[i][3].lower().replace("_"," ")
        if not re.match(r'\d', llm_list[i][1]):
            llm_list[i][1] = 0
        if not re.match(r'\d', llm_list[i][2]):
            llm_list[i][2] = 1
        llm_list[i][1] = int(llm_list[i][1])
        llm_list[i][2] = int(llm_list[i][2])
        #llm_list[i][3] = re.sub(r'\(.*?\)', '', llm_list[i][3])
    print(llm_list)
    gt = gt.values.tolist()

    return gt, llm_list