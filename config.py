import configparser

config = configparser.ConfigParser()
config.read('config.conf')

# Accesso alle configurazioni
project_name = config.get('general', 'project_name')
debug = config.getboolean('general', 'debug')
db_host = config.get('database', 'db_host')
# E così via per le altre configurazioni