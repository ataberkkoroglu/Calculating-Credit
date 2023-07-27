import requests,sys,deep_translator
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QComboBox,QVBoxLayout,QHBoxLayout,QPushButton,QMainWindow,QApplication,QWidget,QLineEdit,QLabel,QTableWidget,QTableWidgetItem,QHeaderView
from PyQt5.QtGui import QFont,QIcon,QKeySequence


class CalculatorCredit(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.Data()
        self.main()

    def Data(self):
     
     url="https://www.hangikredi.com/kredi/hesaplama-araclari"
     response=requests.get(url)
     Content=response.content.decode()
     soup=BeautifulSoup(Content,"html.parser")
     
     url2="https://www.hesapkurdu.com/ziraat-bankasi/ihtiyac-kredisi"
     response2=requests.get(url2)
     Content2=response2.content.decode()
     soup2=BeautifulSoup(Content2,"html.parser")
     self.ziraat=soup2.find_all('p',{'class':"loan-product-card_value__1xlTE"})[1].text

     self.bank=list()
     
     for i in soup.find_all("td"):
       self.bank.append(i.text)
    
    def main(self):
       
       self.window=QWidget()
       self.window.setWindowTitle("Calculating Credit")
       
       self.amount=QLineEdit()
       self.month=QComboBox()
       
       self.Month=[str(i*6) for i in range(1,7)]


       self.month_text=QLabel("Month : ")
       self.month_text.setFont(QFont('arial',16,True))
       
       self.amount_text=QLabel("Amount : ")
       
       self.amount_text.setFont(QFont('arial',16,True))

       
       self.amount.setFont(QFont('arial',16,True))
       self.month.addItems(self.Month)
       
       self.month.setFont(QFont('arial',11,True))

       self.warning=QLabel("Please Write The Amount To Be Withdrawn Without ('.' and ',' )")
       self.warning.setFont(QFont('arial',16,True))
       self.warning.setStyleSheet("color : red")  

       self.warning2=QLabel()
       self.warning2.setFont(QFont('arial',16,True))
       self.warning2.setStyleSheet("color : red")  

       self.button=QPushButton("Calculate")
       self.button.setFont(QFont('arial',20,True))
       self.button.setStyleSheet("background : green")

       self.button2=QPushButton("Clear")
       self.button2.setFont(QFont('arial',20))
       self.button2.setStyleSheet("background : red")

       self.Text=QTableWidget()
       self.Text.setFont(QFont('arial',11,True))  

       self.Text.setColumnCount(5)
       self.Text.setRowCount(len([self.bank[i] for i in range(4,48) if i%4==0]))
              
       
       self.Text.setHorizontalHeaderLabels([
            "Bank",
            "Credit Type",
            "Interest Rate",
            "Total Cost",
            "Monthly Payment",
       ])
       self.Bank2=[self.bank[i] for i in range(4,48) if i%4==0]

       header=self.Text.horizontalHeader()   
       header2=self.Text.verticalHeader()
       
       for i in range(0,len(self.Bank2)):
         
        self.Text.setItem(i,0,QTableWidgetItem(self.Bank2[i]))
         
       header.setSectionResizeMode(QHeaderView.Stretch)  
       header2.setSectionResizeMode(QHeaderView.Stretch)   
  
      
       self.Text.setSortingEnabled(False) 
       self.google=deep_translator.GoogleTranslator()
       self.Type=QComboBox()
       self.Type.addItems([self.google.translate(self.bank[i]) for i in range(1,4)])
       self.Type.setFont(QFont('Arial',16))
       
       self.Type_Text=QLabel("Credit Type : ")
       self.Type_Text.setFont(QFont('Arial',16,True))
       
       self.Type.setMinimumHeight(70)
       self.Type.setMinimumWidth(700)

       self.amount.setMinimumWidth(700)
       self.month.setMinimumWidth(700)

       h_box=QHBoxLayout() 
       h_box.addWidget(self.month_text)
       h_box.addSpacing(60)
       h_box.addWidget(self.month)
       h_box.addStretch()
       
       h_box2=QHBoxLayout()
       h_box2.addWidget(self.amount_text)
       h_box2.addSpacing(45)
       h_box2.addWidget(self.amount)
       h_box2.addStretch()
       h_box3=QHBoxLayout()
       
       h_box3.addWidget(self.Type_Text)
       h_box3.addWidget(self.Type)
       h_box3.addStretch()

       h_box4=QHBoxLayout()
       h_box4.addSpacing(30)
       h_box4.addWidget(self.button)
       h_box4.addSpacing(40)
       h_box4.addWidget(self.button2)
       h_box4.addSpacing(30)

       v_box=QVBoxLayout()
       
       v_box.addLayout(h_box3)
       v_box.addSpacing(20)
       v_box.addLayout(h_box2)
       v_box.addSpacing(20)
       v_box.addLayout(h_box)
       v_box.addSpacing(20)
       v_box.addWidget(self.warning)
       v_box.addWidget(self.warning2)
       v_box.addSpacing(30)
       v_box.addLayout(h_box4)
       v_box.addSpacing(30)
       v_box.addWidget(self.Text)

       self.window.setLayout(v_box)

       self.button.setShortcut('return')
       self.button2.setShortcut(QKeySequence('delete'))

       self.button.clicked.connect(self.process)
       self.button2.clicked.connect(self.process)
       self.window.setStyleSheet("background : lightblue")

       self.window.setMinimumWidth(1000)
       self.window.setMaximumWidth(1000)
       self.window.setMaximumHeight(1100)
       self.window.setMinimumHeight(1100)
       
       self.window.show()
       
    def process(self):
        sender=self.sender()
        
        if sender.text()=="Calculate":
         
         if self.amount.text()!="":
           amount=self.amount.text()
           if '.' in amount:
             amount=amount.replace('.','')

           if ',' in amount:
              amount=amount.replace(',','')

           if float(amount)<=0:
                self.warning2.setText("Please Write The Amount To Be Withdrawn As It Will Be Greater Than Zero.")
                self.amount.clear()
           else:
               self.Text.setColumnCount(5)
               self.Text.setRowCount(len([self.bank[i] for i in range(4,48) if i%4==0]))
               
               #self.Text.setStyleSheet("background : gray")
               self.Text.setHorizontalHeaderLabels([
            "Bank",
            "Credit Type",
            "Interest Rate",
            "Total Cost",
            "Monthly Payment",
               ])
               self.Bank2=[self.bank[i] for i in range(4,48) if i%4==0]
              
               header=self.Text.horizontalHeader()  
               header2=self.Text.verticalHeader()
               for i in range(0,len(self.Bank2)):
         
                self.Text.setItem(i,0,QTableWidgetItem(self.Bank2[i]))
                header.setSectionResizeMode(0,QHeaderView.ResizeToContents)
               header.setSectionResizeMode(QHeaderView.Stretch)  
               header2.setSectionResizeMode(QHeaderView.Stretch)   
       
               
               self.Text.setSortingEnabled(False)
               self.interest=list()
               Type=self.Type.currentText()
               if Type==self.google.translate(self.bank[1]):
                self.interest=[self.bank[i] for i in range(5,48,4)]
                self.interest[6]=self.ziraat
                
               elif self.Type.currentText()==self.google.translate(self.bank[2]):
                 self.interest=[self.bank[i] for i in range(6,48,4)]
                
               elif self.Type.currentText()==self.google.translate(self.bank[3]):
                 self.interest=[self.bank[i] for i in range(7,48,4)]

         

               for i in range(0,len(self.Bank2)):
                self.Text.setItem(i,1,QTableWidgetItem(Type))

                if self.interest[i]!='\n*\n':
                 self.Text.setItem(i,2,QTableWidgetItem(self.interest[i]))
                 percent=self.interest[i].replace('\n','')
                 percent=percent.replace('%','')
                 percent=percent.replace(',','.')
                 
                 total=float(amount)+(float(amount)*float(percent)/100)
                 
                 self.Text.setItem(i,3,QTableWidgetItem(str(round(total,3))))
                 self.Text.setItem(i,4,QTableWidgetItem(str(round((total/float(self.month.currentText())),3))))

                else:
                 
                 self.Text.setItem(i,2,QTableWidgetItem("")) 
                 self.Text.setItem(i,3,QTableWidgetItem("")) 
                 self.Text.setItem(i,4,QTableWidgetItem("")) 
                
               
         else:
               
               self.warning2.setText("Please Write The Amount To Be Withdrawn As It Will Be Greater Than Zero.")
        else:
           
           self.amount.clear()
           self.warning2.clear()
           for i in range(0,len(self.Bank2)):
              for j in range(0,5):
                 self.Text.setItem(i,j,QTableWidgetItem(""))
         

app=QApplication(sys.argv)
app.setWindowIcon(QIcon("Bank.jpg"))
credit=CalculatorCredit()
sys.exit(app.exec())