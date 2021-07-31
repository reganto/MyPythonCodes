from selenium import webdriver
from redis import Redis


redis_connection  = Redis('localhost', 6379, 0)

def manage():
    selection = ''
    print('f - for firefox')
    print('c - for chrome\n')
    selection = input()
    if selection == 'f':
        browser = webdriver.Firefox()
    elif selection == 'c':
        browser = webdriver.Chrome()
    else:
        print('Invalid entry')

    
    browser.get('https://instagram.com/accounts/login')
    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')

    username.clear()
    username.send_keys(input('Enter username: '))
    password.clear()
    password.send_keys(input('Enter password: '))

    login_key = browser.find_element_by_class_name('L3NKy')
    login_key.click()

        
    while True:
        browser.get('https://instagram.com/explore')
        anchors = browser.find_elements_by_xpath('.//a')
        urls = [anchor.get_attribute('href') for anchor in anchors]

        # if browser.current_url == 'https://instagram.com/explore':
        #     break

        print(browser.current_url)

   
    i = 0
    for url in urls:
        if 'https://instagram.com/p' in url:
            redis_connection.setex(i, url, 60)
            i += 1
        else:
            continue
        

    while True:
        try:
            for i in range(17):
                url = redis_connection.get(i)
                browser.get(url)
                like = browser.find_element_by_class_name('afkep')
                comment = browser.find_element_by_class_name('Ypffh')
                post_key = browser.find_elements_by_xpath(".//button[@type='submit']")

                like.click()
                comment.send_keys('خیلی هم عالی')
                post_key.click()
        except Exception as e:
            print(e)

manage()