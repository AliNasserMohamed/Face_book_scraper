import tkinter as tk
from tkinter import *
from selenium import webdriver
import time
import threading
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import pickle
import sys, os


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()

        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#C4C4C4", padx=40, pady=10, width=880, height=500)
        master.geometry("660x400")

        master.title("ID scraper")
        master.resizable(False, False)

        start_header = Label(self, text="Please fill in all fields as required ", bg="#C5C3C3")
        start_header.grid(padx=5, pady=(0, 10), sticky=W, row=0)
        global label1
        frame1 = LabelFrame(self, padx=10, pady=20, bg="#ffffff", borderwidth=0, highlightthickness=0, relief='ridge')
        frame1.grid(padx=5, pady=0, sticky=W, row=1)
        frame11 = LabelFrame(frame1, padx=0, pady=5, bg="#ffffff", borderwidth=0, highlightthickness=0, relief='ridge')
        frame11.grid(row=0, column=0, padx=(0, 20), pady=10, )
        frame12 = LabelFrame(frame1, padx=0, pady=0, bg="#ffffff", borderwidth=0, highlightthickness=0, relief='ridge')
        frame12.grid(row=0, column=1)
        frame13 = LabelFrame(self, padx=20, pady=0, bg="#ffffff", borderwidth=0, highlightthickness=0, relief='ridge')
        frame13.grid(row=2, column=0, padx=0, pady=0)
        label1 = Label(frame11, text="please inter your email ", bg="#ffffff")
        label1.grid(row=0, column=0, padx=5, pady=7, sticky=W)
        global my_entry1
        my_entry1 = Entry(frame11, width=50, highlightthickness=1, background="white")

        my_entry1.insert(0, "email")
        my_entry1.configure(state=DISABLED)

        def on_click1(event):
            my_entry1.configure(state=NORMAL)
            my_entry1.delete(0, END)
            # make the callback only work once
            my_entry1.unbind('<Button-1>', on_click_id)

        on_click_id = my_entry1.bind('<Button-1>', on_click1)
        my_entry1.grid(row=1, column=0, padx=5, pady=2, sticky=W, ipadx=70, ipady=5)

        label1 = Label(frame11, text="Please inter your password  ", bg="#ffffff")
        label1.grid(row=2, column=0, padx=5, pady=7, sticky=W)
        global my_entry2
        my_entry2 = Entry(frame11, width=50, show="*", highlightthickness=1)
        my_entry2.insert(0, "password")
        my_entry2.configure(state=DISABLED)

        def on_click2(event):
            my_entry2.configure(state=NORMAL)
            my_entry2.delete(0, END)
            # make the callback only work once
            my_entry2.unbind('<Button-1>', on_click_id2)

        on_click_id2 = my_entry2.bind('<Button-1>', on_click2)
        my_entry2.grid(row=3, column=0, padx=5, pady=2, sticky=W, ipadx=70, ipady=5)

        label1 = Label(frame11, text="Please inter the link of post you want   ", bg="#ffffff")
        label1.grid(row=4, column=0, padx=5, pady=7, sticky=W)
        global my_entry3
        my_entry3 = Entry(frame11, width=50, highlightthickness=1)
        my_entry3.insert(0, "post link ")
        my_entry3.configure(state=DISABLED)

        def on_click3(event):
            my_entry3.configure(state=NORMAL)
            my_entry3.delete(0, END)
            # make the callback only work once
            my_entry3.unbind('<Button-1>', on_click_id3)

        on_click_id3 = my_entry3.bind('<Button-1>', on_click3)
        my_entry3.grid(row=5, column=0, padx=5, pady=2, sticky=W, ipadx=70, ipady=5)

        def fill_input_data():
            session_data = {"email": my_entry1.get(), "password": my_entry2.get()
                            }
            pickle.dump(session_data, open("save.p", "wb"))

        def get_data(email,password,link):
            csv_file_all = open("post_links.csv", "w", newline='', encoding="utf-8")
            writer_all = csv.writer(csv_file_all)
            writer_all.writerow(["links"])
            chrome_options = Options()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_experimental_option("prefs", {
                "profile.default_content_setting_values.notifications": 1})
            path = r"chromedriver.exe"
            global driver
            if getattr(sys, "chromedriver.exe", False):
                chromedriver_path = (os.path.join(sys._MEIPASS, "chromedriver.exe"))
                webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver_path)
            else:
                 driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)
            """chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
            driver = webdriver.Chrome(path, chrome_options=chrome_options)"""

            driver.get("https://www.facebook.com/")
            time.sleep(2)
            driver.find_element_by_id("email").send_keys(email)
            driver.find_element_by_id("pass").send_keys(password)
            time.sleep(1)
            driver.find_element_by_name("login").click()
            time.sleep(3)
            driver.get(link)
            time.sleep(5)
            try:
                reacts = driver.find_element_by_class_name(
                    "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l gmql0nx0 ce9h75a5 ni8dbmo4 stjgntxs".replace(
                        " ", "."))
            except:
                reacts = driver.find_element_by_class_name(
                    "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l gmql0nx0 ni8dbmo4 stjgntxs".replace(
                        " ", "."))
            print(reacts.text)
            reacts.click()
            time.sleep(5)
            actions = ActionChains(driver)
            checker = True
            counter = 0
            asss = driver.find_element_by_class_name(
                "q5bimw55 rpm2j7zs k7i0oixp gvuykj2m j83agx80 cbu4d94t ni8dbmo4 eg9m0zos l9j0dhe7 du4w35lb ofs802cu "
                "pohlnb88 "
                "dkue75c7 mb9wzai9 l56l04vs r57mb794 kh7kg01d c3g1iek1 otl40fxz cxgpxx05 rz4wbd8a sj5x9vvc a8nywdso".replace(
                    " ", ".")).find_elements_by_class_name(
                "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 "
                "oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 "
                "lrazzd5p".replace(
                    " ", "."))
            while checker:
                counter += 1
                actions.send_keys(Keys.PAGE_DOWN).perform()
                time.sleep(2.5)
                asss = driver.find_element_by_class_name(
                    "q5bimw55 rpm2j7zs k7i0oixp gvuykj2m j83agx80 cbu4d94t ni8dbmo4 eg9m0zos l9j0dhe7 du4w35lb ofs802cu "
                    "pohlnb88 dkue75c7 mb9wzai9 l56l04vs r57mb794 kh7kg01d c3g1iek1 otl40fxz cxgpxx05 rz4wbd8a sj5x9vvc "
                    "a8nywdso".replace(
                        " ", ".")).find_elements_by_class_name(
                    "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o "
                    "kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr "
                    "f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p".replace(
                        " ", "."))
                if counter % 4 == 0:
                    if len(asss) == last_ass:
                        checker = False
                        print("stopeed after while")
                last_ass = len(asss)
            links = [a.get_attribute("href") for a in asss]
            print(len(links))
            for link in links:
                link = link.split("__")[0][0:-1]
                # link = link.replace("?", "")
                if "id=" in link:
                    link = link + "&sk=friends"
                else:
                    link = link + "/friends"
                driver.get(link)
                time.sleep(2)
                try:
                    friends_as = driver.find_element_by_class_name(
                        "j83agx80 btwxx1t3 lhclo0ds i1fnvgqd".replace(" ", ".")).find_elements_by_tag_name("a")

                    friend_count = 0
                    friend_checker = True
                    while friend_checker:
                        friend_count += 1
                        actions.send_keys(Keys.PAGE_DOWN).perform()
                        time.sleep(2)
                        friends_as = driver.find_element_by_class_name(
                            "j83agx80 btwxx1t3 lhclo0ds i1fnvgqd".replace(" ", ".")).find_elements_by_tag_name("a")

                        if friend_count % 4 == 0:
                            if len(friends_as) == last_friends:
                                friend_checker = False
                        last_friends = len(friends_as)
                    friends = [a.get_attribute("href") for a in friends_as]
                    print("friends", len(friends_as))
                    friends=list(tuple(friends))
                    taken_friends=[]
                    for friend in friends:
                        friend=friend.replace("https://www.facebook.com/","")
                        if "/" not in friend:
                            friend = friend.replace("profile.php?", "")
                            friend = friend.replace("profile.php", "")
                            friend = friend.replace("&", "")
                            friend = friend.replace("?", "")
                            friend = friend.replace("id=", "")
                            if friend not in taken_friends:
                                taken_friends.append(friend)
                                writer_all.writerow([friend])
                except:
                    pass
                link=link.split("__cft")[0].replace("https://www.facebook.com/","")
                link=link.replace("profile.php?","")
                link = link.replace("profile.php", "")
                link = link.replace("&", "")
                link = link.replace("?", "")
                link = link.replace("id=", "")
                writer_all.writerow([link])

            driver.quit()
        def auto_fill():
            my_entry1.configure(state=NORMAL)
            my_entry2.configure(state=NORMAL)
            my_entry3.configure(state=NORMAL)

            my_entry1.delete(0, END)
            my_entry2.delete(0, END)


            # f=open("data.txt","r")
            # data_items=f.read()
            # data_items=data_items.split("\n")
            try:
                session_data = pickle.load(open("save.p", "rb"))
                my_entry1.insert(0, session_data["email"])
                my_entry2.insert(0, session_data["password"])


            except:
                pass
            print("we reached end of function auto_fill")
            print("we are printing my_entry_1", my_entry1.get())

        def running_function():
            s1 = threading.Thread(target=get_data, args=[my_entry1.get(), my_entry2.get(), my_entry3.get()])
            s1.start()

        def stop():
            driver.quit()

        remember_button = Checkbutton(frame13, text="remember me", command=fill_input_data, bg="#ffffff")
        remember_button.grid(row=0, column=0, padx=5, pady=2, sticky=W, ipadx=5, ipady=5)

        auto_button = Button(frame13, text="Auto fill", command=auto_fill, bg="#FFD45B", borderwidth=2,
                             highlightthickness=0, relief='ridge')
        auto_button.grid(row=0, column=1, padx=5, sticky=E, pady=2, ipadx=30, ipady=5)

        start_button = Button(frame13, text="start", command=running_function, bg="#35A11B",
                              borderwidth=2, highlightthickness=0, relief='ridge')
        start_button.grid(row=0, column=2, padx=5, pady=2, sticky=E, ipadx=40, ipady=5)

        delete_button = Button(frame13, text="stop program", command=stop, bg="#FFD45B", borderwidth=2,
                               highlightthickness=0, relief='ridge')

        delete_button.grid(row=0, column=3, padx=0, pady=2, sticky='NSEW', ipadx=5, ipady=5)

        footer = Label(self, text="All rights reserved to Ali_Nasser foundation 2021-2022", bg="#C5C3C3")
        footer.grid(row=3, column=0, padx=5, pady=(10, 0), sticky=W)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

