class Parser:
    def __init__(self, path):
        self.path = path

    def get_elements(self):
        file = open(self.path, 'r')
        elements = list()
        for element in file.read().strip().split():
            elements.append(element.strip())
        file.close()
        return elements
