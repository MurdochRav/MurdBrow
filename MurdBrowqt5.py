#!/usr/bin/python3

# put page load on prgress bar
# add stuff and see when it segfaults stopping
# startbroe not worth it 
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtNetwork  import *
from PyQt5.QtWebEngineCore import *

# murdoch for some reason it minimized
# for no reason ?
from rs7 import *
import sys, os,time

# keep track of that
# also nome for cache seems uselessss


class PdfDi( QFileDialog ):
   
    def __init__(self, parent, ptt):
            
        QFileDialog.__init__(self,parent,ptt)
        self.setNameFilter('*.pdf')
        # may have to do  not use native
        #self.pg = p
         
        self.ptry = Svloc()+ ptt
        print ( 'ptry',self.ptry)
        fi = QFileInfo(self.ptry)
        self.setAcceptMode(QFileDialog.AcceptSave)
        self.selectFile(fi.absoluteFilePath())
        print ('64' , fi.isFile())### False
        self.setMinimumSize ( 150,100) 
        if self.layout().__class__.__name__ == 'QGridLayout':
            self.pb = QRadioButton("Portrait")
            self.lb = QRadioButton("Landscape")
            self.pb.setChecked(True)
            self.szr =  QComboBox(self)
            # data is QPageSize::A4 =	0  etc
            self.szr.addItem('A1 594 x 841 mm : 23.4" x 33.1"',6)
            self.szr.addItem('A2 420 x 594 mm : 16.5" x 23.4"',7)
            self.szr.addItem('A3 297 x 420 mm :11.7" x 16.5"',8)
            self.szr.addItem('A4 210 x 297 mm 8.3" x 11.7"',0)
            self.szr.addItem('A5 148 x 210 mm : 5.8" x 8.3"',9)
            self.szr.setCurrentIndex(3)
            # a4 is most common  size
            self.layout().addWidget(self.pb,7, 0)
            self.layout().addWidget(self.lb,7, 1)
            self.layout().addWidget(self.szr,7,2)

class Irq(QWebEngineUrlRequestInterceptor):
    #mPlaying = pyqtSignal(QProcess)
    # had sms thing fo maybe
    # donloading media in mf12ms
    def __init__(self, parent): 
        
        QWebEngineUrlRequestInterceptor.__init__(self)
        self.dad = parent
    def interceptRequest(self,r): 
        #print ('r' , r.resourceType())
        #windows does not show type 8
        # 13 ?????
        # or maybe use b in r.rq.h which is same as
        # r.rq.h.__contains__(b)
        # or find 
        for b in self.dad.blokstuff.BLOK:
            if r.requestUrl().host().count(b)>0:
                print ('blocking' , r.requestUrl())
                r.block(True)
                return        


            elif 'Show Asks' in  self.dad.blokstuff.BLOK:
                print ('Asking For', r.requestUrl(),int(r.resourceType()))
        
            
            
class Findr( QInputDialog):
    luk =  pyqtSignal(str)
    def __init__(self, parent,srch):
        QInputDialog.__init__(self,parent)
        self.setMinimumSize ( 150,50) 
        self.setOkButtonText( "Find" )
        self.setTextValue(srch)
        
        
        
    def accept(self):
        self.luk.emit(self.textValue())

    def reject(self):
        print ('254  finished')
        self.setTextValue('')
        self.luk.emit(self.textValue())
        self.hide()



