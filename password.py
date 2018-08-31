import re

class Password:
    uppercase = re.compile(r'[A-Z]+')
    lowercase = re.compile(r'[a-z]+')
    numbers   = re.compile(r'[0-9]+')
    special_c = re.compile(r'[^\w]+')

    def __init__(self, passwd):
        if len(passwd) < 8 or len(passwd) > 24:
            raise TypeError("Your password length must be less then 24 and greater than 8")
        else:
            if self.uppercase.findall(passwd) and self.lowercase.findall(passwd) and self.numbers.findall(passwd) and self.special_c.findall(passwd):
                self.password = passwd
            else:
                 raise TypeError("Your password must contain upper/lower case, numbers and special characters")



class Typed:
    uppercase = re.compile(r'[A-Z]+')
    lowercase = re.compile(r'[a-z]+')
    numbers   = re.compile(r'[0-9]+')
    special_c = re.compile(r'[^\w]+')

    def __init__(self, passwd):
        self.password = passwd

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.password]
    def __set__(self, instance, passwd):
        if len(passwd) < 8 or len(passwd) > 24:
            raise TypeError("Your password length must be less then 24 and greater than 8")
        else:
            if self.uppercase.findall(passwd) and self.lowercase.findall(passwd) and self.numbers.findall(passwd) and self.special_c.findall(passwd):
                instance.__dict__[self.password] = passwd
            else:
                 raise TypeError("Your password must contain upper/lower case, numbers and special characters")
    def __delete__(self, instance):
        del instance.__dict__[self.password]

class new_pass:
    password = Typed('password')
    def __init__(self, password):
        self.password = password
