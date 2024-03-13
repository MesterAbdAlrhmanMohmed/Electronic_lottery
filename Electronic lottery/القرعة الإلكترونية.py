from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import random
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("القرعة الإلكترونية")
        self.إظهار=qt.QLabel("أكتب أسماء المتقدمين للمسابقة وقم بالفصل بين أسمائهم بالفاصلة الإنجليزية")
        self.ed=qt.QLineEdit()        
        self.ed.setAccessibleName("أكتب أسماء المتقدمين للمسابقة وقم بالفصل بين أسمائهم بالفاصلة الإنجليزية")
        self.إظهار1=qt.QLabel("عدد الفائزين, من 1 الى5")
        self.count=qt.QSlider()
        self.count.setRange(1,5)
        self.count.setAccessibleName("إختيار عدد الفائزين")
        self.choose=qt.QPushButton("سحب الأصوات")
        self.choose.clicked.connect(self.V)
        self.choose.setDefault(True)
        l=qt.QVBoxLayout()        
        l.addWidget(self.إظهار)
        l.addWidget(self.ed)
        l.addWidget(self.إظهار1)
        l.addWidget(self.count)
        l.addWidget(self.choose)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)  
    def V(self):
        try:
            va=self.count.value()
            val=self.ed.text()
            a=val.split(",")
            s=random.sample(a,va)
            qt.QMessageBox.information(self,"الفائزون"," و ".join(s))
        except:
            qt.QMessageBox.information(self,"خطأ","حدث خطأ")
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()