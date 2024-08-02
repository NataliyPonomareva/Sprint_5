import random


class HelpEmail:
    @staticmethod
    def generate_email():
        random_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))
        return f"{random_name}_09_{random.randint(100, 999)}ya.ru"


class HelpPassword:
    @staticmethod
    def generate_password():
        return f"{random.randint(100000, 888888)}ya.ru"
