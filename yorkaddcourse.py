from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tkinter import *
import tkinter.messagebox
from tkinter import ttk




def main_screen():
    screen = Tk()
    #screen.geometry('300x250')
    screen.title('York University Add Courses')

    username_label = Label(screen, text='YorkU Username: ', font=('Calibri', 13))
    username_label.grid(row=0, sticky=E)
    u = StringVar()
    username_entry = Entry(screen, bg='grey', font=('Calibri', 13), textvariable=u)
    username_entry.grid(row=0, column=1)

    password_label = Label(screen, text='Password: ', font=('Calibri', 13))
    password_label.grid(row=1,  sticky=E)
    p = StringVar()
    password_entry = Entry(screen, bg='grey', font=('Calibri', 13), textvariable=p)
    password_entry.grid(row=1, column=1)




    coursecode1_label = Label(screen, text='Input the course codes: ', font=('Calibri', 13))
    coursecode1_label.grid(row=2, sticky=E)
    c = StringVar()
    coursecode_entry = Entry(screen, bg='grey', font=('Calibri', 13), textvariable=c)
    coursecode_entry.grid(row=2, column=1)
    #SCREEN_LOOP = True

    def login_list():
        loginlist = []
        loginlist.append(u.get())
        loginlist.append(p.get())
        loginlist.append(c.get())
        #screen.destroy()
        #global SCREEN_LOOP
        #SCREEN_LOOP = False
        return loginlist




    coursecode2_label = Label(screen, text='Separate the course codes by a comma (,)', font=('Calibri', 10))
    coursecode2_label.grid(row=3, sticky=E)
    courseadd_button = Button(screen, text='Add Courses', command=login_list())
    courseadd_button.grid(row=3, column=1)

    # login_list()

    # def close_window():
       # screen.destroy()


    # SCREEN_LOOP = True
    # while SCREEN_LOOP:
       # screen.update()
        # screen.update()
    screen.mainloop()

    #courseadd_button['command'] = close_window
    return login_list()



login_list = main_screen()



def main(username = login_list[0], password = login_list[1], course_code = login_list[2]):

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://wrem.sis.yorku.ca/Apps/WebObjects/REM.woa/wa/DirectAction/rem')



    def login_york():
        username_entry = driver.find_element_by_id('mli')
        password_entry = driver.find_element_by_id('password')
        login_button = driver.find_element_by_name('dologin')
        username_entry.send_keys(username)
        password_entry.send_keys(password)
        login_button.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, r'5.5.1.27.1.13')))
        Select(driver.find_element_by_name('5.5.1.27.1.11.0')).select_by_value('3')
        driver.find_element_by_name('5.5.1.27.1.13').click()

    # At this point the driver has logged in and we are on the page to select term
    # Now get the table element and select the correct term

    # Wait for page title
    ### Explicit wait
    #wait = WebDriverWait(driver, 10)
    #wait.until(EC.presence_of_element_located((By.NAME, r'5.5.1.27.1.13')))
    ### Explicit wait



    #Select(driver.find_element_by_name('5.5.1.27.1.11.0')).select_by_value('3')
    #driver.find_element_by_name('5.5.1.27.1.13').click()




    # Now comes the page where we just need to press yes on the radio button (this is optional may skip right to the next step)
    # time.sleep(10)

    # radio_yes = driver.find_element_by_xpath(r'/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/input[1]')
    # radio_yes.click()

    # driver.find_element_by_xpath(r'/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/input[2]').click()

    #


    # Now we are in the module and can add courses here.
    def add_course():
        driver.find_element_by_xpath(r'/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[4]/tbody/tr[1]/td[1]/div/input').click()

    # Now input the course code
        driver.find_element_by_xpath(r'/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/span[2]/input[1]').send_keys(course_code)
        driver.find_element_by_xpath(r'/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/span[2]/input[2]').click()
        driver.find_elements_by_tag_name('input')[2].click()

    # After not being added
        driver.find_element_by_name('5.1.27.27.9').click()

    # Execution of the main method
    login_york()
    add_course()
    # algorithms winter

    main_screen()

# Execution of the program


main()


# main('itfibon', 'Dkarnegy55')





