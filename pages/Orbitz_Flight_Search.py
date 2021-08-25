import time
import re
from datetime import datetime,timedelta
from pytz import timezone
from selenium.webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select
import logging
import utilities.custome_logger as cl


class OrbitzFlightSearch(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _flights_link_text = "Flights"
    _roundtrip_link_text = "Roundtrip"
    _leaving_from_button_xpath = "//button[@data-stid='location-field-leg1-origin-menu-trigger']"
    _going_to_button_xpath = "//button[@data-stid='location-field-leg1-destination-menu-trigger']"
    _leaving_from_input_id = "location-field-leg1-origin"
    _going_to_input_id = "location-field-leg1-destination"
    _departure_cal = "d1-btn"
    _next_month_paging = "//div[@class='uitk-calendar']/div[@class='uitk-flex uitk-flex-justify-content-space-between uitk-date-picker-menu-pagination-container']/button[2]"
    _done_button = "//button[@data-stid='apply-date-picker']"
    _search_button = "//button[contains(text(),'Search')]"
    _showMore_button = "showMoreButton"
    _all_search_rendered_items = "//div[@data-test-id='arrival-departure']"
    _rendred_location_names1 = "//div[@data-test-id='arrival-departure' and contains(text(),'San Fr... (SFO) - New York')]"
    _rendred_location_names2 = "//div[@data-test-id='arrival-departure' and contains(text(),'San Fr... (SFO) - Newark')]"
    _non_stop_filter = "stops-0"
    _sort_dropdown = "listings-sort"
    _select_flight_button = "//button[@data-test-id='select-link']"
    _show_details_button = "//button[contains(text(),'Show details')]"
    _fare_type_select= "//button[@data-test-id='fare-type-select']"
    _continue_button = "//button[contains(text(),'Continue')]"
    _flight_price = "//button[@data-test-id='fare-type-select']/span"
    _Departure_Time = "//div[@data-test-id='departure-coordinate-0']/h3/span[contains(text(),'Departure')]/following-sibling::span"
    _Departure_Location = "//div[@data-test-id='departure-coordinate-0']//p/span"
    _Arrival_Time = "//div[@data-test-id='arrival-coordinate-0']/h3/span[contains(text(),'Arrival')]/following-sibling::span"
    _Arrival_Location = "//div[@data-test-id='arrival-coordinate-0']//p/span"
    _Other_details = "//div[@data-test-id='additional-info-0']/span"

    _Departure_Time0 = "//div[@data-test-id='flight-review-0']/div/div/div/div[@data-test-id='departure-coordinate-0']/h3/span[contains(text(),'Departure')]/following-sibling::span"
    _Departure_Location0 = "//div[@data-test-id='flight-review-0']/div/div/div/div[@data-test-id='departure-coordinate-0']//p/span"
    _Arrival_Time0 = "//div[@data-test-id='flight-review-0']/div/div/div/div[@data-test-id='arrival-coordinate-0']/h3/span[contains(text(),'Arrival')]/following-sibling::span"
    _Arrival_Location0 = "//div[@data-test-id='flight-review-0']/div/div/div/div[@data-test-id='arrival-coordinate-0']//p/span"
    _Other_details0 = "//div[@data-test-id='flight-review-0']/div/div/div/div[@data-test-id='additional-info-0']/span"
    _show_details1 = "//div[@data-test-id='flight-review-0']/div/div[@data-test-id='show-details-link']/button"

    _Departure_Time1 = "//div[@data-test-id='flight-review-1']/div/div/div/div[@data-test-id='departure-coordinate-0']/h3/span[contains(text(),'Departure')]/following-sibling::span"
    _Departure_Location1 = "//div[@data-test-id='flight-review-1']/div/div/div/div[@data-test-id='departure-coordinate-0']//p/span"
    _Arrival_Time1 = "//div[@data-test-id='flight-review-1']/div/div/div/div[@data-test-id='arrival-coordinate-0']/h3/span[contains(text(),'Arrival')]/following-sibling::span"
    _Arrival_Location1 = "//div[@data-test-id='flight-review-1']/div/div/div/div[@data-test-id='arrival-coordinate-0']//p/span"
    _Other_details1 = "//div[@data-test-id='flight-review-1']/div/div/div/div[@data-test-id='additional-info-0']/span"
    _show_details2 = "//div[@data-test-id='flight-review-1']/div/div[@data-test-id='show-details-link']/button"
    _Total_Trip_Cost = "//span[@class='uitk-text uitk-type-500 uitk-type-bold uitk-text-emphasis-theme']"

    def NavigateTo_FligtsTab(self):
        self.waitForElement(self._flights_link_text, locatorType="linktext",timeout=30)
        self.ElementClick(self._flights_link_text,locatorType="linktext")

    def NaviagateTo_RondtripTab(self):
        self.waitForElement(self._roundtrip_link_text, locatorType="linktext",timeout=30)
        self.ElementClick(self._roundtrip_link_text, locatorType="linktext")

    def Enter_to_Levingfrom(self,leaving_from):
        self.waitForElement(self._leaving_from_button_xpath,locatorType="xpath")
        self.ElementClick(self._leaving_from_button_xpath,locatorType="xpath")
        self.sendKeys(leaving_from,self._leaving_from_input_id)
        self.sendKeys(Keys.ENTER,self._leaving_from_input_id)

    def Enter_to_GoinTo(self, going_to):
        self.waitForElement(self._going_to_button_xpath, locatorType="xpath")
        self.ElementClick(self._going_to_button_xpath, locatorType="xpath")
        self.sendKeys(going_to, self._going_to_input_id)
        self.sendKeys(Keys.ENTER, self._going_to_input_id)

    def ClikOn_DepartureCalendar(self):
        self.waitForElement(self._departure_cal)
        self.ElementClick(self._departure_cal)

    def DateGenerator(self,time_zone,no_days_to_add):
        Current_date_asper_timezone = datetime.now(timezone(time_zone)).date()
        Required_date_of_travel = Current_date_asper_timezone + timedelta(days=no_days_to_add)
        Date_of_Travel = Required_date_of_travel.strftime("%b %-d, %Y")
        return Date_of_Travel

    def PickDeparture_ReturningDate(self,date_picked):
        Flag = False
        #result = self.isElementPresent("//button[@aria-label='Nov 4, 2021']",locatorType="xpath")
        while Flag == False:
            result = self.isElementPresent("//button[@aria-label='"+date_picked+"']", locatorType="xpath")
            result1 = self.isElementPresent("//button[@aria-label='"+date_picked+" selected, current check in date.']", locatorType="xpath")
            if result == True:
                    self.ElementClick("//button[@aria-label='"+date_picked+"']",locatorType="xpath")
                    Flag = True
            elif result1 == True:
                    self.ElementClick("//button[@aria-label='"+date_picked+" selected, current check in date.']",locatorType="xpath")
                    Flag = True
            else:
                self.ElementClick(self._next_month_paging,locatorType="xpath")

    def ClickOn_Done(self):
        self.waitForElement(self._done_button,locatorType="xpath")
        self.ElementClick(self._done_button,locatorType='xpath')

    def ClickOn_Search(self):
        self.waitForElement(self._search_button, locatorType="xpath")
        self.ElementClick(self._search_button, locatorType='xpath')

    def ClickOn_ShowMore(self):
        self.waitForElement(self._showMore_button,locatorType="name")
        self.ElementClick(self._showMore_button,locatorType="name")

    def SelectFilter_NonStop(self):
        self.waitForElement(self._non_stop_filter)
        self.ElementClick(self._non_stop_filter)

    def SelectSortBy(self,option_text):
        select = Select(self.getElement(self._sort_dropdown))
        select.select_by_visible_text(option_text)

    def SelectFirstFlightInList(self):
        self.waitForElement(self._select_flight_button,locatorType="xpath")
        time.sleep(2)
        self.ElementClick(self._select_flight_button,locatorType="xpath")

    def ClickOn_ShowDetailsButton(self):
        self.waitForElement(self._show_details_button, locatorType="xpath")
        self.ElementClick(self._show_details_button, locatorType="xpath")

    def ClickOn_Continue(self):
        self.ElementClick(self._fare_type_select,locatorType="xpath")
        self.waitForElement(self._continue_button,locatorType="xpath")
        self.ElementClick(self._continue_button,locatorType="xpath")

    def getPriceDetails_DetailsScreen(self):
        flight_price = self.getText(self._flight_price,locatorType="xpath")
        flight_price =  re.sub("[^0-9.]", "", flight_price)
        return flight_price

    def getFlightTimings_Details(self):
        FlightDepartureTime = self.getText(self._Departure_Time, locatorType="xpath")
        FlightDepartureLocation = self.getText(self._Departure_Location, locatorType="xpath")
        FlightArrivalTime = self.getText(self._Arrival_Time, locatorType="xpath")
        FlightArrivalLocation = self.getText(self._Arrival_Location, locatorType="xpath")
        return FlightDepartureTime,FlightDepartureLocation,FlightArrivalTime,FlightArrivalLocation


    def getOtherFlightDetails(self):
        Flight_deatils = self.GetElements(self._Other_details,locatorType="xpath")
        Flight_details_text = [fd.text for fd in Flight_deatils]
        Flight_duration = Flight_details_text[0]
        Airlines_name = Flight_details_text[1]
        Seat_type = Flight_details_text[2]
        return Flight_duration,Airlines_name,Seat_type

    def getFlightTimings_Details1_PaymentScreen(self):
        self.waitForElement(self._show_details1, locatorType="xpath")
        self.ElementClick(self._show_details1, locatorType="xpath")
        FlightDepartureTime = self.getText(self._Departure_Time0, locatorType="xpath")
        FlightDepartureLocation = self.getText(self._Departure_Location0, locatorType="xpath")
        FlightArrivalTime = self.getText(self._Arrival_Time0, locatorType="xpath")
        FlightArrivalLocation = self.getText(self._Arrival_Location0, locatorType="xpath")
        return FlightDepartureTime, FlightDepartureLocation, FlightArrivalTime, FlightArrivalLocation

    def getOtherFlightDetails1_PaymentScreen(self):
        self.waitForElement(self._Other_details0, locatorType="xpath")
        Flight_deatils = self.GetElements(self._Other_details0, locatorType="xpath")
        Flight_details_text = [fd.text for fd in Flight_deatils]
        Flight_duration = Flight_details_text[0]
        Airlines_name = Flight_details_text[1]
        Seat_type = Flight_details_text[2]
        return Flight_duration, Airlines_name, Seat_type

    def getFlightTimings_Details2_PaymentScreen(self):
        self.waitForElement(self._show_details2, locatorType="xpath")
        self.ElementClick(self._show_details2, locatorType="xpath")
        FlightDepartureTime = self.getText(self._Departure_Time1, locatorType="xpath")
        FlightDepartureLocation = self.getText(self._Departure_Location1, locatorType="xpath")
        FlightArrivalTime = self.getText(self._Arrival_Time1, locatorType="xpath")
        FlightArrivalLocation = self.getText(self._Arrival_Location1, locatorType="xpath")
        return FlightDepartureTime, FlightDepartureLocation, FlightArrivalTime, FlightArrivalLocation

    def getOtherFlightDetails2_PaymentScreen(self):
        Flight_deatils = self.GetElements(self._Other_details1, locatorType="xpath")
        Flight_details_text = [fd.text for fd in Flight_deatils]
        Flight_duration = Flight_details_text[0]
        Airlines_name = Flight_details_text[1]
        Seat_type = Flight_details_text[2]
        return Flight_duration, Airlines_name, Seat_type

    def getTotalTripPrice_ReviewScreen(self):
        TotalTripPrice = self.getText(self._Total_Trip_Cost,locatorType="xpath")
        return TotalTripPrice

    def VerifyRenderedSearchResults(self):
        self.waitForElementNotToBePresent(self._showMore_button,locatorType="name")
        total_rendered_items_count =len(self.GetElements(self._all_search_rendered_items,locatorType="xpath"))
        search_result_with_location_name = len(self.GetElements(self._rendred_location_names1,locatorType="xpath")) + len(self.GetElements(self._rendred_location_names2,locatorType="xpath"))
        print("Total rendered flights:"+str(total_rendered_items_count))
        print("Flights from San Francisco to New York:"+str(search_result_with_location_name))
        if total_rendered_items_count == search_result_with_location_name :
            return True
        else:
            return False

    def VerifyTotalTrip_Price(self,Flight1_price,Flight2_price):
        TotalTrip_Price_cal = float(Flight1_price) +float(Flight2_price)
        TotalTrip_Price_cal = '{:.2f}'.format(TotalTrip_Price_cal)
        TotalTrip_Price_RevScreen = self.getTotalTripPrice_ReviewScreen()
        print("Total trip cost added from Detail screen: $" + TotalTrip_Price_cal)
        print("Total trip cost from Review screen:" + TotalTrip_Price_RevScreen)
        result = self.VerifyExpected_and_Actual_Result("$"+TotalTrip_Price_cal,TotalTrip_Price_RevScreen)
        return result


















