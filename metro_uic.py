#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from mainwindow import MainWindow

if __name__ == '__main__':

    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'owen control' )

    # create widget
    window = MainWindow()
    #window.show()
    window.showFullScreen()  

    # connection
    #QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )
    app.lastWindowClosed.connect(quit)

    # execute application
    #sys.exit( app.exec_() )
    app.exec_()
    app.deleteLater()
    sys.exit()    
