darkMode="""
       VideoWidget{
           background-image: url('images/zolo1.png');
       }
       QSlider::groove:horizontal {
       border: 1px solid #0a1931;
       background: white;
       height: 8px;
       border-radius: 4px;
    }

       QSlider::sub-page:horizontal {
        background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
        stop: 0 #66e, stop: 1 #bbf);
        background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
        stop: 0 #bbf, stop: 1 #55f);
        border: 1px solid #777;
        height: 10px;
        border-radius: 4px;
    }

    QSlider::add-page:horizontal {
    background: #fff;
    border: 1px solid #777;
    height: 10px;
    border-radius: 4px;
    }

    QSlider::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 #eee, stop:1 #ccc);
    border: 1px solid #777;
    width: 13px;
    margin-top: -2px;
    margin-bottom: -2px;
    border-radius: 4px;
    }

    QSlider::handle:horizontal:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 #fff, stop:1 #ddd);
    border: 1px solid #444;
    border-radius: 4px;
    }

    QSlider::sub-page:horizontal:disabled {
    background: #bbb;
    border-color: #999;
    }

    QSlider::add-page:horizontal:disabled {
    background: #eee;
    border-color: #999;
    }

    QSlider::handle:horizontal:disabled {
    background: #eee;
    border: 1px solid #aaa;
    border-radius: 4px;
    }
    QWidget{
        background:#364547
       }
    QMenuBar{
        background: #05f519
        
       }
    addMenu{
        font-color:#05f519
    }
    QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 #05f519, stop:1 #81b214);
}
QMenuBar::item {
    spacing: 3px;           
    padding: 2px 10px;
    background-color: #05f519;
    color: #05f519;  
    border-radius: 5px;
}
QMenuBar::item:selected {    
    background-color: #05f519;
}
QMenuBar::item:pressed {
    background: #05f519;
}

/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */  

QMenu {
    background-color: #05f519;   
    border: 1px solid black;
    margin: 2px;
}
QMenu::item {
    background-color: transparent;
}
QMenu::item:selected { 
    background-color:#364547 ;
    color: white;
}
QPushButton{
    color:#05f519;
}
"""