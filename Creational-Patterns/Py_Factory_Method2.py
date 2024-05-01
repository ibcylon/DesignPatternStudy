
class JSONExtractor:
    def __init__(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            self.data = json.load(f)

class XMLExtractor:
    def __init__(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            self.data = json.load(f)

def extraction_factory(file_path):
    if file_path.endswith('json'):
        extractor = JSONExtractor
    elif file_path.endswith('xml'):
        extractor = XMLExtractor
    return extractor(file_path)