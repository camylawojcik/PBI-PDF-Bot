# encoding: utf-8

import os
import os.path

import yaml


class Config:
    __data = {}

    @staticmethod
    def load():
        # Estágio da API
        Config.set('stage', valor=os.getenv("STAGE", "development"))
        Config.set('path_temp_local', valor=os.getenv("PATH_TEMP_LOCAL", "/tmp/"))

        # Configuração de email
        Config.set('mailer', 'server', valor=os.getenv("MAIL_SERVER"))
        Config.set('mailer', 'port', valor=os.getenv("MAIL_PORT"))
        Config.set('mailer', 'ttls', valor=os.getenv("MAIL_TTLS"))
        Config.set('mailer', 'from', valor=os.getenv("MAIL_FROM"))
        Config.set('mailer', 'login', valor=os.getenv("MAIL_LOGIN"))
        Config.set('mailer', 'password', valor=os.getenv("MAIL_PASSWORD"))
        Config.set('mailer', 'status', valor=os.getenv("MAIL_STATUS"))

    @staticmethod
    def load_file(config_path):
        """Carrega um arquivo de configuração.

        :param config_path: caminho do arquivo de configuração
        :type config_path:  str
        """
        # Carrega o arquivo yaml
        with open(os.path.abspath(config_path)) as file:
            config_data = yaml.load(file)
            assert isinstance(config_data, dict)
            # Atualiza os valores padrao com os obtidos no arquivo
            Config.__data.update(config_data)

    @staticmethod
    def get(*args):
        if len(args) == 0:
            return Config.__data
        print(args)
        item = Config.__data[args[0]]
        for arg in args[1:]:
            item = item[arg]
        return item

    @staticmethod
    def set(*args, valor=None):
        if len(args) == 0:
            raise RuntimeError(u'Nenhuma chave de configuração especificada!')

        # Criamos as chaves dentro do dicionário, caso elas não existam
        data = Config.__data
        for key in args:
            if isinstance(key, str) is False:
                raise ValueError("Chave de configuração pode ser somente string!")

            if key not in data:
                data[key] = {}

            # Passamos ao próximo nível da chave
            data = data[key]

        data = Config.__data
        for idx, key in enumerate(args):
            if idx == len(args) - 1:
                # Chegamos ao valor final da chave, guardamos o valor
                data[key] = valor
            else:
                # Passamos ao próximo item dentro do dicionário
                data = data[key]
