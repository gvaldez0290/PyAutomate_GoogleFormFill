# Google Form Auto-Filler

Automate the process of filling out Google Forms with ease using this Python script. This script is a helpful tool for automating repetitive data entry tasks when dealing with Google Forms.

## Use Cases
- Mass Event Registration: Quickly registering multiple participants for events, conferences, or workshops.
- HR Onboarding Processes: Automating the entry of new employee details into various company systems and forms.
- Survey Distribution: Distributing surveys to a large audience without manually entering each recipient.
- Educational Course Enrollment: Enrolling students into new classes or programs in educational institutions.
- Membership Renewals: Processing annual renewals for memberships to organizations or services.
- Marketing Campaigns: Entering potential leads or customer information into CRM platforms from campaign data.
- Data Migration: Transferring data between different systems during software migration or system updates.
- Feedback Collection: Compiling feedback from a large number of users into a centralized form for analysis.
- Your mind is the limit!

## Features

- Opens the Google Form in the default web browser.
- Reads form data from a CSV file, allowing for easy customization.
- Simulates user input to fill out the form fields, including text inputs, dropdown selections, and radio button choices.
- Submits the form and closes the browser window.

## Getting Started

### Prerequisites

To run this script, you need:

- Python 3.x
- pandas (for reading data from a CSV)
- pyautogui (for simulating user input)

You can install the required dependencies using `pip`:

```bash
pip install pandas pyautogui
```

### Usage

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Customize the form data by editing the `form_data.csv` file. Add your own data to match the form fields you want to fill out.

3. Ensure that the browser window is active and the form is loaded before running the script.

4. Run the script:

   ```bash
   python formFiller.py
   ```

   The script will automatically fill out the form based on the data in the CSV file.

## Acknowledgments

This project was adapted from the book "Automate the Boring Stuff with Python" by Al Sweigart. The original concept and code for form filling were inspired by the book.
Changes include opening and closing the browser window, removing the need for user input and also organizing the data into a csv file rather than hardcoding the data. 

## Contributing

Contributions are welcome! If you have any ideas for improvements or bug fixes, please submit an issue or a pull request.
[https://github.com/gvaldez0290/GoogleFormAutoFiller](https://github.com/gvaldez0290/PyAutomate_GoogleFormFill)

## Author
Gerardo "Jerry" Valdez
https://www.linkedin.com/in/gerardov-janusdts/

## Additional Resources

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/chapter20/) by Al Sweigart
- [Python Documentation](https://www.python.org/doc/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [pyautogui Documentation](https://pyautogui.readthedocs.io/en/latest/index.html)
```


