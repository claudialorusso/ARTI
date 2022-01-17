from tkinter import *
from tkinter import ttk, scrolledtext
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile

import sys
import subprocess

# ARTI needs Python three
# as much as you need... me ;)

# Time's computation function was selected after evaluating the following articles' infos:
# https://kodify.net/hugo/strings/reading-time-text/
# https://qualcherisposta.it/quante-parole-si-pronunciano-un-minuto

class Installation:
    """
    Manages the installation GUI.
    If it is the first execution OR the user doesn't dispose of the needed libs
    asks him if he wants to download them, in which case the program proceeds
    with the installation. Else, he can easly close the window.
    """
    def __init__(self):
        # ------------------------------- Installation root creation
        self.__installation_root__ = Tk()
        # -----------------logo
        self.__logo__ = PhotoImage(file="utils/images/arti2.png")
        # -----------------logo minimized
        self.__mini_logo__ = PhotoImage(file="utils/images/arti_medium.png")
        #-----------------ico
        self.__ico__ = "utils/images/arti2.ico"
        #set root icon
        self.__set_ico__()
        #set root title
        self.__title__ = "Program Installation"
        self.__set_title__(self.__title__)
        #---------------------------------- Master installation frame creation
        self.__master_frame__ = Frame(self.__installation_root__)
        self.__master_frame__.grid(row=0, column =0)
        #---------------------------------- Dialog Frame creation
        self.__up_dialog_frame__ = Frame(self.__master_frame__)
        self.__up_dialog_frame__.grid(row=0, sticky= W, padx=(5))
        #---------------------------------- Image installation lbl
        self.__image_lbl__ = Label(self.__up_dialog_frame__, image = self.__mini_logo__, justify="center")
        self.__image_lbl__.grid(row=0, column=0, padx=(10), pady=10)
        #---------------------------------- Welcome installation Frame creation
        self.__welcome_frame__ = Frame(self.__up_dialog_frame__)
        self.__welcome_frame__.grid(row=0, column =1, sticky=W, padx=(5))
        #---------------------------------- Welcome installation lbl
        self.__welcome_lbl__ = Label(self.__welcome_frame__, text='Welcome to aRTi!', font=("Gabriola", 30, "bold"), justify="left")
        self.__welcome_lbl__.grid(row=0, column = 1, sticky =N + W, pady=5)
        #---------------------------------- Instruction installation lbl
        self.__instruction_lbl__ = Label(self.__welcome_frame__, justify ="left", text='Since it is the first execution of the program you need to download \nand install the following libraries in order to correctly run aRTi.\n\nPlease make sure that your device has network connectivity.', font=("Times New Roman", 12))
        self.__instruction_lbl__.grid(row=1, column = 1, sticky =N + W, pady=10)
        # ---------------------------------------------------- TEXTBOX Frame
        self.__box_frame__ = LabelFrame(self.__master_frame__, text="The following packages will be installed:", padx=5, pady=5)
        self.__box_frame__.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E + W + N + S)

        self.__installation_root__.columnconfigure(0, weight=1)
        self.__installation_root__.rowconfigure(1, weight=1)

        self.__box_frame__.rowconfigure(0, weight=1)
        self.__box_frame__.columnconfigure(0, weight=1)

        # Create the textbox widget
        self.__txt_box__ = scrolledtext.ScrolledText(self.__box_frame__, width=40, height=10, font=("Times New Roman", 12))
        self.__txt_box__.grid(row=0, column=0, sticky=E + W + N + S)
        self.__txt_box__.insert(INSERT, self.__get_packages__())
        self.__txt_box__.configure(state="disabled")

        #-----------------------------------------------Accept frame creation
        self.__accept_frame__ = Frame(self.__master_frame__)
        self.__accept_frame__.grid(row=2, padx=(10), pady=10, sticky = W)

        #accept installation boolean variable
        self.__accept_terms__ = BooleanVar()

        # check button
        self.__check_btn__ = Checkbutton(self.__accept_frame__, text="I accept to download and install the previous packages. Click the 'Next' button to continue", variable=self.__accept_terms__, onvalue=True, offvalue=False, command = self.__manage_next_btn__)
        self.__check_btn__.grid(row = 0, sticky = W)

        #next button
        self.__next_btn__ = Button(self.__accept_frame__, text='Next', state = DISABLED, width=10, command = self.__bar__)
        self.__next_btn__.grid(row=2, sticky=E + S, pady=10)

        #progress bar
        self.__progress__ = ttk.Progressbar(self.__accept_frame__, orient=HORIZONTAL, length=600, mode ="determinate")
        self.__progress__.grid(row=1, sticky = W)

        #defines min and max root dimension
        self.__installation_root__.update()
        self.__installation_root__.minsize(self.__installation_root__.winfo_width(), self.__installation_root__.winfo_height())
        self.__installation_root__.maxsize(self.__installation_root__.winfo_width(), self.__installation_root__.winfo_height())
        self.__installation_root__.mainloop()

    def __set_ico__(self):
        """
        Sets the icon of the installation root
        :return:
        """
        self.__installation_root__.iconbitmap(self.__ico__)
        self.__installation_root__.wm_iconphoto(True, self.__logo__)

    def __set_title__(self, title):
        """
        Sets installation root title
        :param title: string which contains installation root title
        :return:
        """
        self.__installation_root__.title(title)

    def __get_packages__(self):
        """
        Puts into a string all of the libraries required to correctly run aRTi.
        Libraries names and versions are taken from the requirements.txt file.
        The test is in the form:
        pack = "lib_1==#version_1\nlib_2==#version_2\n[...]\nlib_n==version_n\n"
        :return:
            A string containing all the Packages required for the installation of aRTi
        """
        pack = "\n"
        with open("requirements.txt", 'r') as f:
            for line in f:
                pack = pack + line + "\n"
        return pack

    def __manage_next_btn__(self):
        """
        Enables and Disables the next button in the installation root.
        If the checkbox value, accept_terms, is set to True the next button is activated.
        :return:
        """
        self.__next_btn__.configure(state="disabled" if not self.__accept_terms__.get() else "normal")

    def __install_libs__(self):
        """
        Download and installs required libraries from requirement.txt file
        :return:
        """
        # implement pip as a subprocess:
        subprocess.run(["pip3", "install", "-r", "requirements.txt"], shell=True, capture_output=True)

    def __import_packs__(self):
        """
        Imports needed packages while managing the progress bar
        :return:
        """
        self.__installation_root__.update_idletasks()
        import os.path
        self.__progress__["value"] = 76
        self.__installation_root__.update_idletasks()
        import PyPDF2
        self.__progress__["value"] = 87
        self.__installation_root__.update_idletasks()
        import docx
        self.__progress__["value"] = 100
        self.__installation_root__.update_idletasks()

    def __disable_widgets__(self):
        """
        Disables check_btn and next_btn.
        :return:
        """
        self.__check_btn__.configure(state=DISABLED)
        self.__next_btn__.configure(state=DISABLED)

    def __bar__(self):
        """
        Manages the progress bar while installing the required processes and importing
        required packages.
        Destroys installation root after installation.
        :return:
        """
        # disable checkbox and next buttons
        self.__disable_widgets__()
        # download and install packages
        self.__progress__["value"] = 5
        self.__installation_root__.update_idletasks()
        self.__install_libs__()
        self.__progress__["value"] = 55
        self.__import_packs__()

        #destroy the installation root
        self.__installation_root__.destroy()

#app methods
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
        input("\npress any key to exit.")
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
        install = Installation()
        #reading_time()
    except ModuleNotFoundError:
        install = Installation()
        reading_time()


