class Constructor:
    def __init__(self):
        self.__body = ""

    def __add_element(self, name: str, content: str = "", pair: bool = True, **params):
        element = "<" + name
        option = [f'{key}="{value}"' for key, value in params.items()]
        if option:
            element += " " + " ".join(option)
        if pair:
            element += f">{content}</{name}>"
        else:
            element += ">"
        return element

    def title(self, title: str):
        self.__title = title

    def P(self, text: str):
        self.__body += self.__add_element("p", text, True)

    def link(self, href: str, text: str):
        self.__body += self.__add_element("a", text, True, href=href)

    def div(self, text: str):
        self.__body += self.__add_element("div", text, True)

    def h(self, NumElement: int, text: str):
        self.__body += self.__add_element(f"h{NumElement}", text, True)

    def img(self, URL: str):
        self.__body += self.__add_element("img", "", False, src=URL)

    def list(self, teg: str, array: list):
        self.__body += self.__add_element(teg, "", False)
        for i in range(len(array)):
            self.__body += self.__add_element("li", array[i], True)
        self.__body += f"</{teg}>"

    def print_text(self, teg: str, text: str):
        self.__body += self.__add_element(teg, text, True)

    def get_body(self) -> str:
        return self.__body

    def render(self):
        return f"""
    <html>
        <head>
            {self.__add_element("title",self.__title, True)}
        </head>
        <body>
            {self.__body}
            </body>
    </html>
    """


html = Constructor()
html.title("Hello World")
html.P("Первый параграф")
html.P("Второй параграф")
html.link("https://yandex.ru/images/search?from=tabbar&text=monkey%20meme", "здесь есть monkey")
html.div("Hello world! - это классика")
html.h(1, "Меня зовут Михаил")
html.h(2, "Я учусь в НФ УУНиТ")
html.img("https://wallpapercave.com/wp/wp9905421.jpg")
html.print_text("Бабуин", "Monkey")
html.add_list("li", ["Сильвестр Сталине", "Желелезный Арнольд Штирлиц", "Чак Норрис"])
print(html.render())