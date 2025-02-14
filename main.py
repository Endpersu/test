from loguru import logger

from novel import Novel
from parser import Parser


def main():
    # https://www.52shuku.vip/yanqing/am/h2QX.html

    logger.add('file.log',
               format='{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}',
               rotation="3 days",
               backtrace=True,
               diagnose=True)

    title = input("Введите название новеллы: ")
    url = input("Введите ссылку на новеллу: ")
    # pars = Parser(title, url)
    # pars.get_novel()

    novel = Novel(title)
    novel.load_novel_from_db()
    novel.print_novel_to_terminal()


if __name__ == '__main__':
    main()
