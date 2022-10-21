import re, wikipedia

# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")


def get_wiki_page(word):
    try:
        wiki_page = wikipedia.page(word)

    except wikipedia.PageError:
        # При вольном тестировании обнаружил что
        # при ненахождении страницы получаем эксепшн
        return "К сожалению такого еще нет на википедии!"

    except Exception:
        return "Не смогли связаться с википедией!"

    try:
        wiki_content = wiki_page.content
        wiki_text_clipped = wiki_content[:1000]
        # Разделяем по точкам
        wiki_text_splitted = wiki_text_clipped.split('.')
        # Отбрасываем всЕ после последней точки
        wiki_text_splitted = wiki_text_splitted[:-1]
        # Создаем пустую переменную для текста
        wikitext_final = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)

        for x in wiki_text_splitted:
            if '==' not in x:
                # Если в строке осталось больше трех символов,
                # добавляем ее к нашей переменной
                # и возвращаем утерянные при разделении строк точки на место
                if len((x.strip())) > 3:
                    wikitext_final = wikitext_final + x + '.'
            else:
                break

    # Теперь при помощи регулярных выражений убираем разметку
            wikitext_final = re.sub('\([^()]*\)', '', wikitext_final)
            wikitext_final = re.sub('\([^()]*\)', '', wikitext_final)
            wikitext_final = re.sub('\{[^\{\}]*\}', '', wikitext_final)

    except Exception:
        return "При форматировании текста произошла ошибка!"

    # Возвращаем текстовую строку
    return wikitext_final
