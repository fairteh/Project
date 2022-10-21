from unittest import TestCase
from unittest.mock import patch, MagicMock, PropertyMock
from wiki import get_wiki_page


class TestWiki(TestCase):
    def test_get_wiki_page_ok(self):
        """
        Базовая проверка, что все будет хорошо
        """
        wiki_page_mock = MagicMock()
        wiki_page_mock.content = "Это очень интересный текст на 1000 символов. А это обрывающейся сло"

        with patch("wikipedia.page") as mock:
            mock.return_value = wiki_page_mock
            result = get_wiki_page("Что то что не имеет значения")

        assert result == "Это очень интересный текст на 1000 символов."

    def test_get_wiki_page_wiki_fail(self):
        """
        Проверка выдачи предупреждения что если википедия
        не ответит по какой-либо причине,
        то мы выдадим юзеру предупреждение
        """
        with patch("wikipedia.page") as mock:
            mock.side_effect = Exception
            result = get_wiki_page("Что то что не имеет значения")
        assert result == "Не смогли связаться с википедией!"

    def test_get_wiki_page_formatting_exception(self):
        """
        Проверка форматирования
        Если википедия выдаст неожиданный ответ,
        то мы сообщим юзеру
        """
        page_magic_mock = MagicMock()
        page_magic_mock.content = PropertyMock(side_effect=Exception)

        with patch("wikipedia.page") as wiki_mock:
            wiki_mock.return_value = page_magic_mock
            result = get_wiki_page("Жизнь прекрасна")


        assert result == "При форматировании текста произошла ошибка!"