class  MurdStak( QStackedWidget):
    def __init__(self,a):
        QStackedWidget.__init__(self)
        qv = int(qVersion ().split('.')[1])
        if qv > 7:
            self.PgSvTyp = 2  # IE mht
        else:
            self.PgSvTyp = 1  # htm
        #print '{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{102'
        self.frstpg = False
        if len(a)> 1 :
            self.frstpg = self.strtpg(a[1]) # only using first ?
        self.setMouseTracking(True)
        if QSystemTrayIcon.isSystemTrayAvailable():
            trayicon= QIcon("images/Dog9.png")
            self.tricon = QSystemTrayIcon(self)
            self.tricon.setIcon(  trayicon)
            self.tricon.show()
            self.tricon.activated.connect(self.iKlik)
            print ('Tray') # YES on windows
        else:
            print ("No Tray")
        self.setWindowIcon (QIcon("images/Dog8.png"))
        mrgn = QMargins(1,30,1,1)
        ##mrgn = QMargins(1,26,1,1)
        self.setContentsMargins(mrgn)
        self.dnld = False
        self.lasthoov = ''
        self.currentChanged.connect(self.fixcnt)
        self.widgetRemoved.connect(self.fixcnt)
        self.surchR = ''
        self.sTart = True
        
        self.toolBar =QToolBar('Controls' , self)
        #self.toolBar =QToolBar('Controls')
        self.toolBar.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.toolBar.setMinimumSize(1500 , 20)
        if IsKde():
            self.toolBar.setStyleSheet("QToolBar {background-color: \
            rgba(200, 255, 125,  190);  }")
            ### KDE plasma puts extraneous black 
            # background behind toolbar I say it is a bug
            # either in  KDE or qt
        else:
            self.toolBar.setStyleSheet("QToolBar {background-color: \
            rgba(200, 255, 125,  90);  }")
        
        
        self.toolBar.setMouseTracking(True)
        
        murdSize(self)
        
        # tool bar not work in plsama with graphics
        if not IsKde():
            efct =QGraphicsDropShadowEffect()
            efct.setBlurRadius(10.0)
            self.toolBar.setGraphicsEffect(efct)
        
        
        self.toolBar.addAction("Menu")
        # can do insertWidget(ACTIN,BEFOREWIDGET )
        
        self.mNu =  QMenu ("MenU" , self) 
        adD=self.mNu.addAction("Add")
        delpg =  self.mNu.addAction("Remove")
        
        
        
        opnpg =  QMenu("Open",self)
        self.mNu.addMenu(opnpg)
        opnpg.addAction('File')
        opnpg.addAction('Web')
        #self.mNu.addAction("Open")
        fndtxt = self.mNu.addAction("Find")
        #print 'add' , self.adD
        self.addAction(fndtxt)
        self.addAction(fndtxt)
        fndtxt.setShortcut(Qt.Key_F12 )
        #fndtxt.setShortcut("Ctrl+F" )
                
        blrb = self.mNu.addAction("Blurb")
        blrb.setShortcut(Qt.Key_F1 )
        self.addAction(blrb)
        blrb.triggered.connect(self.getblurb)
        
        
        shwmnu = QAction(self)
        shwmnu.setShortcut(Qt.Key_F9 )
        shwmnu.triggered.connect(self.mNubr)
        self.addAction(shwmnu)
        
       
        
        self.mNu.addAction("Save")
        self.mNu.addAction("toPdf")
        self.mNu.addAction("Rss")
        
        qUit = QMenu("Quit",self)
        self.mNu.addMenu(qUit)
        qUit.addAction("Quit")
        qUit.addAction("Quit and Clear")
        # consider quit and save
        
        qts = QAction(self)
        self.addAction(qts)
        qts.setShortcut(Qt.Key_F10 )
        qts.triggered.connect(sys.exit)
        self.toolBar.addAction("Settings")
        self.sEt =  QMenu ("SeT" , self)
        
        pgsv = QMenu("Pg Sv Type",self)
        svacgr =  QActionGroup(self)
        x = 0
        for p in Pgsvtp:
            pst = pgsv.addAction(p)
            svacgr.addAction(pst)
            pst.setCheckable(True)
            pst.setData(x)
            x+= 1
        pst.setChecked(True)    
        self.sEt.addMenu(pgsv)
        agnt =  QMenu("Agent",self)
        agntgrp=  QActionGroup(self)
        for a in Agnts:
            ag =agnt.addAction(a)
            agntgrp.addAction(ag)
            ag.setCheckable(True)
            if a == 'Default':
                ag.setChecked (True)
        self.sEt.addMenu(agnt)
        blokr =  self.sEt.addAction('Block')
        self.blokstuff = Ckr(self)
        aBout = self.sEt.addAction('About')
        
        self.mNu.triggered.connect(self.mnuAC)
        self.sEt.triggered.connect(self.setAC)
        self.bkwd = QAction(self.style().standardIcon(\
            QStyle.SP_ArrowBack),"Back" , self)
        self.toolBar.addAction(self.bkwd)
        self.fwd =  QAction(self.style().standardIcon(
           QStyle.SP_ArrowForward),"Fwd" , self)
        self.toolBar.addAction(self.fwd)
        self.rld =  QAction(self.style().standardIcon(
            QStyle.SP_BrowserReload),"Rld" , self)
        self.toolBar.addAction(self.rld)    
        klok = Klok(self)
        klok.wlsig.connect(self.whl)
        
        
        
     
        
        
        self.toolBar.actionTriggered.connect(self.toolAc)
        self.nXt = QAction(self.style().standardIcon(\
            QStyle.SP_ArrowDown),"Next" , self)
        self.Icon = QIcon('images/Dog12.png')
        self.iCn = QAction(QIcon('images/Dog12.png'),"Clpb",self)
        # rather than action label because I want to
        # use wheel to go through pages
        self.iCn.setWhatsThis('arsehole')
        
        self.pRv = QAction(self.style().standardIcon(\
         QStyle.SP_ArrowUp),"Previous" , self)
        #print ' prv is' , self.pRv
        self.toolBar.addAction(self.pRv)        
        #self.Iconac = self.toolBar.addAction(self.Icon,'url to clipbard')
        self.toolBar.addWidget(klok)
        
        self.toolBar.addAction(self.nXt)
        
        # some kind of  style thing 
        
        self.inf = QLabel()
        self.inf.setText('  Empty  ')
        self.toolBar.addWidget(self.inf)
        self.lcd =  QLCDNumber(self)
        self.lcd.setNumDigits( 4)
        self.lcd.setStyleSheet("QLCDNumber {background-color: \
               rgb(10%, 30%, 10%)  }")
        self.toolBar.addWidget(self.lcd)
        self.fntSzr = QSlider(Qt.Horizontal,self)
        self.fntSzr.setRange ( -20, 100 )
        self.fntSzr.setMinimumWidth (50) 
        self.fntSzr.setMaximumWidth (100) 
        self.fntSzr.setToolTip("Font Size")
        self.fntSzr.valueChanged.connect(self.webfnt)
        
        self.toolBar.addWidget(self.fntSzr)
        self.jsbut = QRadioButton("Spt", self)
        self.jsbut.setMaximumSize(QSize(100,100))
        
        self.jsbut.setChecked ( True )
        self.jsbut.setToolTip("Script On Off")
        self.jsbut.setAutoExclusive(False) 
        self.jsbut.toggled.connect(self.scripT)
        self.Pbut = QRadioButton("Plg",self)
        self.Pbut.setMaximumSize(QSize(100,100))
        self.Pbut.setChecked ( False )
        self.Pbut.setToolTip("Plugins (Flash)")
        self.Pbut.setAutoExclusive(False) 
        self.Pbut.toggled.connect(self.pluG)
        self.toolBar.addWidget(self.jsbut)
        self.toolBar.addWidget(self.Pbut)
        self.fcs = QAction(self.style().standardIcon(\
           QStyle.SP_MessageBoxQuestion), "Focus??", self)
        self.toolBar.addAction(self.fcs)
        self.toolBar.addAction(self.iCn)
        
        self.stat =  QStatusBar(self.toolBar)
        #self.stat =  QStatusBar(self)
        self.stat.setStyleSheet("QStatusBar {background-color: \
               rgba(255, 255, 0, 150);  }")
        self.stat.setMinimumSize(350 , 20)
        self.stat.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding)
        
        self.toolBar.addWidget(self.stat)
        self.prgb = QProgressBar(self)
        self.prgb.setFormat('%p%') 
        self.stat.addPermanentWidget(self.prgb)
        self.prgb.hide()
        
        
        
        
        
        #self.adD.trigger()
        #self.mnuAC('Add')
        self.flscr =  QAction(self)
        self.flscr.setShortcut(Qt.Key_F11)
        self.flscr.triggered.connect( self.fUlscr)
        # screws up at my first page ??
        self.addAction( self.flscr)
        
        QWebEngineSettings.globalSettings().setAttribute (QWebEngineSettings.FullScreenSupportEnabled, True)
        ##print 'adD'
        adD.trigger()
        ##print 'adD' sets up first page
        #prf = self.currentWidget().page().profile() 
        #prf.downloadRequested.connect(self.dWnld)
            
        #self.webfnt(20)
        self.fntSzr.setValue(FoNT)
        self.rqi = Irq(self)
        
        
    def getblurb(self):
        print ('load blurb ie Help!', BlrbPth)
        self.currentWidget().load(BlrbPth)
        
        
        
    def iKlik(self,r):
        # this needed for stalone tray unminimize
        #print 'System Icon kliked or something' , r
        print ('iklik')
        if self.isMinimized():
            print ('Normal')
            self.showNormal()
            self.move(0,0)
            
        
        
        
    def whl(self,i):
        # wheel on clock for going thru paged
        print ('klok wheel' , i)
        if i > 0:
            self.toolAc('Previous')
        elif i < 0:
            self.toolAc('Next')
        
    def mNubr(self):
        Vis = self.toolBar.isVisible() 
        print ( 'show the toolbar' , Vis)
        if Vis:
            # demobrowser starts new webenginview
            
            self.toolBar.setVisible(False)
            mrgn = QMargins(0,5,0,0)
            self.setContentsMargins(mrgn)
                  
            #self.removeWidget(self.toolBar) 
            # BUT BACKGROUND STAYS THERE 
            # NUMBSKULL not background BUT margin !!!!
            #self.toolBar.setMaximumHeight (2)
            #self.toolBar.lower()
            #self.redraw()
        else:
            mrgn = QMargins(0,26,0,0)
            self.setContentsMargins(mrgn)
            self.toolBar.setVisible(True)
            #self.toolBar.raise_()
        
    def mouseMoveEvent(self,ev) :
        #print ('264 mous' , ev.pos().y())
        #print ('264 mous' , ev.parent())
        #self.toolBar.move(ev.pos())
        
        Vis = self.toolBar.isVisible()
        if not Vis:
            # would be neat if this were just temporary
            self.toolBar.setVisible(True)
            self.toolBar.raise_()    
            #self.repaint()
            print ("mouse???", self.mouseGrabber())
            QTimer.singleShot(6000, self.hideTB)
    
    def hideTB(self):
        # if I am doing klok wheel thing do not hide toolbar
        # comes here after I change page ???
        # No  NO new page comes on top of toolbar
        # toolbar raise_ fixes this 
        print ('hide toolbar again')
        self.toolBar.setVisible(False)
            
    
    def fUlscr(self):
        print ('720')
        # toggle thru full reg and minimized
        #print ('Can Do Full Screen' ,  self.br.settings().globalSettings().\
        #testAttribute(QWebEngineSettings.FullScreenSupportEnabled))
        # unminimalize never gets HERE
        # it returns to previous state
        # hence below makes sense.
        if self.isFullScreen() :
            self.showNormal()
            self.showMinimized()
        #elif self.isMinimized(): 
            
            #print 'Normal'
        else:
            self.showFullScreen()
        
            
        
    def pluG(self,b):
        print ('Plug' , b)
        crnt = self.currentWidget()
        try:
            crnt.settings().setAttribute (QWebEngineSettings.PluginsEnabled,b)
        except:
            print ('no Plug')
    
    def scripT(self,b):
        print ('script' , b)
        crnt = self.currentWidget()
        crnt.settings().setAttribute (QWebEngineSettings.JavascriptEnabled,b)
    
        
        
    def fixcnt(self,i= -1):
        t = self.count()
        i= self.currentIndex() +1 
        infstr = str(i) + ' of ' + str(t)
        self.inf.setText(infstr)
       
    
        
  
        
    def hoover(self,h):
        #print 'hoover' , h
        if len(h)> 0:
            self.stat.showMessage(h , 2000)
        self.lasthoov = QUrl(h)
    def Getting(self):
        ur = self.currentWidget().url().toString()
        print ('ur' , ur) 
        if  ur.find('chrome-error')> -1 :
            self.delPage()
            print ('delete page')
            
            return
        
        ## or toString  errorString() does nothing
        print ('_____________________Getting_______', ur)
        # above is where we ar coming FROM 
        # fix font scrpt etc.
        self.chngd()
   
        
    def Gotit(self):
        print ('Got it') 
        print ('Donload ??' , self.dnld ,self.sTart)
                
        if self.sTart:
            # do this stuf once only
            prf = self.currentWidget().page().profile() 
            prf.downloadRequested.connect(self.dWnld)
            #rqi = Irq(self)
            #prf.setRequestInterceptor(rqi) segfaults
            prf.setRequestInterceptor(self.rqi)
            self.cach = self.currentWidget().page().profile().cachePath()
            self.spy = self.currentWidget().page().profile().persistentStoragePath()
            print ('cache and spy are' , self.cach ,self.spy)
            
            self.sTart = False
            
        elif str(self.currentWidget().page().url()).find('/murdQUIT')> -1:
            print ('406  QUIT')
            sys.exit()
            # need / above for windoze 10
        elif self.dnld:
            c = self.count()
            print ('lastwid is ' , self.widget(c-1).url(), 'of' , str(c))
            lw = self.widget(c-1)
            if lw.url().isEmpty() :
                print ('Empty Widget')
                
                self.removeWidget(lw)
                lw.deleteLater()
            self.dnld = False
        crnt = self.currentWidget()
        zm = self.lcd.value()
        print ('crnt' , crnt ,zm) 
        crnt.setZoomFactor (zm)
        #crnt.setFocus()
        
        
        
            
          
    def dwngot(self,p,y=0):
        ##print 'p y' , p , y 
         
        # download item thingy comes here with
        # received, total
        # webview would give a number 0 to 100
        # IE percent
        self.prgb.show()
        if y != 0:
            z = p*100/y
            self.prgb.setValue(z)
            print ('prgb set' , z)
        elif p != 0:
            self.prgb.setValue(p)
            ##print '460 prgb set' , p
        #print ('downloading' , p, 'of' , y)
        if p == y and y!= 0  :
            QTimer.singleShot(3000, self.prgb.hide)
        elif p == 100 and y ==0:
            QTimer.singleShot(3000, self.prgb.hide)
                
                
    def dWnld(self,d):
        print ('237 download' , d , d.__class__.__name__)
        #print 'dld??' , self.dnld
        #d is a webenginedownload item 
        # sometimes comes here True with 
        ### save image 
        ## this self.dnld is not
        # being used correctly
        if self.dnld:
            # may not be correct 
            # linits to 1 download at a time ???
            self.dnld = False
            try:
                d.accept()
                d.downloadProgress.connect(self.dwngot)
            except:
                print ('I goofed d is ' , d)
            return
        # i GET USELESS BLANK PAGE
        # when downloading 
        # have some kind of if thingy in mf12m
        #d.accept()
        self.dnld = True
        if d.__class__.__name__ == "MurdPage":
            if self.PgSvTyp == 2 :
                nm = d.title()+'.mht'
            else:
                nm = d.title()+'.htm'
            
            # getting with gtk
            # not a qt download
        else:
            nm = d.url().fileName()
            # why is this wrong ????
            print ('actual url' , d.url())
            print ('500 name' ,nm)
            # save pic comes here
            # but not from guglmap
            # came rom 237 download
            #print 'local' , d.url().toLocalFile()nothing
            # 
        sgst =  Svloc()+ nm
        #print( 'SAVE in' , Svloc()
        print ('503 sgst nm' , nm) 
        print ('513 last.hoov' , self.lasthoov.fileName())
        # use above to correct name ?????
        # somehow let user pick ????
        self.svnm =  QFileDialog.getSaveFileName(self, 'Save As', sgst)[0]
        print ('save as' , self.svnm)
        if self.svnm == '':
            return
        elif d.__class__.__name__ == "MurdPage":
            #self.sAving = True
            qv = int(qVersion ().split('.')[1])
            if qv < 8:
                print ('Save Will not Work Automatically')
                hd =  'console.log(document.documentElement.innerHTML)'
                cwp = self.currentWidget().page()
                cwp.svScrNm = self.svnm
                cwp.svScr = True
                cwp.runJavaScript(hd)
                
                
                
            try:
                svd = d.save(self.svnm,self.PgSvTyp)
                # 2 means mht
                #1 means htm with directories
                # 0 means htm Only IE. nop pics etc
                print ('svd' , svd )  #None for qt5.9 also jscript save
            except:
                print ('Save Not Working')
                # 2 is mht
                # 1 is complete ???
                
            #self.dnld = False comment out for 5.8 abd up
            # chrome automatiacally adds html 
            # which is wrong should be htm
            # comes back here 
            # do I need accept ?
        
        else:
            d.setPath(self.svnm)
            #d.downloadProgress.connect(self.dwngot) 
            d.finished.connect(self.Gotit)
            #d.stateChanged.connect(self.dwnstate)
            
            d.accept()
            d.downloadProgress.connect(self.dwngot) 
        
        
    def nubr(self):
        print ('454 nubr')
        b = MurdVu(self)
        #b.page().linkHoverd.connect(self,hoover)
        c=self.addWidget(b)
        self.fixcnt()
        b.loadStarted.connect(self.Getting)
        b.loadFinished.connect(self.Gotit)
        # moved from mnuAC
        b.page().linkHovered.connect(self.hoover)
        b.page().fullScreenRequested.connect(self.FlPg)
        b.page().isig.connect(self.icOn)
                
        return b
        

    def webfnt(self,n,b=False):
        #print ('webfnt' , n)
        z = n /100.0
        self.lcd.display(z + 1)
        if not b:
            self.currentWidget().setZoomFactor (z + 1)
        else :
            b.setZoomFactor (z + 1)
    
    def setAC(self,a):
        print ('a', a , a.data())
        t= a.text()
        print ('637 t' , t,a.data())
        ### confusing agent comes with None
        ## but block comes with ''
        if a.data() != None:
            print('not none')
            self.PgSvTyp = a.data()
        elif t == "Default":
            self.currentWidget().page().profile().setHttpUserAgent("")
            ## QTdocs do not show this !!!!
        elif t == 'Block':
            print ('Block' , a)
            self.doblok(a)
        elif t == 'About':
            inf = 'Murdbrowqt5 .0012  Copyright Martin M Raivio\n \
            email murdochrav at yahoo.ca\n \
            for more info click Blurb on start page '
            
            abt =  QMessageBox.about(self,'About',inf)
        
            
        else:
            print ('Fell Thru ????')
            self.currentWidget().page().profile().setHttpUserAgent(t)
            
            
        
    def mnuAC(self,a):
        t= a.text()
        print ('655 t' , t)
        if  t == 'Add':
            # murdoch somwhow Add failed once ??? 
            print ('add Browser')
            br = self.nubr()
            # NEED case where argv has file ur url
            if self.frstpg:
                br.load(self.frstpg)
                self.frstpg = False
            else:
                h = HOMEPG()
                br.setHtml(h,HmRsrc)
            z = self.fntSzr.value()
            self.webfnt(z,br)
            
        elif t == 'Remove':
            self.delPage()
        elif t =='Find':
            findr= Findr(self,self.surchR)
            findr.luk.connect(  self.luking)
            findr.show()
            findr.destroyed.connect(self.luking)
        elif t== 'Quit':
            sys.exit()
        elif t == "Quit and Clear":
            self.cLear()
        elif t == 'Save':
            self.Svpg()
        
        elif t == "Rss":
            self.doRSS()
        elif t == "toPdf":
            self.strtPDF()
        elif t == "File":
            print ('Open')
            sgst =  Svloc()
            gtflnm =  QFileDialog.getOpenFileUrl(self, 'Open', sgst)
            # Above is really a pyqt bug
            #Why a tuple ??
            
            print ('Get' , gtflnm)
            self.currentWidget().load(gtflnm[0])  
        elif t == "Web":
            print ('Open Web')
            # QInputDialog::getText(QWidget *parent, const QString &title, 
            #const QString &label,
            gtwb =  QInputDialog.getText(self, 'Web ', 'http')
            if gtwb[1]:
                if gtwb[0][:4].lower() != 'http':
                    ldwb = 'http://' + gtwb[0]
                else:
                    ldwb = gtwb[0]
                self.currentWidget().load(QUrl(ldwb))  
            
        elif t == "Default":
            self.currentWidget().page().profile().setHttpUserAgent("")
            ## QTdocs do not show this !!!!
        else:
            self.currentWidget().page().profile().setHttpUserAgent(t)
                
    def cLear(self):
        print ('remove' , self.cach, 'and',  self.spy, 'and leave')
        #print 'cach path here ???', self.currentWidget().page()
        #.profile().cachePath()
        # reports WRONG
        import shutil
        try:
            shutil.rmtree(self.cach)
            shutil.rmtree(self.spy)
        except:
            print ('dirs probably already deleated')
        # leaves 2 empty directories UP in place 
        sys.exit()    
            
    def doRSS(self):
        #do as popup rather than page
        self.gssgt = Rssr(self)
        self.gssgt.setModal(False)
        self.gssgt.rssdun.connect(self.gotrspg)
        self.gssgt.exec_()
    
    def gotrspg(self,s):
        print ('Got RSPG'  ,s)
        # if clock NO
        self.currentWidget().load(s)
        self.gssgt.deleteLater() 
    
        
        
        
    def icOn(self,i,p):
        print ('new icon' , i ,' for ' ,p)
        if p == self.currentWidget().page():
            print ('New Icon here')
            self.iCn.setIcon(i)
        
    def delPage(self):
        print ('delete')
        br = self.currentWidget()
        if self.count()> 1:
            # first make different page current
            i = self.currentIndex()
            print ( 'AT' , i)
            if i == 0:
                n = i+1
            else: 
                n = i -1
            
            self.removeWidget(br)
            br.deleteLater() 
        else:
            br.setHtml(HOMEPG(),HmRsrc)
    def FlPg(self ,rq):
        # need for video full screen
        if not self.isFullScreen():
            self.showFullScreen()
        rq.accept()
    
        
    def doblok(self,a):
        print ('Block', a)
        self.blokstuff.popup(self.pos())
        
    def Svpg(self):
        print ('Save Page')
        spg = self.currentWidget().page()
        self.dWnld(spg)
        
        
    def strtPDF(self):
        print ('SSSSSSSSSSSSSSSSSSSSStart pdf')
        ptt =self.currentWidget().page().title().replace('/', '_')+'.pdf'
        ptry = Svloc()+ ptt
        self.prnm = PdfDi(self,ptt)
        print ('PRNM =' ,self.prnm)
        pdfdid = self.prnm.show()
        print ('pdfdid' , pdfdid)
        self.prnm.fileSelected.connect(self.pdfdun)

    def pdfdun(self,f):
        print ('pdf picked' , f)
        # only comes here if I accept overwrite
        p = self.currentWidget().page()
        print ('print', p)
        try:
            sz = self.prnm.szr.currentData()
        except :
            sz = 0
        ps =(QPageSize(sz))
        print ('size' ,ps)
        try:
            ldscp = self.prnm.lb.isChecked()
        except:
            ldscp = False
        print ('Land scape ?' , ldscp)
        
        pL = QPageLayout(ps,ldscp,QMarginsF(0.0, 0.0, 0.0, 0.0)) 
        p.printToPdf(f,pL)
    
        
        
            
    def luking(self,l):
        print ( 'look for' , l)
        self.surchR = l
        self.currentWidget().findText(l)
        # in qt 5.9 i tkkeps on looking
        # even after I shut down finder
        
    def toolAc(self,act):
        try:
            txt = act.text()
        except:
            # came with string'
            txt = act
        print ('toolax' , txt)
        if txt == 'Menu':
            if WinDoz():
                self.showNormal()
            #for some reason file pop menu
            # not showing in windoz maximized
            p = QPoint( self.pos().x()+10, self.pos().y()+30)
            print ('show menu', self.mNu , 'at', p)
            #QWidget::mapToGlobal()
            #exec(QCursor::pos()
            #self.mNu.exec_(p)
            self.mNu.popup(p)
        elif txt  == 'Settings':
           
            if WinDoz(): 
                self.showNormal()
            
            print ('show settings', self.sEt)
            p = QPoint( self.pos().x()+40, self.pos().y()+30)
            #self.sEt.exec_(p)
            self.sEt.popup(p)
        elif  txt == 'Back':
            self.currentWidget().back()
            
            print ('BACK')
        elif txt == 'Fwd':
            self.currentWidget().forward()
        elif txt == "Rld":
            self.currentWidget().reload()    
        
        elif txt == 'Next':
            nx = self.currentIndex() +1
            #c= self.count()
            print ('nx',nx) 
            self.setCurrentIndex(nx )
            self.toolBar.raise_()
            # note for next and previous
            # we either set self.fntSzr
            # and also script and plugins
            # to what browser is at
            # or set browser to what 
            # do THAT as it does not need
            # a new function
            # self.fntSzr is at
            #print 'fontszr at' , self.fntSzr.value()
            self.chngd()
            
            
        elif txt == 'Previous':
            pv = self.currentIndex() -1
            self.setCurrentIndex(pv )
            self.toolBar.raise_()
            # seems to just fail if
            # not possible no crash no probs
            self.chngd()
            
            
            
        elif txt == 'Clpb':
            print ('clip')
            u= self.currentWidget().url().toDisplayString()
            QGuiApplication.clipboard().setText(u)
            # right ckick does not come here 
             
             
        elif txt == 'Focus??':
           # I say this is qt bug sometimes browser stops working
           # never happens in wayland ??
           # this fixes it https://www.w3schools.com/htmL/tryit.asp?filename=tryhtml5_geolocation
           print ('Browser kiddies' ,  self.currentWidget().children())
           ind = self.currentIndex()
           print ('current' ,  ind)
           #self.setCurrentIndex(ind )
           # try glwidget update
           # murdoch fix
           # should really make sure [2]
           # IS gl widget
           # it just reports as being a widget ???
           # in Debian THAT is action thing
           for chld in self.currentWidget().children():
               #print ('Kiddie class' , chld.__class__.__name__)
               if chld.__class__.__name__ == 'QOpenGLWidget':
                   chld.update()
           #print ('[2] IS ', self.currentWidget().children()[2].__class__)
           #self.currentWidget().children()[2].update()
           #### YESSS THIS WORKS 
           # should test that wid is glwidget
           # no guarantee that that will be [2]
           # OK doing that in Deb qt 5.7 it Is
             
    def chngd(self):
        # common stuff for previous or next
        # set self.fntSzr
        # to what browser is at
        self.webfnt(self.fntSzr.value())
        b = self.jsbut.isChecked() 
        self.scripT(b)
        b = self.Pbut.isChecked() 
        #print '
        self.pluG(b)
        picn = self.currentWidget().page().icon()
        print ('icon Is' , picn.isNull()) 
        if  picn.isNull() :
           self.iCn.setIcon(QIcon('images/Dog12.png') )
        else:
            self.iCn.setIcon(picn)
        
        self.currentWidget().setFocus()
             
    def strtpg(self,a):
        print ('strtpg')
        z = a[:4].lower()
        if z == 'http':
                hmpg = QUrl(a)
        elif z[0] == '/' :
            hmpg = QUrl("file://" + a)
        elif z == 'file':
            hmpg = QUrl(a)
        else:
            print ('a', a)
            r = os.getcwd() +'/' + a
            print('relative' , r) 
            hmpg =  QUrl("file://" +r)
        print ('return ' , hmpg)
        return hmpg
    


