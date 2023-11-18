from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

browser = None


def star_robot():
    global browser
    my_options = webdriver.ChromeOptions()
    my_options.add_argument('--enable-logging')
    browser = webdriver.Chrome(options=my_options)
    browser.get('https://web.whatsapp.com')


def send_message(message):
    chat_box = browser.find_element(By.XPATH,
                                    '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    chat_box.send_keys(message)
    send_button = browser.find_element(By.CLASS_NAME, 'tvf2evcx.oq44ahr5.lb5m6g5c.svlsagor.p2rjqpw5.epia9gcq')
    send_button.click()


def get_messages_out():
    elements = browser.find_elements(By.CLASS_NAME, 'message-out.focusable-list-item._1AOLJ._1jHIY')
    messages = []
    for element in elements:
        try:
            text = element.find_element(By.CLASS_NAME, '_11JPr.selectable-text.copyable-text')
            messages.append(text.text)
        except NoSuchElementException as element:
            pass

    return messages


def get_messages_in():
    elements = browser.find_elements(By.CLASS_NAME, 'message-in.focusable-list-item._1AOLJ._2UtSC._1jHIY')
    messages = []
    for element in elements:
        try:
            text = element.find_element(By.CLASS_NAME, '_11JPr.selectable-text.copyable-text')
            if text.text != 'um segundo, estou procurando uma resposta......':
                messages.append(text.text)
        except NoSuchElementException as element:
            pass

    return messages


def get_last_message():
    last_message = ''
    elements = browser.find_elements(By.CLASS_NAME, 'CzM4m._2zFLj')
    last = elements[len(elements) - 1]

    try:
        last_message = last.find_element(By.CLASS_NAME, '_11JPr.selectable-text.copyable-text').text
    except NoSuchElementException as error:
        pass

    return last_message


def open_read_more():
    elements = browser.find_elements(By.CLASS_NAME, 'o0rubyzf.le5p0ye3.ajgl1lbb.l7jjieqr.read-more-button')
    for element in elements:
        element.click()


def clear_chat():
    triple_dots = browser.find_element(By.XPATH, '//*[@id="main"]/header/div[3]/div/div[3]/div/div/span')
    triple_dots.click()
    clear_option = browser.find_element(By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/div/li[6]/div')
    clear_option.click()
    confirm = browser.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/button[2]')
    confirm.click()