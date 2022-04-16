from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
from gtts import gTTS
import os

        
root = Tk()
root.title('Translator')
root.geometry('1000x500')

def audiotranslation():
    try:
        for key, value in languages.items():
            if(value == original_combo.get()):
                language = key
                
        output = gTTS(text= original_text.get(1.0,END),lang = language,slow=False)
        output.save("output.mp3")
        os.system("open output.mp3")
        
    except Exception as e:
        messagebox.showerror("Translator",e)
  
def transaudio():
    try:
        for key, value in languages.items():
            if(value == trans_combo.get()):
                language2 = key
                
        output = gTTS(text= translated_text.get(1.0,END),lang = language2,slow=False)
        output.save("output.mp3")
        os.system("open output.mp3")
    except Exception as e:
        messagebox.showerror("Translator",e)     
        
def translation():
    translated_text.delete(1.0,END)
    try:
        for key, value in languages.items():
            if(value == original_combo.get()):
                from_language_key = key
                
        for key, value in languages.items():
            if(value == trans_combo.get()):
                to_language_key = key
                
        words = textblob.TextBlob(original_text.get(1.0,END))
        words = words.translate(from_lang= from_language_key, to=to_language_key)
        
        translated_text.insert(1.0,words)
        
        
    except Exception as e:
        messagebox.showerror("Translator",e)

def clear():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)
    
languages = googletrans.LANGUAGES 
language_list = list(languages.values())


original_text = Text(root, height = 10, width=40)
original_text.grid(row=0,column=0, pady=20, padx=10)


translated_text = Text(root,height=10,width =40)
translated_text.grid(row=0,column=2, pady=20, padx=10)


original_combo = ttk.Combobox(root,width=40,value=language_list)
original_combo.current(21)
original_combo.grid(row=1,column=0)


trans_combo = ttk.Combobox(root,width=40,value=language_list)
trans_combo.current(26)
trans_combo.grid(row=1,column=2)

translatebtn = Button(root,text="Translate", command= lambda:translation())
translatebtn.grid(row=0,column=1,padx=10)

audiobtn = Button(root,text="speech",command = lambda:audiotranslation())
audiobtn.grid(row = 2,column = 0)

transaudiobtn = Button(root,text="speech",command = lambda:transaudio())
transaudiobtn.grid(row = 2,column = 2)

clearbtn = Button(root,text="clear",command= clear)
clearbtn.grid(row=2, column=1)

root.mainloop()