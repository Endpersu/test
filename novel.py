import json
from loguru import logger


class Novel:
    def __init__(self, title):
        self.title = title
        self.chapters = {}

    def write_novel_to_db(self, chapters):
        self.chapters = chapters
        with open (f"{self.title}.json", 'w', encoding='UTF-8') as json_file:
            loaded_data = json.dump(self.chapters, 
                                    json_file, 
                                    ensure_ascii=False)
        logger.info(f"chapters of the novel {self.title} are written to file")

    def load_novel_from_db(self):
        try:
            with open(f'{self.title}.json', 'r', encoding='UTF-8') as json_file:
                self.chapters = json.load(json_file)
            

        except FileNotFoundError:
            logger.error(f'file {self.title}.json is not found')
        except json.JSONDecodeError:
            logger.error("Ошибка декодирования JSON")

    def print_novel_to_terminal(self):
        logger.info("Приступаем к распечатыванию новеллы в терминал: ")
        print(f"Название: {self.title}")
        print("Главы: ")
        for chapter_title, chapter_content in self.chapters.items():
            print(f"{chapter_title}: {chapter_content}")