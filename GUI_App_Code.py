#import Modules
import tkinter as tk
import time
import pypokedex
import datetime as dt
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
import requests,json

api_key = "3c91f2ad78ccc17451c13dd68f107148"
expression = ""


#Pokemon-Game
def new_window():
    window = tk.Toplevel(root)
    window.geometry("700x700")
    window.title("Pokemon Pokedex")
    window.config(padx=10,pady=10)
    button = tk.Button(window, text="new window", bg='black', fg='#469A00',
                              command=lambda: new_window())

    title_label = tk.Label(window, text="Pokemon Pokedex")
    title_label.config(font=("arial",32))
    title_label.pack(padx=10,pady=10)

    pokemon_image = tk.Label(window)
    pokemon_image.pack(padx=10,pady=10)

    pokemon_info = tk.Label(window)
    pokemon_info.config(font=("arial",20))
    pokemon_info.pack(padx=10,pady=10)

    pokemon_types = tk.Label(window)
    pokemon_types.config(font=("arial",20))
    pokemon_types.pack(padx=10,pady=10)

    pokemon_height = tk.Label(window)
    pokemon_height.config(font=("arial",20))
    pokemon_height.pack(padx=10,pady=10)

    pokemon_weight = tk.Label(window)
    pokemon_weight.config(font=("arial",20))
    pokemon_weight.pack(padx=10,pady=10)

    pokemon_ability = tk.Label(window)
    pokemon_ability.config(font=("arial",20))
    pokemon_ability.pack(padx=10,pady=10)

    def load_pokemon(event):
        try:
            pokemon = pypokedex.get(name=text_id_name.get(1.0,"end-1c").lower().strip())
    
            http = urllib3.PoolManager()
            response = http.request('GET', pokemon.sprites.front.get('default'))
            image = PIL.Image.open(BytesIO(response.data))
    
            img = PIL.ImageTk.PhotoImage(image)
            pokemon_image.config(image=img)
            pokemon_image.image = img
    
            pokemon_info.config(text="Pokedex: "+str(pokemon.dex)+", Name: "+str(pokemon.name).title())
            pokemon_types.config(text="Type: "+" - ".join([t for t in pokemon.types]).title())
    
            z=[]
            for i in range(0,len(pokemon.abilities)):
                z.append(pokemon.abilities[i][0])
            pokemon_ability.config(text="Ability: "+", ".join(z).title())
            pokemon_height.config(text="Height: "+str(pokemon.height))
            pokemon_weight.config(text="Weight: "+str(pokemon.weight))
            text_id_name.delete("1.0","end")
        except:
            text_id_name.delete("1.0","end")
            home1=tk.Toplevel()
            home1.geometry('250x70')
            home1.resizable(0, 0)
            home1.title('Error')
            label0 = tk.Label(home1,text='Enter Valid ID or Name',fg='red')
            label0.config(font=("arial",12))
            label0.pack(padx=10,pady=10)


    label_id_name = tk.Label(window, text="ID or Name")
    label_id_name.config(font=("arial",20))
    label_id_name.pack(padx=10,pady=10)

    text_id_name = tk.Text(window, height="1")
    text_id_name.config(font=("arial",20))
    text_id_name.pack(padx=10,pady=10)
    text_id_name.bind("<Return>",load_pokemon)

    button = tk.Button(window, text="Load Pokemon")
    button.bind("<Button-1>",load_pokemon)
    button.config(font=("arial",20))
    button.pack(padx=10,pady=10)
    window.mainloop()


#calculator
def new_window2():
    win = tk.Toplevel(root)
    win.geometry("312x324")  
    win.resizable(0, 0)  
    win.title("Calculator")
    global expression

    def btn_click(item):
        global expression
        expression = expression + str(item)
        input_text.set(expression)

    def bt_clear(): 
        global expression 
        expression = "" 
        input_text.set("")
 
    def bt_equal():
        global expression
        try:
            result = str(eval(expression)) 
            input_text.set(result)
        except:
            home1=tk.Toplevel()
            home1.geometry('250x70')
            home1.title('Error')
            home1.resizable(0, 0)
            label0 = tk.Label(home1,text='Enter Valid Expression',fg='red')
            label0.config(font=("arial",12))
            label0.pack(padx=10,pady=10)
            input_text.set("")            
        expression = ""
 
    expression = "" 
    input_text = tk.StringVar()
 
    input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2) 
    input_frame.pack(side="top")
 
    input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify="right") 
    input_field.grid(row=0, column=0) 
    input_field.pack(ipady=10) 
    btns_frame = tk.Frame(win, width=312, height=272.5, bg="grey") 
    btns_frame.pack()
 
    # first row 
    clear = tk.Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1) 
    divide = tk.Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
    # second row 
    seven = tk.Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1) 
    eight = tk.Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1) 
    nine = tk.Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1) 
    multiply = tk.Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
    # third row 
    four = tk.Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
    five = tk.Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
    six = tk.Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
    minus = tk.Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
    # fourth row
    one = tk.Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
    two = tk.Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
    three = tk.Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
    plus = tk.Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
    # fourth row
    zero = tk.Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
    point = tk.Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
    equals = tk.Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

    win.mainloop()


