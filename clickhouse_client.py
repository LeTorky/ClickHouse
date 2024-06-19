import clickhouse_connect

# Set port to the exposed port on the docker container that maps to 8123.
PORT_NO = 9000

client = clickhouse_connect.get_client(
    host='localhost',
    secure=False,
    port=PORT_NO,
)

TABLE_NAME = 'table_one'
ID_COL_NAME = 'id'
FIRST_COL_NAME = 'name'


def create_table():
    """Run once to create table"""
    client.command(
        f'''
            CREATE TABLE {TABLE_NAME} ({ID_COL_NAME} UInt32, {FIRST_COL_NAME} String) ENGINE MergeTree ORDER BY {ID_COL_NAME}
        '''
    )


def add_entries():
    """Run to add entries"""
    row1 = [1, 'John']
    row2 = [2, 'Doe']
    data = [row1, row2]

    client.insert(TABLE_NAME, data, column_names=[ID_COL_NAME, FIRST_COL_NAME])


def query():
    """Query entries"""
    result = client.query(
        f'''SELECT {ID_COL_NAME},
        {FIRST_COL_NAME} FROM {TABLE_NAME}
        '''
    )

    print(result.result_rows)


# create_table()
# add_entries()
query()
