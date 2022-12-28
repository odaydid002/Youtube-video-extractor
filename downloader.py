from pytube import YouTube as yt
from tkinter import *
import win32clipboard, webbrowser  
import subprocess as sp

def getTitle():
    f = open('Log/title.txt','w')
    f.close
    link = str(linked.get())
    videoTitle = yt(link).title
    g = open('Log/title.txt','r+')
    g.write(videoTitle)
    g.close
    sp.Popen(["notepad.exe", 'Log/title.txt'])
    # os.system('start title.txt')
    
def getDesc():
    f = open('Log/description.txt','w')
    f.close
    link = str(linked.get())
    videoDescription = yt(link).description
    g = open('Log/description.txt','r+')
    g.write(videoDescription)
    g.close
    sp.Popen(["notepad.exe", 'Log/description.txt'])
    # os.system('start description.txt')
    
def getKeys():
    f = open('Log/keywords.txt','w')
    f.close
    link = str(linked.get())
    videoKeywords = yt(link).keywords
    g = open('Log/keywords.txt','r+')
    for key in videoKeywords:
        g.write('\n'+key+',')
    g.close
    sp.Popen(["notepad.exe", 'Log/keywords.txt'])
    # os.system('start keywords.txt')
    
def getThum():
    link = str(linked.get())
    videoThumbnail = str( yt(link).thumbnail_url)
    webbrowser.open_new_tab(videoThumbnail)

def download(res):
        window.title("Downloading...")
        link = str(linked.get())
        videoMp4 = yt(link).streams.filter(file_extension='mp4')
        vidMp4 = list(enumerate(videoMp4))
        j=0
        if res == '144p':
            for i in vidMp4:
                if 'res="144p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
                    videoMp4[j].download('Downloads/')
                    window.title("YoudownTube")
                    canvas.create_text(450,480,text='Success!!')
                j +=1
        elif res == '240p':
            for i in vidMp4:
                if 'res="240p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
                    videoMp4[j].download('Downloads/')
                    window.title("YoudownTube")
                    canvas.create_text(450,480,text='Success!!')
                j +=1
        elif res == '360p':
            for i in vidMp4:
                if 'res="360p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
                    videoMp4[j].download('Downloads/')
                    window.title("YoudownTube")
                    canvas.create_text(450,480,text='Success!!')
                j +=1                
        elif res == '480p':
            for i in vidMp4:
                if 'res="480p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
                    videoMp4[j].download('Downloads/')
                    window.title("YoudownTube")
                    canvas.create_text(450,480,text='Success!!')
                j +=1                                
        elif res == '720p':
            for i in vidMp4:
                if 'res="720p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
                    videoMp4[j].download('Downloads/')
                    window.title("YoudownTube")
                    canvas.create_text(450,480,text='Success!!')
                j +=1
        elif res == '720p60':
            for i in vidMp4:
                if 'res="720p60"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
                    videoMp4[j].download('Downloads/')
                    window.title("YoudownTube")
                    canvas.create_text(450,480,text='Success!!')
                j +=1
        elif res == '1080p':
            for i in vidMp4:
                if 'res="1080p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
                    videoMp4[j].download('Downloads/')
                    window.title("YoudownTube")
                    canvas.create_text(450,480,text='Success!!')
                j +=1               
        elif res == '1080p60':
            for i in vidMp4:
                if 'res="1080p60"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
                    videoMp4[j].download('Downloads/')
                    window.title("YoudownTube")
                    canvas.create_text(450,480,text='Success!!')
                j +=1       
        else:
            canvas.create_text(250,500,text='Resolution not existe')        
            
def get(): 
    link = str(linked.get())
    videoTtile = yt(link).title
    canvas.create_text(250,300,text=videoTtile)
    canvas.create_window(100,350,window=title)
    canvas.create_window(200,350,window=desc)
    canvas.create_window(300,350,window=keys)
    canvas.create_window(400,350,window=thum)
    canvas.create_line(50,380,450,380)
    canvas.create_text(250,400,text='Download',font=('Arial',14))

    videoMp4 = yt(link).streams.filter(file_extension='mp4')
    vidMp4 = list(enumerate(videoMp4))
    Texts=[]    
    for i in vidMp4:
        if 'res="144p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
            Texts.append('144p')
        if 'res="240p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
            Texts.append('240p')
        if 'res="360p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
            Texts.append('360p')
        if 'res="480p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
            Texts.append('480p')
        if 'res="720p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
            Texts.append('720p')
        if 'res="720p60"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
            Texts.append('720p60')
        if 'res="1080p"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
            Texts.append('1080p')
        if 'res="1080p60"' in str(i) and 'progressive="False"' in str(i) and 'type="video"' in str(i):
            Texts.append('1080p60')
            
    Buttons=[]

    for i, z in enumerate(Texts):
        Buttons.append(Button(window, text=z, command= lambda ztemp=z : download(ztemp)))
        Buttons[i].pack(side='left', padx=5)     
    
        
def Past():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    linked.insert(0,data)
         

      
window = Tk()
window.title("YoudownTube")
icon = PhotoImage(file=("Assets/icon.png"))
window.iconphoto(True,icon)

canvas = Canvas(window,width=500, height=500)
canvas.pack()


logo = PhotoImage(file='Assets/logo2.png')

logo = logo.subsample(5,5)

canvas.create_image(250,80, image=logo)

canvas.create_line(50,150,450,150)

canvas.create_text(250,180,text='Enter Video Link',font=('Arial',15))

linked = Entry(window,width=50)

past = Button(text='Past',command=Past)

canvas.create_window(450,200,window=past)

canvas.create_window(250,200,window=linked)

get = Button(text='Get Video Informations',command=get)

canvas.create_window(250,250,window=get)

canvas.create_line(50,280,450,280)



title = Button(window,text="Title",command=getTitle)
desc = Button(window,text="Description",command=getDesc)
keys = Button(window,text="Keywords",command=getKeys)
thum = Button(window,text="Thumbnail",command=getThum)




window.mainloop()










