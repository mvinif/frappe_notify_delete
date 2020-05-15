
# Doc delete monitoring in Frappe/ERPNext

This method is a simple way to keep monitoring which file was deleted and by whom, also providing the deleted information

## Usage
To ideal usage of this method, firstly we need :

 - Setup a default outgoing email account in Frappe configuration
 - Configure hook.py file
 - Insert main.py in frappe app
 - Configure which doctypes are going be monitored inside the file main.py
 
After the configuration the method runs automatically once someone made a change
 
 ## Functionality
 Each deleted trigger the function, which verify if the doctype is in monitored list, once validated, the method send the e-mail notification
