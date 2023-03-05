# Инкапсяция в Python
# self.name = name - публичный атрибут (public)
# self._name = name - защищенный атрибут (protected)
# self.__name = name - приватный атрибут (private)
class VKAccountINWedSite():
    """Ваш аккаунт в VK, на сайте VK"""

    def __init__(self, name, login_id, password):
        self.__name = name
        self.__login_id = login_id
        self.__password = password

    def __loginVK(self):
        if self.__login_id == 123 and self.__password == 456:
            print('Привет ' + self.__name)
        return True

    def publicLogin(self):  # доступ к приватной функции за пределами класса (аналог сеттера в JAVA)
        self.__loginVK()


vkakk = VKAccountINWedSite('Alex', 123, 456)
vkakk.publicLogin()
# print(vkakk.__name)
