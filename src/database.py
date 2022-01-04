import argparse
import sqlalchemy as db

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'zack',
    'password': 'root_password',
    'database': 'test_db'
}

class SqlRunner(object):

    def __init__(self, config=None):
        if config is None:
            config = DEFAULT_CONFIG
        db_user = config.get('user')
        db_pwd = config.get('password')
        db_host = config.get('host')
        db_port = config.get('port')
        db_name = config.get('database')
        connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
        engine = db.create_engine(connection_str)
        self.connection = engine.connect()


    def execute(self, statement):
        return self.connection.execute(statement)


CREATE_STATEMENTS = [
    "CREATE TABLE Teams(teamId INT, teamName VARCHAR(20));",
    "INSERT INTO Teams(teamId, teamName) VALUES(1, 'Wildcats')"
]
READ_STATEMENTS = [
    "SELECT * FROM Teams"
]
DROP_STATEMENTS = [
    "DROP TABLE Teams"
]

def main():

    parser = argparse.ArgumentParser(description="default parser")
    parser.add_argument('--mode')
    args = parser.parse_args()

    runner = SqlRunner()
    if args.mode in ['a', 'add', 'c', 'create']:
        statements = CREATE_STATEMENTS
    elif args.mode in ['r', 'read']:
        statements = READ_STATEMENTS
    elif args.mode in ['d', 'drop', 'delete']:
        statements = DROP_STATEMENTS
    else:
        statements = []

    for statement in statements:
        result = runner.execute(statement)
        try:
            for row in result:
                print(row)
        except:
            pass


if __name__ == "__main__":
    main()
