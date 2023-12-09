import time

from selenium.webdriver.common.by import By


def test_button_present(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_displayed(), ("the button must be "
                                                                                              "present on the page")