#Text Editor
def new_window3():
    window3 = tk.Toplevel(root)
    window3.title("Text Editor Application")
    window3.rowconfigure(0, minsize=600, weight=1)
    window3.columnconfigure(1, minsize=600, weight=1)
    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window3.title(f"Text Editor Application - {filepath}")

    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window3.title(f"Text Editor Application - {filepath}")
    
    txt_edit = tk.Text(window3)
    fr_buttons = tk.Frame(window3, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
    btn_exit = tk.Button(fr_buttons, text="Exit", command=window3.destroy)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    btn_exit.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window3.mainloop()


#Weather
def new_window4():
    home=tk.Toplevel(root)
    home.geometry('500x450')
    home.title('Weather App')
    home.resizable(0, 0)
    try:
        bg0 = tk.PhotoImage(file = "background\mountain.png")
        label100 = tk.Label( home, image = bg0,width = 500, height =500)
        label100.place(x = 0, y = 0)
    except:
        home.config(bg="light blue")

    def proceed():
        city=cit.get()
        if city=='':
            home1=tk.Toplevel()
            home1.geometry('150x70')
            home1.title('Error')
            home1.resizable(0, 0)
            label0 = tk.Label(home1,text='Enter City Name',fg='red')
            label0.config(font=("arial",12))
            label0.pack(padx=10,pady=10)
            return    
        else:
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            cityname = city
            complete_url = base_url + "appid=" + api_key + "&q=" + cityname 
            response = requests.get(complete_url) 
            x = response.json()  
            if x["cod"] != "404": 
      
                y = x["main"] 
                currenttemp = y["temp"] 
                currentpressure = y["pressure"] 
                currenthumidiy = y["humidity"]
                z = x["weather"] 
                weather_description = z[0]["description"]  
                tk.Label(home,text='Temperature: '+str(round(currenttemp-272.15))+' degree celsius',font=4).place(x=10,y=150)
                tk.Label(home,text='Atmospheric Pressure: '+str(currentpressure)+' hPa',font=4).place(x=10,y=180)
                tk.Label(home,text='Humidity: '+str(currenthumidiy),font=4).place(x=10,y=210)
                tk.Label(home,text='Description: '+str(weather_description),font=4).place(x=10,y=240)
            else:
                home1=tk.Toplevel()
                home1.geometry('150x70')
                home1.title('Error')
                home1.resizable(0, 0)
                label0 = tk.Label(home1,text='No City Found',fg='red')
                label0.config(font=("arial",12))
                label0.pack(padx=10,pady=10)             
                return
            
    cit=tk.StringVar()
    label1 = tk.Label(home,text='Weather App',font=('Helvetica 12 bold',18), pady=10)
    label1.place(x=10,y=5)
    label2 = tk.Label(home,text='Enter City:',font=4)
    label2.place(x=10,y=60)
    bar = tk.Entry(home,width=15,textvariable=cit,font=4)
    bar.place(x=110,y=60)
    button = tk.Button(home,text='Proceed',command=proceed, font=1)
    button.place(x=300,y=55)

    home.mainloop()


#Gallery
def new_window5():
    home=tk.Toplevel(root)
    home.geometry('305x370')
    home.title('Gallery')
    home.config(bg='black')
    home.resizable(0, 0)
      
    def forward(img_no,label33,button_forward,button_back):
        label33.grid_forget()

        label33 = tk.Label(home,image=List_images[img_no-1])
        button_forward = tk.Button(home,bg="black",fg="white",text="Forward",font=1,command=lambda: forward(img_no+1,label33,button_forward,button_back))
        button_back = tk.Button(home,bg="black",fg="white",text="Back",font=1,command=lambda: back(img_no - 1,label33,button_forward,button_back))
        if img_no == 10:
            button_forward = tk.Button(home,bg="black",fg="white",text="Forward",font=1, state=tk.DISABLED)
  
        label33.grid(row=1, column=0, columnspan=3)
        button_back.place(x=18,y=328)
        button_forward.place(x=208,y=328)
  
  
    def back(img_no,label33,button_forward,button_back):
        label33.grid_forget()

        label33 = tk.Label(home,image=List_images[img_no-1])
        button_forward = tk.Button(home,bg="black",fg="white",text="Forward",font=1,command=lambda: forward(img_no+1,label33,button_forward,button_back))
        button_back = tk.Button(home,bg="black",fg="white",text="Back",font=1,command=lambda: back(img_no - 1,label33,button_forward,button_back))
        if img_no == 1:
            button_back = tk.Button(home,bg="black",fg="white",text="Back",font=1, state=tk.DISABLED)
  
        label33.grid(row=1, column=0, columnspan=3)
        button_back.place(x=18,y=328)
        button_forward.place(x=208,y=328)

    image_no_1 = ImageTk.PhotoImage(Image.open("pictures\sample1.gif").resize((301,318),Image.ANTIALIAS))
    image_no_2 = ImageTk.PhotoImage(Image.open("pictures\sample2.gif").resize((301,318),Image.ANTIALIAS))
    image_no_3 = ImageTk.PhotoImage(Image.open("pictures\sample3.gif").resize((301,318),Image.ANTIALIAS))
    image_no_4 = ImageTk.PhotoImage(Image.open("pictures\sample4.gif").resize((301,318),Image.ANTIALIAS))
    image_no_5 = ImageTk.PhotoImage(Image.open("pictures\sample5.gif").resize((301,318),Image.ANTIALIAS))
    image_no_6 = ImageTk.PhotoImage(Image.open("pictures\sample6.gif").resize((301,318),Image.ANTIALIAS))
    image_no_7 = ImageTk.PhotoImage(Image.open("pictures\sample7.gif").resize((301,318),Image.ANTIALIAS))
    image_no_8 = ImageTk.PhotoImage(Image.open("pictures\sample8.gif").resize((301,318),Image.ANTIALIAS))
    image_no_9 = ImageTk.PhotoImage(Image.open("pictures\sample9.gif").resize((301,318),Image.ANTIALIAS))
    image_no_10 = ImageTk.PhotoImage(Image.open("pictures\sample10.gif").resize((301,318),Image.ANTIALIAS))

    List_images = [image_no_1, image_no_2, image_no_3, image_no_4, image_no_5, image_no_6, image_no_7, image_no_8, image_no_9, image_no_10]  
    label33 = tk.Label(home,image=image_no_1)

    label33.grid(row=1, column=0, columnspan=3)
    button_back = tk.Button(home,bg="black",fg="white",text="Back",font=1,command=back,state=tk.DISABLED)
    button_exit = tk.Button(home,bg="black",fg="red",text="Exit",font=1,command=home.destroy)  
    button_forward = tk.Button(home,bg="black",fg="white",text="Forward",font=1,command=lambda: forward(2,label33,button_forward,button_back))
    button_back.place(x=18,y=328)
    button_exit.place(x=118,y=328)
    button_forward.place(x=208,y=328)
    
    home.mainloop()


#Flames-Game
def new_window6():
    home=tk.Toplevel(root)
    home.configure(background = 'orange')
    home.geometry("500x430")
    home.title("Flames Game")
    home.resizable(0, 0)

    def remove_match_char(list1, list2):
 
        for i in range(len(list1)) :
            for j in range(len(list2)) :
                if list1[i] == list2[j] :
                    c = list1[i]
                    list1.remove(c)
                    list2.remove(c)
                    list3 = list1 + ["*"] + list2
                    return [list3, True]
 
        list3 = list1 + ["*"] + list2
        return [list3, False]
 

    def tell_status() :

        Status_field.delete(0,"end")
        p1 = Player1_field.get()
        p1 = p1.lower()
        p1 = "".join(p1.split())
        p1_list = list(p1)

        p2 = Player2_field.get()
        p2 = p2.lower()
        p2 = "".join(p2.split())
        p2_list = list(p2)

        proceed = True
        while proceed :
            ret_list = remove_match_char(p1_list, p2_list)

            con_list = ret_list[0]
            proceed = ret_list[1]
            star_index = con_list.index("*")
            p1_list = con_list[ : star_index]
            p2_list = con_list[star_index + 1 : ]
 
        count = len(p1_list) + len(p2_list)
        result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

        split_index = ((count%len(result)) - 1)
        if(count==0):
            Status_field.insert(0, "Soulmate")
        else:
            Status_field.insert(0, result[split_index])
 
 
    def clear_all() : 
        Player1_field.delete(0,"end")  
        Player2_field.delete(0,"end")
        Status_field.delete(0,"end")
        Player1_field.focus_set()
        
      
    label0 = tk.Label(home, text = "FLAMES Game",font=('Arial',26) ,fg = 'red', bg = 'orange')
    label0.place(x=10,y=10)

    label1 = tk.Label(home, text = "Player 1 Name: ",font=10 ,fg = 'black', bg = 'orange')
    label2 = tk.Label(home, text = "Player 2 Name: ",font=10 ,fg = 'black', bg = 'orange')
    label3 = tk.Label(home, text = "Relationship Status: ",font=10 ,fg = 'black', bg = 'orange')
 
    label1.place(x=10,y=110)
    label2.place(x=10,y=150) 
    label3.place(x=10,y=240)

    Player1_field = tk.Entry(home,font=10 ) 
    Player2_field = tk.Entry(home,font=10 ) 
    Status_field = tk.Entry(home,font=10 )
 
    Player1_field.place(x=200,y=110)
    Player2_field.place(x=200,y=150) 
    Status_field.place(x=200,y=240)

    button1 = tk.Button(home, text = "Submit",font=10 , bg = "light blue",fg = "black", command = tell_status)
    button2 = tk.Button(home, text = "Clear",font=10 , bg = "light blue",fg = "black", command = clear_all)
 
    button1.place(x=200,y=190)
    button2.place(x=300,y=190)
    Player1_field.focus_set()

    home.mainloop()




#Desktop
    
HEIGHT = 700
WIDTH = 700
root = tk.Tk()
root.geometry(str(HEIGHT)+"x"+str(WIDTH))
root.title("Window")
root.resizable(0, 0)

#Background-Image
try:
    bg = ImageTk.PhotoImage(Image.open("background\city.gif").resize((700,700),Image.ANTIALIAS))
    label100 = tk.Label( root, image = bg,width = 700, height =700)
    label100.place(x = 0, y = 0)
except:
    root.config(bg="light blue")
#Time-Date
time1 = ''
clock = tk.Label(root, font=('arial', 20, 'bold'),fg='white', bg='black', width=24)
clock.place(x=250,y=0)
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)

