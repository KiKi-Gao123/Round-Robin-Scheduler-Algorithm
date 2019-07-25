from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox

class rr:
    def __init__(self, win):
        self.window = win
        self.time_piece = 0
        self.curTimes = 0
        self.info = ''
        self.TxtPath = ''
        self.ReadyQue = [[]]
        self.InputQue = []
        self.OutputQue = []
        self.WaitQue = []

    def msg(self, widget, context):
        echo = QMessageBox.information(widget, "提示", context, QMessageBox.Yes)

    def PromShow(self, que):
        self.info = "时间片" + str(self.curTimes) + ':' + que[0][0] + '[ ' + que[0][1] + ' ]'
        self.window.main_ui.process_lineEdit.setText(que[0][0])
        self.window.main_ui.times_lineEdit.setText(str(self.curTimes))
        self.logTxt.write(self.info + "\n")
        print(self.info)

    def OpenFile(self):
        file_Name, file_type = QFileDialog.getOpenFileName(self.window,
                                                           "选取文件",
                                                           "D:\Python\RR",
                                                           "Text Files (*.txt)")
        # print(file_Name,file_type)
        return file_Name

    def InitQue(self):
        count = 0
        self.TxtPath= self.OpenFile()
        if self.TxtPath != '':
            self.txt = open(self.TxtPath, "r")
            for line in self.txt.readlines():
                if line.split()[0][0] == 'P':
                    self.ReadyQue[count].append(line.split()[0])
                    continue
                elif line.split()[0][0] != 'H':
                    self.ReadyQue[count].append(line.split()[0])
                    continue
                elif line.split()[0][0] == 'H':
                    self.ReadyQue[count].append(line.split()[0])
                    count = count + 1
                    self.ReadyQue.append([])
                # print(self.ReadyQue)
            self.txt.close()
            self.ReadyQue.pop()
            for i in range(count-1):
                if self.ReadyQue[i][1][0] == 'I':
                    self.InputQue.append(self.ReadyQue[i])
                    del self.ReadyQue[i]
                elif self.ReadyQue[i][1][0] == 'O':
                    self.OutputQue.append(self.ReadyQue[i])
                    del self.ReadyQue[i]
                elif self.ReadyQue[i][1][0] == 'W':
                    self.WaitQue.append(self.ReadyQue[i])
                    del self.ReadyQue[i]
            self.window.main_ui.ready_tableWidget.setRowCount(len(self.ReadyQue))
            self.window.main_ui.in_tableWidget.setRowCount(len(self.InputQue))
            self.window.main_ui.out_tableWidget.setRowCount(len(self.OutputQue))
            self.window.main_ui.wait_tableWidget.setRowCount(len(self.WaitQue))
            self.UpdateQue()

    def UpdateQue(self):
        if len(self.ReadyQue) != 0 :
            for i in range(len(self.ReadyQue)):
                self.window.main_ui.ready_tableWidget.setItem(i, 0, QTableWidgetItem(self.ReadyQue[i][0]))
                self.window.main_ui.ready_tableWidget.setItem(i, 1, QTableWidgetItem(self.ReadyQue[i][1]))
        if len(self.InputQue) != 0:
            for i in range(len(self.InputQue)):
                self.window.main_ui.in_tableWidget.setItem(i, 0, QTableWidgetItem(self.InputQue[i][0]))
                self.window.main_ui.in_tableWidget.setItem(i, 1, QTableWidgetItem(self.InputQue[i][1]))
        if len(self.OutputQue) != 0:
            for i in range(len(self.OutputQue)):
                self.window.main_ui.out_tableWidget.setItem(i, 0, QTableWidgetItem(self.OutputQue[i][0]))
                self.window.main_ui.out_tableWidget.setItem(i, 1, QTableWidgetItem(self.OutputQue[i][1]))
        if len(self.WaitQue) != 0:
            for i in range(len(self.WaitQue)):
                self.window.main_ui.wait_tableWidget.setItem(i, 0, QTableWidgetItem(self.WaitQue[i][0]))
                self.window.main_ui.wait_tableWidget.setItem(i, 1, QTableWidgetItem(self.WaitQue[i][1]))
    ###
    def ReadyQueSche(self):
        if len(self.ReadyQue) != 0 and self.ReadyQue[0][1][0] == 'H':
            del self.ReadyQue[0]
        if len(self.ReadyQue) != 0:
            if self.ReadyQue[0][1][0] == 'C':
                if int(self.ReadyQue[0][1][1:]) != 1:
                    self.ReadyQue[0][1] = 'C' + str(int(self.ReadyQue[0][1][1:]) - 1)
                    self.PromShow(self.ReadyQue)
                else:
                    self.ReadyQue[0][1] = 'C' + '0'
                    self.PromShow(self.ReadyQue)
                    del self.ReadyQue[0][1]
                self.ReadyQue.append(self.ReadyQue[0])
                del self.ReadyQue[0]
            elif self.ReadyQue[0][1][0] == 'I':
                self.InputQue.append(self.ReadyQue[0])
                del self.ReadyQue[0]
            elif self.ReadyQue[0][1][0] == 'O':
                self.OutputQue.append(self.ReadyQue[0])
                del self.ReadyQue[0]
            elif self.ReadyQue[0][1][0] == 'W':
                self.WaitQue.append(self.ReadyQue[0])
                del self.ReadyQue[0]

    def InputQueSche(self):
        if len(self.InputQue) != 0 and self.InputQue[0][1][0] == 'H':
            del self.InputQue[0]
        if len(self.InputQue) != 0:
            if self.InputQue[0][1][0] == 'I':
                if int(self.InputQue[0][1][1:]) != 1:
                    self.InputQue[0][1] = 'I' + str(int(self.InputQue[0][1][1:]) - 1)
                    self.PromShow(self.InputQue)
                else:
                    self.InputQue[0][1] = 'I' + '0'
                    self.PromShow(self.InputQue)
                    del self.InputQue[0][1]
                self.InputQue.append(self.InputQue[0])
                del self.InputQue[0]
            elif self.InputQue[0][1][0] == 'C':
                self.ReadyQue.append(self.InputQue[0])
                del self.InputQue[0]
                if len(self.ReadyQue) >= 1:
                    self.ReadyQueSche()
            elif self.InputQue[0][1][0] == 'O':
                self.OutputQue.append(self.InputQue[0])
                del self.InputQue[0]
            elif self.InputQue[0][1][0] == 'W':
                self.WaitQue.append(self.InputQue[0])
                del self.InputQue[0]

    def OutputQueSche(self):
        if len(self.OutputQue) != 0 and self.OutputQue[0][1][0] == 'H':
            del self.OutputQue[0]
        if len(self.OutputQue) != 0:
            if self.OutputQue[0][1][0] == 'O':
                if int(self.OutputQue[0][1][1:]) != 1:
                    self.OutputQue[0][1] = 'O' + str(int(self.OutputQue[0][1][1:]) - 1)
                    self.PromShow(self.OutputQue)
                else:
                    self.OutputQue[0][1] = 'O' + '0'
                    self.PromShow(self.OutputQue)
                    del self.OutputQue[0][1]
                self.OutputQue.append(self.OutputQue[0])
                del self.OutputQue[0]
            elif self.OutputQue[0][1][0] == 'I':
                self.InputQue.append(self.OutputQue[0])
                del self.OutputQue[0]
                if len(self.InputQue) >= 1:
                    self.InputQueSche()
            elif self.OutputQue[0][1][0] == 'C':
                self.ReadyQue.append(self.OutputQue[0])
                del self.OutputQue[0]
                if len(self.ReadyQue) >= 1:
                    self.ReadyQueSche()
            elif self.OutputQue[0][1][0] == 'W':
                self.WaitQue.append(self.OutputQue[0])
                del self.OutputQue[0]

    def WaitQueSche(self):
        if len(self.WaitQue) != 0 and self.WaitQue[0][1][0] == 'H':
            del self.WaitQue[0]
        if len(self.WaitQue) != 0:
            if self.WaitQue[0][1][0] == 'W':
                if int(self.WaitQue[0][1][1:]) != 1:
                    self.WaitQue[0][1] = 'W' + str(int(self.WaitQue[0][1][1:]) - 1)
                    self.PromShow(self.WaitQue)
                else:
                    self.WaitQue[0][1] = 'W' + '0'
                    self.PromShow(self.WaitQue)
                    del self.WaitQue[0][1]
                self.WaitQue.append(self.WaitQue[0])
                del self.WaitQue[0]
            elif self.WaitQue[0][1][0] == 'I':
                self.InputQue.append(self.WaitQue[0])
                del self.WaitQue[0]
                if len(self.InputQue) >= 1:
                    self.InputQueSche()
            elif self.WaitQue[0][1][0] == 'C':
                self.ReadyQue.append(self.WaitQue[0])
                del self.WaitQue[0]
                if len(self.ReadyQue) >= 1:
                    self.ReadyQueSche()
            elif self.WaitQue[0][1][0] == 'O':
                self.OutputQue.append(self.WaitQue[0])
                del self.WaitQue[0]
                if len(self.OutputQue) >= 1:
                    self.OutputQueSche()
    ###
    def RunOneTimeRange(self):
        if len(self.ReadyQue) == 0 and len(self.InputQue) == 0 and len(self.OutputQue) == 0 and len(self.WaitQue) == 0:
            self.EndTimer()
            self.logTxt.close()
            self.ReadyQue = [[]]
            self.curTimes = 0
            self.window.main_ui.process_lineEdit.setText('')
            self.msg(self.window, "完成调度！")
        else:
            self.curTimes += 1
            self.ReadyQueSche()
            self.InputQueSche()
            self.OutputQueSche()
            self.WaitQueSche()

            self.window.main_ui.ready_tableWidget.setRowCount(len(self.ReadyQue))
            self.window.main_ui.in_tableWidget.setRowCount(len(self.InputQue))
            self.window.main_ui.out_tableWidget.setRowCount(len(self.OutputQue))
            self.window.main_ui.wait_tableWidget.setRowCount(len(self.WaitQue))
            self.UpdateQue()

    def StartTimer(self):
        if self.window.main_ui.timepiece_lineEdit.text() == '':
            self.msg(self.window, "请输入时间片的值！")
        elif int(self.window.main_ui.timepiece_lineEdit.text()) == 0:
            self.msg(self.window, "时间片的值不能为0！")
        elif self.TxtPath == '':
            self.msg(self.window, "请载入文件！")
        else:
            self.time_piece = int(self.window.main_ui.timepiece_lineEdit.text())
            self.window.timer.start(self.time_piece)
            self.logTxt = open("log.txt", "w")
            self.window.main_ui.start_pushButton.setEnabled(False)
            self.window.main_ui.suspend_pushButton.setEnabled(True)

    def EndTimer(self):
        self.window.timer.stop()
        self.window.main_ui.suspend_pushButton.setEnabled(False)
        self.window.main_ui.start_pushButton.setEnabled(True)