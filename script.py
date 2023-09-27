import ftplib

host = "66.220.9.50"
username = "shahid22032000"
password = "Shado7875"

def read_config():
    # read from config.json
    # return config.json content in a dict
    return ""

def connect_ftp(host, username, password):
    ftp = ftplib.FTP(host)
    ftp.login(user=username, passwd=password)
    return ftp

def main():
    ftp = connect_ftp(host, username, password)
    dirList = ftp.dir()
    print(dirList)

if __name__ == "__main__":
    main()