from selenium import webdriver
from time import sleep


from time import sleep
class InstaBot:
    def __init__(self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(11)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        #self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        #self.driver.get('https://www.instagram.com/akhil_shalil/')
        sleep(6)

    def get_unfollowers(self):
        self.driver.get('https://www.instagram.com/instausername/')
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]").click()
        following = self._get_names()
        # sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        # self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]").click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        with open('gfg.txt', 'w+') as f:
            # write elements of list
            for items in not_following_back:
                f.write('%s\n' % items)

            print("File written successfully")

        # close the file
        f.close()

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script(
                """arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;""", scroll_box
            )
            sleep(1)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
            .click()
        print("Got names of following")
        return names

my_bot = InstaBot('instausername', 'instapassword')
my_bot.get_unfollowers()
