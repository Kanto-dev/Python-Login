from tkinter import *
from tkinter import messagebox
import random
import smtplib
from email.message import EmailMessage

def validate_login():
    username = username_entry.get()
    gmail = gmail_entry.get()
    password = password_entry.get()
    
    if username == "admin" and gmail and password == "fuel":
        messagebox.showinfo("Login Info", "Login Successful")
        otp = generate_otp()
        send_otp_email(otp, gmail)
        root.withdraw()  # Hide the login window
        otp_window(otp)
    elif username == "" or gmail == "" or password == "":
        messagebox.showwarning("Login Info", "Please fill in all fields")
    else:
        messagebox.showwarning("Login Info", "Login Failed")

root = Tk()
root.title("Login Screen")
root.geometry("800x500")

# Centering the login menu
frame = Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(frame, text="Username").grid(row=0, column=0, padx=10, pady=10)
username_entry = Entry(frame)
username_entry.grid(row=0, column=1, padx=10, pady=10)

Label(frame, text="Gmail").grid(row=1, column=0, padx=10, pady=10)
gmail_entry = Entry(frame)
gmail_entry.grid(row=1, column=1, padx=10, pady=10)

Label(frame, text="Password").grid(row=2, column=0, padx=10, pady=10)
password_entry = Entry(frame, show='*')
password_entry.grid(row=2, column=1, padx=10, pady=10)

Button(frame, text="Login", command=validate_login, bg="red", fg="white").grid(row=3, column=1, pady=10)

# OTP generation

def generate_otp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))
    return otp

def send_otp_email(otp, to_email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    from_email = ''
    server.login(from_email, '')

    msg = EmailMessage()
    msg['subject'] = "OTP Verification | Made by LimitedIsListed"
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(username, "Your OTP is: " + otp)

    server.send_message(msg)
    server.quit()

# OTP Window

def otp_window(expected_otp):
    otp_win = Toplevel()
    otp_win.title("OTP Verification")
    otp_win.geometry("400x200")
    
    Label(otp_win, text="Enter OTP").grid(row=0, column=0, padx=10, pady=10)
    otp_entry = Entry(otp_win)
    otp_entry.grid(row=0, column=1, padx=10, pady=10)
    
    def verify_otp():
        entered_otp = otp_entry.get()
        if entered_otp == expected_otp:
            messagebox.showinfo("OTP Info", "OTP Verified Successfully")
            otp_win.destroy()  # Close the OTP window
            root.deiconify()  # Show the main window again if needed
        else:
            messagebox.showwarning("OTP Info", "Invalid OTP")
    
    Button(otp_win, text="Verify OTP", command=verify_otp, bg="blue", fg="white").grid(row=1, column=1, pady=10)

root.mainloop()
