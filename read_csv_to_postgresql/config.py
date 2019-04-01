from configparser import ConfigParser

"""
Reads database.ini and get postgresql configs
Pass section to functuion if you wish to use any other configuration e.g

-----Add this to database.ini -------
[another_postgresql_config]
host = POSTGRESQL_HOST
database = YOUR_DATABASE
user = USER
password = PASSWORD

now you can use the added configuration by calling config() and passing a section parameter
Default section parameter is postgresql
conn = config(section='another_postgresql_config')

Similarly you can also pass another file with your configurations


"""
def config(filename = 'database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the file'.format(section, filename))

    return db
