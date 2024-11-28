import requests
import pandas as pd


#-------------------------------------------------------------------------------------- This section is only run the first time
# def wiki_repl_url(gt):
#     for i in range(len(gt)):
#         url = gt.iloc[i]['url']
#         ent = wikidata_entity(url)
#         print(ent)
#         gt.loc[i, 'url'] =  ent
        
#     save_dataset(gt)
#     return gt


# def wikidata_entity(url):
#     entity_id = url.split('/')[-1]
#     #print(entity_id)  # Output: Q17201685
#     url = f"https://www.wikidata.org/wiki/Special:EntityData/{entity_id}.json"
#     response = requests.get(url)
#     data = response.json()  # Parse the JSON response
#     entity_id = redir_check(data)
#     ent = data['entities'][entity_id]['labels']['en']['value']
#     #print(ent)
#     return ent

# def redir_check(data):
#     first_key = next(iter(data['entities']))
#     return first_key


# def save_dataset(gt):
#     gt.to_csv('data/gt.csv', index=False)
#----------------------------------------------------------------------------------------
     