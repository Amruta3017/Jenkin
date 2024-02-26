import configparser
from Utilities.commonMethods import get_path

config = configparser.RawConfigParser()
config.read(get_path("Configurations", "config.ini"))


class ReadConfig:
    @staticmethod
    def get_app_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_email():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_admin_url():
        url = config.get('admin info', 'adminURL')
        return url

    @staticmethod
    def get_admin_email():
        email = config.get('admin info', 'email')
        return email

    @staticmethod
    def get_admin_pass():
        password = config.get('admin info', 'password')
        return password

    @staticmethod
    def get_first_name():
        fname = config.get('fullname info', 'fname')
        return fname

    @staticmethod
    def get_last_name():
        lname = config.get('fullname info', 'lname')
        return lname

    @staticmethod
    def aws_db_url():
        aws = config.get('database info', 'dbURL')
        return aws

    @staticmethod
    def db_get_name():
        db = config.get('database info', 'dbName')
        return db

    @staticmethod
    def tb_auth_user():
        tb = config.get('database table info', 'userTbName')
        return tb

    @staticmethod
    def tb_premise():
        tb = config.get('database table info', 'premiseTBName')
        return tb


    @staticmethod
    def get_email1():
        email1 = config.get('common info1', 'email1')
        return email1

    @staticmethod
    def get_password1():
        password1 = config.get('common info1', 'password1')
        return password1

    @staticmethod
    def get_email_staff():
        email_staff = config.get('common info2', 'email_staff')
        return email_staff

    @staticmethod
    def get_password_staff():
        password_staff = config.get('common info2', 'password_staff')
        return password_staff