class Klok(QLabel):
    wlsig  = pyqtSignal(int)
    def __init__(self,p):
        
        QLabel.__init__(self )
        self.mom = p
        fnt = QFont()
        fnt.setBold(True)
        self.setFont(fnt) 
        self.tick()
        tmr = QTimer(self)
        tmr.timeout.connect(self.tick)
        tmr.start(20000)
        #print 'timer IS' , tmr
        self.setCursor(QCursor (Qt.OpenHandCursor))
        
    def tick(self):
        now = QTime. currentTime()
        self.setText( now.toString("h : mm  ap"))
        # murdoch BUG if keybord maybe mouse
        # CLICKED during THIS CRASHES 
        # QT ???
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print ('86 Klik' , self.mom)
            self.dragPosition = event.globalPos() - self.mom.frameGeometry().topLeft()
            
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.mom.move(event.globalPos() - self.dragPosition)
            event.accept()

    def wheelEvent(self,e):
        d = e.angleDelta().y() 
        print ('wheel' , d)
        self.wlsig.emit(d)
        e.accept()
            
class MurdVu(QWebEngineView):
    def __init__(self,p,a=False ):
        print ('921 a' , a)
        self.main = p
        QWebEngineView.__init__(self )
        self.setPage(MurdPage(self))
        cWd =  os.getcwd()
        bpth = 'file://'+cWd+'/bookmarks.html'
        bu = QUrl(bpth)
        print ('bu' , bu)
        self.loadProgress.connect(p.dwngot) #scales 0 100
        self.load(bu)
        #self.setFocus( Qt.StrongFocus)
        ### above pukes in new pyqt
        print ('748', bpth , 'focus' , self.focusPolicy())
        # did segfault after here ???
        # yes was print page thingy on leons ?
    def contextMenuEvent(self,ev) : 
        menu = self.page().createStandardContextMenu()
        menu.addSeparator() 
        menu.addAction(self.page().action(QWebEnginePage.OpenLinkInNewTab))
        #The default implementation ignores the context event
        murdac = QAction("Murdac", self)
        murdac.triggered.connect(self.mUrdac)
        menu.addAction(murdac)
        menu.exec_(ev.globalPos())
        
    def mUrdac(self,x):
        print ('Murdac' , self.page() ,x)
        #dumpObjectInfo() const
        #dumpObjectTree() con
    #def createWindow(self,x):
        #print 'create',x
        #return self
        
