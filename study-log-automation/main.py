from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

driver=webdriver.Chrome()

try:
    driver.get("https://forms.gle/EhLmS1hLNWxgRb296")
    time.sleep(2)

    date=datetime.now().strftime("%d-%m-%Y")
    subject=input("Enter subject: ")
    hours=input("Enter hours studied: ")
    topic=input("Enter topic studied: ")
    notes=input("Enter notes: ")

    #Date
    date_input=driver.find_element(
        By.XPATH,
        "//input[@aria-labelledby='i1 i4']"
    )

    date_input.send_keys(date)

    #Subject
    subject_input=driver.find_element(
        By.XPATH,
        "//input[@aria-labelledby='i6 i9']"
    )

    subject_input.send_keys(subject)

    #Hours studied
    hours_input=driver.find_element(
        By.XPATH,
        "//input[@aria-labelledby='i11 i14']"
    )

    hours_input.send_keys(hours)

    #topic studied
    topic_input=driver.find_element(
        By.XPATH,
        "//input[@aria-labelledby='i16 i19']"
    )
    topic_input.send_keys(topic)

    #notes
    notes_input = driver.find_element(
        By.XPATH,
        "//textarea[@aria-labelledby='i21 i24']"
    )

    notes_input.send_keys(notes)

    #submit
    submit_button=driver.find_element(
        By.XPATH,
        "//div[@role='button' and @aria-label='Submit']"
    )
    submit_button.click()

    time.sleep(3)
finally:
    driver.quit()