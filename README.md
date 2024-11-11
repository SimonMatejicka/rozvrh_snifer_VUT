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
```

## Configuration

You need to specify the login credentials for the university portal:

`username`: Your university login.
`password`: Your university password.
Modify these in the display_schedule function:

```python
username = "your_login"
password = "your_password"
```

Additionally, make sure the following URLs are correctly set for your university portal:
```
schedule_url: The URL for the student's schedule.
login_url: The URL for the login page.
```

## Running the Application

To run the application, execute the following command:
```bash
python app.py
```
This will start a local Flask server, typically accessible at http://127.0.0.1:5000/. When you visit the page, your class schedule will be displayed.

## Example Output
The app will display your class schedule in a grid format, using an HTML template provided in the **HTML_TEMPLATE** variable.

## Troubleshooting
Ensure that your WebDriver is compatible with your browser version.
If you encounter login issues, double-check your login credentials.
Ensure that the university portal's structure hasn't changed, as the app relies on specific HTML elements to function.

## License
This project is licensed under the MIT License.

