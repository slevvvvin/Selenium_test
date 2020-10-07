# PREREQUISTES (INSTALLATIONS)
SELENIUM
CHROMEDRIVER

# USING THE SCRIPT
RUNNING LOCALLY
WHAT YOU WILL SEE

### Install SELENIUM
Selenium is an open source automation tool that uses PYTHON API's to connect to browsers and send commands.

# Run the command below to get selenium
$ pip3 install selenium

### Install CHROMEDRIVER and set executable in system path
You can use IE, Firefox, etc webdrivers 

# Download the CHROMEDRIVER that is compatible with your version of Chrome at the link below
https://chromedriver.chromium.org/downloads
put the file in the directory: Python / scripts
OR
# Set webdriver executable path
Open terminal and run the command below
$ sudo nano /etc/paths
Enter your password
Add your path to the bottom of the file
Control-x to quit
Y to save
Press enter to confirm

# RUNNING TESTS LOCALLY
python3 -m unittest tests.py
