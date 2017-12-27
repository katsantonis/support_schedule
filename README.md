# Support Team tools
## /schedule
  * weekly scheduler
## /timesheets
A simple timesheet exporter In order to be usable by lets say user Adam, do the following configurations inside **config.py**
 * add "Adam" to list users
 * add "Adam" to dictionary calendar_urls with his authorized url.
   * Attention the url for the same calendar is different for each owncloud account, so make sure that **config.py** uses the urls of the account you re about to log in
