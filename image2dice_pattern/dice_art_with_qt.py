from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 250)
        MainWindow.setWindowTitle('PHOTO TO DICE')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(643, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(30, 140, 301, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setGeometry(QtCore.QRect(210, 20, 80, 25))
        self.Browse.setObjectName("Browse")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(24, 21, 25, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(31, 171, 64, 17))
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(24, 58, 50, 25))
        self.label_11.setObjectName("label_3")
        self.edt_scale = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_scale.setGeometry(QtCore.QRect(80, 58, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.edt_scale.setSizePolicy(sizePolicy)
        self.edt_scale.setObjectName("edt_scale")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(80, 95, 80, 25))
        self.run.setObjectName("run")
        self.edt_file = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_file.setGeometry(QtCore.QRect(55, 21, 142, 25))
        self.edt_file.setObjectName("edt_file")
        self.total_dice = QtWidgets.QLabel(self.centralwidget)
        self.total_dice.setEnabled(False)
        self.total_dice.setGeometry(QtCore.QRect(300, 171, 50, 20))
        self.total_dice.setObjectName("total_dice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.Browse.clicked.connect(self.getfile)
        self.run.clicked.connect(self.convert)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PHOTO TO DICE"))
        MainWindow.setWindowIcon(QtGui.QIcon('1.png'))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.edt_scale.setText('خالی')
        self.edt_file.setText('خالی')
        self.label_2.setText(_translate("MainWindow", "File:"))
        self.label_3.setText(_translate("MainWindow", "total dice:"))
        self.label_11.setText(_translate("MainWindow", "scale:"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.total_dice.setText(_translate("MainWindow", "0"))
    def getfile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)  
        if fileName:
            self.edt_file.setText(fileName)
    def convert(self):
        self.progressBar.setEnabled(True)
        self.label_11.setEnabled(True)
        import sys
        try:
            from PIL import Image ,ImageOps ,ImageDraw
        except ImportError:
            print("Please install Pillow from: https://pypi.python.org/pypi/Pillow/3.0.0")
            sys.exit(1)

        import os ,sys
        img = None
        try:
            img = Image.open(self.edt_file.text())
        except (FileNotFoundError,AttributeError):
            self.getfile()
            while not img:
                try:
                    img = Image.open(self.edt_file.text())
                except (FileNotFoundError,AttributeError):
                    self.getfile()
        self.img_name = img.filename.split('/')[-1]
        d1 = Image.open('./dice/1.jpg')
        d2= Image.open('./dice/2.jpg')
        d3 = Image.open('./dice/3.jpg')
        d4 = Image.open('./dice/4.jpg')
        d5 = Image.open('./dice/5.jpg')
        d6 = Image.open('./dice/6.jpg')
        dicew =300
        dicesize = int(img.width*1.0/dicew)
        if dicesize < 20 :
            dicesize = 20
        print(f'diseSize "{dicesize}"')
        dices= [d1,d2,d3,d4,d5,d6]
        for i in range(0,len(dices)):
            dices[i]=dices[i].resize((dicesize,dicesize),Image.ANTIALIAS)
            dices[i].save("./temp/"+str(i)+".temp","JPEG")
        img = ImageOps.grayscale(img)
        img = ImageOps.equalize(img)
        img.save("./temp/pngconvert.jpg","JPEG")
        if self.edt_scale.text()!='خالی':
            try:
                scale = int(self.edt_scale.text())
                if scale <= 0:
                    scale = 1
                img=img.resize((img.width*scale,img.height*scale))
            except:
                pass
                print(f'cant scaled-: "{self.edt_scale.text()}"')
                qmb = QtWidgets.QMessageBox()
                qmb.setText(f'ضریب مقیاس درست وارد نشده')
                qmb.setStandardButtons(QtWidgets.QMessageBox.Ok)
                qmb.setIcon(QtWidgets.QMessageBox.Warning)
                result = qmb.exec_()
                return 0
        print (f'dicew : "{dicew}"')
        nim = Image.new("L",(img.width,img.height),'white')
        nimdd = Image.new("L",(img.width,img.height),'white')
        nimd = ImageDraw.Draw(nim)

        total=0
        for y in range(0,img.height-dicesize,dicesize):
            for x in range(0,img.width-dicesize,dicesize):
                thisSectorColor = 0
                for dicex in range(0,dicesize):
                    for dicey in range(0,dicesize):
                        thisColor = img.getpixel((x+dicex,y+dicey))
                        thisSectorColor+=thisColor
                thisSectorColor/=(dicesize**2)
                diceNumber = int((255-thisSectorColor)*6.0/255+1)
                if diceNumber < 1:
                    diceNumber = 1
                if diceNumber > 6:
                    diceNumber = 6
                box=(x,y,x+dicesize,y+dicesize)
                if diceNumber==1:
                    nimdd.paste(dices[0],box)
                elif diceNumber==2:
                    nimdd.paste(dices[1],box)
                elif diceNumber==3:
                    nimdd.paste(dices[2],box)
                elif diceNumber==4:
                    nimdd.paste(dices[3],box)
                elif diceNumber==5:
                    nimdd.paste(dices[4],box)
                elif diceNumber==6:
                    nimdd.paste(dices[5],box)
                self.progressBar.setValue(int((y+1)*100/img.height)+1)
                total+=1
                self.total_dice.setText(str(total))

        self.progressBar.setValue(100)
        self.total_dice.setText(str(total))
        print(f'total dice "{total}"')
        nimdd.save(self.img_name,"JPEG")
        qmb = QtWidgets.QMessageBox()
        qmb.setText(f'تبدیل عکس شما به پایان رسید. آیا مایل به تبدیل عکس دیگری هستید؟')
        qmb.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        qmb.setIcon(QtWidgets.QMessageBox.Warning)
        result = qmb.exec_()
        if result == QtWidgets.QMessageBox.Yes:
            self.progressBar.setValue(0)
            self.total_dice.setText('0')
            self.edt_file.setText('خالی')
            self.edt_scale.setText('خالی')
            return 0

        sys.exit(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('1.png'))
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('1.png'))
    MainWindow.setWindowTitle('PHOTO TO DICE')
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
