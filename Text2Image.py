from Tkinter import *
from PIL import Image
from PIL import ImageTk
from pytesser import *
import os,glob
from PIL import ImageFilter, ImageEnhance
from string import ascii_letters, digits


class Window(Frame):

    

    def client_search(self):

        key = passg.get()

        #key = raw_input("Enter the Text to be Searched in the Images:  ")

        #print "The Images Containing the Key are: \n"
        for file_name in glob.glob("*.jpg"):
            
            #print file_name


            #file_name = raw_input("Enter the Image name along with extension:  ")

            fileN = os.path.splitext(file_name)[0]

            fileN = fileN + '.tiff'

            im = Image.open(file_name)

            im.save(fileN)



            #im = Image.open("han.tiff")
            im = im.convert('RGB')
            im = im.filter(ImageFilter.MedianFilter())
            enhancer = ImageEnhance.Contrast(im)
            im = enhancer.enhance(2)
            im = im.convert('1')
            text = image_to_string(im)
            #print text
            #print "text = \n{} ".format(text)

            text = text.lower()
            key = key.lower()
            


            y=text.split()
            z=key.split()

            for i in z:
                
                if i in y:
                    
                       
                         
                            #print file_name
                            i = Image.open(file_name)
                            i.show()

            os.remove(fileN)








    
    def __init__(self,master = None):
        global passg
        Frame.__init__(self,master)
        msgtitle = Message(master, text="SEARCH ENGINE")
        msgtitle.config(font=('timesnewroman',30), width=400)

        msgtitle3 = Message(master, text="rAhulSyed")
        msgtitle3.config(font=('timesnewroman',15), width=400)
        msgtitle4 = Message(master, text="rahulsyd.rs@gmail.com")
        msgtitle4.config(font=('timesnewroman',10), width=400)
        msgtitle5 = Message(master, text="SyedSaqib")
        msgtitle5.config(font=('timesnewroman',15), width=400)
        msgtitle6 = Message(master, text="syedsaqib96@gmail.com")
        msgtitle6.config(font=('timesnewroman',10), width=400)

        canvas_width = 200
        canvas_height = 40
        w = Canvas(master, 
               width=canvas_width,
               height=canvas_height)




        
        msgtitle.pack()
        msgtitle3.pack()
        msgtitle4.pack()
        msgtitle5.pack()
        msgtitle6.pack()
        w.pack()
        msgtitle2 = Message(master, text="Enter the words in an Image to be searched")
        msgtitle2.config(font=('helvetica',15), width=500)
        msgtitle2.pack()


        passg = Entry(master,width=50)
        passg.pack()



        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("Search")
        self.pack(fill = BOTH, expand = 1)
        searchButton = Button(self, text = "Search",command = self.client_search,width=15,height =2)
        searchButton.place(x=350,y=250)
        searchButton.pack(side =BOTTOM )
        #searchButton.grid(row=350,column= 450)



root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
