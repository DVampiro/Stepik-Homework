from selenium import webdriver



link = "http://suninjuly.github.io/cats.html"
with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element_by_id("button")

