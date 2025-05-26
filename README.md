# Selenium Tutorial

This repository contains sample code and resources for learning Selenium, a popular tool for automating web browsers.

## Project Overview

## 1. Google Search Automation using Selenium

This script demonstrates how to automate a Google search using Python and Selenium. It performs the following steps:

1. Opens Google in a Chrome browser
2. Waits for the search input box to appear
3. Enters a search query (e.g., `"Selenium"`)
4. Submits the search
5. Waits for search results to load
6. Clicks the first link containing the word `"Selenium"`

## 2. Locaters - TAG NAME

This is a simple Python automation script that uses Selenium WebDriver to locate an element using their Tag Names :

- Launch Chrome
- Navigate to [Test Automation Practice Blog](https://testautomationpractice.blogspot.com/)
- Maximize the browser window
- Count the number of `<input>` elements on the page
- Print the count in the console

## 3. Locaters - CSS SELECTORS

This is a simple Python automation script that uses **Selenium WebDriver** to demonstrate how to locate elements using **CSS Selectors**.

- Launches the **Google Chrome** browser
- Navigates to [Facebook](https://www.facebook.com/)
- Maximizes the browser window
- Uses **CSS Selectors** to:
  - Enter a name in the **email input field** using `input#email`
  - Enter a password in the **second input field** with class `inputtext`
- Waits for 10 seconds before quitting


---


Install Selenium:

```bash
pip install selenium


2. 

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd selenium_tut
    ```

2. **Install dependencies:**
    - Make sure you have Python and pip installed.
    - Install Selenium:
      ```bash
      pip install selenium
      ```

3. **WebDriver Setup:**
    - Download the appropriate WebDriver (e.g., ChromeDriver, GeckoDriver) and add it to your system PATH.

## Usage

- Run the example scripts to see Selenium in action:
  ```bash
  python <script_name>.py
  ```

## Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [WebDriver Downloads](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

