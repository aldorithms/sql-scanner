import socket
import pyodbc

# set up the connection string template
connection_string = 'Driver=ODBC Driver 17 for SQL Server;Server=%s;Database=master;Trusted_Connection=yes;'

# define a function to check if a server is running SQL Server
def is_sql_server(server):
    try:
        socket.gethostbyname_ex(server)
        conn = pyodbc.connect(connection_string % server)
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM sys.databases')
        databases = [database[0] for database in cursor.fetchall()]
        conn.close()
        return True, databases
    except:
        return False, []
    
# search for SQL databases on the network
servers = ['server1', 'server2', 'server3'] # replace with the names of the servers you want to search
databases = {}
for server in servers:
    print(f'Searching {server}...')
    is_running, database_list = is_sql_server(server)
    if is_running:
        print(f'{server} is running SQL Server with the following databases:')
        print(database_list)
        databases[server] = database_list
    else:
        print(f'{server} is not running SQL Server.')

# Print the list of databases
print('Found the following databases:')
print(databases)

# define a function to check if a server is running SQL Server
def is_sql_server(server):
    try:
        socket.gethostbyname_ex(server)
        conn = pyodbc.connect(connection_string % server)
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM sys.databases')
        databases = [database[0] for database in cursor.fetchall()]
        conn.close()
        return True, databases
    except:
        return False, []

# search for SQL databases on the network
servers = ['server1', 'server2', 'server3'] # replace with the names of the servers you want to search
databases = {}
for server in servers:
    print(f'Searching {server}...')
    is_running, database_list = is_sql_server(server)
    if is_running:
        print(f'{server} is running SQL Server with the following databases:')
        print(database_list)
        databases[server] = database_list
    else:
        print(f'{server} is not running SQL Server.')

# Print the list of databases
print('Found the following databases:')
print(databases)