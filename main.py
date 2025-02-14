from loguru import logger


def main():
    logger.add("file.log", format ="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation = "3 days",
               backtrace = True,
               diagnose = True)
    
    title = input("Введите название новеллы: ")
    url = input("Введите ссылку на новеллу: ")
    logger.info(f"Пользователь ввел название {title} новеллы и ссылку {url}.")


if __name__ == '__main__':
    main()
