import json
from loguru import logger


class Novel:
    def __init__(self, title):
        self.title = title
        self.chapter = {}

    def write_novel_to_db(self, chapters):
        self.chapters = chapters
        with open (f"{self.title}.json", 'w', encoding='UTF-8') as json_file:
            loaded_data = json.dump(self.chapters, 
                                    json_file, 
                                    ensure_ascii=False)
        logger.info(f"chapters of the novel {self.title} are written to file")

    def load_novel_from_db(self):
        pass

    def print_novel_to_terminal(self):
        pass