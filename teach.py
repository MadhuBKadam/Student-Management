import tkinter as tk
import mysql.connector

# connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="system",
  database="studentdata"
  
)

# create the table if it does not exist
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS subjects (id INT AUTO_INCREMENT PRIMARY KEY, topic VARCHAR(255))")

# function to insert a new subject into the database
def add_subject():
    topic = topic_entry.get()
    sql = "INSERT INTO subjects (topic) VALUES (%s)"
    val = (topic,)
    mycursor.execute(sql, val)
    mydb.commit()
    topic_entry.delete(0, tk.END)
    show_subjects()

# function to display all subjects from the database on the screen
def show_subjects():
    mycursor.execute("SELECT * FROM subjects")
    subjects = mycursor.fetchall()
    subject_listbox.delete(0, tk.END)
    for subject in subjects:
        subject_listbox.insert(tk.END, subject[1])

# create the tkinter window and widgets
root = tk.Tk()
root.title("Subject Topics")
root.configure(bg='peach puff')
root.geometry('1174x680+0+0')
root.resizable(0,0)


topic_label = tk.Label(root, text="Enter a new subject topic:")
topic_entry = tk.Entry(root, width=50)
add_button = tk.Button(root, text="Add", command=add_subject)
subject_listbox = tk.Listbox(root, width=50)
show_subjects()

topic_label.pack()
topic_entry.pack()
add_button.pack()
subject_listbox.pack()

root.mainloop()
