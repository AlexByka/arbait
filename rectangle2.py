import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
import rec
class work(QtWidgets.QMainWindow, rec.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.setColumnCount(5)
        self.pushButton_6.clicked.connect(self.addition)
        self.pushButton_8.clicked.connect(self.delete)
        self.pushButton_7.clicked.connect(self.changeData)
        self.pushButton_9.clicked.connect(self.cross)
        self.pushButton_4.clicked.connect(self.unhideVL4)
        self.pushButton.clicked.connect(self.unhideVL1)
        self.pushButton_2.clicked.connect(self.unhideVL2)
        self.pushButton_3.clicked.connect(self.unhideVL3)
        self.pushButton_5.clicked.connect(self.hideAll)
        self.setWindowTitle("Работа с базой данных через SQL-запросы через графический интерфейс QtCreator'a")
        self.tableWidget.setHorizontalHeaderLabels(['name', 'x1', 'y1', 'x2', 'y2'])
        self.comboBox_2.addItem('name')
        self.comboBox_2.addItem('x1')
        self.comboBox_2.addItem('y1')
        self.comboBox_2.addItem('x2')
        self.comboBox_2.addItem('y2')
        self.hideAll()
        self.showDB()



    def hideAll(self):
        self.hideVL1()
        self.hideVL2()
        self.hideVL3()
        self.hideVL4()

    def showMenu(self):
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.pushButton_4.show()
        self.pushButton_5.hide()
        self.lineEdit_4.clear()

    def hideMenu(self):
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.label_2.hide()
        self.pushButton_5.show()

    def hideVL1(self):
        self.label_3.hide()
        self.label_4.hide()
        self.label_7.hide()
        self.label_10.hide()
        self.label_9.hide()
        self.label_11.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()
        self.lineEdit_8.hide()
        self.pushButton_6.hide()
        self.showMenu()

    def unhideVL1(self):
        self.label_3.show()
        self.label_4.show()
        self.label_7.show()
        self.label_10.show()
        self.label_9.show()
        self.label_11.show()
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.lineEdit_6.show()
        self.lineEdit_7.show()
        self.lineEdit_8.show()
        self.pushButton_6.show()
        self.hideMenu()

    def hideVL2(self):
        self.label_5.hide()
        self.label_6.hide()
        self.label_8.hide()
        self.comboBox.hide()
        self.comboBox_2.hide()
        self.lineEdit_3.hide()
        self.pushButton_7.hide()
        self.showMenu()

    def unhideVL2(self):
        self.label_5.show()
        self.label_6.show()
        self.label_8.show()
        self.comboBox.show()
        self.comboBox_2.show()
        self.lineEdit_3.show()
        self.pushButton_7.show()
        self.hideMenu()

    def hideVL3(self):
        self.label_12.hide()
        self.comboBox_3.hide()
        self.pushButton_8.hide()
        self.showMenu()

    def unhideVL3(self):
        self.label_12.show()
        self.comboBox_3.show()
        self.pushButton_8.show()
        self.hideMenu()

    def hideVL4(self):
        self.label_13.hide()
        self.pushButton_9.hide()
        self.comboBox_5.hide()
        self.comboBox_4.hide()
        self.lineEdit_4.hide()
        self.showMenu()

    def unhideVL4(self):
        self.label_13.show()
        self.pushButton_9.show()
        self.comboBox_5.show()
        self.comboBox_4.show()
        self.lineEdit_4.show()
        self.hideMenu()

    def showDB(self):
        for i in range(self.tableWidget.rowCount()): # очистка таблицы
            self.tableWidget.removeRow(0)
        db = sqlite3.connect('rectangle.db')  # подключаем базу
        cursor = db.cursor()  # создаем курсор для обращения к базе через запросы
        cursor.execute("SELECT * FROM Rectangle")
        result=cursor.fetchall()
        self.comboBox.clear()
        self.comboBox_3.clear()
        self.comboBox_4.clear()
        self.comboBox_5.clear()
        for i in range(len(result)):
            name = result[i][1]
            x1 = result[i][2]
            y1 = result[i][3]
            x2 = result[i][4]
            y2 = result[i][5]
            numRows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(numRows)
            self.tableWidget.setItem(numRows, 0, QTableWidgetItem(str(name)))
            self.tableWidget.setItem(numRows, 1, QTableWidgetItem(str(x1)))
            self.tableWidget.setItem(numRows, 2, QTableWidgetItem(str(y1)))
            self.tableWidget.setItem(numRows, 3, QTableWidgetItem(str(x2)))
            self.tableWidget.setItem(numRows, 4, QTableWidgetItem(str(y2)))
            self.comboBox.addItem(name)
            self.comboBox_3.addItem(name)
            self.comboBox_4.addItem(name)
            self.comboBox_5.addItem(name)
        cursor.close()
        db.close()

    def changeData(self):
        db = sqlite3.connect('rectangle.db')  # подключаем базу
        cursor = db.cursor()  # создаем курсор для обращения к базе через запросы
        name = self.comboBox.currentText()
        key = self.comboBox_2.currentText()
        cursor.execute("SELECT * FROM Rectangle WHERE name='" + name + "'")
        value = self.lineEdit_3.text()
        if value == "":
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText('Вы не ввели новое значение!')
            error.show()
            error.exec_()
        else:
            cursor.execute("UPDATE Rectangle SET "+ key +"='" + value + "' WHERE name = '" + name + "'")
            self.lineEdit_3.clear()
        db.commit()
        self.showDB()
        cursor.close()
        db.close()

    def addition(self):
        db = sqlite3.connect('rectangle.db')  # подключаем базу
        cursor = db.cursor()  # создаем курсор для обращения к базе через запросы
        name = self.lineEdit.text()
        x1 = self.lineEdit_7.text()
        y1 = self.lineEdit_6.text()
        x2 = self.lineEdit_2.text()
        y2 = self.lineEdit_8.text()
        if name=='' or x1=='' or y1=='' or x2=='' or y2=='':
            error=QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText('Для добавления в базу данных необходимо заполнить все поля!')
            error.show()
            error.exec_()
        else:
            cursor.execute("INSERT INTO Rectangle(name, x1, y1, x2, y2) VALUES ('" + name + "', '" + x1 + "', '" + y1 + "','" + x2 + "', '" + y2 + "')")
            self.lineEdit.clear()
            self.lineEdit_7.clear()
            self.lineEdit_6.clear()
            self.lineEdit_2.clear()
            self.lineEdit_8.clear()
        db.commit()
        self.showDB()
        db.close()

    def delete(self):
        db = sqlite3.connect('rectangle.db')  # подключаем базу
        cursor = db.cursor()  # создаем курсор для обращения к базе через запросы
        name = self.comboBox_3.currentText()
        cursor.execute("DELETE FROM Rectangle WHERE name = '" + name + "'")
        db.commit()
        self.showDB()
        db.close()

    def cross(self):
        db = sqlite3.connect('rectangle.db')  # подключаем базу
        cursor = db.cursor()  # создаем курсор для обращения к базе через запросы
        name1 = self.comboBox_4.currentText()
        name2 = self.comboBox_5.currentText()
        cursor.execute("SELECT x1,y1,x2,y2 FROM Rectangle WHERE name = '" + name1 + "'")
        name1_DB = cursor.fetchall()
        cursor.execute("SELECT x1,y1,x2,y2 FROM Rectangle WHERE name = '" + name2 + "'")
        name2_DB = cursor.fetchall()
        z = list(name1_DB[0])
        q = list(name2_DB[0])
        z.sort()
        q.sort()
        z.pop(3)
        z.pop(0)
        q.pop(3)
        q.pop(0)
        print(q[0])
        self.lineEdit_4.setText("A:" + "(" + str(z[0])+","+str(q[1]) + ")" + " B:" + "(" + str(z[1])+","+str(q[1]) + ")" + " C:" + "(" + str(z[1])+","+str(q[0]) + ")" + " D:" + "(" + str(z[0])+","+str(q[0]) + ")")
        db.commit()
        self.showDB()
        cursor.close()
        db.close()



def main():
    app=QtWidgets.QApplication(sys.argv)
    window = work()
    window.show()
    app.exec_()


main()