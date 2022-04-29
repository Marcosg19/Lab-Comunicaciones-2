from tkinter import *
import cifdefHill
import cifradocesar
#import cifradocreado
import cifradovigenere
import random
import os
import serial
import receptor


serialcomm = serial.Serial('COM3', 57600)
serialcomm.timeout = 1


def Encriptar(texto):
    os.system('clear')
    texto=texto
    
    indice= random.randint(1, 3)
    #indice =3
    

    if (indice==1):
        print("********  Hill     *********************")
    elif (indice==2):
        print("********  Cesar    ********************")
    elif (indice==3):
        print("**********Vigenere ********************")
    
    
    if (indice==1):
        texto=cifdefHill.cifrado(texto)
    elif (indice==2):
        texto=cifradocesar.cifradocesar(texto)
    elif (indice==3):
        texto=cifradovigenere.cifrado3(texto)
        
    
    
    texto=str(indice)+'.'+ texto
    
    

    return texto















BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Chat Seguro")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Bienvenido", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Enviar", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.035, relheight=0.025, relwidth=0.22)

            # receive button
        send_button = Button(bottom_label, text="Recibir", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.msg2(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.025, relwidth=0.22)

     
    def _on_enter_pressed(self, event):

        msg =  self.msg_entry.get()

        msg_ = Encriptar( msg)
    
        serialcomm.write(msg_.encode())
        self._insert_message(msg, "Tu")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


    def msg2(self,event):

         #msg2_=serialcomm.readline().decode('ascii')
        
         msg2 = receptor.Desencriptar_(serialcomm.readline().decode('ascii'))
         #msg2 = serialcomm.readline().decode('ascii')

         self._insert_message2(msg2,"Usuario")
        
    def _insert_message2(self, msg2, sender):
        if not msg2:
            return
        
        self.msg_entry.delete(0, END)
        msg2 = f"{sender}: {msg2}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

          
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()