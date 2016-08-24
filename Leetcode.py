from webutil import Selenium

class Leetcode(Selenium):
    def __init__(self):
        self.url = 'https://leetcode.com/problemset/algorithms/'
        self.head = 'https://leetcode.com'
    def __enter__(self):
        self.driver = self.init()
        self.driver.get(self.url)
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()

    def getAllQuestionLinks(self):
        PL = self.getElementById(self.driver, 'problemList')
        PLbody = self.getElementByTagName(PL, 'tbody')
        a = self.getElementsByTagName(PLbody, 'a')
        return [(elem.text.encode("utf-8") ,elem.get_attribute('href')) for elem in a]

    def login(self):
        BTN = self.getElementByClassName(self.driver, 'btn-default')
        self.clickElement(BTN)
        user = self.getElementById(self.driver, 'id_login')
        user.send_keys('raydai')
        pwd = self.getElementById(self.driver, 'id_password')
        pwd.send_keys('abc123456')
        pwd.submit()

    def toFile(self, links):
        for name, link in links:
            with open('/Users/Ray/Desktop/LeetcodeCrawler/description/'+name+'.txt', 'w+') as f:
                self.driver.get(link)
                description = self.getElementByCss(self.driver, 'meta[name=description]')
                f.write(description.get_attribute('content').encode("utf-8"))

    def toPage(self, links):
        for name, link in links:
            self.driver.get(link)
            self.savePage(self.driver)

with Leetcode() as lc:
    lc.login()
    links = lc.getAllQuestionLinks()
    lc.toPage(links)
