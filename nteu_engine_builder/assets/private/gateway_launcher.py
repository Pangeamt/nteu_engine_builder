import asyncio
import logging
from nteu_gateway.server import NTEUGatewayServer
from translate import translate


# create logger
logging.getLogger("aiohttp.access").setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO)

asyncio.run(NTEUGatewayServer.run(
        "{{config['gateway']['host']}}",
        {{config['gateway']['port']}},
        "openapi.yaml",
        "{{config['segmenter']['host']}}",
        {{config['segmenter']['port']}},
        True,
        32,
        2,
        "{{config['translationEngine']['srcLang']}}",
        "{{config['translationEngine']['tgtLang']}}",
        "Translate {{config['translationEngine']['srcLang']}}->{{config['translationEngine']['tgtLang']}}",
        "TODO",
        translate
    ))
