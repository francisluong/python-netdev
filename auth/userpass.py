from Crypto.Cipher import AES
from Crypto import Random

class Userpass:

    def __init__ (self):
        self.length = dict()
        self.database = dict()
        self.current_user = ""
        self.mode = AES.MODE_CBC
        self.bs = 32
        self.key = Random.new().read(self.bs)
        self.iv = Random.new().read(16)

    def add_user_passwd (self, user, passwd):
        #track length of password per user
        self.length[user] = len(passwd)
        c = AES.new(self.key, self.mode, self.iv)
        self.database[user] = c.encrypt(passwd.ljust(self.bs))

    def user (self):
        return self.current_user

    def passwd (self):
        user = self.current_user
        length = self.length[user]
        c = AES.new(self.key, self.mode, self.iv)
        return c.decrypt(self.database[user])[0:length]

    def change_user(self, user):
        if user in self.database:
            self.current_user = user

    def load (self, filename):
        import yaml
        import sys
        if sys.platform == "linux2":
            import os,stat
            os.chmod(filename,stat.S_IRUSR|stat.S_IWUSR)
        with open(filename) as fh:
            yamldict = yaml.safe_load(fh)
        users = yamldict["users"]
        firstuser = ""
        for user in users:
            if firstuser == "":
                firstuser = user
            self.add_user_passwd(user,users[user])
        if yamldict.has_key("defaultuser"):
            #set default user from defaultuser key
            firstuser = yamldict["defaultuser"]
        else:
            #keep existing first user
            firstuser = firstuser
        self.change_user(firstuser)

    def keys(self):
        return self.database.keys()
