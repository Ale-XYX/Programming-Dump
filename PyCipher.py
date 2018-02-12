import tkinter as tk
import tkinter.font as tkFont
import tkinter.scrolledtext as tkText
import tkinter.ttk as ttk
import pyperclip
import random

class Public:
    decode_output_data = []
    random_active = False
    brute_active = False

class Functions:
    key = [']', '!', 'q', 'n', 'k', ';', 'D', '\\', 'F', '}', 
    'l', 'H', 'h', 'X', 'o', 'v', 'x', ':', 'C', '*', '1', 's', 
    'u', '>', 'm', 'L', 'G', '@', 'f', '$', '"', 'E', ')', 'O', 
    "'", '{', '&', ',', 'A', 'Z', 'Y', 'j', '2', '+', 'K', 'y', 
    'V', '(', '6', '[', 'd', 'p', '7', 'i', '0', 'J', 'S', '?', 
    ' ', '`', '-', 'M', 'N', 'P', '/', '|', 'T', 'W', '3', 'c', 
    'Q', 'I', '8', '4', '^', '=', 'U', 'z', 'a', 'B', '%', 'b', 
    't', 'g', '#', '<', 'R', '.', 'e', '5', 'w', '~', '9', 'r', 
    '_']

    def encode(box, rbool, spinbox, output, btn_disable):
        string = list(box.get())
        if rbool:
            rot = random.randint(0, len(Functions.key))
        elif not rbool:
            rot = spinbox.get()
        for i, char in enumerate(string):
            string[i] = Functions.key.index(string[i])
            string[i] = (int(string[i]) + int(rot)) % len(Functions.key)
            string[i] = Functions.key[string[i]]

        output.insert(tk.END, ''.join(string) + '\n')
        btn_disable.config(state=tk.DISABLED)

    def decode_update(output, var):
        val = var.get()
        val = val % len(Public.decode_output_data)
        output.delete('1.0', tk.END)
        output.insert(tk.END, Public.decode_output_data[val])
        
    def decode(box, bbool, spinbox_get, spinbox_control, output, var, btn_disable):
        string = list(box.get())
        if bbool:
            for i in range(92):
                temp = string[:]
                for _i, c in enumerate(temp):
                    temp[_i] = Functions.key.index(temp[_i])
                    temp[_i] = (int(temp[_i]) - i) % len(Functions.key)
                    temp[_i] = Functions.key[temp[_i]]

                Public.decode_output_data.append(''.join(temp))

            spinbox_control.config(state='readonly')
            output.config(state=tk.NORMAL)
            Functions.decode_update(output, var)

        elif not bbool:
            rot = spinbox_get.get()
            for i, c in enumerate(string):
                print(rot)
                string[i] = Functions.key.index(string[i])
                string[i] = (int(string[i]) - int(rot)) % len(Functions.key)
                string[i] = Functions.key[string[i]]

            output.config(state=tk.NORMAL)
            output.insert(tk.END, ''.join(string)) 
            var.set(rot)

        btn_disable.config(state=tk.DISABLED)

    def encode_copy(box):
        string = box.get('1.0', tk.END)
        string = string[0:len(string) - 2]
        pyperclip.copy(string)

    def decode_copy(box):
        string = box.get('1.0', tk.END)
        string = string[0:len(string) - 1]
        pyperclip.copy(string)

    def rbutton_check(v, spinbox):
        status = v.get()
        if status == 0:
            Public.random_active = False
            spinbox.config(state='readonly')
        elif status == 1:
            Public.random_active = True
            spinbox.config(state=tk.DISABLED)

    def bbutton_check(v):
        status = v.get()
        if status == 0:
            Public.brute_active = False
        elif status == 1:
            Public.brute_active = True

    def encode_clear(output_clear, btn_enable):
        output_clear.delete('1.0', tk.END)
        btn_enable.config(state=tk.NORMAL)

    def decode_clear(output_clear, spinbox_clear, var, btn_enable):
        output_clear.delete('1.0', tk.END)
        var.set(0)
        spinbox_clear.config(state=tk.DISABLED)
        output_clear.config(state=tk.DISABLED)
        Public.decode_output_data = []
        btn_enable.config(state=tk.NORMAL)

    def switch_scenes(ebool, dbool, ebtn, dbtn, eframe, dframe):
        if ebool:
            dbtn.config(relief='raised')
            ebtn.config(relief='sunken')
            eframe.lift()
        elif dbool:
            dbtn.config(relief='sunken')
            ebtn.config(relief='raised')
            dframe.lift()           

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(width=400, height=400)
        self.root.maxsize(width=400, height=400)
        self.root.resizable(False, False)
        self.root.title('PyCipher')
        
        self.standard_font = tkFont.Font(family='Helevecta', size=10, weight='bold')

        self.encode_frame = tk.Frame(self.root)
        self.rbutton_status = tk.IntVar()
        self.encode_rotationbox = tk.Spinbox(self.encode_frame, increment=1, from_=0, to_=93)
        self.encode_text = tk.Label(self.encode_frame, text='Place text to encode here', font=self.standard_font)
        self.encode_entry = tk.Entry(self.encode_frame)
        self.encode_output = tkText.ScrolledText(self.encode_frame)
        self.encode_btn = tk.Button(self.encode_frame, bd=1, text='Encode!', command=lambda: Functions.encode(self.encode_entry, Public.random_active, self.encode_rotationbox, self.encode_output, self.encode_btn))
        self.encode_copy_btn = tk.Button(self.encode_frame, bd=1,  text='Copy', command=lambda: Functions.encode_copy(self.encode_output))
        self.encode_clear_btn = tk.Button(self.encode_frame, bd=1, text='Clear', command=lambda: Functions.encode_clear(self.encode_output, self.encode_btn))
        self.encode_random_checkbutton = tk.Checkbutton(self.encode_frame, text='Random', variable=self.rbutton_status, command=lambda: Functions.rbutton_check(self.rbutton_status, self.encode_rotationbox))

        self.decode_frame = tk.Frame(self.root)
        self.bbutton_status = tk.IntVar()
        self.output_rotationbox_status = tk.IntVar()
        self.decode_rotationbox = tk.Spinbox(self.decode_frame, increment=1, from_=0, to_=93)
        self.decode_text = tk.Label(self.decode_frame, text='Place text to decode here', font=self.standard_font)
        self.decode_entry = tk.Entry(self.decode_frame)
        self.decode_output = tkText.ScrolledText(self.decode_frame)
        self.decode_output_text = tk.Label(self.decode_frame, text='Output at rotation', font=self.standard_font)
        self.decode_output_rotationbox = tk.Spinbox(self.decode_frame, increment=1, from_=0, to_=93, textvariable=self.output_rotationbox_status, command=lambda: Functions.decode_update(self.decode_output, self.output_rotationbox_status), wrap=True)
        self.decode_btn = tk.Button(self.decode_frame, text='Decode!', bd=1, command=lambda: Functions.decode(self.decode_entry, Public.brute_active, self.decode_rotationbox, self.decode_output_rotationbox, self.decode_output, self.output_rotationbox_status, self.decode_btn))
        self.decode_brute_checkbutton = tk.Checkbutton(self.decode_frame, text='Brute Force', variable=self.bbutton_status, command=lambda: Functions.bbutton_check(self.bbutton_status))
        self.decode_copy_btn = tk.Button(self.decode_frame, bd=1, text='Copy', command=lambda: Functions.decode_copy(self.decode_output))
        self.decode_clear_btn = tk.Button(self.decode_frame, bd=1, text='Clear', command=lambda: Functions.decode_clear(self.decode_output, self.decode_output_rotationbox, self.bbutton_status, self.decode_btn))

        self.main_encode_activate = tk.Button(self.root, text='Encode', command=lambda: Functions.switch_scenes(True, False, self.main_encode_activate, self.main_decode_activate, self.encode_frame, self.decode_frame), bd=1)
        self.main_decode_activate = tk.Button(self.root, text='Decode', command=lambda: Functions.switch_scenes(False, True, self.main_encode_activate, self.main_decode_activate, self.encode_frame, self.decode_frame), bd=1)

    def build(self):
        self.encode_frame.lift()
        self.main_encode_activate.config(relief='sunken')
        self.encode_rotationbox.config(state='readonly')
        self.decode_rotationbox.config(state='readonly')
        self.decode_output.config(state=tk.DISABLED)
        self.decode_output_rotationbox.config(state=tk.DISABLED)

        self.main_encode_activate.place(height=30, width=200)
        self.encode_frame.place(height=470, width=400, y=30)
        self.encode_rotationbox.place(height=20, width=55, x=237, y=80)
        self.encode_text.place(height=30, width=200, x=100, y=0)
        self.encode_entry.place(height=20, width=200, x=100, y=25)
        self.encode_output.place(height=200, width=300, x=57, y=120)
        self.encode_btn.place(height=30, width=100, x=100, y=63)
        self.encode_copy_btn.place(height=30, width=100, x=100, y=325)
        self.encode_clear_btn.place(height=30, width=100, x=200, y=325)
        self.encode_random_checkbutton.place(height=20, width=100, x=215, y=55)

        self.main_decode_activate.place(height=30, width=200, x=200)
        self.decode_frame.place(height=470, width=400, y=30)
        self.decode_rotationbox.place(height=20, width=55, x=237, y=80)
        self.decode_text.place(height=30, width=200, x=100, y=0)
        self.decode_entry.place(height=20, width=200, x=100, y=25)
        self.decode_output.place(height=150, width=300, x=57, y=175)
        self.decode_output_text.place(height=30, width=200, x=57, y=140)
        self.decode_output_rotationbox.place(height=20, width=55, x=237, y=147)
        self.decode_btn.place(height=30, width=100, x=100, y=63)
        self.decode_brute_checkbutton.place(height=20, width=100, x=215, y=55)
        self.decode_copy_btn.place(height=30, width=100, x=100, y=333)
        self.decode_clear_btn.place(height=30, width=100, x=200, y=333)

if __name__ == '__main__':
    a = Application()
    a.build()
    a.root.mainloop()