from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
# change link ,user and password here
username = "01142765209"
password = "Ali29810012408278"
post_link = "https://mbasic.facebook.com/story.php?story_fbid=4158481884273405&id=314471908674441"

path = r"chromedriver.exe"
csv_file_all = open("post_links.csv", "w", newline='', encoding="utf-8")
writer_all = csv.writer(csv_file_all)
writer_all.writerow(["links"])
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)
"""chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
driver = webdriver.Chrome(path, chrome_options=chrome_options)"""


def get_data(link, username, password):
    driver.get("https://www.facebook.com/")
    time.sleep(2)
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("login").click()
    time.sleep(3)
    driver.get(link)
    time.sleep(3)
    print("we get link")
    time.sleep(4)
    comment_profiles = driver.find_element_by_class_name(
        "cwj9ozl2 tvmbv18p".replace(" ", ".")).find_elements_by_tag_name("a")

    comment_checker = True
    comment_counter = 0
    while comment_checker:
        try:
            comment_counter += 1
            more = driver.find_element_by_class_name(
                "oajrlxb2 bp9cbjyn g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 "
                "rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 g5gj957u p7hjln8o "
                "kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys p8fzw8mz qt6c0cv9 a8nywdso l9j0dhe7 "
                "i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh gpro0wi8 m9osqain buofh1pr".replace(
                    " ", "."))
            more.click()
            time.sleep(3)
            comment_profiles = driver.find_element_by_class_name(
                "cwj9ozl2 j83agx80 cbu4d94t buofh1pr d76ob5m9 eg9m0zos du4w35lb".replace(" ",
                                                                                         ".")).find_elements_by_tag_name(
                "a")
        except:
            pass
        if comment_counter % 20 == 0:
            try:
                if len(comment_profiles) == previos_count:
                    comment_checker = False
            except:
                pass
        previos_count = len(comment_profiles)

    comment_profiles = driver.find_element_by_class_name(
        "cwj9ozl2 tvmbv18p".replace(" ", ".")).find_elements_by_tag_name(
        "a")

    comment_links = [a.get_attribute("href") for a in comment_profiles]
    # print("lenght_comment_length", len(comment_links))
    all_comment = []
    written_comments = []
    for c in comment_links:
        if "profile.php?id=" in c:
            # print(c)
            c = c.split("comment")[0]
            #c = c.replace("https://www.facebook.com/", "")
            c = c.replace("profile.php?", "")
            c = c.replace("profile.php", "")
            c = c.replace("&", "")
            c = c.replace("?", "")
            c = c.replace("id=", "")
            c = c.split("__", 0)[0]
            if c not in all_comment and len(c) < 30:
                all_comment.append(c)
                c = re.sub("[^0-9]", "", c)
                writer_all.writerow([c])
        else:
            written_comments.append(c)

    driver.get(link)
    time.sleep(8)
    try:
        reacts = driver.find_element_by_class_name(
            "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 "
            "cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl "
            "l9j0dhe7 abiwlrkh p8dawk7l gmql0nx0 ce9h75a5 ni8dbmo4 stjgntxs".replace(
                " ", "."))
    except:
        reacts = driver.find_element_by_class_name(
            "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 "
            "cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl "
            "l9j0dhe7 abiwlrkh p8dawk7l gmql0nx0 ni8dbmo4 stjgntxs".replace(
                " ", "."))
    # print(reacts.text)
    reacts.click()
    time.sleep(2)
    actions = ActionChains(driver)
    checker = True
    counter = 0
    asss = driver.find_element_by_class_name(
        "q5bimw55 rpm2j7zs k7i0oixp gvuykj2m j83agx80 cbu4d94t ni8dbmo4 eg9m0zos l9j0dhe7 du4w35lb ofs802cu pohlnb88 "
        "dkue75c7 mb9wzai9 l56l04vs r57mb794 kh7kg01d c3g1iek1 otl40fxz cxgpxx05 rz4wbd8a sj5x9vvc a8nywdso".replace(
            " ", ".")).find_elements_by_class_name(
        "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 "
        "oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 "
        "lrazzd5p".replace(
            " ", "."))
    while checker:
        counter += 1
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(0.5)
        asss = driver.find_element_by_class_name(
            "q5bimw55 rpm2j7zs k7i0oixp gvuykj2m j83agx80 cbu4d94t ni8dbmo4 eg9m0zos l9j0dhe7 du4w35lb ofs802cu "
            "pohlnb88 dkue75c7 mb9wzai9 l56l04vs r57mb794 kh7kg01d c3g1iek1 otl40fxz cxgpxx05 rz4wbd8a sj5x9vvc "
            "a8nywdso".replace(
                " ", ".")).find_elements_by_class_name(
            "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 "
            "cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl "
            "oo9gr5id gpro0wi8 lrazzd5p".replace(
                " ", "."))
        if counter % 4 == 0:
            if len(asss) == last_ass:
                checker = False
        last_ass = len(asss)
    links = [a.get_attribute("href") for a in asss]
    # print(len(links))
    for link in links:
        if "profile.php?id=" in link:
            # print(link)
            link = link.split("__")[0].replace("https://www.facebook.com/", "")
            link = link.replace("profile.php?", "")
            link = link.replace("profile.php", "")
            link = link.replace("&", "")
            link = link.replace("?", "")
            link = link.replace("id=", "")
            link=re.sub("[^0-9]", "", link)
            writer_all.writerow([link])
        else:
            written_comments.append(link)
    written_comments = list(tuple(written_comments))
    geted_comments = []
    for written_c in written_comments:
        if "story_fbid=" not in written_c and "photo.php?" not in written_c and written_c[0:30] not in geted_comments:
            driver.get(written_c)
            geted_comments.append(written_c[0:30])
            try:
                page_text = str(driver.page_source)
                id = page_text.split("userID")[1].split("}")[0]
                id = id.replace(":", "")
                id = id.strip()
                id = id.replace('"', "")
                # print("we find id",id)
                if id not in all_comment and len(id) > 11:
                    all_comment.append(id)
                    id = re.sub("[^0-9]", "", id)
                    writer_all.writerow([id])
            except:
                pass


get_data(post_link, username, password)
