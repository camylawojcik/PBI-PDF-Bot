# encoding: utf-8
import os
from src.config.config import Config

# Obtendo configurações de acesso a API conforme o ambiente
application_environment = os.getenv('APP_ENV', default="development")
assert application_environment in ("production", "staging", "development")
if application_environment == "production":
    config_file = os.path.join(__file__, os.pardir, 'config', 'config-prd.yaml')
elif application_environment == "staging":
    config_file = os.path.join(__file__, os.pardir, 'config', 'config-stg.yaml')
else:
    config_file = os.path.join(__file__, os.pardir, 'config', 'config-dev.yaml')

# Log.d(f"Carregando configuracao de {config_file}")
Config.load_file(config_file)
