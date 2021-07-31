import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


selection = ''
selection = input('f - Firefox\nc - Chrome\n')
if selection == 'f':
    browser = webdriver.Firefox()
elif selection == 'c':
    browser = webdriver.Chrome()
else:
    print('Error')


# ok
def login_to_insta():
    ''' Get username and password from user and login to insta then open Explore page'''

    global browser
    browser.get('https://instagram.com/accounts/login')
    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')
    login_key = browser.find_element_by_class_name('sqdOP')

    username.send_keys(input('Enter username: '))
    password.send_keys(input('Enter password: '))
    login_key.click()
    time.sleep(5)
    browser.get('https://www.instagram.com/explore')


def get_post_urls():
    ''' Generator -> Get urls from visible posts '''
    
    login_to_insta()
    global browser

    anchors = browser.find_elements_by_xpath(".//a")
    urls = [anchor.get_attribute('href') for anchor in anchors]

    print(urls)
    
    finall = []
    for url in urls:
        if 'https://www.instagram.com/p' in url:
            finall.append(url)
        else:
            continue

    print(finall)
    return finall


posts = get_post_urls()
print(posts)

def like_and_comment():
    ''' Like and comment in a specefic page '''

    pass
    # global browser
    # print(posts)
    # browser.get(posts[0])

    # like = browser.find_element_by_class_name('afkep')
    # comment = browser.find_element_by_class_name('Ypffh')
    # post_key = browser.find_element_by_xpath(".//button[@type='submit']")

    # like.click()
    # comment.send_keys('Cool')
    # post_key.click()
    
    # like_and_comment()


if __name__ == "__main__":
    like_and_comment()
