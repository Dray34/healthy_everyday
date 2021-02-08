#!/home/fang/anaconda3/bin/python
# -*- coding: utf-8 -*-
import os
import random
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 随机选择列表中的一项
def click_select_list(my_driver, data_id, answer_position):
    wait = WebDriverWait(my_driver, 60)
    main_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-id='%s'][1]" % (data_id,))))
    my_driver.execute_script("arguments[0].click();", main_button)
    list_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-id='%s']/..//li[@rel='%d']/a" % (data_id, answer_position))))
    my_driver.execute_script("arguments[0].click();", list_item)


def upload(username, password):
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')

    # login
    driver = webdriver.Chrome(options=option)
    # 打开网址，未登录，跳转到数字北林登陆
    driver.get(address)
    wait = WebDriverWait(driver, 60)
    # 输入账号密码登陆
    elem = driver.find_element_by_id('un')
    elem.send_keys(username)
    elem = driver.find_element_by_id('pd')
    elem.send_keys(password)
    # 从文件中读出的password末尾自带空格，不需要点击登陆按钮
    elem = wait.until(EC.element_to_be_clickable((By.ID, 'index_login_btn')))
    elem.click()
    driver.implicitly_wait(2)

    # 登陆成功，重新打开报平安网址
    driver.get(address)

    wait.until(EC.frame_to_be_available_and_switch_to_it('formIframe'))

    # 随机选择一个体温
    click_select_list(driver, "TW1", 1)
    click_select_list(driver, "TW2", 1)
    click_select_list(driver, "TW3", 1)

    click_select_list(driver, "TW1", random.randint(2, 6))
    click_select_list(driver, "TW2", random.randint(2, 6))
    click_select_list(driver, "TW3", random.randint(2, 6))

    driver.switch_to.default_content()

    commit = wait.until(EC.element_to_be_clickable((By.ID, 'commit')))
    commit.click()
    driver.close()


if __name__ == '__main__':
    address = 'https://s.bjfu.edu.cn/tp_fp/view?m=fp#from=hall&serveID=99f0cf19-3ca4-4786-badb-521f0f734cad&act=fp/serveapply'
    username = os.environ.get('ACTION_USERNAME')
    password = os.environ.get('ACTION_PASSWORD')
    print(datetime.today())
    try:
        upload(username, password)
        print(username + "uploaded")
    except UnexpectedAlertPresentException:
        print(username + "had uploaded")
