import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Список URL страниц, на которых будем проверять футер
URLS = [
    "https://only.digital/",
    "https://only.digital/company",
    "https://only.digital/fields",
    "https://only.digital/job",
    "https://only.digital/blog",
    "https://only.digital/contacts"
]


# ------------------- Фикстура для драйвера -------------------
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


# ------------------- Вспомогательная функция -------------------
def wait_for_footer(driver, timeout=10):
    try:
        wait = WebDriverWait(driver, timeout)
        footer = wait.until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
        driver.execute_script("arguments[0].scrollIntoView(true);", footer)
        return footer
    except TimeoutException:
        pytest.fail("Футер не появился на странице после ожидания")


# ------------------- Тесты -------------------

@pytest.mark.parametrize("url", URLS)
def test_footer_exists(driver, url):
    driver.get(url)
    footer = wait_for_footer(driver)
    assert footer.is_displayed(), f"Футер найден, но скрыт на странице {url}"


@pytest.mark.parametrize("url", URLS)
def test_footer_links(driver, url):
    driver.get(url)
    footer = wait_for_footer(driver)
    links = footer.find_elements(By.TAG_NAME, "a")
    assert links, f"Футер есть, но ссылок в нем нет на странице {url}"
    normal_links = [a.get_attribute("href") for a in links if
                    a.get_attribute("href") and a.get_attribute("href").startswith("http")]
    assert normal_links, f"Нет обычных http/https ссылок в футере на странице {url}"


@pytest.mark.parametrize("url", URLS)
def test_footer_phone(driver, url):
    driver.get(url)
    footer = wait_for_footer(driver)
    links = footer.find_elements(By.TAG_NAME, "a")
    phone_links = [a.get_attribute("href") for a in links if
                   a.get_attribute("href") and a.get_attribute("href").startswith("tel:")]
    assert phone_links, f"Телефон отсутствует в футере на {url}"

@pytest.mark.parametrize("url", URLS)

def test_footer_email(driver, url):
    driver.get(url)
    footer = wait_for_footer(driver)
    links = footer.find_elements(By.TAG_NAME, "a")
    email_links = [a.get_attribute("href") for a in links if
                   a.get_attribute("href") and a.get_attribute("href").startswith("mailto:")]
    assert email_links, f"Email отсутствует в футере на {url}"


@pytest.mark.parametrize("url", URLS)
def test_footer_pdf(driver, url):

    driver.get(url)
    footer = wait_for_footer(driver)
    links = footer.find_elements(By.TAG_NAME, "a")
    pdf_links = [a.get_attribute("href") for a in links if
                 a.get_attribute("href") and "pdf" in a.get_attribute("href").lower()]
    assert pdf_links, f"PDF файлы отсутствуют в футере на {url}"
