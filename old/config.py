config = {
    'dbname':'dbexch',
    'user':'scru',
    'password':'sq0tr3',
    'port':'5432',
    'host':'185.143.173.37'
}
def db_config():
    return 'pq://{user}:{password}@{host}:{port}/{dbname}'.format(
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
        dbname=config['dbname']
    )
