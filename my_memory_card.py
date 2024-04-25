from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
       self.question = question
       self.right_answer = right_answer
       self.wrong1 = wrong1
       self.wrong2 = wrong2
       self.wrong3 = wrong3
voprocy = list()
voprocy.append(Question('Сколько дней в неделе?', '7', '6', '8', '5'))
voprocy.append(Question('Сколько дней в декабре?', '31', '30', '32', '29'))
voprocy.append(Question('Сколько месяцев в году?', '12', '10', '11', '13'))
voprocy.append(Question('Сколько лет в одном веке?', '100', '200', '150', '50'))
priloshenie = QApplication([])
okno = QWidget()
text = QLabel('hjhgjghj')
text1 = QPushButton('Ответить')
kvadrat = QGroupBox('Варианты ответов')
knopka1 = QRadioButton('vbdshtr')
knopka2 = QRadioButton('vbdsth')
knopka3 = QRadioButton('vbdshmhg')
knopka4 = QRadioButton('vjggjt')
liniyaG = QHBoxLayout()
liniyaV1 = QVBoxLayout()
liniyaV2 = QVBoxLayout()
liniyaV1.addWidget(knopka1)
liniyaV1.addWidget(knopka2)
liniyaV2.addWidget(knopka3)
liniyaV2.addWidget(knopka4)
liniyaG.addLayout(liniyaV1)
liniyaG.addLayout(liniyaV2)
kvadrat.setLayout(liniyaG)
kvadrat2 = QGroupBox('Результат теста')
text2 = QLabel('прав ты или нет')
text3 = QLabel('ghjkggjhk')
liniyaV3 = QVBoxLayout()
liniyaV3.addWidget(text2, alignment=Qt.AlignLeft| Qt.AlignTop)
liniyaV3.addWidget(text3, alignment=Qt.AlignCenter, stretch=2)
kvadrat2.setLayout(liniyaV3) ##########################################
liniyaG1 = QHBoxLayout()
liniyaG2 = QHBoxLayout()
liniyaG3 = QHBoxLayout()
liniyaG1.addWidget(text, alignment=Qt.AlignCenter)
liniyaG3.addStretch(1)
liniyaG3.addWidget(text1, stretch=2)
liniyaG3.addStretch(1)
liniyaV4 = QVBoxLayout()
liniyaV4.addLayout(liniyaG1)
liniyaV4.addLayout(liniyaG2)
liniyaV4.addLayout(liniyaG3)
okno.setLayout(liniyaV4)
liniyaG2.addWidget(kvadrat)   
liniyaG2.addWidget(kvadrat2) 
kvadrat2.hide()
okno.setWindowTitle('Memory_card')
RGroup = QButtonGroup()
RGroup.addButton(knopka1)
RGroup.addButton(knopka2)
RGroup.addButton(knopka3)
RGroup.addButton(knopka4)
spisok = [knopka1, knopka2, knopka3, knopka4]
def result():
    kvadrat.hide()
    kvadrat2.show()
    text1.setText('Следующий вопрос')
def voproc():
    kvadrat2.hide()
    kvadrat.show()
    text1.setText('Ответить')
    RGroup.setExclusive(False)
    knopka1.setChecked(False)
    knopka2.setChecked(False)
    knopka3.setChecked(False)
    knopka4.setChecked(False)
    RGroup.setExclusive(True)
def ask(q: Question):
    shuffle(spisok)
    spisok[0].setText(q.right_answer)
    spisok[1].setText(q.wrong1)
    spisok[2].setText(q.wrong2)
    spisok[3].setText(q.wrong3)
    text.setText(q.question)
    text3.setText(q.right_answer)
    voproc()
def result1(res):
    text2.setText(res)
    result()
def chek_answers():
    if spisok[0].isChecked():
        result1('Правильно!')
        okno.score += 1
        print('Статистика:', '\n Всего вопросов:', okno.total, '\n Павильные ответы:', okno.score)
        print('Рейтинг:', okno.score / okno.total * 100, '%')
    else:
        if spisok[1].isChecked() or spisok[2].isChecked() or spisok[3].isChecked():
            result1('Неправильно!')
            print('Рейтинг:', okno.score / okno.total * 100, '%')
def rand():
    okno.total += 1
    print('Статистика:', '\n Всего вопросов:', okno.total, '\n Павильные ответы:', okno.score)
    rand1 = randint(0, 3)
    q = voprocy[rand1]
    ask(q)
def prover():
    if text1.text() == 'Ответить':
        chek_answers()
    else:
        rand()
text1.clicked.connect(prover)
okno.total = 0
okno.score = 0
rand()
okno.resize(400, 300)
okno.show()
priloshenie.exec()