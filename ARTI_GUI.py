from tkinter import *
from tkinter import ttk, scrolledtext, messagebox
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
import os
import sys

# ARTI needs Python three
# as much as you need... me ;)

# Time's computation function was selected after evaluating the following articles' infos:
# https://kodify.net/hugo/strings/reading-time-text/
# https://qualcherisposta.it/quante-parole-si-pronunciano-un-minuto

# last update: 2022/19/01

class Installation:
    """
    Manages the installation GUI.
    If it is the first execution OR the user doesn't dispose of the needed libs
    asks him if he wants to download them, in which case the program proceeds
    with the installation. Else, he can easly close the window.
    """
    def __init__(self):
        # ------------------------------- Termination variable. Default = False; if True wont open App.
        self.__termination__ = False
        # ------------------------------- Installation root creation
        self.__installation_root__ = Tk()

        # path logo
        logo = __get_path__("utils\\images\\aRTi_white_giant.png")
        # -----------------logo
        self.__logo__ = PhotoImage(file=logo)
        # path logo
        logo_min = __get_path__("utils\\images\\aRTi_medium.png")
        # -----------------logo minimized
        self.__mini_logo__ = PhotoImage(file=logo_min)
        # path ico
        ico = __get_path__("utils\\images\\aRTi_white_giant_ico.ico")
        #-----------------ico
        self.__ico__ = ico
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
        self.__welcome_lbl__ = Label(self.__welcome_frame__, text='Welcome to aRTi!', font=("Berlin Sans FB Demi", 30, "bold"), justify="left")
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

        #termination program variable
        terminate = BooleanVar()

        #progress bar
        self.__progress__ = ttk.Progressbar(self.__accept_frame__, orient=HORIZONTAL, length=600, mode ="determinate")
        self.__progress__.grid(row=1, sticky = W)

        #defines min and max root dimension
        self.__installation_root__.update()
        self.__installation_root__.minsize(self.__installation_root__.winfo_width(), self.__installation_root__.winfo_height())
        self.__installation_root__.maxsize(self.__installation_root__.winfo_width(), self.__installation_root__.winfo_height())
        #terminate installation, open app
        self.__installation_root__.mainloop()


    def get_terimantion(self):
        """
        Returns the termination variable
        :return:
            the termination variable = True if libs were correctly installed
        """
        return self.__termination__

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
        import sys
        import subprocess
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
        self.__termination__ = True
        #destroy the installation root
        self.__installation_root__.destroy()

