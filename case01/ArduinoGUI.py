import tkinter as tk
'''
+----------------+
|__3__  傳送      |
|766,20.50,52.00 |
'''
root = tk.Tk()
root.geometry("600x400")
root.title("Arduino GUI")

respText = tk.StringVar()
respText.set("0,0.0,0.0")

sendButton0 = tk.Button(text="0")
sendButton1 = tk.Button(text="1")
sendButton2 = tk.Button(text="2")
sendButton3 = tk.Button(text="3")
sendButton4 = tk.Button(text="4")
sendButton5 = tk.Button(text="5")
sendButton6 = tk.Button(text="6")
sendButton7 = tk.Button(text="7")
sendButton8 = tk.Button(text="8")
receiveLabel = tk.Label(root, textvariable=respText)

root.rowconfigure((0,1), weight=1)
root.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

sendButton0.grid(row=0, column=0, columnspan=1, sticky='EWNS')
sendButton1.grid(row=0, column=1, columnspan=1, sticky='EWNS')
sendButton2.grid(row=0, column=2, columnspan=1, sticky='EWNS')
sendButton3.grid(row=0, column=3, columnspan=1, sticky='EWNS')
sendButton4.grid(row=0, column=4, columnspan=1, sticky='EWNS')
sendButton5.grid(row=0, column=5, columnspan=1, sticky='EWNS')
sendButton6.grid(row=0, column=6, columnspan=1, sticky='EWNS')
sendButton7.grid(row=0, column=7, columnspan=1, sticky='EWNS')
sendButton8.grid(row=0, column=8, columnspan=1, sticky='EWNS')
receiveLabel.grid(row=1, column=0, columnspan=2, sticky='EWNS')

root.mainloop()
