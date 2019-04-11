from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys,os , datetime 

# do not need gtk br as this NOW does mht
# Pick your own name 
#This is your browser give it your name??
import getpass

Blurb ="html/blurb.htm"
BukMarx ="html/bookmarks.htm"
#BROWNAME='Mozilla Firefox'
BROWNAME ='MurdBrowQt5'
#BROWNAME= getpass.getuser()[:4]+'Browser'
# a cute idea but makes it easier for Google
# facebook etc to track you
MurdFindKey = Qt.Key_F12 
MurdFindKey ="Ctrl+F" 
# for windoze people

FoNT = 25
# default font works out to 1.25
#BROWNAME = 'Murdbrow E'

RSSitms= ['Pick', 'http://feeds.bbci.co.uk/news/rss.xml',\
'http://feeds.bbci.co.uk/news/business/rss.xml',\
 'http://www.guardian.co.uk/technology/rss',\
 'http://www.guardian.co.uk/world/rss',\
 'http://www.guardian.co.uk/business/rss',\
 'http://rss.cbc.ca/lineup/topstories.xml',\
 'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',\
 
 'http://rss.cbc.ca/lineup/technology.xml',\
 'http://www.thestar.com/content/thestar/feed.RSSManagerServlet.topstories.rss',\
 'http://feeds.reuters.com/Reuters/worldNews',\
 'http://www.sciencemag.org/rss/news_current.xml',\
 'http://www.aljazeera.com/xml/rss/all.xml',\
 'http://rss.slashdot.org/Slashdot/slashdotMain',\
 'https://www.cnet.com/rss/all/',\
 
 ]
               

# print ('running ON' , QSysInfo().prettyProductName())

