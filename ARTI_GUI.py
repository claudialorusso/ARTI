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

def launch():
    next_btn.configure(state = "disabled" if not accept_terms.get() else "normal")

def bar():
    """

    :return:
    """
    #disable checkbox and next buttons
    check_btn.configure(state=DISABLED)
    next_btn.configure(state=DISABLED)

    #download and install packages
    progress["value"] = 5
    installation_root.update_idletasks()
    # implement pip as a subprocess:
    subprocess.run(["pip3", "install", "-r", "requirements.txt"], shell=True, capture_output=True)
    progress["value"] = 55
    installation_root.update_idletasks()
    #time.sleep(0.1)
    import os.path
    progress["value"] = 76
    installation_root.update_idletasks()
    import PyPDF2
    progress["value"] = 87
    installation_root.update_idletasks()
    import docx
    progress["value"] = 100
    installation_root.update_idletasks()

    #root = Tk()
    installation_root.destroy()




    """
    
    progress['value']=20
    root.update_idletasks()
    time.sleep(1)
    progress['value']=50
    root.update_idletasks()
    time.sleep(1)
    progress['value']=80
    root.update_idletasks()
    time.sleep(1)
    progress['value']=100
    """

def get_packages():
    pack = "\n"
    with open("requirements.txt", 'r') as f:
        for line in f:
            pack = pack + line + "\n"
    return pack


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
    try:#TODO

        """
        installation_root = Tk()
        logo = PhotoImage(file="utils/images/output-onlinepngtools.png")
        installation_root.geometry("500x500")
        installation_root.resizable(0,1)
        installation_root.title("Program installation")
        installation_root.iconphoto(False, logo)


        frame = Frame(installation_root)
        #frame.pack_propagate(0)
        frame.grid(row=0,column=0, sticky = W+E)

        title_label = Label(frame, image = logo, justify = "left")

        title_label.grid(column = 0, row = 0, padx=(10), pady=10)

        infolabel = Label(frame, anchor = "n", font= "arial", text = "Since it is the first execution of the program you need to install the following libraries in order to correctly run ARTI:")
        infolabel.grid(column = 0, row = 0,padx=(10), pady=10)
        """
        installation_root = Tk()

        logo = PhotoImage(file="utils/images/arti2.png")
        mini_logo = PhotoImage(file="utils/images/arti_medium.png")

        #root.iconphoto(False, logo
        installation_root.iconbitmap("utils/images/arti2.ico")
        installation_root.wm_iconphoto(True, logo)
        installation_root.title("Program Installation")


        # Parent widget for the buttons
        master_frame = Frame(installation_root)
        master_frame.grid(row=0, column =0)

        dialog_frame = Frame(master_frame)
        dialog_frame.grid(row=0, sticky= W, padx=(5))#+ E + S)

        image_lbl = Label(dialog_frame, image = mini_logo, justify="center")
        image_lbl.grid(row=0, column=0,padx=(10), pady=10)#, sticky=N+W)

        welcome_frame = Frame(dialog_frame)
        welcome_frame.grid(row=0, column =1, sticky=W, padx=(5))

        welcome_lbl = Label(welcome_frame, text='Welcome to aRTi!', font=("Gabriola", 30, "bold"), justify="left")
        welcome_lbl.grid(row=0, column = 1, sticky = N+W, pady=5)#, sticky=N)

        instruction_lbl = Label(welcome_frame, justify = "left",text='Since it is the first execution of the program you need to download \nand install the following libraries in order to correctly run aRTi.\nPlease make sure to have an internet connection.', font=("Times New Roman", 12))
        instruction_lbl.grid(row=1, column = 1, sticky = N+W, pady=10)#, sticky=N)

        prova_frame = Frame(master_frame)
        prova_frame.grid(row=0, column=2)#, sticky=N + W)#+ E + S)



        # ---------------------------------------------------- BOX Frame
        box_frame = LabelFrame(master_frame, text="The following packages will be installed:", padx=5, pady=5)
        box_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E + W + N + S)

        installation_root.columnconfigure(0, weight=1)
        installation_root.rowconfigure(1, weight=1)

        box_frame.rowconfigure(0, weight=1)
        box_frame.columnconfigure(0, weight=1)

        # Create the textbox
        txtbox = scrolledtext.ScrolledText(box_frame, width=40, height=10, font=("Times New Roman", 12))
        txtbox.grid(row=0, column=0, sticky=E + W + N + S)
        txtbox.insert(INSERT, get_packages())
        txtbox.configure(state="disabled")

        #-----------------------------------------------accept frame
        accept_frame = Frame(master_frame)
        accept_frame.grid(row=2, padx=(10), pady=10, sticky = W)

        accept_terms = BooleanVar()

        # check button
        check_btn = Checkbutton(accept_frame, text="I accept to download and install the previous packages. Click the 'Next' button to continue", variable=accept_terms, onvalue=True, offvalue=False, command = launch)
        check_btn.grid(row = 0, sticky = W)

        #next button
        next_btn = Button(accept_frame, text='Next', state = DISABLED, width=10, command = bar)
        next_btn.grid(row=2, sticky=E+S, pady=10)


        #progress bar
        progress = ttk.Progressbar(accept_frame, orient=HORIZONTAL, length=600, mode = "determinate")
        progress.grid(row=1, sticky = W)

        #defines min and max root dimension
        installation_root.update()
        installation_root.minsize(installation_root.winfo_width(), installation_root.winfo_height())
        installation_root.maxsize(installation_root.winfo_width(), installation_root.winfo_height())
        installation_root.mainloop()


        #reading_time()


        #installation_root.mainloop()
    except ModuleNotFoundError:

        installation_root = Tk()

        installation_root.geometry("750x250")
        installation_root.title("Program installation")
        installation_root.iconphoto(False, PhotoImage(file="utils/images/output-onlinepngtools.png"))
        installation_root.pack()

        print("Since it is the first execution of the program you need to install the following libraries in order to correctly run ARTI:\n")
        with open("requirements.txt", 'r') as f:
            lines = f.readlines()
            print(lines)
        choice = input("\nDo you want to proceed with the installation? Type 'Y' to proceed or type any other key to close the process:\t").lower()
        if choice == 'y':
        # implement pip as a subprocess:
            subprocess.run(["pip3", "install", "-r", "requirements.txt"], shell=True, capture_output=True)
            import os.path
            import PyPDF2
            import docx
            print("\nPackages correctly installed!\n")
            reading_time()
            input("\npress any key to exit.")
        else:
            print("\nBye! ", "\U0001F984")
        installation_root.mainloop()
