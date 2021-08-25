The UI framework is implemented using Page object modeling and can run tests parallelly in Chrome and Firefox browser for the Orbitz Flight booking website.

The tests directory has a test file with two test cases:
1. Verifying the search result in Chrome and Firefox browsers
2. Verifying all flight details and Prices in Chrome and Firefox browsers

Steps to Run tets:
1. git clone https://github.com/NamrathaKRao/OrbitzFlightSearchUIAutomation.git
2. Within the OrbitzFlightSearchUIAutomation directory run: pip3 freeze > requirements.txt
3. Running Tests:
   1. To run tests in parallel : pytest -s -v tests/ -n 2 --html=report.html
   2. To run tests one by one: pytest -s -v tests/ --html=report.html
4. Logs can be checked in the automation.log file that gets generated once the test is run
5. Test case report can be viewed by opening report.html file that gets generated once the test is run in any of the browsers




