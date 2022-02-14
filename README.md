# aRTi

<img align="right" width="30%" src="https://github.com/claudialorusso/aRTi/blob/master/utils/images/aRTi_large.png" alt="aRTi">

**Reading time** computator.

### What is aRTi

**aRTi** is a portable software that enables the user to compute the *reading time* of a document.

Are you a university student that needs to know how much time does it take to read your thesis speech?

Does your boss encharged you to produce a presentation that can't go over the standard ten minutes or "you're fired!!" ??

Or do you just need to know how much time does it take to read that particular book (yeah, that one.) ???

*No worries!!* **aRTi** is here to help you!

You just need to upload the preferred file ('.pdf', '.docx', 'txt' only) and the software will tell you how many minutes and seconds you need to read the entire content.

### aRTi: Why the name ?

That's an easy question... whose answer lies in the English pronunciation of the first letter of both *Reading* and *Time* words:

![arti_pronunciation](https://user-images.githubusercontent.com/38263840/153881479-e6c23fdd-2f2d-43e5-92a7-96969f9442d3.png)

:)

### Sources

The software is based on a time's computation function ideated after the evaluation of the following articles:

<ul>
<li>
<a href = https://kodify.net/hugo/strings/reading-time-text/> source 1</a>;
</li>
<li> 
<a href = https://qualcherisposta.it/quante-parole-si-pronunciano-un-minuto> source 2</a>;
</li>
<li> 
<a href = https://www.sciencedirect.com/science/article/abs/pii/S0749596X19300786> source 3</a>.
</li>
</ul>

In few words, the function is based on the fact that, in Occidental Countries, an individual can read an avarage of 200 words per minutes (<i>wpm</i>).

### Usage

**aRTi** could not be more easier...

You can either choose to download the executable <a href="https://github.com/claudialorusso/aRTi/blob/master/aRTi.exe">aRTi.exe</a> or charge it via command line.

If you choose to download the *.exe*, the software is ready to be used while if you choose the command line option please read the section below for a correct execution.

### Command Line Experience

First thing, since the progam is **Python 3** based, you need to install it on your machine.

**Please** install **Python 3.9** or below.

Open the command prompt and jump to the **aRTi** folder.

Assuming the folder is in "C:\\aRTi" you just need to type in the command line the following instructions:

```
cd "C:\\aRTi"
py ARTI_GUI.py
```

If it is the first launch of the program **or** the program detects missing packages, an installation window will pop-up asking you the authorization to download and install these lasts.
Please make sure that your device has network connectivity.


<p align="center">
  <img width=60% src= "https://user-images.githubusercontent.com/38263840/153883598-b784df6e-53d3-4586-ba5c-c4cbfd358d0d.png" alt="Installazione">
</p>

Check the box and click on the "Next" button: **aRTi** will, finally, open.

