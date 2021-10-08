# encoding: utf-8

# library
from cryptography.fernet import Fernet

# class EncryptDecrypt
class EncryptDecrypt:
    def __init__(self, keySecret=None):
        self.key = keySecret

    def encryptFile(self, items: list):
        if self.key is None:
            self.key = self.generateKey()
        f = Fernet(self.key)
        for item in items:
            fileContent = open(item, 'rb').read()
            contentEncrypt = f.encrypt(fileContent)
            open(item, 'wb').write(contentEncrypt)

    def decryptFile(self, items):
        if self.key is None:
            self.key = self.loadKey()
        f = Fernet(self.key)
        for item in items:
            fileContent = open(item, 'rb').read()
            contentEncrypt = f.decrypt(fileContent)
            open(item, 'wb').write(contentEncrypt)

    @staticmethod
    def generateKey():
        keySecret = Fernet.generate_key()
        open('key.key', 'wb').write(keySecret)
        return keySecret

    @staticmethod
    def loadKey():
        return open('key.key', 'rb').read()