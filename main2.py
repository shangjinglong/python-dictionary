from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()


        self.btn_generate = QtWidgets.QPushButton(self)
        self.btn_generate.setObjectName("btn_generate")
        self.btn_generate.setText("生成")
        self.btn_generate.clicked.connect(self.generate)

    def generate(self):
        path = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        print(path)  # 打印文件夹路径



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
