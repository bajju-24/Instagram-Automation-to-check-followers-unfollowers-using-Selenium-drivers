from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pas import Password

class InstaBot:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img').click()
        sleep(4)

        self.get_unfollowers()

    def get_unfollowers(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        following = self.get_names()
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        followers = self.get_names()
        notfollowing= [user for user in following if user not in followers]
        followingfollowers= [user for user in followers if user not in following]

        print(len(notfollowing))
        print(notfollowing)
        print(len(followingfollowers))
        print(followingfollowers)


    def get_names(self):
        sleep(1)
        sugs= self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div')
        self.driver.execute_script('arguments[0].scrollIntoView()',sugs)
        sleep(1)
        last_ht,ht =0,1
        while last_ht!=ht:
            last_ht=ht
            sleep(1)
            scrollbox= self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
            ht= self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """,scrollbox)
        links = self.driver.find_elements_by_class_name('FPmhX')

        names=[]
        for name in links:
            names.append(name.text)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        return names

#Enter username and password
'''

InstaBot("Username","password")

'''
