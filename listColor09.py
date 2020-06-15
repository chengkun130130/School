# ui 组件
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QStringListModel 
from PyQt5.QtWidgets import   QMessageBox,QListView, QStatusBar,  QMenuBar,QMenu,QAction,QLineEdit,QStyle,QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QStandardItem,QStandardItemModel
from PyQt5.QtCore import QStringListModel,QAbstractListModel,QModelIndex,QSize

import tkinter as tk
from PIL import ImageGrab
from aip import AipOcr
import pyautogui,time,sys
# import  pymssql
import pymysql

# APP_ID = '18671135'
# API_KEY = 'k2YWlrlg14PXGBA2RE9ede9O'
# SECRET_KEY = 'vClNwl9OME8yIrG8Q5VuqK04q6EAA2mv'

APP_ID = '20396492'
API_KEY = 'RVO4b6fBqefILMnebAa2932A'
SECRET_KEY = '8Vom46kx0LeIKgnSlsiEeKUIcpeIOGhB'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
window = tk.Tk()
window.title('新建文本文档')
window.geometry('400x800+1300+100')
filePath = r"D:\DNweituo.png"
# 数据库连接参数
hostVal="rm-bp1b7b8guumr51js9oo.mysql.rds.aliyuncs.com"
portVal=3306
userVal="my_python"
passwdVal="1qaz2wsx@"
dbVal="my_python"
# 本地数据库
# hostVal="127.0.0.1"
# portVal=3306
# userVal="root"
# passwdVal="1qaz2wsx@"
# dbVal="python"
# 更改编队信息
seatVal="9号机"
teamVal = '3'      #队伍编号    4台机器一个队伍 
marshallingVal="1" #第一个屏幕   16台主机用于清空数据
# 清除的sql
deleteSql = "DELETE  FROM  task WHERE marshalling ='1'" #删除第一个屏幕显示的数据 改数字更改屏幕
# 查看的sql
getSql1 = "SELECT DISTINCT cont FROM task where team = '1'"#查询编队为5的任务 更改数字更改编队
getSql2 = "SELECT DISTINCT cont FROM task where team = '2'"#查询编队为6的任务 更改数字更改编队
getSql3 = "SELECT DISTINCT cont FROM task where team = '3'"#查询编队为7的任务 更改数字更改编队
getSql4 = "SELECT DISTINCT cont FROM task where team = '4'"#查询编队为8的任务 更改数字更改编队

# 截图
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
# 插入数据
def setVal(conten):
    connSet= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
    connSet.ping(reconnect=True) 
    curSet = connSet.cursor()

    batchVal = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    contVal=conten
    sql = "INSERT INTO task(batch, cont,seat,team,marshalling)\
         VALUES('%s','%s','%s','%s','%s')" %(batchVal, contVal, seatVal, teamVal ,marshallingVal)
    try:
        print(random.randint(12, 20))
        curSet.execute(sql)
        connSet.commit()
        curSet.close()
        connSet.close()
    except:
        connSet.rollback()


