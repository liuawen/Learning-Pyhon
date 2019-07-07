import win32ui

dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
dlg.SetOFNInitialDir('E:/Python')  # 设置打开文件对话框中的初始显示目录
dlg.DoModal()

filename = dlg.GetPathName()  # 获取选择的文件名称
self.lineEdit_InputId_AI.setText(filename)  #将获取的文件名称写入名为“lineEdit_InputId_AI”可编辑文本框中
