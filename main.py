from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_youtube_channel_country(youtube_channel_url):
    # Set up Selenium WebDriver with the specified options
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')  # Uncomment this to run headless (without GUI)
    options.add_argument('window-size=1920x1080')  # Set window size
    options.add_argument("disable-gpu")  # Disable GPU acceleration
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15)  # Implicitly wait for elements to be ready

    try:
        # Load the YouTube channel page
        driver.get(youtube_channel_url)
        time.sleep(3)  # Allow time for the page to load

        # Click on the "...more" button using the provided XPath
        more_button_xpath = '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-description-preview-view-model/truncated-text/button/span/span'
        more_button = driver.find_element(By.XPATH, more_button_xpath)
        more_button.click()
        time.sleep(1)  # Allow time for the bio to expand

        # Now get the country name from the specific XPath
        country_name_xpath = '//*[@id="additional-info-container"]/table/tbody/tr[8]/td[2]'
        country_name_element = driver.find_element(By.XPATH, country_name_xpath)
        country_name = country_name_element.text.strip()

        return country_name

    except Exception as e:
        return f"Error occurred: {str(e)}"

    finally:
        driver.quit()

# Example usage
youtube_channel_url = 'https://www.youtube.com/@rolexmusic01'  # Replace with the actual channel URL
country = get_youtube_channel_country(youtube_channel_url)
print(f"Country: {country}")
