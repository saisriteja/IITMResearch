import pandas as pd
import os
import json


from src.research_info import get_all_info
def update_cache():

    # tags 
    all_paper_tags = []    

    json_file = 'cache/research_papers.json'

    all_papers = os.listdir('research_papers/all/')

    # check if the json file exists
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            info = json.load(f)
    else:
        info = {}

    # check if the paper name is in the json tag
        

    all_papers_json = list(info.keys())

    # diff between all_papers and all_papers_json
    all_papers = list(set(all_papers) - set(all_papers_json))

    for paper in all_papers:
        if paper not in info:
            file_info = get_all_info(f'research_papers/all/{paper}')
            info[paper] = file_info['Tags']
    
    # dump the json file
    with open(json_file, 'w') as f:
        json.dump(info, f, indent=4)

    return


if __name__ == '__main__':
    update_cache()

