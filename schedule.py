from flask import Flask, render_template_string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time

app = Flask(__name__)

# HTML template for displaying the schedule in a grid format
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Class Schedule</title>
    <link rel="stylesheet" type="text/css" href="https://www.vut.cz/i/www_base/css/rozvrh.css?version=2024-08-31">

    
</head>
<body style="font-family:roboto;">
    {{ schedule|safe }}
</body>
</html>
"""

def fetch_class_schedule(schedule_url, login_url, username, password):
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()  # Ensure the correct WebDriver for your browser is installed
    driver.get(login_url)  # Navigate to the login page

    # Step 1: Enter username and submit
    driver.find_element(By.NAME, "login").send_keys(username)
    driver.find_element(By.NAME, "btnsubmit").click()

    # Wait for the password field to load
    # time.sleep(2)

    # Step 2: Enter password and submit again
    driver.find_element(By.NAME, "passwd").send_keys(password)
    driver.find_element(By.NAME, "btnSubmit").click()

    # Wait for the login process to complete

    # Navigate to the schedule page
    driver.get(schedule_url)

    # Parse page content
    schedule_data = driver.find_elements(By.CLASS_NAME, "rozvrh")[0]
    schedule_data_out = schedule_data.get_attribute('outerHTML')

    driver.quit()
    return schedule_data_out

@app.route('/')
def display_schedule():
    # Define URLs and credentials
    current_date = datetime.now().strftime("%d.%m.%Y")
    schedule_url = f"https://www.vut.cz/studis/student.phtml?sn=osobni_rozvrh&datum_od={current_date}&datum_do=&typ_rozvrhu=2&zobrazit_nadpisy=0&prazdne_dny=0&skryt_detail=0&zvoleny_tyden_form=0&pouze_aktivni=0"
    login_url = "https://id.vut.cz/auth"
    username = "your_login"
    password = "your_password"

    # Fetch the schedule data
    schedule = fetch_class_schedule(schedule_url, login_url, username, password)

    # Render the schedule in the browser
    return render_template_string(HTML_TEMPLATE, schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