Agnts= ["Default", \
        "Mozilla/5.0   (Windows; U; Windows NT 5.1; en",\
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; es-es) AppleWebKit/531.21.10\
        KHTML, like Gecko) Version/4.0.4 Mobile/7B360 Safari/531.21.10",\
        "AppleWebKit/426.9 (KHTML, like Gecko\
         Version/4.0dp1 Safari/426.8"]
         # 2 means mht
         #1 means htm with directories
         # 0 means htm Only IE. nop pics etc
         # so below in THAT order
Pgsvtp= ['htm ONE only main htm', 'htm ALL with data in directories',\
'mht ALL in onefile' ]
        
        
        
        
FeAtures={ 1:"Geolocation",2:"Audio Capture",3:"Video Capture",\
         4:"Audio and Video Capture", 5:"Mouse Lock", 6:"Display Capture",\
         7:"Desktop Audio Video Capture"}



def murdSize(wid):
    pfh = int(  QDesktopWidget().screenGeometry().height()* .95)
    pfw = int(QDesktopWidget().screenGeometry().width() * .90)
    print ('Desk' , pfh ,pfw)
    wid.setMinimumSize(pfw,pfh)
    # or
    #wid.setMinimumSize(1200,700)
###AGENT =  str( QWebEnginePage().profile().httpUserAgent() )
FoNT = 25

def  HOMEPG():
    # below comes from qt
    qtver =  qVersion ()
    try:
        plfrm = str( QSysInfo().prettyProductName())
        pyver = str(sys.version_info[0])+'.'+str(sys.version_info[1])\
        +'.'+ str(sys.version_info[2])

        agnts =  str( QWebEnginePage().profile().httpUserAgent() )
        chrminf = agnts.find('Chrome')
        sfrinf = agnts.find('Safari')
        endinf = len(agnts)
        #print agnts[chrminf:sfrinf], agnts[sfrinf:endinf]
        wvr = '<br>'+ agnts[chrminf:sfrinf]+'<br>'+ agnts[sfrinf:endinf] 
    except:
        wvr = 'Guess Chrome Webengine etc. '
        
    htm1 ='<!DOCTYPE html><head><title>Home Page</title><style type="text/css">\
      body { background-image: url("images/mbr10.jpg");\
      background-repeat: no-repeat;background-size:cover; }\
      </head></style><body TEXT="#ffff8f"><h1>QT version ' + qtver + '</h1> \
      <br><h2>WebEngine  ON '+plfrm+ wvr +'</h2>\
      <br><h2>Python '+pyver +'</br></h2>\
      <br><h2>'+ BROWNAME+ '</h2>\
      <br><h3><A HREF='+ BukMarx +  '>Bookmarks</A></h3>\
      <h3><A HREF='+ Blurb +'>Blurb</A></h3>\
      <p><h2><A HREF="murdQUIT">QUIT<//A></H2>\
      </body> </html>'
	
      ### no-repeat center center fixed
    
    print ('htm1 is ' , htm1)
    return htm1 


## <p><h2><A HREF="murdRSTR">RESTORE<//A></H2>\
### do not know about restore BS
#below NOT in windoze
#HmRsrc = QUrl('file://' + os.getcwd()+'/')
#cWd =  os.getcwd()
cPth = QDir.currentPath()+ QDir.separator()
#+ '/'
#fromNativeSeparators(con
#print ('cWd' , cWd, cpth)
print ('cpth' , cPth)
HmRsrc =  QUrl.fromLocalFile(cPth )
# murdoch never used
#used in menu
BlrbPth = QUrl.fromLocalFile(cPth + 'html/blurb.htm')
def WinDoz():
    try:
        wver = QSysInfo().windowsVersion()
        print ('On Windows' , wver)
        return True
    except:
        print ('Not on Windows')
        return False
        



#HmRsrc = QUrl('file://'+os.path.abspath(os.path.dirname(__file__))+'/')




print ('HmRsrc' , HmRsrc)
def HOMEDIR():
    hOme = QUrl.fromLocalFile( os.path.expanduser('~'))
    print ('hOme', hOme)
    return  hOme

    
# will have to be changed montly ??
#SVLOC = '/home/murdoch/Internet/Apr2016/'


def Svloc():
    #in Arch saving in 
    # save in Eg /home/murdoch/Internet/Apr2016/
    home = os.path.expanduser("~") 
    #svhm = '/Back/murdoch/' 
    d =  datetime.date.today()
    svdir = d.strftime("%b%Y").lower()
    # sometimes leave out lower
    svloc = home +'/Internet/' + svdir +'/'
    print ('163 svloc' , svloc)
    if not os.path.isdir(svloc):
        os.makedirs(svloc)  
    print ('return' , svloc)
    return svloc
'''
def StgPth():
    H = os.getenv("HOME") +'/'
    stgpth = H+'Erase/Junk3'
    return stgpth
    # this only works for cookies 
'''
# may block
#Junk = ('facebook','fbcdn','idsync','LinkTracker','doubleclick',\
#       'pagead','moatads', 'google')
#Is blocked
###BLOK = {'facebook' , 'doubleclick',






if   (sys.version_info > (3, 0)):
    from urllib.request import urlopen
else:
    from urllib2 import urlopen

    
from xml.dom import minidom




class Blokr(QDialog):
    #rssdun =  pyqtSignal(QUrl )
    #print '11'
    def __init__(self,a):
        #self.mom = a
        print ('138')
        QDialog.__init__(self)
        self.setLayout(QVBoxLayout())
        self.bLOk = QComboBox()
        #self.rSSs.addItem('Pick')
        for i in RSSitms:
            #print( 'add' , i
            self.rSSs.addItem(i)
        self.layout().addWidget(self.rSSs)
        self.setMinimumSize ( 700,500)


        

class Ckr(QMenu):
    def __init__(self, parent):
        QMenu.__init__(self)
        self.setMinimumSize ( 450,600)
        lay = QVBoxLayout()
        self.BLOK = ['facebook', 'doubleclick','rtb.dsp','moatads',\
        'rllcll.com','dcr.imrworldwide', 'taboola.com','zergnet.com' ]
        Junk = ['NOTHING','facebook','fbcdn','idsync','LinkTracker','doubleclick',\
       'pagead','moatads', 'google','rtb.dsp', 'rllcll.com' ,\
        'dcr.imrworldwide','taboola.com','zergnet.com',\
	'chartbeat.net','Show Asks']

        #self.setText('Ars')
        for j in Junk:
            lay.addWidget(self.adstuff(j))
       
        self.setLayout(lay)
        
    # radio button eclusive
    # checkbox non exclusive
    
    def tEst(self):
        print ('blok' , self.BLOK) 
        for b in self.BLOK:
            print ('blok' , b) 
    def adstuff(self,t):
        ac = QCheckBox(t)
        ac.clicked.connect(self.klikt)
        if t in self.BLOK:
            ac.setChecked(True)
        return ac
    def klikt(self,k):
        print ('klikt' , k, self.sender().text())
        if k :
            if self.sender().text() == 'NOTHING':
                print ('UNBLOCK')
                self.BLOK = []
                # now have to unclick everything except
                # NOTHING
                for c in self.children():
                    cnm = c.__class__.__name__
                    if cnm.find('QCheckBox')>-1:
                        if c.text() != 'NOTHING':
                            c.setChecked(False)
           
            else:
                self.BLOK.append(str(self.sender().text()))
            
        else:
            rmv = str(self.sender().text())
            print ('remove' , rmv)
            # logical would be to redo my default blok list
            # for NOTHING but easiest is just to return
            #print ('BLOK has' , self.BLOK)
            if rmv == 'NOTHING':
                return
            self.BLOK.remove(rmv)
        print ('Blok' , self.BLOK)
       




# below is only necessary because textbrowser is useless
# and with some html tries to open a file it cannot
# find and goes into a loop


    
class Rssr(QDialog):
    rssdun =  pyqtSignal(QUrl )
    #print '11'
    def __init__(self,a):
        #self.mom = a
        print ('15')
        QInputDialog.__init__(self)
        self.setLayout(QVBoxLayout())
        self.rSSs = QComboBox()
        #self.rSSs.addItem('Pick')
        for i in RSSitms:
            #print( 'add' , i
            self.rSSs.addItem(i)
        self.layout().addWidget(self.rSSs)
        self.setMinimumSize ( 700,500)
        self.tb= QTextBrowser ()
                   
        #print 'surch' ,  self.tb.searchPaths() 
        self.tb.setOpenLinks(False)
        # could set that only if not standalone
        self.tb.sourceChanged.connect(self.gotrss)
        self.tb.anchorClicked.connect(self.klikt)
        self.layout().addWidget(self.tb)
        self.rSSs.activated.connect(self.getrss)
        print ('27')
        
    
    def getrss(self,p):
        if p == 0:
            return
        print ('30' ,p)
        
        rspg = '<html><head><title>RSS stuff </title></head><body><p><h1>RSS '
        #urllib2.urlopen("http://example.com", timeout = 1)       
        # Must establish connection within that time ???
        #print 'Get RSS',p,  self.rSSs.currentText() 
        feedres = ''
        
        try: 
            connection = urlopen( self.rSSs.currentText(),\
            timeout=2)
        except:
            self.tb.setText("RSS Timed Out")
            print ('Timed Out')
            return
        print ('connection' , connection.url)
        feed = minidom.parse(connection)
        #print 'feed' , feed
        rssitems = feed.getElementsByTagName('item')
        itemnum = 0
        for r in rssitems:
            lnk = r.getElementsByTagName('link')[0]
            lInk =  lnk.childNodes[0].data
            ttl = r.getElementsByTagName('title')[0]
            tItle =  ttl.childNodes[0].data
            dscr =  r.getElementsByTagName('description')[0]
            descr = dscr.childNodes[0].data
            try:
                dt =  r.getElementsByTagName('pubDate')[0]
                dAte = dt.childNodes[0].data
            except:
                try :
                    dt =  r.getElementsByTagName('dc:date')[0]
                    dAte = dt.childNodes[0].data
                except: 
                    dAte = 'No Date?'
            feedres += '<p><A HREF="'+ lInk + '"><h3>'+ tItle + '</h3></A>  '\
            + dAte +'<br>' + descr+ '\n'
            itemnum +=1
        itemcount = '  '+ str(itemnum) + ' Items '
        print('itemcount', itemcount)
        rspg += itemcount + '</h1><p>'
        print('365 rspg ' , rspg)
        rspg += feedres + ' </body> </html>'
       
        
        
        self.tb.setText(rspg)
        #self.tb.insertPlainText(rspg)
        #self.tb.insertHtml(rspg)
        #except:
        
        #print '54'
    
            
    
            
    def gotrss(self,rs):
        print ('61', rs)
        self.rssdun.emit(rs)
        self.lower()
        #return
        #if self.mom.__class__.__name__  == 'MurdStak':
        #self.mom.currentWidget().load(QUrl(rs))
        #print '777777777777777777777777772'
        #self.tb.backward()
        #print '77777777777777777777777777777774'

    def klikt(self,u):
        print ('86   klikt' , u)
        self.rssdun.emit(u)

          

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    app.setApplicationName(BROWNAME)
    # of course with a distinct name
    # you will be esier to track so maybe not
    rssr = Rssr(sys.argv)
    
    rssr.show()
    sys.exit(app.exec_())
### wrt slashdot
#Got it
#Donload ?? False
#toolax Menu
#show menu
#306 t Rss
#15
#27
#('30', 14)
#QFSFileEngine::open: No file name specified
# som rss thingies do that ????


def Goofpg(u):
    print ('did chrome goof' ,u)
    htm1 ='<!DOCTYPE html><head><title>Goof Page</title>\
      <head>GOOF</head><body><h1>Chrome Goof</h1> \
      <br>Looks like Chrome goofed url is <br>'\
      +u +'</body></html>'
    return htm1