class App:
    """
    Defines the aRTi GUI.
    Pressing the "Select File" button the user can simply choose the desired file that has one of the following extentions:
    - .pdf
    - .docx
    - .txt
    Pressing the "Start" button, the program will compute the reading time of the doc.
    The game is done.
    """
    def __init__(self):
        # ------------------------------- Installation root creation
        self.__root__ = Tk()
        self.__root__.configure(background="#F6FBFF")
        # path logo
        logo = __get_path__("utils\\images\\aRTi_white_giant.png")
        # -----------------logo
        self.__logo__ = PhotoImage(file=logo)
        # path logo
        logo_min = __get_path__("utils\\images\\aRTi_200.png")
        # -----------------logo minimized
        self.__mini_logo__ = PhotoImage(file=logo_min)
        # path ico
        ico = __get_path__("utils\\images\\aRTi_white_giant_ico.ico")
        #-----------------ico
        self.__ico__ = ico
        #set root icon
        self.__set_ico__()

        #set root title
        self.__title__ = "aRTi"
        self.__set_title__(self.__title__)
        #---------------------------------- Master frame creation
        self.__master_frame__ = Frame(self.__root__, background="#F6FBFF")#F6ECEC
        self.__master_frame__.grid(row=0)
        #---------------------------------- Dialog Frame creation
        self.__up_dialog_frame__ = Frame(self.__master_frame__, background="#F6FBFF")
        self.__up_dialog_frame__.grid(padx=(10), pady=10)
        #---------------------------------- Image lbl
        self.__image_lbl__ = Label(self.__up_dialog_frame__, image = self.__mini_logo__, background="#F6FBFF")
        self.__image_lbl__.grid(row=0, column = 0, padx=(10), pady=10)

        #---------------------------------- clolorusso label
        self.__clo_lbl__ = Label(self.__up_dialog_frame__, text ="  by clolorusso", background="#F6FBFF",font=("Bahnschrift Light",10))
        self.__clo_lbl__.grid(row=1, column = 0, sticky = N)
        #---------------------------------- Instruction Frame creation
        self.__instruction_frame__ = Frame(self.__master_frame__, relief = RIDGE, borderwidth = 2,background="#F8FAFC")
        self.__instruction_frame__.grid(row=0, column = 1, sticky=W, padx=(10), pady=10)
        #---------------------------------- Instruction lbl

        str_bold_reading_time = "\033[1m" + "reading time" + "\033[0m"
        str_bold_aRTi = "\033[1m" + "aRTi" + "\033[0m"
        instructions = "Howdy Guys!!!\n\nSeems like you're in a desperate need for help or else " \
                       "you'd have never downloaded \nand installed a program retrieved from a " \
                       "remote corner of GitHub...\n\nAnyway, aRTi is here to HELP YOU!!\n\n" \
                       "Are you interested in discovering the READING TIME of your speech or a book?\n" \
                       "You just have to select the doc ('.txt','.docx' or '.pdf' only) by clicking the " \
                       "'Select File' \nbutton. Afterwards, press 'Start' and the game is done."

        self.__instruction_lbl__ = Label(self.__instruction_frame__, justify ="left", text=instructions, font=("Times New Roman", 12), background="#F8FAFC")
        self.__instruction_lbl__.grid(row=0, column = 0, pady=10)

        #-----------------------------------------------File name frame creation
        self.__fname_frame__ = Frame(self.__master_frame__, padx=5, pady=5, relief = GROOVE, background="#F8FAFC")
        self.__fname_frame__.grid(row=1, column = 0, padx=(10), pady=10)

        #Reading Time txt label
        self.__RT_txt__ = Label(self.__fname_frame__,text="Reading Time", background="#F6FBFF",font=("Berlin Sans FB Demi", 30, "bold"), justify="center")
        self.__RT_txt__.grid(row=0, column=0)
        #file name string
        self.__filename__ = StringVar()

        # Perfomed lbl
        self.__perf_txt__ = Label(self.__fname_frame__,text="Press 'Select File' button", background="#F6FBFF",font=("Bahnschrift Light",10), justify="center")
        self.__perf_txt__.grid(row=1, column=0)

        #-----------------------------------------------Computation frame creation
        self.__computation_frame__ = LabelFrame(self.__fname_frame__,text=" Make your choice: ", padx=5, pady=5, borderwidth = 2, relief = GROOVE, background="#F8FAFC",font=("Bahnschrift Light",10))
        self.__computation_frame__.grid(row=2, column = 0, padx=(10), pady=10)


        #reading time value
        self.__reading_time__ = StringVar()


        #Select file button
        self.__select_btn__ = Button(self.__computation_frame__, text ="Select File", width=10,command = self.__select_file__, background="#BCDBF7")
        self.__select_btn__.grid(row=0, column = 0, padx=10,pady=10, sticky = E+N)

        # start button
        self.__start_btn__ = Button(self.__computation_frame__, text ="Start", state = DISABLED, width=10, command = self.__compute__, background="#BCDBF7")
        self.__start_btn__.grid(row=0, column = 1, padx=10,pady=10, sticky=W+N)

        # ---------------------------------------------------- TEXTBOX Frame
        self.__box_frame__ = LabelFrame(self.__master_frame__, text="Reading time is:", padx=5, pady=5, background="#F6FBFF",font=("Bahnschrift Light",10))
        self.__box_frame__.grid(row=1, column=1, columnspan=3, padx=10, pady=10, sticky=E + W + N + S)

        self.__root__.columnconfigure(0, weight=1)
        self.__root__.rowconfigure(1, weight=1)

        self.__box_frame__.rowconfigure(0, weight=1)
        self.__box_frame__.columnconfigure(0, weight=1)

        # Create the textbox widget
        self.__txt_box__ = scrolledtext.ScrolledText(self.__box_frame__, width=40, height=10, font=("Times New Roman", 12), state = DISABLED)
        self.__txt_box__.grid(row=0, column=0, sticky=E + W + N + S)

        #defines min and max root dimension
        self.__root__.update()
        self.__root__.minsize(self.__root__.winfo_width(), self.__root__.winfo_height())


        self.__root__.mainloop()

    def __compute__(self):
        """
        Computes reading time
        :return:
        """
        self.__txt_box__.configure(state=NORMAL)
        self.__txt_box__.delete("1.0", END)
        self.__txt_box__.configure(state="disabled")
        if not self.__file_name__ == "":
            path = self.__file_name__
            warning = False
            minutes, secs, warning = self.__compute_time__(path)
            # get file name from path
            file_name = os.path.basename(path)
            if warning:
                pass
            elif not (minutes == 0 and secs == 0):
                #get string containing reading time
                self.__reading_time__ = "Reading time for " +file_name+" is:\n\n" + str(minutes) + " minutes and " + str(secs) + " seconds.\n\nPlease select another file for a new computation."
                self.__txt_box__.configure(state=NORMAL)
                self.__txt_box__.insert(INSERT, self.__reading_time__)
                self.__txt_box__.configure(state="disabled")
            else:
                messagebox.showinfo("Info!", file_name +
                                       " outputted 0 minutes and 0 seconds.\nReasons maybe one of the following:"
                                       "\n-\tthe file is empty;"
                                       "\n-\tthe file contains only images;"
                                        "\n-\tthe file is corrupted."
                                        "\n\nSelect another file for a new computation.")
        self.__start_btn__.configure(state="disabled")

    def __select_file__(self):
        """
        Let the user select a file. The file type must be one of the allowed ones (see self.__filetypes__ function).
        Enables and disables start button.
        :return:
        """

        self.__file_name__ = fd.askopenfilename(
            title = "Select File",
            initialdir="\\",
            filetypes = self.__filetypes__()
        )

        #Enables and disables start button
        self.__start_btn__.configure(state = NORMAL if not self.__file_name__ == "" else DISABLED)
        file_name = os.path.basename(self.__file_name__)
        #specify doc selected
        doc_select_rd_txt = "will be computed for\n" + file_name + "\n\nPress 'Start' to continue"
        self.__perf_txt__.config(text = doc_select_rd_txt if not file_name == "" else "Press 'Select File' button")



    def __filetypes__(self):
        """
        Returns all of the filetypes allowed
        :return:
        tuple of all of the filetypes allowed
        """
        filetypes = (
            ("*.txt", "*.txt"),
            ("*.docx", "*.docx"),
            ("*.pdf", "*.pdf")
        )
        return filetypes

    def __set_ico__(self):
        """
        Sets the icon of the installation root
        :return:
        """
        self.__root__.iconbitmap(self.__ico__)
        self.__root__.wm_iconphoto(True, self.__logo__)

    def __set_title__(self, title):
        """
        Sets installation root title
        :param title: string which contains installation root title
        :return:
        """
        self.__root__.title(title)

    #app methods

    def __ask_path__(self):
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

    def __getWordNumbTxt__(self, path):
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

    def __getWordNumbDocx__(self, path):
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

    def __getWordNumbPDF__(self, path):
        """
        Computates the total of words in the PDF.
        :param path: path of the file
        :return:
            number_of_words: total of words in the doc.
        """
        # creating an object
        file = open(path, 'rb')
        # creating a pdf reader object
        fileReader = PyPDF2.PdfFileReader(file,strict=False)
        number_of_words = 0
        for page in fileReader.pages:
            for line in page.extractText().splitlines():
                word_list = line.split()
                number_of_words += len(word_list)
        file.close()
        return number_of_words

    def __get_number_of_words__(self, path):
        """
        Calls the method to computate the total number of words
        :param path: path of the file
        :return:
            number_of_words: total number of words in the doc
        """
        number_of_words = 0
        warning = False

        try:
            if path.endswith(".txt"):
                number_of_words = self.__getWordNumbTxt__(path)
            elif path.endswith(".docx"):
                number_of_words = self.__getWordNumbDocx__(path)
            elif path.endswith(".pdf"):
                number_of_words = self.__getWordNumbPDF__(path)
        except:
            warning = True
            messagebox.showwarning("Warning", "The file you selected maybe protected by password.\nPlease select another file.")
        return number_of_words, warning


    def __compute_time__(self, path):
        """
        Computes reading time.
        :param path: file's path
        :return:
            minutes: minutes of reading
            secs: seconds of reading
        """
        minutes = 0
        secs = 0

        number_of_words, warning = self.__get_number_of_words__(path)
        if not warning:
            # 200 = average number of words that can be read in a minute
            dvd = number_of_words / 200
            minutes = self.__compute_minutes__(dvd)
            secs = self.__compute_seconds__(dvd)
        return minutes, secs, warning

    def __compute_minutes__(self, dvd):
        """
        Computes minutes
        :param dvd: number of words divided by the avg number of words tha can be read in a minute
        :return: minutes of reading
        """
        return round(dvd)

    def __compute_seconds__(self, dvd):
        """
        Computes seconds
        :param dvd: number of words divided by the avg number of words tha can be read in a minute
        :return: seconds of reading
        """
        secs = round((dvd * 60) % 1, 3)
        return int(str(secs)[2:])

def __get_path__(relative_path):
    """
    if (hasattr(sys, "_MEIPASS")):
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        return relative_path
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    termination = False
    try:
        import os.path
        import PyPDF2
        import docx

        termination = True
    except ModuleNotFoundError:
        install = Installation()
        termination = install.get_terimantion()

    if termination:
        app = App()

