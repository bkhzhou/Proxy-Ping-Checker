import requests
import tkinter as tk
from tkinter import filedialog
import timeit

window = tk.Tk()
window.geometry('750x400')
window.title('KH Proxy Pinger')

def deleteMSScreen():
   msText.delete("1.0","end")
# http://httpbin.org/ip

def input():
    msText.config(state=tk.NORMAL)
    deleteMSScreen()
    url = entry.get()
    timeout = 1000
    text = inputText.get('1.0', tk.END).splitlines()
    # start = timeit.default_timer()
    export = ''
    for line in text:
        line = line.strip()
        line = swap(line)
        rank = { 'http': 'http://'+line }
        try:
            response = requests.get(url, proxies=rank, timeout=1)
            print(response.content)
            timeoutSec = response.elapsed.total_seconds()
            milliseconds = int(timeoutSec * 1000)
            if milliseconds < timeout:
                msText.insert(tk.INSERT,  str(milliseconds) + "ms\n")
                export +=line+'\n'
            elif milliseconds > timeout:
                msText.insert(tk.INSERT, "Bad Proxy\n")
        except requests.exceptions.Timeout:
            msText.insert(tk.INSERT, "Timeout\n")
        except requests.exceptions.RequestException as e:
            msText.insert(tk.INSERT, "Conn Err\n")
    msText.config(state=tk.DISABLED)
    # stop = timeit.default_timer()
    # execution_time = stop - start
    # print(execution_time)
    swapOriginal(export)

def saveFile(export):
    file = filedialog.asksaveasfile(
        defaultextension='.txt',
        filetypes=[
            ("Text documents (*.txt)",".txt"),
            ("All files", ".*"),
        ])
    file.write(export)
    file.close()
    
def swap(line):
    result = line.split(':')
    newproxy = result[2] + ":" + result[3] + "@" + result[0] + ":" + result[1]
    return newproxy

def swapOriginal(line):
    line = line.splitlines()
    originalProxy = ''
    for x in line:
        result = x.split(':') # 0 2
        atSign = result[1].split('@')
        # print(result) # user port
        # print(atSign) # pass ip
        originalProxy += atSign[1] + ':' + result[2] + ':' + result[0] + ':' + atSign[0] + '\n'
    saveFile(originalProxy)

# adding a label to the root window
label = tk.Label(window, text = "Link:")
label.config(font =("Courier", 14))
# adding Entry Field
entry = tk.Entry(window, width=50)
footerlabelleft = tk.Label(window, text = "Twitter @ ghostedkh")
footerlabel = tk.Label(window, text = "made by kh")

pingIT = tk.Button(window, text = "Ping", command=lambda:input())

inputText = tk.Text(window, height = 15, width = 58, font=('Courier',14))
msText = tk.Text(window, height = 15, width = 8, font=('Courier',14))

# grid
label.grid(row=0,column=0,padx=20,pady=2)
entry.grid(row=0,column=1,padx=5,pady=2)
pingIT.grid(row=0,column=2,columnspan=2,padx=2,pady=5)
inputText.grid(row=2,column=0,columnspan=2,padx=2,pady=2)
msText.grid(row=2,column=3,padx=2,pady=2)
footerlabelleft.grid(row=3,column=0,columnspan=2,padx=2,pady=2)
footerlabel.grid(row=3,column=2,columnspan=2,padx=2,pady=2)

# run exe
window.resizable(False,False)
window.mainloop()
