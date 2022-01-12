import os.path
import PyPDF2
import docx


def reading_time():
    path = __ask_path__()
    minutes, secs = __compute_time__(path)
    print("reading time for this article is:\t" + str(minutes) + " minutes and " + str(secs) + " seconds")


def __ask_path__():
    exists = False
    path = ""
    while not exists:
        path, exists = __check_file__()
    return path


def __check_file__():
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


def __getWordNumbTxt__(path):
    with open(path, 'r', encoding='utf-8', errors="ignore") as inF:
        number_of_words = 0
        for line in inF:
            word_list = line.split()
            number_of_words += len(word_list)
    return number_of_words


def __getWordNumbDocx__(path):
    doc = docx.Document(path)
    number_of_words = 0
    for para in doc.paragraphs:
        txt = para.text
        word_list = txt.split()
        number_of_words += len(word_list)
    return number_of_words


def __getWordNumbPDF__(path):
    # creating an object
    file = open(path, 'rb')  # , encoding = 'utf-8', errors="ignore")
    # creating a pdf reader object
    fileReader = PyPDF2.PdfFileReader(file)
    number_of_words = 0
    for page in fileReader.pages:
        for line in page.extractText().splitlines():
            word_list = line.split()
            number_of_words += len(word_list)
    file.close()
    return number_of_words


def __get_number_of_words__(path):
    if path.endswith(".txt"):
        number_of_words = __getWordNumbTxt__(path)
    elif path.endswith(".docx"):
        number_of_words = __getWordNumbDocx__(path)
    elif path.endswith(".pdf"):
        number_of_words = __getWordNumbPDF__(path)
    return number_of_words


def __compute_time__(path):
    number_of_words = __get_number_of_words__(path)
    # 200 = average number of words that can be read in a minute
    dvd = number_of_words / 200
    minutes = __compute_minutes__(dvd)
    secs = __compute_seconds__(dvd)
    return minutes, secs


def __compute_minutes__(dvd):
    return round(dvd)


def __compute_seconds__(dvd):
    secs = round((dvd * 60) % 1, 3)
    return int(str(secs)[2:])


if __name__ == '__main__':
    reading_time()

#FONTI
# https://kodify.net/hugo/strings/reading-time-text/
# https://qualcherisposta.it/quante-parole-si-pronunciano-un-minuto
