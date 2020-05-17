# postaw-na-milion-
projekt do stawiania na milion

def zamykanie_okna():
    messagebox.showinfo("witaj", imie.get())
    glowne_okno.destroy()


glowne_okno=glowne.Tk()             #tworzenie okna początkowego/glownego
glowne_okno.title("Postaw na milion")
glowne_okno.geometry("600x400")
opis_pole_tekstowe=Label(glowne_okno,text="Witamy serdecznie w programie Postaw na milion,\n Wpisz imię")     #co ma się znaleźć w oknie                                                                                                                 początkowym  

opis_pole_tekstowe.grid(row=0,column=0)                 #gdzie ma sie pojawic tekst
imie=Entry(glowne_okno)                                 #tworzenie pola tekstowego do którego wpiszemy imie
imie.grid(row=1,column=0)                               #gdzie to pole tekstowe ma się pojawić

przycisk1=Button(glowne_okno,text="Przejdź do gry!",command=zamykanie_okna)         #tworzenie przycisku zaczynającego rozgrywkę,                                                                                         "command=zamykanie okna" odpala nam funkcję, która zamyka to                                                                                 okno gdy już klikniemy przycisk
przycisk1.grid(row=0,column=2)          #gdzie ten przycisk ma się znajować

glowne_okno.mainloop()        #to po prostu odpala nam wszystko i jest niezbędne, chyba nie da się tego inaczej wytłumaczyć XD
