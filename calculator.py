from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QHBoxLayout,QVBoxLayout,QPushButton
import sys
class Calculator(QWidget):
    def __init__(self):
        super(Calculator,self).__init__()
        
        self.setWindowTitle("Calculator1")
        
        self.input=QLineEdit(self)
        self.b_1=QPushButton("1")
        self.b_2=QPushButton("2")
        self.b_3=QPushButton("3")
        self.b_4=QPushButton("4")
        self.b_5=QPushButton("5")
        self.b_6=QPushButton("6")
        self.b_7=QPushButton("7")
        self.b_8=QPushButton("8")
        self.b_9=QPushButton("9")
        self.b_0=QPushButton("0")
        self.b_plus=QPushButton("+")
        self.b_minus=QPushButton("-")
        self.b_umn=QPushButton("*")
        self.b_del=QPushButton("/")
        self.b_Co=QPushButton("C")
        self.b_result=QPushButton("=")
        
        self.main_box=QVBoxLayout()

        self.input_box=QHBoxLayout()
        self.first_box=QHBoxLayout()
        self.second_box=QHBoxLayout()
        self.third_box=QHBoxLayout()
        self.four_box=QHBoxLayout()

        self.main_box.addLayout(self.input_box)
        self.main_box.addLayout(self.first_box)
        self.main_box.addLayout(self.second_box)
        self.main_box.addLayout(self.third_box)
        self.main_box.addLayout(self.four_box)
        
        self.input_box.addWidget(self.input)
        self.first_box.addWidget(self.b_1)
        self.first_box.addWidget(self.b_2)
        self.first_box.addWidget(self.b_3)
        self.second_box.addWidget(self.b_4)
        self.second_box.addWidget(self.b_5)
        self.second_box.addWidget(self.b_6)
        self.third_box.addWidget(self.b_7)
        self.third_box.addWidget(self.b_8)
        self.third_box.addWidget(self.b_9)
        self.four_box.addWidget(self.b_0)
        
        self.first_box.addWidget(self.b_plus)
        self.first_box.addWidget(self.b_minus)
        self.second_box.addWidget(self.b_umn)
        self.second_box.addWidget(self.b_del)
        self.third_box.addWidget(self.b_Co)
        self.third_box.addWidget(self.b_result)
        
        self.setLayout(self.main_box)

        self.b_1.clicked.connect(lambda: self._addNum("1"))
        self.b_2.clicked.connect(lambda: self._addNum("2"))
        self.b_3.clicked.connect(lambda: self._addNum("3"))
        self.b_4.clicked.connect(lambda: self._addNum("4"))
        self.b_5.clicked.connect(lambda: self._addNum("5"))
        self.b_6.clicked.connect(lambda: self._addNum("6"))
        self.b_7.clicked.connect(lambda: self._addNum("7"))
        self.b_8.clicked.connect(lambda: self._addNum("8"))
        self.b_9.clicked.connect(lambda: self._addNum("9"))
        self.b_0.clicked.connect(lambda: self._addNum("0"))
        
        
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_umn.clicked.connect(lambda: self._operation("*"))
        self.b_del.clicked.connect(lambda: self._operation("/"))
        self.b_Co.clicked.connect(lambda: self._operation("C"))
        self.b_result.clicked.connect(self._result)

    def _addNum(self,param):
        line=self.input.text()
        self.input.setText(line+param)

    def _operation(self,op):
        if self.input.text()=="":
            self.input.setText(str("Введите число!"))
        elif self.input.text()=="0" and self.op=="/":
            self.input.setText(str("Операция на ноль!"))
        else:
            onlynumber=0
            try:
                float(self.input.text())
                onlynumber=1
            except ValueError:
                onlynumber=0
            if onlynumber==1:
                self.num1=float(self.input.text())
                self.op=op
                self.input.setText("")
            else:
                self.input.setText(str("Вы ввели символы!"))
                
    def _result(self):
        if self.input.text()=="":
            self.input.setText(str("Введите число!"))
        elif self.input.text()=="0" and self.op=="/":
            self.input.setText(str("Операция на ноль!"))
        else:
            onlynumber=0
            try:
                float(self.input.text())
                onlynumber=1
            except ValueError:
                onlynumber=0
            if onlynumber==1:
                self.num2=float(self.input.text())
                self.input.setText("")
                if self.op=="+":
                    self.input.setText(str(self.num1+self.num2))
                elif self.op=="-":
                    self.input.setText(str(self.num1-self.num2))
                elif self.op=="*":
                    self.input.setText(str(self.num1*self.num2))
                elif self.op=="/":
                    self.input.setText(str(self.num1/self.num2))
                elif self.op=="C":
                    self.input.setText("")
                else:
                    self.input.setText(str("Введите знак!"))
            else:
                self.input.setText(str("Вы ввели символы!"))
                       
app=QApplication(sys.argv)
win=Calculator()
win.show()
sys.exit(app.exec_())
