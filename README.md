# Footer Automation Tests

Автоматизированный проект для проверки футера на страницах сайта **only.digital**.  
Тесты проверяют наличие футера, его видимость, основные элементы и корректность ключевых ссылок.

---

##  Используемые технологии

Проект написан на **Python** и использует следующие технологии:

- **Pytest**  
- **Selenium WebDriver**    
- **Chrome / ChromeDriver**  
- **Headless** 
- **WebDriverWait + Expected Conditions** 

---

##  Тестируемые страницы

    "https://only.digital/",
    "https://only.digital/company",
    "https://only.digital/fields",
    "https://only.digital/job",
    "https://only.digital/blog",
    "https://only.digital/contacts"


## На каждой странице выполняется набор проверок:

### 1. Проверка наличия футера (`test_footer_exists`)
- Страница открывается
- Ожидается появление тега `<footer>`
- Проверяем, что футер видимый и доступный

### 2. Проверка наличия ссылок в футере (`test_footer_links`)
- Проверяем все ссылки внутри `<footer>`
- Проверяем наличие обычных HTTP/HTTPS ссылок

### 3. Проверка телефона в футере (`test_footer_phone`)
- Проверяем все `tel:` ссылки
- Проверяем, что телефон указан

### 4. Проверка email в футере (`test_footer_email`)
- Ищем все `mailto:` ссылки
- Проверяем, что email присутствует

### 5. Проверка наличия PDF документов (`test_footer_pdf`)
- Ищем ссылки, содержащие `pdf`
- Проверяем наличие хотя бы одного PDF-файла

---

##  Как запустить проект

###  Установите зависимости

```bash
pip install -r requirements.txt
```
###  Запустите Pytest с HTML-отчетом

```bash
pytest -v --html=report.html --self-contained-html
```
