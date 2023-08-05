# coding=utf-8
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

# 运行完成后不退浏览器
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

global browser  # 打开浏览器驱动
browser = webdriver.Chrome(options=options)  # 浏览器对象

browser.implicitly_wait(6)  # 隐身等待

browser.get('https://shiguangpu.com/')  # 打开sk官网

browser.implicitly_wait(6)  # 隐身等待
browser.find_element(By.XPATH, '/html/body/header/div/div[3]/div/div/div[2]/a[2]').click()  # 点击sk网页版


def read_lines_from_file(filename, start_line, end_line):
    with open(filename, 'r') as file:
        lines = file.readlines()[start_line - 1:end_line]
    return lines


def main():
    zhanghao_file = '登录账号.txt'
    target_file = '用户名.txt'
    lines_per_account = 15  # 发送多少个用户

    with open(zhanghao_file, 'r') as zhanghao:
        accounts = zhanghao.readlines()

    for i, account in enumerate(accounts):
        account = account.strip()
        start_line = i * lines_per_account + 1
        end_line = (i + 1) * lines_per_account
        account_data = read_lines_from_file(target_file, start_line, end_line)

        # 获取第二个窗口
        cls = browser.window_handles
        browser.switch_to.window(cls[1])  # 当出现新窗口时，需要控制新的窗口

        # 处理读取到的账号数据
        print(f"账号: {account}")

        account = account.strip()

        # 输入账号密码并点击
        browser.find_element(By.XPATH, '//input[@type="email" and @name="loginfmt"]').send_keys(account)
        browser.find_element(By.XPATH, '//input[@type="submit" and @id="idSIButton9"]').click()
        browser.implicitly_wait(6)  # 隐身等待

        # 密码
        with open('登录密码.txt', 'r', encoding="utf-8") as f1:
            line1 = f1.read()
            browser.find_element(By.XPATH, '//input[@type="password" and @id="i0118"]').send_keys(line1)
            browser.find_element(By.XPATH, '//input[@type="submit" and @value="登录"]').click()
            browser.implicitly_wait(6)  # 隐身等待
        # 点击否
        try:
            browser.find_element(By.XPATH, '//input[@type="button" and @value="否"]').click()
            browser.implicitly_wait(6)

        except:
            browser.find_element(By.ID, 'footerSignout').click()  # 账号被封点击注销
            print(f"账号被封禁或者其它原因：{account}")
            print('\n')
            continue  # 跳出本次循环进入下一个账号

        print("读取的数据:")
        for line in account_data:
            browser.implicitly_wait(10)  # 隐身等待

            # 新建聊天
            browser.find_element(By.XPATH, '//div[contains(@data-text-as-pseudo-element, "新建聊天")]').click()
            browser.find_element(By.XPATH, '//div[@data-text-as-pseudo-element="新建多人会话"]').click()
            time.sleep(2)

            # 输入多人会话群名
            with open('新建群聊名.txt', 'r', encoding="utf-8") as f2:
                line2 = f2.read()
                browser.find_element(By.XPATH, '//input[@aria-label="群组名称: "]').send_keys(line2)
                time.sleep(1)

            # 点击下一个
            browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/button').click()
            time.sleep(1)

            # 读取txt账号输入
            browser.find_element(By.XPATH, '//input[@aria-label="搜索"]').send_keys(line)
            time.sleep(5)

            # 点击搜索到用户
            elements = browser.find_elements(By.XPATH,'//div[@role="none" and @style="position: relative; display: flex; flex-direction: row; flex-grow: 1; flex-shrink: 1; overflow: hidden; align-items: center; background-color: rgba(0, 0, 0, 0);"]')
            # 统计匹配的元素数量
            num_elements = len(elements)
            print(f"共找到 {num_elements} 个匹配的元素。")
            # 点击所有匹配的元素
            for element in elements:
                element.click()
                time.sleep(0.5)

            browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div').click()
            time.sleep(0.5)

            # 点击完成
            browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div/div[3]/button').click()
            time.sleep(5)

            # 点击添加文件
            browser.find_element(By.XPATH, '//button[@title="添加文件"]').click()
            time.sleep(0.5)

            # 使用pyautogui输入文件地址，上传。
            pyautogui.typewrite(r'C:\Users\Administrator\Desktop\v2rayN.lnk')
            pyautogui.press(keys='ENTER', presses=3)  # ENTER 大小写都可以
            time.sleep(0.5)

            # 点击发送
            browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/button/div').click()
            time.sleep(1)

            # 打印输入用户账号
            print(f"发送账号：{line.strip()}")

        print('\n')

        # 退出账号
        browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div[2]/button').click()
        time.sleep(0.5)

        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[3]/button/div').click()
        time.sleep(0.5)

        browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div[1]/div/div[7]/div').click()
        time.sleep(0.5)

        browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[3]/div/div/div[3]/button[2]').click()
        time.sleep(20)
        browser.close()

        ws = browser.window_handles[0]
        browser.switch_to.window(ws)
        browser.refresh()
        time.sleep(1)

        browser.find_element(By.XPATH, '/html/body/header/div/div[3]/div/div/div[2]/a[2]').click()  # 点击sk网页版

    pyautogui.alert(text='完成', title='sk脚本运行状况')


if __name__ == "__main__":
    main()