![home_arti](https://user-images.githubusercontent.com/38263840/153883724-74673e61-b281-479c-a3e2-fccf9027c866.png)


### UWP

<b>aRTi</b> is an <b>UWP</b> (<i>Universal Windows Platform</i>) this means that it is compatible with several windows version, according to the <a href="https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/">windows SDK</a> requirements.

### Libraries

The following libraries were used to create <b>aRTi</b>:
<ul>
<li><a href ="https://github.com/mstamy2/PyPDF2">PyPDF2</a> </li>
<li><a href ="https://python-docx.readthedocs.io/en/latest/user/documents.html">python-docx</a> </li>
<li><a href ="https://docs.python.org/3/library/tkinter.html">tkinter</a> (GUI purposes) </li>
</ul>

<details>
<summary>Italiano</summary>

# aRTi

<img align="right" width="30%" src="https://github.com/claudialorusso/aRTi/blob/master/utils/images/aRTi_large.png" alt="aRTi">

Calcolatore del <b>tempo di lettura</b>.

### Che cos'è aRTi

**aRTi** è un programma portabile che permette all'utente di calcolare il <i>tempo di lettura</i> di un documento.

Sei uno studente universitario e vuoi sapere quanto tempo ci metterai a recitare la tua discussione di tesi di laurea?

Il tuo capo ti ha incaricato una presentazione che non può oltrepassare i 10 minuti "altrimenti sei licenziato!!" ??

O hai semplicemente bisogno di sapere quanto tempo ci metterai a leggere un determinato libro (si. Mi riferisco proprio a quel libro.) ???

<i>Non ti preoccupare!!</i> <b>aRTi</b> è qui per darti una mano!

Devi soltanto caricare il file che desideri (scegliendo tra '.pdf', '.docx' oppure 'txt') ed il software ti comunicherà i minuti ed i secondi di lettura complessivi dell'intero documento.

### aRTi: Perchè quel nome... ?

...  semplice ... la risposta risiede nella pronuncia inglese della prima lettera di *Reading* e di *Time* (<i>reading time</i> == <i> tempo di lettura</i>):

![aRTi_pronuncia](https://user-images.githubusercontent.com/38263840/153881479-e6c23fdd-2f2d-43e5-92a7-96969f9442d3.png)

:)

### Fonti

Il software si basa su di una funzione di computazione del tempo di lettura ideata in seguito alla valutazione dei seguenti articoli:

<ul>
<li>
<a href = https://kodify.net/hugo/strings/reading-time-text/> source 1</a>;
</li>
<li> 
<a href = https://qualcherisposta.it/quante-parole-si-pronunciano-un-minuto> source 2</a>;
</li>
<li> 
<a href = https://www.sciencedirect.com/science/article/abs/pii/S0749596X19300786> source 3</a>.
</li>
</ul>

In soldoni, la funzione si basa sul fatto che, nei Paesi Occidentali, gli individui sono in grado di leggere in media 200 parole al minuto (<i>wpm</i>).

### Utilizzo

**aRTi** non potrebbe essere più semplice di così...

Puoi scegliere se effettuare il download dell'eseguibile <a href="https://github.com/claudialorusso/aRTi/blob/master/aRTi.exe">aRTi.exe</a> o di avviarlo tramite prompt dei comandi.

Se scegli di effettuare il download dell'<i>.exe</i>, il software è pronto all'uso; se, invece, scegli l'opzione della linea di comando, per favore, leggi attentamente la sezione sottostante per una corretta esecuzione.

### Command Line Experience

Per prima cosa, poichè il programma è basato su <b>Python 3</b>, è necessario scaricarlo sulla tua macchina.

**Per favore** installa **Python 3.9** or precedenti.

Apri il prompt dei comandi e vai nella cartella in cui hai scaricato **aRTi** .

Supponendo che la cartella si trovi in "C:\\aRTi" devi soltanto riportare le seguenti istruzioni nel prompt:

```
cd "C:\\aRTi"
py ARTI_GUI.py
```
Se si tratta della prima esecuzione **oppure** è stata rilevata la mancanza di alcune librerie propedeutiche all'avviamento del software, apparirà una finestra in cui ti vengono chieste le autorizzazioni per scaricare ed installare queste ultime.

Per favore, assicurati di essere connesso ad internet.

<p align="center">
  <img width=60% src= "https://user-images.githubusercontent.com/38263840/153883598-b784df6e-53d3-4586-ba5c-c4cbfd358d0d.png" alt="Installazione">
</p>

Spunta la relativa box e clicca sul pulsante "Next": al termine del caricamento si aprirà, finalmente, **aRTi**.

![home_arti](https://user-images.githubusercontent.com/38263840/153883724-74673e61-b281-479c-a3e2-fccf9027c866.png)


### UWP

<b>aRTi</b> è una <b>UWP</b> (<i>Piattaforma Windows Universale</i>) il che significa che è compatibile con diverse versioni di windows, in accordo ai requisiti di <a href="https://developer.microsoft.com/it-it/windows/downloads/windows-sdk/">windows SDK</a>.

### Libraries

Le librerie utilizzate per la creazione di <b>aRTi</b> sono le seguenti:
<ul>
<li><a href ="https://github.com/mstamy2/PyPDF2">PyPDF2</a> </li>
<li><a href ="https://python-docx.readthedocs.io/en/latest/user/documents.html">python-docx</a> </li>
<li><a href ="https://docs.python.org/3/library/tkinter.html">tkinter</a> (GUI purposes) </li>
</ul>


</details>