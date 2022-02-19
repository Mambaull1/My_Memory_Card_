from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton,  QPushButton, QLabel)
from random import randint, shuffle
app = QApplication([])

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3): 
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный Язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России','Зелёный','Красный','Синий','Белый'))
questions_list.append(Question('Кто автор Робинзона Крузо?','Даниэль Дефо','Жюль Верн','Джек Лондон','Александр Дюм'))
questions_list.append(Question('Национальное хижина якутов','юрта','2','3','4'))
questions_list.append(Question('Какого газа в атмосфере Земли больше всего?','Азот','Кислород','Углерод','Углекислый газ'))
questions_list.append(Question('Какой римской цифры не существует?','0','1000','10000','100000'))
questions_list.append(Question('Чего боятся люди, которые страдают алекторофобией?','Кур','Собак','Змей','Котов'))
questions_list.append(Question('В какой стране более одной столицы?','ЮАР','Алжир','Сша','Тунис'))
questions_list.append(Question('Назовите столицу Европейского Союза?','Брюссель','Париж','Берлин','Вена'))
questions_list.append(Question('В каком году была разрушена Берлинская стена?','1989','1988','1990','1991'))


btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
   
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!') 

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.show()

layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide() 

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=1) 
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) 

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий Вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)   
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)  
    lb_Correct.setText(q.right_answer)
    show_question()

def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Стастистика всего вопросов:',window.total,'Правильных ответов', window.score)
        print('Рейтинг', (window.score/window.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно')
            print('Рейтинг',(window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Стастистика всего вопросов:',window.total,'Правильных ответов', window.score)
    cur_question = randint(0, len(questions_list) -1)  
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1
q = Question('Государственный Язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
ask(q)
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.show()
app.exec()