# murdoch there is .page().iconUrlChanged

class MurdPage( QWebEnginePage):
    isig = pyqtSignal(QIcon, QWebEnginePage)
    def __init__(self,parent):
        
        QWebEnginePage.__init__(self,parent)
        print ('768 parent' , parent.main)
        self.svScr = False
        self.svScrNm = ''
        # did segfault after here
        self.mAin = parent.main
        self.sAving = False
        self.iconChanged.connect(self.iCon)
        self.featurePermissionRequested.connect(self.ftrq)
        
    def iCon(self,i):
        print ('new icon' , i)
        # use .icon() to get it
        self.isig.emit(i,self)
        
    def authenticationRequired(self,auth):
        print ('authenticate' , auth)
        
        
        
    def createWindow(self,t):
        print ('100 Create' , t)
        # seems kind of circular ????
        nupg= self.mAin.nubr().page()
        print ('nupg' , nupg)
        return nupg
        #did segfault here for some reason create 1
        # 1 is web browser tab
        # createStandardContextMenu() for Page
        ### It is working !!!!!!  almost
        #below only necessary for qt less than 5.8
    
    def javaScriptConsoleMessage(self,l,m,x,s):
        ### runJavaScript comes here 
        #level,msg,line#,src
        print ('79 SAVE ??' , self.svScr )
        if self.svScr :
            # YES gets here from cwp.runJavaScript(hd)
            import codecs
            #print ("would save" , m)
            savm =  u'<htm> ' + m + u' </htm>'
            f = codecs.open(self.svScrNm,'w', "utf-8")
            f.write(savm)
            self.svScr = False
            self.svScrNm = ''
        
        
        
        
    def svhtm(self,h):
        # Not Used !!!
        print ('save as' , self.sv)
        inf = 'Saving text only as ' + self.sv + ' ".mht" only works for\
          Qt 5.8 or newer '
        msg =  QMessageBox.warning(None,'Using javscript', inf)
        print ('msg' , msg)
        #print '575 h' , h
        import codecs
        f = codecs.open(self.sv,'w', "utf-8")
        #f= open(self.sv,'w')
        f.write(h)
        f.close() 
            
        
    def ftrq(self,u,f):
        print ('-----Feature---------------------' , u , FeAtures[f])
        print ('for' , u)
        rq = 'Request Feature' + FeAtures[f] + 'by'
        ###print 'messageboc CAN' , dir(QMessageBox)
        
        fdi = QMessageBox.question(self.mAin,'Feature'  , FeAtures[f] + 'has been requested by\n'\
               + u.toDisplayString(),  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print ('fdi' , fdi)
        ####print webengepage can' , dir(QWebEnginePage)
        if fdi ==  QMessageBox.Yes:
            print ('1038 Yes')
            self.setFeaturePermission(u,f,QWebEnginePage.PermissionGrantedByUser)
            # for geoloc have to have  Qt Location working
            #I need  GeoClue version 0.12.99)
        else:
            print ('1043 no')
            # useless docs do not show that I had to use dir()
            self.setFeaturePermission(u,f,QWebEnginePage.PermissionDeniedByUser)
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    app.setApplicationName(BROWNAME)
    brwsr =  MurdStak(sys.argv)
    #app.processEvents()
    brwsr.setWindowFlags(Qt.CustomizeWindowHint)
    # get rid of titlebar
    brwsr.show()
    
    sys.exit(app.exec_())


# wierd Flash 11.2.999 per whatismybrowser
# but 26,0,0,137 per Flash website ???
# sometimes menu wrong loc.
# sometimes download just does automatic
## no asset type protection scheme
## IE I have no copy protection BS thing
### speed test 
#http://browserbench.org/ARES-6/index.html
# error in console ???
### JetStream  My browser does very well

#js: Uncaught SyntaxError: Unexpected token )
#js: Synchronous XMLHttpRequest on the main thread is deprecated because of its detrimental effects to the end user's experience. For more help, check https://xhr.spec.whatwg.org/.
#js: Uncaught ReferenceError: parserIndexJS is not defined




# murdoch fix  font size not consistantly correct
# script on off not consitantly correct
##* Error in `python': double free or corruption (fasttop):
# in Lenove may crash sometimes    
# Examples/Qt-5.9.2/webenginewidgets/build
#-simplebrowser-Desktop_Qt_5_9_2_GCC_64bit-Debug/simplebrowser
#
#
# sometimes downloading tuncates name
# actualy the way saved in github
# firefox gets name right
# maybe have to extract name from link ?#
# link IS https://github.com/davisking/dlib/archive/v19.7/dlib-19.7.tar.gz
# what is going on is I think at site that name is actually a link to
# https://codeload.github.com/davisking/dlib/tar.gz/v19.7
#python 3 octane 27110 python2 34859
# tried again and got 34929 for python3
#######Chrome/69.0.3497.128 before update feb2019
# under some conditions malformed Internet
# eg httsp opens up xdg in linux this is right IN chrome