tick()
w1= tk.Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}",width=18, fg="white", bg="black", font=("helvetica", 20))
w1.place(x=0,y=0)

#Pokemon-Game
photo = ImageTk.PhotoImage(Image.open("icons\pokeball.png").resize((100,100),Image.ANTIALIAS))
button = tk.Button(root,image=photo, text="Pokedex",font=('times', 20), bg='white', fg='white',command=lambda: new_window())
button.place(y=130,x=140)
tk.Label(root,bg='black',fg="white",text="Pokemon Game",width=14).place(y=235,x=141)

#Calculator
photo2 = ImageTk.PhotoImage(Image.open("icons\calculator.png").resize((100,100),Image.ANTIALIAS))
button2 = tk.Button(root, image=photo2, text="Calculator",font=('times', 20), bg='white', fg='white',command=lambda: new_window2())
button2.place(y=280,x=140)
tk.Label(root,bg='black',fg="white",text="Calculator",width=14).place(y=385,x=141)

#Text-Editor
photo3 = ImageTk.PhotoImage(Image.open("icons\editer.png").resize((100,100),Image.ANTIALIAS))
button3 = tk.Button(root, image=photo3, text="Text Editor",font=('times', 20), bg='white', fg='white',command=lambda: new_window3())
button3.place(y=430,x=140)
tk.Label(root,bg='black',fg="white",text="Text Editor",width=14).place(y=535,x=141)

