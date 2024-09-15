from tkinter import messagebox
import webbrowser 
from random import choice

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout)

def get_film_Jocker():
    webbrowser.open('https://www.kinopoisk.ru/film/1048334/')
def get_film_Batman():
    webbrowser.open('https://www.kinopoisk.ru/film/4205/')
def get_film_Thor():
    webbrowser.open('https://www.kinopoisk.ru/film/258941/')
def get_film_Deadpool():
    webbrowser.open('https://www.kinopoisk.ru/film/462360/')
def get_film_TheWolverine():
    webbrowser.open('https://www.kinopoisk.ru/film/462754/')
def get_film_Superman():
    webbrowser.open('https://www.kinopoisk.ru/film/7145/')

def get_RANDOM_film():
    film = choice(lst_films)
    if film == 'surprize':
        message = messagebox()
        message.setWindowTitle('Окно')
        message.setText('ПАСХАЛОЧКА!!!')
        message.exec()
    else:
        webbrowser.open(film)


lst_films:{} # type: ignore
'https://www.kinopoisk.ru/film/1048334/'
'https://www.kinopoisk.ru/film/4205/'
'https://www.kinopoisk.ru/film/258941/'
'https://www.kinopoisk.ru/film/462360/'
'https://www.kinopoisk.ru/film/462754/'
'https://www.kinopoisk.ru/film/7145/'
app = QApplication ([])
window = QWidget()
window.resize(400, 300)
window.setWindowTitle('Кинопоиск')

main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

text = QLabel('Выберите фильм')
button1 = QPushButton('Джокер')
button2 = QPushButton('Бэтмен')
button3 = QPushButton('Тор')
button4 = QPushButton('Дэдпул')
button5 = QPushButton('Расомаха')
button6 = QPushButton('Суперман')

button1.clicked.connect(get_film_Jocker)
button2.clicked.connect(get_film_Batman)
button3.clicked.connect(get_film_Thor)
button4.clicked.connect(get_film_Deadpool)
button5.clicked.connect(get_film_TheWolverine)
button6.clicked.connect(get_film_Superman)

line1.addWidget(button1, alignment=Qt.AlignCenter)
line1.addWidget(button2, alignment=Qt.AlignCenter)
line2.addWidget(button3, alignment=Qt.AlignCenter)
line2.addWidget(button4, alignment=Qt.AlignCenter)
line3.addWidget(button5, alignment=Qt.AlignCenter)
line3.addWidget(button6, alignment=Qt.AlignCenter)



main_line.addWidget(text, alignment=Qt.AlignCenter)
main_line.addLayout(line1)
main_line.addLayout(line2)
main_line.addLayout(line3)

window.setLayout(main_line)
window.show()
app.exec()
