from typing import List

import aiohttp


class Speller:
    @staticmethod
    async def check_text(
            text: str,
            lang: str = 'ru',
            url: str = 'https://speller.yandex.net/services/spellservice.json/checkText'
    ) -> List[dict]:
        """ Функция для проверки правописания через сервис 'Яндекс.спеллер' """
        async with aiohttp.ClientSession() as session:
            params: dict = {'text': text, 'lang': lang}

            async with session.get(url, params=params) as response:
                return await response.json()

    @staticmethod
    async def fix_errors(text: str, errors: list) -> str:
        """ Функция исправляет ошибки, найденные в тексте """
        for error in errors:
            start_detail: str = ''.join(text[:error['pos']])
            fixed_detail: str = error['s'][0]
            end_detail: str = ''.join(text[error['pos'] + error['len']:])

            text = start_detail + fixed_detail + end_detail
        return text
