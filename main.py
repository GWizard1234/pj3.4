from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, QListWidget , QVBoxLayout, QComboBox, QLabel)

app = QApplication([])
window  = QWidget()


label = QLabel( 'Сума:' )
label2 = QLabel( 'У валюту:' )
label3 = QLabel( 'Результат:' )
line22 = QLabel()
but1 = QPushButton("Конвертувати")
line  = QLineEdit()
combo = QComboBox()
list1 = ['eur','usd']
combo.addItems(list1)

v = QVBoxLayout()
v.addWidget(label)
v.addWidget(line)
v.addWidget(label2)
v.addWidget(combo)
v.addWidget(label3)
v.addWidget(line22)
v.addWidget(but1)

def add_task():
    t = line.text()
    c = combo.currentText()
    if c == 'eur':
        r = int(t) * 41.39
        line22.setText(str(r))
    elif c == 'usd':
        r = int(t) * 37.80
        line22.setText(str(r))
    
            
but1.clicked.connect(add_task)


window.setLayout(v)







window.show()
app.exec_()