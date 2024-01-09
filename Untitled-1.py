from  PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QSpinBox, QHBoxLayout, QRadioButton, QButtonGroup,QGroupBox 

app = QApplication([]) #сторюємо віконний додаток

from  Untitled1 import *

win = QWidget() # створємо вікно
win.resize(600, 600)
win.setWindowTitle("Річки") 

 
time_spin = QSpinBox() 
time_spin.setValue(3) 
 
time_lb = QLabel("Хвилини") 
 
row1 = QHBoxLayout() 
row1.addWidget("lengths") 
row1.addStretch(1) 
row1.addWidget("rivers") 
row1.addWidget(time_spin) 
row1.addWidget(time_lb) 
 
main_line = QVBoxLayout() 
main_line.addLayout(row1) 
rivers = QLabel["Дніпро", "Дунай", "Дністер", "Південний Буг", "Десна"]
lengths = QLabel[2201, 2860, 1352, 806, 1130]  

    

length = sum(lengths)
average = length / len(rivers)
max = max(lengths)
min = min(lengths)

print("Сумарна довжина:",length,"км.")
print("Середня довжина:", average , "км.")
print("Максимальна довжина:",max, "км.")
print("Мінімальна довжина:",min,"км.")


win.show() 
app.exec_()