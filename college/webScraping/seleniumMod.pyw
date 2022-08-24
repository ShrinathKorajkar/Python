from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(ChromeDriverManager().install())
print(type(browser))
browser.get('https://inventwithpython.com')
try:
    # by_css_selector, id, partial_link_text, link_text, name, tag_name
    elem = browser.find_element_by_class_name('card-title')
    print('found %s element with that class name :' % (elem.tag_name))
    print('attribute name : ', elem.get_attribute('class'))
    print('text : ', elem.text)
    print('displayed : ', elem.is_displayed())
    print('enabled : ', elem.is_enabled())
    print('location : ', elem.location)
except:
    print('was not able to find element with that class name')

# Click , Fill , Submit, Special keys

linkElem = browser.find_element_by_partial_link_text('More Info')
print(type(linkElem))
linkElem.click()

browser.get('https://gmail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('shrinathkorajkar@gmail.com')
# passwdElem = browser.find_element_by_id('passwd')
# passwdElem.send_keys('phoenix@246')
emailElem.submit()

browser.get('https://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.HOME)

# Browser buttons
browser.back()
browser.refresh()
browser.forward()
browser.quit()
