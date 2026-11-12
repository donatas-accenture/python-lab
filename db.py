class ConnectionDatabase:

  #Constructor
    def __init__(self, port, hostname, username, password):
        #encapsulation
        self.port = port
        self.hostname = hostname
        self.username = username
        self.password = password

    def show_connection_params(self):
        print("Connection to database details is:")
        print(f"Username is {self.username} & password is {self.password} & hostname is {self.hostname} & port is {self.port}")
  

conn = ConnectionDatabase(443, "localhost", "db_user", "db_pass_123#$")

conn.show_connection_params()