import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_weixin():
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "localhost:9222"
        #self.driver = webdriver.Chrome(options=chrome_args)
        self.driver = webdriver.Chrome()



    def teardown_method(self):
        self.driver.quit()

    def test_cookie(self):
        # self.driver.get('https://work.weixin.qq.com/')
        # sleep(10)
        # cookies = self.driver.get_cookies()
        # with open('cookie.json','w') as f:
        #     json.dump(cookies,f)
        #     print(cookies)
        self.driver.get("https://work.weixin.qq.com/")
        with open('cookie.json','r') as f:
            cookies = json.load(f)
            #print(cookies)
        for cookie in cookies:
         self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.XPATH,'//*[@id="menu_customer"]/span').click()

    # def test_s(self):
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
    #     self.driver.find_element(By.XPATH,'//*[@id="menu_customer"]/span').click()
    #     self.driver.close()