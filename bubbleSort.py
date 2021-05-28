# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bubble_sort.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
# '#001219' "#ee9b00"
def main():
        class Ui_MainWindow(object):
            def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(990, 970)
                MainWindow.setMinimumSize(QtCore.QSize(990, 965))
                MainWindow.setMaximumSize(QtCore.QSize(990, 970))
                MainWindow.setStyleSheet('background:#001219; color:#ee9b00')

                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
                self.scrollArea.setGeometry(QtCore.QRect(0, 0, 982, 943))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())

                self.scrollArea.setSizePolicy(sizePolicy)
                self.scrollArea.setMinimumSize(QtCore.QSize(0, 500))
                self.scrollArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.WaitCursor))
                self.scrollArea.setAcceptDrops(False)
                self.scrollArea.setAutoFillBackground(True)
                self.scrollArea.setStyleSheet("border:none;\n"
        "QScrollBar\n"
        "{\n"
        "background : lightgreen;}")
                self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
                self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
                self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 961, 1018))
                self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
                self.frame.setMinimumSize(QtCore.QSize(0, 1000))
                self.frame.setAcceptDrops(False)
                self.frame.setStyleSheet("border:none")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
                self.frame.setObjectName("frame")



                self.complexity_label = QtWidgets.QLabel(self.frame)
                self.complexity_label.setGeometry(QtCore.QRect(10, 770, 211, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)

                self.complexity_label.setFont(font)
                self.complexity_label.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.complexity_label.setTextFormat(QtCore.Qt.PlainText)
                self.complexity_label.setObjectName("complexity_label")
                self.algo_header = QtWidgets.QLabel(self.frame)
                self.algo_header.setGeometry(QtCore.QRect(10, 460, 331, 41))

                self.algo_header.setFont(font)
                self.algo_header.setObjectName("algo_header")
                self.header_label = QtWidgets.QLabel(self.frame)
                self.header_label.setGeometry(QtCore.QRect(10, 0, 251, 51))

                font.setPointSize(25)

                self.header_label.setFont(font)
                self.header_label.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.header_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.header_label.setObjectName("header_label")
                self.algorithm = QtWidgets.QLabel(self.frame)
                self.algorithm.setGeometry(QtCore.QRect(20, 510, 901, 251))

                font.setPointSize(14)
                self.algorithm.setFont(font)
                self.algorithm.setObjectName("algorithm")
                self.gif_label = QtWidgets.QLabel(self.frame)
                self.gif_label.setGeometry(QtCore.QRect(20, 230, 371, 191))

                font.setPointSize(14)
                self.gif_label.setFont(font)
                self.gif_label.setScaledContents(True)
                self.gif_label.setObjectName("gif_label")
                self.header_info_label = QtWidgets.QLabel(self.frame)
                self.header_info_label.setGeometry(QtCore.QRect(10, 60, 921, 131))

                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)

                self.header_info_label.setFont(font)
                self.header_info_label.setFocusPolicy(QtCore.Qt.NoFocus)
                self.header_info_label.setTextFormat(QtCore.Qt.AutoText)
                self.header_info_label.setScaledContents(False)
                self.header_info_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
                self.header_info_label.setWordWrap(True)
                self.header_info_label.setIndent(1)
                self.header_info_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
                self.header_info_label.setObjectName("header_info_label")
                self.complexity_table = QtWidgets.QTableWidget(self.frame)
                self.complexity_table.setGeometry(QtCore.QRect(30, 830, 501, 61))

                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.complexity_table.setFont(font)
                self.complexity_table.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.complexity_table.setStyleSheet("border:\'black\'")
                self.complexity_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.complexity_table.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.complexity_table.setLineWidth(1)
                self.complexity_table.setMidLineWidth(1)
                self.complexity_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                self.complexity_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                self.complexity_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
                self.complexity_table.setShowGrid(True)
                self.complexity_table.setGridStyle(QtCore.Qt.DashDotDotLine)
                self.complexity_table.setObjectName("complexity_table")
                self.complexity_table.setColumnCount(5)
                self.complexity_table.setRowCount(1)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                item.setFont(font)
                item.setBackground(QtGui.QColor(255, 255, 255))
                self.complexity_table.setVerticalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                item.setFont(font)
                self.complexity_table.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.complexity_table.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.complexity_table.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.complexity_table.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.complexity_table.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.complexity_table.setItem(0, 0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.complexity_table.setItem(0, 1, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.complexity_table.setItem(0, 2, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.complexity_table.setItem(0, 3, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.complexity_table.setItem(0, 4, item)
                self.complexity_table.horizontalHeader().setVisible(True)
                self.complexity_table.horizontalHeader().setCascadingSectionResizes(False)
                self.complexity_table.verticalHeader().setVisible(False)
                self.complexity_table.verticalHeader().setHighlightSections(True)
                self.verticalLayout_3.addWidget(self.frame)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

            def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Bubble Sort"))
                self.complexity_label.setText(_translate("MainWindow", "Complexity"))
                self.algo_header.setText(_translate("MainWindow", "Algorithm:"))
                self.header_label.setText(_translate("MainWindow", "BubbleSort"))
                self.algorithm.setText(_translate("MainWindow", "Step 1: Repeat Step 2 For i = 0 to N-1\n"
        "Step 2: Repeat For J = i + 1 to N - I\n"
        "Step 3: IF A[J] > A[i]\n"
        "SWAP A[J] and A[i]\n"
        "[END OF INNER LOOP]\n"
        "[END OF OUTER LOOP\n"
        "Step 4: EXIT\n"
        ""))
                #adding gif to the gif label
                self.gif_label.setText(_translate("MainWindow", "Bubble-sort-example-gif"))
                self.movie=QMovie(".\gifs\Bubble-sort.gif")
                self.gif_label.setMovie(self.movie)
                self.movie.start()


                self.header_info_label.setText(_translate("MainWindow", "Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order (ascending or descending arrangement). The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted."))
                item = self.complexity_table.verticalHeaderItem(0)
                item.setText(_translate("MainWindow", "Bubblesort"))
                item = self.complexity_table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Best"))
                item = self.complexity_table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Average"))
                item = self.complexity_table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Worst"))
                item = self.complexity_table.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Memory"))
                item = self.complexity_table.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "Stable"))
                __sortingEnabled = self.complexity_table.isSortingEnabled()
                self.complexity_table.setSortingEnabled(False)
                item = self.complexity_table.item(0, 0)
                item.setText(_translate("MainWindow", "n"))
                item = self.complexity_table.item(0, 1)
                item.setText(_translate("MainWindow", "n2"))
                item = self.complexity_table.item(0, 2)
                item.setText(_translate("MainWindow", "n2"))
                item = self.complexity_table.item(0, 3)
                item.setText(_translate("MainWindow", "1"))
                item = self.complexity_table.item(0, 4)
                item.setText(_translate("MainWindow", "Yes"))
                self.complexity_table.setSortingEnabled(__sortingEnabled)


        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        app.exec_()