import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import os

from selenium.webdriver.chrome.options import Options



# Streamlit app for webpage URL input and screenshot capture
def app():
    st.title("Webpage Screenshot Capture")

    # Get the user input for the website URL
    url = st.text_input("Please enter the website URL:")

    if st.button("Capture Screenshot"):
        try:
            # Set up Selenium webdriver
            path = os.path.join(os.getcwd(), 'C:\\Users\\KIIT\\Desktop\\webSS\\chromedriver-win64\\chromedriver.exe')  # Replace with the path to your chromedriver
            service = Service(executable_path=path)
            browser = webdriver.Chrome(service=service)
            options = Options()
            options.headless = True
            browser = webdriver.Chrome(service=service, options=options)

            # Navigate to the website
            browser.get(url)

            # Save the screenshot
            screenshot_path = os.path.join(os.getcwd(), "screenshot.png")
            browser.save_screenshot(screenshot_path)
            st.success(f"Screenshot saved at: {screenshot_path}")

            # Display the screenshot in the app
            st.image(screenshot_path, caption="Screenshot", use_column_width=True)

            # Close the browser
            browser.quit()

        except WebDriverException as e:
            st.error(f"Error: {str(e)}")
            st.error("Please enter a valid URL.")

    # Allow the user to input more URLs
    more_urls = st.button("Enter another URL")
    if more_urls:
        st.session_state.clear()

if __name__ == "__main__":
    app()