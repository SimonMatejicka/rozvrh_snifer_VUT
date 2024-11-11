# Class Schedule Scraper and Viewer

This Flask application scrapes the class schedule of a university using Selenium and displays it in a web page. It allows users to log in to the university portal, retrieve their class schedule, and display it in a grid format.

## Features

- **Login to University Portal**: The app uses Selenium to log into the university portal.
- **Class Schedule Display**: After logging in, it fetches the class schedule for the current date and displays it in a grid format.
- **Dynamic Schedule Fetch**: The app retrieves the schedule dynamically based on the current date, so it always shows the latest information.

## Requirements

- Python 3.x
- Flask
- Selenium
- WebDriver (Chrome, Firefox, etc.)

### Install Dependencies

To set up the project, you need to install the required dependencies using `pip`. You can create a virtual environment and install the packages using the following commands:

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install Flask and Selenium
pip install flask selenium
