from PyQt5.QtWidgets import QMessageBox

def TetrisAboutWindow():
    msgBox = QMessageBox(
                QMessageBox.Information,
                "О программе | About",
                "Данная программа была сделана в ходе выполнения лабораторных работ в университете (БРгТУ, Системное Программирование, Комиссаров А.Е.)\n-------------------------\nThis program was created while completing assignments at my university (BSTU, subject of system programming, Komissarov A.E.)",
                QMessageBox.Ok
                )
    return msgBox

