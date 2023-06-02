from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def debug(self, text: str):
        pass

    @abstractmethod
    def info(self, text: str):
        pass

    @abstractmethod
    def warning(self, text: str):
        pass

    @abstractmethod
    def error(self, text: str):
        pass

    @abstractmethod
    def crit_error(self, text: str):
        pass


class ConsoleLog(Log):
    def debug(self, text: str):
        print("\033[37m{}".format(text))

    def info(self, text: str):
        print("\033[4m\033[32m{}\033[0m".format(text))

    def warning(self, text: str):
        print("\033[34m{}".format(text))

    def error(self, text: str):
        print("\033[31m\033[1m{}".format(text))

    def crit_error(self, text: str):
        print("\033[33m\033[4m{}".format(text))


run = ConsoleLog()
run.debug("Дебаг")
run.info("Полезная информация")
run.warning("Предупреждение")
run.error("Ошибка!")
run.crit_error("Критическая ошибка!")