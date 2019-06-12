"""A collection of function for doing my project."""

import random, os, re,PyPDF2
from docx import Document

def extSort():
    path = os.getcwd()
    files = os.listdir()
    
    for item in files:
        if item.endswith('.txt') or item.endswith('.doc') or item.endswith('.docx') or item.endswith('.pdf'):
            if item != 'requirements.txt':
                try:
                    os.mkdir("Text Files")
                except:
                    next
                os.rename(os.path.join(path+'/'+ item) , os.path.join(path+'/'+"Text Files" +"/"+item))
                print(item+" moved to Text Files")
            else:
                print("requirements.txt cannot be moved")
        elif item.endswith('.png') or item.endswith('.jpg'):
            try:
                os.mkdir("Images")
            except:
                next
            os.rename(os.path.join(path+'/'+ item) , os.path.join(path+'/'+"Images" +"/"+item))
            print(item+' moved to Images')

def bracketSort():
    path = os.getcwd()
    files = os.listdir()
    for item in files:
        if "[" and "]" in item:
            m = re.search(r"\[([A-Za-z0-9_ ]+)\]", item) 
            #re.search() used to get string in between bracket
            dirname = m.group(1).replace(" ", "").upper()
            #taken from https://stackoverflow.com/questions/8569201/get-the-string-within-brackets-in-python/8569258
            try:
                os.mkdir(dirname)
                os.rename(os.path.join(path+'/'+ item) , os.path.join(path+'/'+dirname+"/"+item))
                print(item + " moved to " + dirname)
            except:
                os.rename(os.path.join(path+'/'+ item) , os.path.join(path+'/'+dirname+"/"+item))
                print(item + " moved to " + dirname)

        else:
            continue

def inTextSort():
    '''
    This file sorter attempts to open up text files and reads the lines
    to find available course codes.
    PDF files are possible to read, but if coverted from docx with photos
    the text will become jumbled.
    '''
    classes = ['COGS 18', 'COGS 10', 'COGS 1','COGS 100']
    #add your own classes if necessary
    path = os.getcwd()
    odir = os.listdir()
    
    for file in odir:
        if file.endswith('.txt'):
            try:
                f = open(file,'r')
                fl = f.readlines()
                for line in fl:
                    for course in classes: 
                        if course in line:
                            separate = ':'
                            sep = line.split(separate,1)[0]
                        else:
                            continue
                        if sep == course:
                            try:
                                os.mkdir(course.replace(" ", "").upper())
                            except:
                                next
                            f.close()
                            os.rename(os.path.join(path+'/'+ file) , os.path.join(path+'/'+course.replace(" ", "").upper()+"/"+file))
                            print(file + " moved to " + course)  
                        else:
                           next
            except:
                next
        elif file.endswith('.docx'):
            document = Document(file)
            for line in document.paragraphs:
                for course in classes:
                    if re.search(course,line.text) is not None:
                        separate = ':'
                        sep = line.text.split(separate,1)[0]
                        if sep == course:
                            try:
                                os.mkdir(course.replace(" ", "").upper())
                            except:
                                next
                            document.save(file)
                            os.rename(os.path.join(path+'/'+ file) , os.path.join(path+'/'+course.replace(" ", "").upper()+"/"+file))
                            print(file + " moved to " + course)
                            break
                    else:
                        next
        elif file.endswith('.pdf'):
            pdf = open(file,'rb')
            pdfReader = PyPDF2.PdfFileReader(pdf)
            page = pdfReader.getPage(0)
            pageContent = page.extractText().split('\n',1)
            for line in pageContent:
                for course in classes:
                    if re.search(course,line) is not None:
                        separate = ':'
                        sep = line.split(separate,1)[0]

                        if sep.strip() == course:
                            try:
                                os.mkdir(course.replace(" ", "").upper())
                            except:
                                next
                            os.rename(os.path.join(path+'/'+ file) , os.path.join(path+'/'+course.replace(" ", "").upper()+"/"+file))
                            print(file + " moved to " + course) 
                            break
                        else:
                            continue
                            
                    else:
                        next
            
def createFiles():
    amt = input("How many files would you like to create? ")
    if amt.isnumeric():
        counter = 0
        while counter < int(amt):
            ext = ['.jpg', '.png', '.txt']
            course = ['COGS 1', 'COGS 10', 'COGS 18', 'COGS 100']
            f = open("[" + random.choice(course) + ']' + str(counter) + random.choice(ext), "w+")
            f.write(random.choice(course))
            f.close()
            counter+=1
        print(amt + " files created")
    else:
        print("Please enter an integer")
        createFiles()


    
#specificFiles()      
inTextSort()


