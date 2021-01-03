from tkinter import *

root = Tk()
root.title('Chat Bot')

root.geometry('400x500')
#menu
main_manu = Menu(root)

file_menu = Menu(root)
file_menu.add_command(label = 'New..')
file_menu.add_command(label='Save As..')
file_menu.add_command(label='Exit')

main_manu.add_cascade(label='File', menu = file_menu)
main_manu.add_command(label='Edit')
main_manu.add_command(label='Quit')
root.config(menu=main_manu)

chatwindow = Text(root, bd=1, bg="black", width = 50, height = 8)
chatwindow.place(x=6, y=6, height= 385, width = 370)

#text
messagewindow = Text(root, bg="black", width = 30, height =4, )
messagewindow.place(x=128, y=400, height= 88, width = 260)


#button
Button = Button(root, text='Send', bg='blue', activebackground='light blue', width= 12, height=5, font=('Arial', 12) )
Button.place(x=6, y=400, height= 88, width= 120)

scrollbar = Scrollbar(root, command=chatwindow.yview())
scrollbar.place(x=375, y=5, height= 385)
root.mainloop()