#Вариант 11
from datetime import datetime
import shlex

class Work:
    def __init__(self, name: str, topic: str, issue):
        self.name = name
        self.topic = topic
        self.issue = issue
    def __str__(self):
        return f'Имя студента: {self.name}, Тема работы: {self.topic}, Дата: {datetime.strftime(self.issue, "%Y.%m.%d")}'

text = input("Введите объект: ")
part = shlex.split(text)

if part[0] == "Work":
    obj = Work(part[1], part[2], datetime.strptime(part[3], "%Y.%m.%d"))

print(obj)