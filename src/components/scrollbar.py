from PySide2.QtWidgets import *

class CScrollBar(QScrollBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("""
         QScrollBar:vertical {
            border: none;
            background: rgb(52, 59, 72);
            width: 3px;
            margin: 21px 0 21px 0;
            border-radius: 0px;
         }
         QScrollBar::handle:vertical {  
            background: #536D79;
            min-height: 25px;
            border-radius: 4px
         }
         QScrollBar::add-line:vertical {
             border: none;
            background: rgb(55, 63, 77);
             height: 20px;
            border-bottom-left-radius: 4px;
            border-bottom-right-radius: 4px;
             subcontrol-position: bottom;
             subcontrol-origin: margin;
         }
         QScrollBar::sub-line:vertical {
            border: none;
            background: rgb(55, 63, 77);
             height: 20px;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
             subcontrol-position: top;
             subcontrol-origin: margin;
         }
         QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
             background: none;
         }

         QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
             background: none;
         }""")