import os.path
import PyPDF2
import docx


def reading_time():
    path = ask_path()
    minutes, secs = compute_time(path)
    print("reading time for this article is:\t" + str(minutes) + " minutes and " + str(secs) + " seconds")

def ask_path():
    # Using fileinput.input() method
    exists = False
    path=""
    while exists == False:
        path, exists = check_file()
    return path

def check_file():
    path = input("Enter Filename: ")
    exists = True
    if os.path.isfile(path):
        if path.endswith((".txt", ".pdf", ".docx")):
            pass
        else:
            print("Invalid file extension.")
            exists = False
    else:
        print("File doesn't exists OR missed extension. Please try again.")
        exists = False
    return path, exists

def getWordNumbTxt(path):
    with open(path, 'r', encoding='utf-8', errors="ignore") as inF:
        number_of_words = 0
        for line in inF:
            word_list = line.split()
            number_of_words += len(word_list)
    return number_of_words

def getWordNumbDocx(path):
    doc = docx.Document(path)
    number_of_words = 0
    for para in doc.paragraphs:
        txt = para.text
        word_list = txt.split()
        number_of_words += len(word_list)
    return number_of_words

def getWordNumbPDF(path):
    # creating an object
    file = open(path, 'rb')#, encoding = 'utf-8', errors="ignore")
    # creating a pdf reader object
    fileReader = PyPDF2.PdfFileReader(file)
    number_of_words = 0
    for page in fileReader.pages:
        for line in page.extractText().splitlines():
            word_list = line.split()
            number_of_words += len(word_list)
    file.close()
    return number_of_words

def get_number_of_words(path):
    if (path.endswith(".txt")):
        number_of_words = getWordNumbTxt(path)
    elif(path.endswith(".docx")):
        number_of_words = getWordNumbDocx(path)
    elif(path.endswith(".pdf")):
        number_of_words = getWordNumbPDF(path)
    return number_of_words

def compute_time(path):
    number_of_words = get_number_of_words(path)
    #200 = average number of words that can be read in a minute
    dvd = number_of_words/200
    minutes = compute_minutes(dvd)
    secs = compute_seconds(dvd)
    return minutes, secs

def compute_minutes(dvd):
    return round(dvd)

def compute_seconds(dvd):
    secs = round((dvd * 60) % 1, 3)
    return int(str(secs)[2:])

if __name__ == '__main__':

    reading_time()

#https://kodify.net/hugo/strings/reading-time-text/
#https://qualcherisposta.it/quante-parole-si-pronunciano-un-minuto