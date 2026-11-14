#Вариант 11
#Вариант 11
from datetime import date
import shlex
import tkinter as tk
from tkinter import ttk

class Work:

    def __init__(self, name: str, topic: str, issue):
        self.name = name
        self.topic = topic
        self.issue = issue

    def __str__(self):
        return f'Имя студента: {self.name}, Тема работы: {self.topic}, \
            Дата: {date.strftime(self.issue, "%Y.%m.%d")}'

def parse_work(line):
    part = shlex.split(line)
    if part[0] == "Work":
        obj = Work(part[1], part[2], date.strptime(part[3], "%Y.%m.%d"))
        return obj

def load_work(filename):
    works = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            works.append(parse_work(line))
    return works

def add_work(filename):
    work = create_work()
    works.append(work)
    display_work(work)
    save_work(filename)
    clear_entries()

def delete_work(filename):
    selected = table.selection()
    if selected:
        item_id = selected[0]
        work = items[item_id]
        works.remove(work)
        table.delete(item_id)
        del items[item_id]
    save_work(filename)

def save_work(filename):
    with open(filename, "w", encoding="utf-8") as f:
        for work in works:
            f.write(f'Work {shlex.quote(work.name)} {shlex.quote(work.topic)} \
                    {date.strftime(work.issue, "%Y.%m.%d")}\n')

def display_work(work):
    item_id = table.insert("", "end", values=(
        work.name,
        work.topic,
        work.issue.strftime("%Y.%m.%d")
    ))
    items[item_id] = work

def create_work():
    name = name_entry.get()
    topic = topic_entry.get()
    issue = issue_entry.get()
    return Work(name, topic, date.strptime(issue, "%Y.%m.%d"))

def clear_entries():
    name_entry.delete(0, tk.END)
    topic_entry.delete(0, tk.END)
    issue_entry.delete(0, tk.END)

root = tk.Tk()
root.geometry("1280x720")
root.title("Темы работ")

columns = ("name", "topic", "issue")
table = ttk.Treeview(root, columns=columns, show="headings")

table.heading("name", text="Имя студента")
table.heading("topic", text="Тема работы")
table.heading("issue", text="Дата выдачи")

table.pack(fill="both", expand=True)

works = load_work("data.txt")
items = {}

for work in works:
    display_work(work)

frame = ttk.Frame(root)
frame.pack(fill='x', padx=5, pady=5)

ttk.Label(frame, text="Имя студента").pack()
name_entry = ttk.Entry(frame, width=30)
name_entry.pack()

ttk.Label(frame, text="Тема работы").pack()
topic_entry = ttk.Entry(frame, width=30)
topic_entry.pack()

ttk.Label(frame, text="Дата выдачи").pack()
issue_entry = ttk.Entry(frame, width=30)
issue_entry.pack()

delete_button = ttk.Button(frame, text="Удалить", 
                           command=lambda: delete_work("data.txt"))
delete_button.pack(side="bottom", padx=5, pady=5)

add_button = ttk.Button(frame, text="Добавить", 
                        command=lambda: add_work("data.txt"))
add_button.pack(side="bottom", padx=5, pady=15)


root.mainloop()