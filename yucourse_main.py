import selenium as selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from tkinter import *
import tkinter.messagebox
import tkinter as tk
import time


class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        # Fields
        self.master = master
        self.username_label = None
        self.username_entry = None
        self.password_label = None
        self.password_entry = None
        self.coursecode_label = None
        self.coursecode_entry = None
        self.addcourse_button = None
        self.quit_button = None

        self.u = tk.StringVar()
        self.p = tk.StringVar()
        self.c = tk.StringVar()  # login info

        # Methods
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.username_label = tk.Label(self, text='YorkU Username: ', font=('Calibri', 13))
        self.username_label.grid(row=0, column=0)

        self.username_entry = tk.Entry(self, textvariable=self.u, font=('Calibri', 13))
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self, text='Password: ', font=('Calibri', 13))
        self.password_label.grid(row=1, column=0)

        self.password_entry = tk.Entry(self, textvariable=self.p, font=('Calibri', 13))
        self.password_entry.grid(row=1, column=1)

        self.coursecode_label = tk.Label(self, text='Courses to add: ', font=('Calibri', 13))
        self.coursecode_label.grid(row=2, column=0)

        self.coursecode_entry = tk.Entry(self, textvariable=self.c, font=('Calibri', 13))
        self.coursecode_entry.grid(row=2, column=1)
        
        self.addcourse_button = tk.Button(self)
        self.addcourse_button["text"] = "Add"
        self.addcourse_button["command"] = main
        self.addcourse_button.grid(row=3, column=0)

        self.quit_button = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit_button.grid(row=3, column=1)

    def get_username(self):
        return self.u.get()

    def get_password(self):
        return self.p.get()

    def get_coursecodes(self):
        return self.c.get()

# print(app.get_coursecodes())

# OOP GUI IS OVER


class BrowserApp(webdriver.Chrome):
    def __init__(self, username, password, coursecode):
        super().__init__()

        # Fields
        self.username = username
        self.password = password
        self.coursecode = coursecode

        # Methods
        self.get('https://wrem.sis.yorku.ca/Apps/WebObjects/REM.woa/wa/DirectAction/rem')

    def login_york(self):
        username_entry = self.find_element_by_id('mli')
        password_entry = self.find_element_by_id('password')
        login_button = self.find_element_by_name('dologin')
        username_entry.send_keys(self.username)
        password_entry.send_keys(self.password)
        login_button.click()
        wait = WebDriverWait(self, 10)
        wait.until(EC.presence_of_element_located((By.NAME, r'5.5.1.27.1.13')))
        Select(self.find_element_by_name('5.5.1.27.1.11.0')).select_by_value('3')
        self.find_element_by_name('5.5.1.27.1.13').click()

    def add_course(self):
        self.find_element_by_xpath(r'/html/body/form/div[1]/table/tbody/tr[4]'
                                   r'/td[2]/table/tbody/tr/td/table[4]/tbody/tr[1]/td[1]/div/input').click()

    # Now input the course code
        self.find_element_by_xpath(r'/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/span[2]/input[1]').send_keys(self.coursecode)
        self.find_element_by_xpath(r'/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/span[2]/input[2]').click()
        self.find_elements_by_tag_name('input')[2].click()
        time.sleep(5)  # To see if added or not

    # After not being added
        self.find_element_by_name('5.1.27.27.9').click()


def main():
    driver = BrowserApp(app.get_username(), app.get_password(), app.get_coursecodes())
    try:
        driver.login_york()
        driver.add_course()
    except selenium.common.exceptions.WebDriverException as ex:
        print(ex)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    app = Application(root)
    app.mainloop()









