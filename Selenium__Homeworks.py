from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.service import Service
s = Service("C:\\Users\\ACER\\Downloads\\edgedriver_win64\\msedgedriver.exe")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\Users\\ACER\\Downloads\\geckodriver-v0.28.0-win64\\geckodriver.exe",
                               options=options)
driver.get("https://www.demoblaze.com/")
driver.save_screenshot("C:\\Users\\ACER\\Desktop\\scrinshot\\EdgeScreenshot.png")
wait = WebDriverWait(driver, 10)


def edge_web_browser():
    driver1 = webdriver.Edge(service=s)
    driver1.get("https://www.demoblaze.com/")
    driver1.maximize_window()
    driver1.save_screenshot("C:\\Users\\ACER\\Desktop\\FirefoxScreenshot\\New Text Document.png")


def locate_header_elements():
    try:
        header_element = driver.find_element(By.XPATH, '//div[@class="navbar-collapse"]')
        if header_element:
            print("Element is located")
        else:
            print("No Such Element")
    except ValueError:
        print("Check your code again")


def locate_categories():
    categories = driver.find_element(By.CSS_SELECTOR, "a[class='list-group-item']")

    try:
        if categories:
            print("Element is located")
        else:
            print("No Such Element")
    except ValueError:
        print("Check your code again")


def find_highest_price():
    product_elements = driver.find_elements(By.XPATH, '//h4[@class="card-title"]')
    price_elements = driver.find_elements(By.TAG_NAME, "h5")
    list1 = []
    list2 = []
    for product in product_elements:
        list1.append(product.text)
    print(list1[1])
    for price in price_elements:
        list2.append(price.text)
    print(max(list2))


wait.until(EC.presence_of_element_located((By.XPATH, '//h4[@class="card-title"]')))


def verify_pages():
    click_phones = driver.find_element(By.XPATH, '//a[contains(text(), "Phones")]')
    click_phones.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//a[contains(text(), "Sony vaio i5")]')))

    verify_phone = driver.find_elements(By.CSS_SELECTOR, 'a[class="hrefch"]')
    length = len(verify_phone)
    assert length == 7, "Your test is fail"
    for phone in verify_phone:
        assert phone.is_displayed(), "Your test is fail"


def verify_laptops():
    laptops_page = driver.find_element(By.XPATH, '//a[contains(text(), "Laptops")]')
    laptops_page.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'h4[class="card-title"]')))
    find_laptops = driver.find_elements(By.CSS_SELECTOR, 'a[class="hrefch"]')
    laptops_length = len(find_laptops)
    assert laptops_length == 6, "Your test is fail"
    for laptops in find_laptops:
        assert laptops.is_displayed(), "Your test is fail"


def verify_monitors():
    click_monitors = driver.find_element(By.XPATH, '//a[contains(text(), "Monitors")]')
    click_monitors.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'h4[class="card-title"]')))
    find_monitors = driver.find_elements(By.CSS_SELECTOR, 'a[class="hrefch"')
    monitors_length = len(find_monitors)
    assert monitors_length == 2, "Your test is fail"
    for monitors in find_monitors:
        assert monitors.is_displayed(), "Your test is fail"


locate_header_elements()
locate_categories()
find_highest_price()
verify_pages()
verify_laptops()
verify_monitors()
# edge_web_browser()
driver.quit()

