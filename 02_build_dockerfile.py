import logging
from nteu_engine_builder.nteu_engine_builder import NTEUEngineBuilder

logging.getLogger().setLevel(logging.INFO)

# Create an `assets`
NTEUEngineBuilder.build_dockerfile()