#Weather-App
photo4 = ImageTk.PhotoImage(Image.open("icons\weather.png").resize((100,100),Image.ANTIALIAS))
button4 = tk.Button(root,image=photo4,  text="Weather App",font=('times', 20), bg='white', fg='white',command=lambda: new_window4())
button4.place(y=130,x=390)
tk.Label(root,bg='black',fg="white",text="Weather App",width=14).place(y=235,x=391)

#Gallery
photo5 = ImageTk.PhotoImage(Image.open("icons\photos.png").resize((100,100),Image.ANTIALIAS))
button5 = tk.Button(root, image=photo5, text="Gallery",font=('times', 20), bg='white', fg='black',command=lambda: new_window5())
button5.place(y=280,x=390)
tk.Label(root,bg='black',fg="white",text="Gallery",width=14).place(y=385,x=391)

#Flames-Game
photo6 = ImageTk.PhotoImage(Image.open("icons\game.png").resize((100,100),Image.ANTIALIAS))
button6 = tk.Button(root, image=photo6, text="Flames",font=('times', 20), bg='white', fg='black',command=lambda: new_window6())
button6.place(y=430,x=390)
tk.Label(root,bg='black',fg="white",text="Flames Game",width=14).place(y=535,x=391)

#Exit
exitbutton = tk.Button(root, text="Exit", font=('times', 16), fg='red',bg='white', command=root.destroy)
exitbutton.place(y=0,x=648)

root.mainloop()
