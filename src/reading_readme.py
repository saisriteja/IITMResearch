
import re

class ReadingReadMe:
    def __init__(self, path):
        self.path = path

    def run(self):
        self.content = self.read_readme()
        self.information = self.information_extraction()
        print(self.information)


    def read_readme(self):
        with open(self.path, 'r') as f:
            return f.read()

    def information_extraction(self):
        # get all the ## titles

        sections = {}
        current_heading = None

        lines = self.content.split('\n')
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
                    sections[current_heading].append(point)
        return sections
    


if __name__ == '__main__':

    path = '/home/cilab/teja/IITMResearch/research_papers/diffusion/ddpm.md'
    file_info = ReadingReadMe(path)
    file_info.run()
        