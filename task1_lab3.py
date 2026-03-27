import tkinter as tk

#Task1: o interfata grafica, caruia ii atribui un nume si o dimensiune 500x500.
 #(a) Plaseaza pe interfata grafica o imagine gif, caruia sa ii functioneze animatia.
 #(b) Evaluati ce librarii puteti sa mai folositi pe langa Tkinter. Propuneti variante/solutii.  

#def main():
# win = GraphWin('My Graphics', 500, 500)
# win.getMouse() # pastreaza window up
# win.close()
#main()


def animeaza_gif(cadru_curent):
    label_gif.config(image=cadre[cadru_curent]) # Schimbăm imaginea afișată
    
    urmatorul_cadru = (cadru_curent + 1) % len(cadre)# Calculăm matematic următorul cadru (se întoarce la 0 când ajunge la final)
    
    win.after(100, animeaza_gif, urmatorul_cadru) # După 100ms, funcția se apelează pe ea însăși cu următorul cadru
    
# 1. Creăm unica fereastră principală
win = tk.Tk()
win.title('My Graphics')
win.geometry('500x500')
# 2. Încărcăm cadrele
cadre = []
try:
    for i in range(20): # Extragem 20 de cadre
        # ATENȚIE AICI: am adăugat master=win.  Asta forțează imaginea să se lege de fereastra pe care o vrem noi!
        
        imagine = tk.PhotoImage(file='animatie.gif', format=f'gif -index {i}', master=win)
        cadre.append(imagine)
except tk.TclError:
    pass # Ne oprim când Tkinter ne zice că nu mai sunt cadre în GIF

if not cadre:
    print("Eroare: Nu am putut încărca cadrele din 'animatie.gif'!")
else:
    label_gif = tk.Label(win)# 3. Creăm rama și o punem pe ecran
    label_gif.pack(expand=True)# 4. Pornim animația
    
    animeaza_gif(0)

win.mainloop()# 5. Ținem fereastra deschisă

#(b)Alte librarii pe langa Tlkinter
#pyqt5: Este probabil cel mai puternic și complet framework pentru crearea de aplicații desktop profesionale în Python
#
#Pygame: Este o librărie concepută special pentru dezvoltarea de jocuri 2D și aplicații multimedia interactive.
#
#
#