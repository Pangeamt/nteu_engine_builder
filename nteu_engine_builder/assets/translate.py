from typing import List
import aiohttp
from nteu_gateway.translation_error import TranslationError


async def translate(texts: List[str]) -> List[str]:
    """

    :param texts: A list of texts to translate
    :return: The list of translations
    """

    host = '0.0.0.0'
    port = 10002

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                    f'http://{host}:{port}/translate',
                    json={'texts': texts}) as response:
                if response.status == 200:
                    result = await response.json()
                    translations = list(map(lambda x: x['translation'], result['translations']))
                    return translations
                else:
                    error_msg = await response.text()
                    raise TranslationError(f'Error from translation server: {error_msg}')
        except Exception as e:
            raise TranslationError(f'Error during translation server connection: {e}')
