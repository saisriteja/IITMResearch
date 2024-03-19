# Research PaperName	
# Priority	
# Conference 	
# Year	
# Lab	
# Github / Project	


# Abstract	
# Results	
# Future Works	


# Gaps in research ps	
# Gaps in methodology	
# Explicit Limits	


# Changing Task of Interest	
# Change in eval strategy	
# change the proposed method	


# Global Structure	
# Seq of figs	
# Abstract Structure	
# Intro Structure	
# Related work structure	
# Conclusion Structure	
# method and exp structure


import re



keys = [
    'Research PaperName',
    'Priority',
    'Conference',
    'Year',
    'Lab',
    'Github_Project',
    'Abstract',
    'Results',
    'Future Works',
    'Gaps in research ps',
    'Gaps in methodology',
    'Explicit Limits',
    'Changing Task of Interest',
    'Change in eval strategy',
    'change the proposed method',
    'Global Structure',
    'Seq of figs',
    'Abstract Structure',
    'Intro Structure',
    'Related work structure',
    'Conclusion Structure',
    'method and exp structure'
]




def get_all_info(readmepath):
    content = []
    with open(readmepath, 'r') as f:
        content = f.read()

    sections = {}
    current_heading = None

    lines = content.split('\n')


    for line in lines:
        # Check if it's a heading
        heading_match = re.match(r'^##\s*([\w\s]+)', line)
        if heading_match:
            current_heading = heading_match.group(1).strip()
            sections[current_heading] = []
        elif current_heading is not None:
            # If it's not a heading, add it as a point to the current heading
            point = line.strip()
            if point:
                sections[current_heading].append(point.replace('- ', ''))
    return sections


if __name__ == '__main__':
    path = 'research_papers/all/animatediff.md'
    get_all_info(path)