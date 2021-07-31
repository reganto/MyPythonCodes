from selenium import webdriver
import time


def post_like():
    '''
    Login to Instagram and load explore page then post and like there
    '''

    selection = ''
    selection = input('f - firefox\nc - chrome\n')
    
    if selection == 'f':
        browser = webdriver.Firefox()
    elif selection == 'c':
        browser = webdriver.Chrome()
    else:
        print('Enter a valid option!')
    
    # login
    browser.get('https://instagram.com/accounts/login')
    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')
    login_btn = browser.find_element_by_class_name('L3NKy')
    username.clear()
    username.send_keys(input('Enter username: '))
    password.send_keys(input('Enter password: '))
    login_btn.click()

    time.sleep(5)

    # go to viral posts
    browser.get('https://instagram.com/explore')

    # SCROLL_PAUSE_TIME = 0.5
    # flag = 'y'
    # while flag == 'y':
    #     browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #     time.sleep(SCROLL_PAUSE_TIME)
    #     flag = input('Continue to load posts(y/n)?')
    time.sleep(5)
    # get posts links
    anchors = browser.find_elements_by_xpath('.//a')
    urls = [anchor.get_attribute('href') for anchor in anchors]

    posts_urls = []
    for url in urls:
        if 'https://instagram.com/p' in url:
            posts_urls.append(url)
        else:
            continue
    
    for url in posts_urls:
        browser.get(url)
        like = browser.find_element_by_class_name('afkep')
        comment = browser.find_element_by_class_name('Ypffh')
        post_btn = browser.find_element_by_xpath(".//button[@type='submit']")

        like.click()
        comment.send_keys('خیلی هم عالی')
        post_btn.click()
