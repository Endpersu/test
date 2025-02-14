from loguru import logger

from parser import Parser


def main():
    # https://www.52shuku.vip/yanqing/am/h2QX.html

    logger.add("file.log", format ="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation = "3 days",
               backtrace = True,
               diagnose = True)
    
    title = input("Введите название новеллы: ")
    url = input("Введите ссылку на новеллу: ")
    pars = Parser(title, url)
    page = pars.get_webpage(url)
    print(page.text)


if __name__ == '__main__':
    main()
