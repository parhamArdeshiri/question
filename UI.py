from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon, QPixmap
from os import system, listdir, mkdir
from PyQt6.QtCore import QDir, QSize
from os.path import abspath
from reader import Reader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reader")

        icon = QPixmap("./icon.png")
        icon = icon.scaled(QSize(4096, 4096))
        icon = QIcon(icon)

        self.setFixedSize(175, 90)
        self.setWindowIcon(icon)


        self.BLoadF = QPushButton("load input file", self)
        self.BLoadDF = QPushButton("load dat file", self)
        self.BSaveDF = QPushButton("save dat file", self)
        self.BBack = QPushButton("back", self)

        self.TEOutput = QTextEdit(self)

        self.BLoadF.move(40, 5)
        self.BLoadDF.move(40, 55)
        self.BSaveDF.move(200, 315)
        self.BBack.move(100, 315)

        self.BLoadF.clicked.connect(self.__loadFile)
        self.BLoadDF.clicked.connect(self.__loadDF)
        self.BSaveDF.clicked.connect(self.__saveDatFile)
        self.BBack.clicked.connect(self.__back)

        self.TEOutput.setStyleSheet("QTextEdit{background-color: rgba(0, 0, 0, 0%);}")
        self.TEOutput.setReadOnly(True)
        self.TEOutput.setGeometry(1000, 1000, 360, 295)
        
    def __loadFile(self):

        try:
            with open(QFileDialog.getOpenFileName(self, "select your file", QDir.homePath())[0])as inp:
                self.__file = Reader(inp)
        
            self.setFixedSize(400, 350)

        
            self.BLoadF.move(1000, 1000)
            self.BLoadDF.move(1000, 1000)

            self.TEOutput.move(20, 15)
            self.TEOutput.setText(str(self.__file).replace("|", " "))

        except:
            pass

    def __saveDatFile(self):
        Path = QFileDialog.getExistingDirectory(self, "select your directory", QDir.homePath()) + "/save.bin"

        if Path != "/save.bin":
            cd = abspath("cache")
            try:
                caches = listdir("./cache")
            except:
                mkdir("./cache")
                caches = listdir("./cache")

            if "output.txt" not in caches:    
                with open(f"{cd}/output.txt", "x")as f:
                    f.write(str(self.__file))

            else:
                with open(f"{cd}/output.txt", "w")as f:
                    f.write(str(self.__file))

            if "path.txt" not in caches:
                with open(f"{cd}/path.txt", "x")as f:
                    f.write(Path)
                
            else:
                with open(f"{cd}/path.txt", "w")as f:
                    f.write(Path)

            system("saver.exe")

            try:
                with open(f"{cd}/stat.txt")as sf:
                    if sf.read() == "0":
                        QMessageBox.question(self, "Reader", "The output saved succesfully.", QMessageBox.StandardButton.Ok)
                    else:
                        QMessageBox.question(self, "Reader", "Sorry but i can't save the output.", QMessageBox.StandardButton.Ok)
            except:
                QMessageBox.question(self, "Reader", "Sorry but i can't save the output.", QMessageBox.StandardButton.Ok)

    def __loadDF(self):
        Path = QFileDialog.getOpenFileName(self, "select your file", QDir.homePath())[0]

        if Path != "":
            cd = abspath("cache")
            
            try:
                caches = listdir("./cache")
            except:
                mkdir("./cache")
                caches = listdir("./cache")

            if "path.txt" not in caches:
                with open(f"{cd}/path.txt", "x")as f:
                    f.write(Path)
                
            else:
                with open(f"{cd}/path.txt", "w")as f:
                    f.write(Path)

            system("loader.exe")

            try:
                with open(f"{cd}/stat.txt")as sf:
                    if sf.read() == "0":
                        with open(f"{cd}/output.txt")as of:
                            loadedContent = of.read().replace("|", " ")
                        
                        self.setFixedSize(400, 350)
                        
                        self.BLoadF.move(1000, 1000)
                        self.BLoadDF.move(1000, 1000)

                        self.TEOutput.move(20, 15)
                        self.TEOutput.setText(loadedContent)
                    else:
                        QMessageBox.question(self, "Reader", "Sorry but i can't load the file.", QMessageBox.StandardButton.Ok)
            except:
                QMessageBox.question(self, "Reader", "Sorry but i can't load the file.", QMessageBox.StandardButton.Ok)


    def __back(self):
        self.setFixedSize(175, 90)
        self.BLoadF.move(40, 5)
        self.BLoadDF.move(40, 55)
        self.BSaveDF.move(200, 315)
        self.TEOutput.move(1000, 1000)
        
    
        
if __name__ == "__main__":
    from sys import exit, argv

    App = QApplication(argv)

    _MainWindow = MainWindow()

    _MainWindow.show()

    exit(App.exec())