class Ui_Dialog(object):
    view1=[]
    view2=[]
    view3=[]
    view4=[]
    view5=[]
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 1000)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        desktop = QApplication.desktop()

        # 通过桌面的宽和高来比例位置显示
        Dialog.move(desktop.width()*1-320, desktop.height()*0)
        
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 160, 180))
        self.listWidget.setObjectName("listWidget") 
        
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)

        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(160, 0, 160, 180))
        self.listWidget_2.setObjectName("listWidget_2")

        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)

        self.listWidget_3 = QtWidgets.QListWidget(Dialog)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 180, 160, 180))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)    
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)    
        self.listWidget_4 = QtWidgets.QListWidget(Dialog)
        self.listWidget_4.setGeometry(QtCore.QRect(160, 180, 160, 180))
        self.listWidget_4.setObjectName("listWidget_4")
        
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        

        self.listWidget_5 = QtWidgets.QListWidget(Dialog)
        self.listWidget_5.setGeometry(QtCore.QRect(0, 360, 381, 500))
        self.listWidget_5.setObjectName("listWidget_5")
        
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)

        # item = QtWidgets.QListWidgetItem()
        # font = QtGui.QFont()
        # font.setPointSize(26)
        # item.setFont(font)
        # brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item.setForeground(brush)
        # self.listWidget_5.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)
        
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)
        # 逆袭
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(26)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 870, 75, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 930, 75, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 870, 75, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 930, 75, 50))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # 截图写入数据
    def catch(self):
        img=ImageGrab.grab(bbox=(580,400,1020,480))
        img.save(filePath)
        image = get_file_content(filePath)
        req = client.basicGeneral(image)
        all_test =''
        # all_test =req["words_result"][0]["words"]
        for i in req['words_result']:
            all_test += i['words']
        if (all_test==""):
            all_test="没有截取可用数据"
        self.view5=[]
        self.view5.append(all_test)
        self.view5_new=["","","","","","","","","",""]
        if(len(self.view5)<8):
            for newI5 in range(len(self.view5)):
                self.view5_new[newI5]=self.view5[newI5]    
        MainWindow = QMainWindow()
        # self.retranslateUi(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        for i5 in range(len(self.view5_new)):
            item = self.listWidget_5.item(i5)
            item.setText(_translate("Dialog", ""))
        item = self.listWidget_5.item(0)
        item.setText(_translate("Dialog", self.view5[0]))
        self.listWidget_5.setSortingEnabled(__sortingEnabled)         
        sheet = ['传说中的魔兽','渔夫的生活',"不是胆小鬼","胜负","查尔德不是孩子","消失的名字","勇士之路"]
        all_test = all_test.replace('!','')
        if(all_test in sheet):
            if(all_test=='传说中的魔兽'):
                all_test="狮蝎巢穴"            
            elif(all_test=="渔夫的生活"):
                all_test="卡伊伦巢穴"
            elif(all_test=="不是胆小鬼"):
                all_test="大主教巢穴"
            elif(all_test=="胜负"):
                all_test="K博士巢穴"
            elif(all_test=="查尔德不是孩子"):
                all_test="代达罗斯巢穴"
            elif(all_test=="消失的名字"):
                all_test="格拉诺巢穴"
            elif(all_test=="勇士之路"):
                all_test="火山巢穴"  
            setVal(all_test)
            # pyautogui.moveTo(930,560)
            pyautogui.click(930,560)
        elif("逆袭" in all_test):
            setVal(all_test)
            # pyautogui.moveTo(930,560)
            pyautogui.click(930,560)
        else:
            pyautogui.click(790,560)
            
    # 清除数据
    def removeVal(self):
        connDelete= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curDelete = connDelete.cursor()
        # sql = "DELETE  FROM  task WHERE marshalling ='2'" #删除第一个屏幕显示的数据 改数字更改屏幕
        # curDelete.execute(sql)
        curDelete.execute(deleteSql)
        connDelete.commit()
        connDelete.close() 

        self.testGet()
    # 查看数据
    def testGet(self):
        self.view1=[]
        self.view2=[]
        self.view3=[]
        self.view4=[]
        self.view5=[]
        connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curSelect = connSelect.cursor()
        # sql = "SELECT DISTINCT cont FROM task where team = '5'"#查询编队为1的任务 更改数字更改编队
        curSelect.execute(getSql1)
        sqlList=curSelect.fetchall()
        
        for i in sqlList:
            self.view1.append(i[0].strip())
        # sql2 = "SELECT DISTINCT cont FROM task where team = '6'"
        curSelect.execute(getSql2)
        sqlList2=curSelect.fetchall()
        for i2 in sqlList2:
            self.view2.append(i2[0].strip())
        # sql3 = "SELECT DISTINCT cont FROM task where team = '7'"
        curSelect.execute(getSql3)
        sqlList3=curSelect.fetchall()
        for i3 in sqlList3:
            self.view3.append(i3[0].strip())
        # sql4 = "SELECT DISTINCT cont FROM task where team = '8'"
        curSelect.execute(getSql4)
        sqlList4=curSelect.fetchall()
        for i4 in sqlList4:
            self.view4.append(i4[0].strip())
        connSelect.close()
        newList=[]
        newNxList=[]
        if(len(self.view1)!=0):
            i1 = 0
            while i1 < len(self.view1):
                if "逆袭" in self.view1[i1]:
                    newNxList.append(self.view1[i1])
                    self.view1.pop(i1)
                    i1 -= 1
                i1 += 1
        if(len(self.view2)!=0):
            i2 = 0
            while i2 < len(self.view2):
                if "逆袭" in self.view2[i2]:
                    newNxList.append(self.view2[i2])
                    self.view2.pop(i2)
                    i2 -= 1
                i2 += 1
        if(len(self.view3)!=0):
            i3 = 0
            while i3 < len(self.view3):
                if "逆袭" in self.view3[i3]:
                    newNxList.append(self.view3[i3])
                    self.view3.pop(i3)
                    i3 -= 1
                i3 += 1
        if(len(self.view4)!=0):
            i4 = 0
            while i4 < len(self.view4):
                if "逆袭" in self.view4[i4]:
                    newNxList.append(self.view4[i4])
                    self.view4.pop(i4)
                    i4 -= 1
                i4 += 1
        if(len(self.view1)!=0):
            newList=self.view1
        if(len(self.view2)!=0):
            if(len(newList)==0):
                newList=self.view2
            else:
                newList=list(set(newList).intersection(set(self.view2)))
        if(len(self.view3)!=0):
            # if(len(newList)==0):
            if(len(self.view1)==0 and len(self.view2)==0):
                newList=self.view3
            else:
                newList=list(set(newList).intersection(set(self.view3)))
        if(len(self.view4)!=0):
            # if(len(newList)==0):
            if(len(self.view1)==0 and len(self.view2)==0 and len(self.view3)==0):
                newList=self.view4
            else:
                newList=list(set(newList).intersection(set(self.view4)))
        newNxList = list(set(newNxList))
        self.view5=newList
        MainWindow = QMainWindow()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
        # 第一个显示格子
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.NoneList=["","","","","","","","","",""]
        for None1 in range(len(self.NoneList)):
            item = self.listWidget.item(None1)
            item.setText(_translate("Dialog", self.NoneList[None1]))
        for i1 in range(len(self.view1)):
            item = self.listWidget.item(i1)
            item.setText(_translate("Dialog", self.view1[i1]))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        #第二个格子
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        for None1 in range(len(self.NoneList)):
            item = self.listWidget_2.item(None1)
            item.setText(_translate("Dialog", self.NoneList[None1]))
        
        for i2 in range(len(self.view2)):
            item = self.listWidget_2.item(i2)
            item.setText(_translate("Dialog", self.view2[i2]))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        #第三个格子
        __sortingEnabled= self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        for None1 in range(len(self.NoneList)):
            item = self.listWidget_3.item(None1)
            item.setText(_translate("Dialog", self.NoneList[None1]))
        for i3 in range(len(self.view3)):
            item = self.listWidget_3.item(i3)
            item.setText(_translate("Dialog", self.view3[i3]))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        #第四个格子
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        for None1 in range(len(self.NoneList)):
            item = self.listWidget_4.item(None1)
            item.setText(_translate("Dialog", self.NoneList[None1]))
        for i4 in range(len(self.view4)):
            item = self.listWidget_4.item(i4)
            item.setText(_translate("Dialog", self.view4[i4]))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        #第五个格子
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)

        if ("K博士巢穴" in self.view5):
            item = self.listWidget_5.item(0)
            item.setText(_translate("Dialog", "K博士巢穴"))
        else:
            item = self.listWidget_5.item(0)
            item.setText(_translate("Dialog", ""))

        if("狮蝎巢穴" in self.view5):
            item = self.listWidget_5.item(1)
            item.setText(_translate("Dialog", "狮蝎巢穴"))
        else:
            item = self.listWidget_5.item(1)
            item.setText(_translate("Dialog", ""))

        if("大主教巢穴" in self.view5):
            item = self.listWidget_5.item(2)
            item.setText(_translate("Dialog", "大主教巢穴"))
        else:
            item = self.listWidget_5.item(2)
            item.setText(_translate("Dialog", ""))

        if("格拉诺巢穴" in self.view5):
            item = self.listWidget_5.item(3)
            item.setText(_translate("Dialog", "格拉诺巢穴"))
        else:
            item = self.listWidget_5.item(3)
            item.setText(_translate("Dialog", ""))

        if("卡伊伦巢穴" in self.view5):
            item = self.listWidget_5.item(4)
            item.setText(_translate("Dialog", "卡伊伦巢穴"))
        else:
            item = self.listWidget_5.item(4)
            item.setText(_translate("Dialog", ""))
        
        if("代达罗斯巢穴" in self.view5):
            item = self.listWidget_5.item(5)
            item.setText(_translate("Dialog", "代达罗斯巢穴"))
        else:
            item = self.listWidget_5.item(5)
            item.setText(_translate("Dialog", ""))

        if("火山巢穴" in self.view5):
            item = self.listWidget_5.item(6)
            item.setText(_translate("Dialog", "火山巢穴"))
        else:
            item = self.listWidget_5.item(6)
            item.setText(_translate("Dialog", ""))

        nxIndex=6
        item = self.listWidget_5.item(7)
        item.setText(_translate("Dialog", ""))
        item = self.listWidget_5.item(8)
        item.setText(_translate("Dialog", ""))
        item = self.listWidget_5.item(9)
        item.setText(_translate("Dialog", ""))
        item = self.listWidget_5.item(10)
        item.setText(_translate("Dialog", ""))
        if(len(newNxList)!=0):
            for index in range(len(newNxList)):
                nxIndex=nxIndex+1
                item = self.listWidget_5.item(nxIndex)
                item.setText(_translate("Dialog", newNxList[index]))  
        self.listWidget_5.setSortingEnabled(__sortingEnabled)

    def delSql(self):
        img=ImageGrab.grab(bbox=(580,400,1020,480))
        img.save(filePath)
        image = get_file_content(filePath)
        req = client.basicGeneral(image)
        all_test =''
        # all_test =req["words_result"][0]["words"]
        for i in req['words_result']:
            all_test += i['words']
        all_test = all_test.replace('!','')
        if (all_test==""):
            all_test="没有截取可用数据"
        if(all_test=='传说中的魔兽'):
            all_test="狮蝎巢穴"            
        elif(all_test=="渔夫的生活"):
            all_test="卡伊伦巢穴"
        elif(all_test=="不是胆小鬼"):
            all_test="大主教巢穴"
        elif(all_test=="胜负"):
            all_test="K博士巢穴"
        elif(all_test=="查尔德不是孩子"):
            all_test="代达罗斯巢穴"
        elif(all_test=="消失的名字"):
            all_test="格拉诺巢穴"
        elif(all_test=="勇士之路"):
            all_test="火山巢穴"
        self.view5=[]
        self.view5.append(all_test)
        self.view5_new=["","","","","","","","","",""]
        if(len(self.view5)<8):
            for newI5 in range(len(self.view5)):
                self.view5_new[newI5]=self.view5[newI5]    
        MainWindow = QMainWindow()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        for i5 in range(len(self.view5_new)):
            item = self.listWidget_5.item(i5)
            item.setText(_translate("Dialog", ""))
        item = self.listWidget_5.item(0)
        item.setText(_translate("Dialog", self.view5[0]))
        self.listWidget_5.setSortingEnabled(__sortingEnabled)

        connDelSql= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curDelSql = connDelSql.cursor()
        sqlDelRql="SELECT DISTINCT seat,cont FROM task where cont = '"+all_test+"' and team = '"+teamVal+"'"
        #print(sqlDelRql)
        curDelSql.execute(sqlDelRql)
        #curDelSql.execute("SELECT DISTINCT cont FROM task where team = '1'")
        sqlDelRqlList=curDelSql.fetchall()
        connDelSql.close()
        print(sqlDelRqlList)
        if(len(sqlDelRqlList)>0):
            if(all_test==sqlDelRqlList[0][1] and seatVal == sqlDelRqlList[0][0]):
                pyautogui.click(930,560)
                print("是本机器")
            else:
                print("不是本机器")
                pyautogui.click(790,560)
        else:
            print("没查到相关数据")
            pyautogui.click(790,560)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        # 第一个显示格子
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        for i1 in range(len(self.view1)):
            item = self.listWidget.item(i1)
            item.setText(_translate("Dialog", self.view1[i1]))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        #第二个格子
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        for i2 in range(len(self.view2)):
            item = self.listWidget_2.item(i2)
            item.setText(_translate("Dialog", self.view2[i2]))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        #第三个格子
        __sortingEnabled= self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        for i3 in range(len(self.view3)):
            item = self.listWidget_3.item(i3)
            item.setText(_translate("Dialog", self.view3[i3]))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        #第四个格子
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        for i4 in range(len(self.view4)):
            item = self.listWidget_4.item(i4)
            item.setText(_translate("Dialog", self.view4[i4]))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        #第五个格子
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        for i5 in range(len(self.view5)):
            item = self.listWidget_5.item(i5)
            item.setText(_translate("Dialog", self.view5[i5]))
        self.listWidget_5.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(_translate("Dialog", "截图"))
        self.pushButton.clicked.connect(self.catch)

        self.pushButton_2.setText(_translate("Dialog", "查看"))
        self.pushButton_2.clicked.connect(self.testGet)

        self.pushButton_3.setText(_translate("Dialog", "截图2"))
        self.pushButton_3.clicked.connect(self.delSql)

        self.pushButton_4.setText(_translate("Dialog", "清除"))
        self.pushButton_4.clicked.connect(self.removeVal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
