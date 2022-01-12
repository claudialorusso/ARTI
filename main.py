import sys
import subprocess

# ARTI needs Python three
# as much as you need... me ;)

# Time's computation function was selected after evaluating the following articles' infos:
# https://kodify.net/hugo/strings/reading-time-text/
# https://qualcherisposta.it/quante-parole-si-pronunciano-un-minuto

def reading_time():
    """
    It makes every computation.
    :return:
        Prints the reading time
    """
    path = __ask_path__()
    minutes, secs = __compute_time__(path)

    print("reading time for this article is:\t" + str(minutes) + " minutes and " + str(secs) + " seconds")

def __ask_path__():
    """
    Asks the user for the path's file
    :return:
        path: path of the file
    """
    exists = False
    path = ""
    while not exists:
        path, exists = __check_file__()
    return path

def __check_file__():
    """
    Checks if the file actually exists.
    :return:
        path: path of the file
        exists: control variable: it is True if the file actually exists; either it is False.
    """
    path = input("Enter Filename:\t")
    exists = True
    if os.path.isfile(path):
        if path.endswith((".txt", ".pdf", ".docx")):
            pass
        else:
            print("Invalid file extension: '.TXT', '.PDF' and '.DOCX' only.")
            exists = False
    else:
        print("File doesn't exist OR missed extension. Please try again.")
        exists = False
    return path, exists

def __getWordNumbTxt__(path):
    """
    Computates the total of words in the TXT.
    :param path: path of the file
    :return:
        number_of_words: total of words in the doc.
    """
    with open(path, 'r', encoding='utf-8', errors="ignore") as inF:
        number_of_words = 0
        for line in inF:
            word_list = line.split()
            number_of_words += len(word_list)
    return number_of_words

def __getWordNumbDocx__(path):
    """
    Computates the total of words in the DOCX.
    :param path: path of the file
    :return:
        number_of_words: total of words in the doc.
    """
    doc = docx.Document(path)
    number_of_words = 0
    for para in doc.paragraphs:
        txt = para.text
        word_list = txt.split()
        number_of_words += len(word_list)
    return number_of_words

def __getWordNumbPDF__(path):
    """
    Computates the total of words in the PDF.
    :param path: path of the file
    :return:
        number_of_words: total of words in the doc.
    """
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
    """
    Calls the method to computate the total number of words
    :param path: path of the file
    :return:
        number_of_words: total number of words in the doc
    """
    number_of_words = 0
    try:
        if path.endswith(".txt"):
            number_of_words = __getWordNumbTxt__(path)
        elif path.endswith(".docx"):
            number_of_words = __getWordNumbDocx__(path)
        elif path.endswith(".pdf"):
            number_of_words = __getWordNumbPDF__(path)
        return number_of_words
    except:
        print("FILE ERROR: maybe it is protected by password? Please enter a NON protected file.")
        reading_time()
        sys.exit()
    return number_of_words


def __compute_time__(path):
    """
    Computes reading time.
    :param path: file's path
    :return:
        minutes: minutes of reading
        secs: seconds of reading
    """
    minutes = 0
    secs = 0

    number_of_words = __get_number_of_words__(path)

    # 200 = average number of words that can be read in a minute
    dvd = number_of_words / 200
    minutes = __compute_minutes__(dvd)
    secs = __compute_seconds__(dvd)

    return minutes, secs

def __compute_minutes__(dvd):
    """
    Computes minutes
    :param dvd: number of words divided by the avg number of words tha can be read in a minute
    :return: minutes of reading
    """
    return round(dvd)

def __compute_seconds__(dvd):
    """
    Computes seconds
    :param dvd: number of words divided by the avg number of words tha can be read in a minute
    :return: seconds of reading
    """
    secs = round((dvd * 60) % 1, 3)
    return int(str(secs)[2:])

if __name__ == '__main__':
    try:
        import os.path
        import PyPDF2
        import docx
        reading_time()
    except ModuleNotFoundError:
        print("Since it is the first execution of the program you need to install the following libraries in order to correctly run ARTI:\n")
        with open("requirements.txt", 'r') as f:
            lines = f.readlines()
            print(lines)
            f.close()
        choice = input("\nDo you want to proceed with the installation? Type 'Y' to proceed or type any other key to close the process:\t").lower()
        if choice == 'y':
        # implement pip as a subprocess:
            subprocess.run(["pip3", "install", "-r", "requirements.txt"], shell=True, capture_output=True)
            import os.path
            import PyPDF2
            import docx
            print("\nPackages correctly installed!\n")
            reading_time()
        else:
            print("\nBye! ", "\U0001F984")
