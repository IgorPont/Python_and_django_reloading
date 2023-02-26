"""
class NameClass():
    #атрибуты класса и инициализация
    def __init__(self.atr1, atr2, atr3):
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3
    #метод класса
    def func(self)
        Действие с atr...
"""
# Пример встроенного класса list
new_list = [1, 2, 3]


# print(type(new_list)) # Тип class
# help(list) # Описание класса и его методов

# Создание собственых классов (его свойств - атрибутов и состояний - методов)
class CommentFromWebSite():  # Имя класса принято в кэмелкейсе
    """
    Комментарии с сайта
    """

    def __init__(self, data, text, likes):  # self - ссылка на экземпляр класса
        self.data = data
        self.text = text
        self.likes = int(likes)

    def showComment(self):
        """
        Вывести комментарий в консоль
        """
        print(f'\nКомментарий с сайта, \n дата: {self.data},'
              f'\n тескт: {self.text}, лайков: {self.likes}')

    def changeLikes(self):
        """
        Прибавляет один лайк
        """
        self.likes += 1

    def changeComment(self, new_text):
        """
        Изменение комментария
        """
        self.text = new_text


new_comment = CommentFromWebSite('11/02/20', 'Первый', '11')
print(type(new_comment))  # Экземпляр класса CommentFromWebSite
print(new_comment.data)  # Обратились к атрибуту экземпляра класса

new_comment.text = 'Новый коммент!'
print(new_comment.text)  # Изменить значение атрибута экземпляра класса
new_comment2 = CommentFromWebSite('22/03/19', 'Второй', '5')

new_comment.showComment()
new_comment.changeLikes()
new_comment.showComment()

new_comment.changeComment('Изменили комментарий!')
new_comment.showComment()
