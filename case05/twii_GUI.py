import tkinter as tk
import sqlite3 as twiisql
from tkinter import scrolledtext as st

twii_result = ''
result = '證券代號\t證券名稱\t殖利率\t股利年度\t本益比\t股價淨值比\t財報年紀\t資料時間\r\n'

def select():
    global twii_result
    conn = twiisql.connect('twii.db')
    curses = conn.cursor()

    sql = '''
            SELECT * FROM STOCK
          '''
    curses.execute(sql)
    twii_result = curses.fetchall()
    conn.commit()
    print('完成')
    conn.close()


if __name__ == "__main__":
    select()
    win = tk.Tk()
    win.geometry("800x500")
    win.title('TWII股票查詢')

    entry = tk.Entry(win, width=20)
    btn1 = tk.Button(win, text='更新', width=10)
    btn2 = tk.Button(win, text='確認', width=10)
    Tb = tk.Entry(win, text="", width=15)
    ST = st.ScrolledText(win, width=77, height=35)

    ST.place(x=230, y=30)
    btn1.place(x=50, y=400)
    btn2.place(x=50, y=150)
    entry.place(x=50, y=100)
    for i in range(0,len(twii_result)):
        for j in range(1,9):
            result += str(twii_result[i][j])
            result += '|\t|'
        result += '\r\n'
    ST.insert(tk.INSERT, result)
    win.mainloop()



# tkinter.messagebox.showinfo(title = 'Hello', message = msg)