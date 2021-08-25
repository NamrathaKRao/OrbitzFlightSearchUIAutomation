import time
from ddt import ddt, data, unpack
from utilities.teststatus import Status
import utilities.read_data as rd
from base.selenium_driver import SeleniumDriver
from base.webdriverFactory import WebDriverFactory
import pytest
import unittest
from pages.Orbitz_Flight_Search import OrbitzFlightSearch


@ddt()
@pytest.mark.usefixture("oneTimeSetUp", "setUp")
class OrbitzFlight(unittest.TestCase):


    def MethodSetup(self,browser, url):
        self.wdf = WebDriverFactory()
        driver = self.wdf.getWebDriverInstance(browser, url)
        self.ofs = OrbitzFlightSearch(driver)
        self.ts = Status(driver)
        self.sd = SeleniumDriver(driver)
        return driver

    """This has two tests 
        1.Running on Chrome
        2. Running on firefox"""
    @unpack
    @data(*rd.JSON_Reader("data/JSON_SearchFlights.json", "TS1"))
    def test_TC_01_VerifyFlightSearch(self,browser,url,leaving_from,going_to,time_zone,departure_no_days_fromnow,return_no_days_fromnow):
        driver = self.MethodSetup(browser,url)
        self.ofs.NavigateTo_FligtsTab()
        self.ofs.NaviagateTo_RondtripTab()
        self.ofs.Enter_to_Levingfrom(leaving_from)
        self.ofs.Enter_to_GoinTo(going_to)
        self.ofs.ClikOn_DepartureCalendar()
        Departure_date = self.ofs.DateGenerator(time_zone, departure_no_days_fromnow)
        Return_date = self.ofs.DateGenerator(time_zone, return_no_days_fromnow)
        print("DATEE")
        print(Departure_date)
        print(Return_date)
        self.ofs.PickDeparture_ReturningDate(Departure_date)
        self.ofs.PickDeparture_ReturningDate(Return_date)
        self.ofs.ClickOn_Done()
        self.ofs.ClickOn_Search()
        self.ofs.ClickOn_ShowMore()
        result = self.ofs.VerifyRenderedSearchResults()
        self.ts.markFinal("test_TC_01_VerifyFlightSearch", result, "Count of all rendered searched items matches the count of flights from San Francisco to New York")
        driver.quit()

    """This has two tests 
           1.Running on Chrome
           2. Running on firefox"""
    @unpack
    @data(*rd.JSON_Reader("data/JSON_SearchFlights.json", "TS2"))
    def test_TC_02_VerifyFlightDetails_And_Price(self,browser,url,leaving_from,going_to,time_zone,departure_no_days_fromnow,return_no_days_fromnow,sort_option_flight1,sort_option_flight2):
        driver =  self.MethodSetup(browser,url)
        self.ofs.NavigateTo_FligtsTab()
        self.ofs.NaviagateTo_RondtripTab()
        self.ofs.Enter_to_Levingfrom(leaving_from)
        self.ofs.Enter_to_GoinTo(going_to)
        self.ofs.ClikOn_DepartureCalendar()
        Departure_date = self.ofs.DateGenerator(time_zone, departure_no_days_fromnow)
        Return_date = self.ofs.DateGenerator(time_zone, return_no_days_fromnow)
        print(Departure_date)
        print(Return_date)
        self.ofs.PickDeparture_ReturningDate(Departure_date)
        self.ofs.PickDeparture_ReturningDate(Return_date)
        self.ofs.ClickOn_Done()
        self.ofs.ClickOn_Search()
        self.ofs.SelectFilter_NonStop()
        self.ofs.SelectSortBy(sort_option_flight1)
        self.ofs.SelectFirstFlightInList()
        self.ofs.ClickOn_ShowDetailsButton()
        time.sleep(3)
        """---FLIGHT DETAILS SCREEN"""
        """-----TRIP1-----"""
        F1_DepartureTime_Det,F1_DepartureLocation_Det,F1_ArrivalTime_Det,F1_ArrivalLocation_Det = self.ofs.getFlightTimings_Details()
        F1_duration_Det,F1_AirlinesName_Det,F1_SeatType_Det = self.ofs.getOtherFlightDetails()
        Flight1_price_Det = self.ofs.getPriceDetails_DetailsScreen()
        print(Flight1_price_Det)
        self.ofs.ClickOn_Continue()
        self.ofs.SelectFilter_NonStop()
        self.ofs.SelectSortBy(sort_option_flight2)
        self.ofs.SelectFirstFlightInList()
        self.ofs.ClickOn_ShowDetailsButton()
        """----TRIP2----"""
        F2_DepartureTime_Det,F2_DepartureLocation_Det,F2_ArrivalTime_Det,F2_ArrivalLocation_Det = self.ofs.getFlightTimings_Details()
        F2_duration_Det, F2_AirlinesName_Det, F2_SeatType_Det = self.ofs.getOtherFlightDetails()
        Flight2_price_Det = self.ofs.getPriceDetails_DetailsScreen()
        print(Flight2_price_Det)
        self.ofs.ClickOn_Continue()
        self.sd.SwitchWindow(1)
        """-----REVIEW SCREEN-------"""
        """--TRIP1"""
        F1_DepartureTime_Rev, F1_DepartureLocation_Rev, F1_ArrivalTime_Rev, F1_ArrivalLocation_Rev = self.ofs.getFlightTimings_Details1_PaymentScreen()
        F1_duration_Rev, F1_Airlines_name_Rev, F1_Seat_type_Rev = self.ofs.getOtherFlightDetails1_PaymentScreen()
        """---TRIP 2---"""
        F2_DepartureTime_Rev, F2_DepartureLocation_Rev, F2_ArrivalTime_Rev, F2_ArrivalLocation_Rev = self.ofs.getFlightTimings_Details2_PaymentScreen()
        F2_duration_Rev, F2_Airlines_name_Rev, F2_Seat_type_Rev = self.ofs.getOtherFlightDetails2_PaymentScreen()

        print("DETAILS of FLIGHT1 from DETAILS SCREEN: "+F1_DepartureTime_Det, F1_DepartureLocation_Det, F1_ArrivalTime_Det, F1_ArrivalLocation_Det)
        print(F1_duration_Det, F1_AirlinesName_Det, F1_SeatType_Det)
        print("DETAILS of FLIGHT1 from REVIEW SCREEN :"+F1_DepartureTime_Rev, F1_DepartureLocation_Rev, F1_ArrivalTime_Rev, F1_ArrivalLocation_Rev)
        print(F1_duration_Rev, F1_Airlines_name_Rev, F1_Seat_type_Rev)

        print("DETAILS of FLIGHT2 from DETAILS SCREEN :" + F2_DepartureTime_Det, F2_DepartureLocation_Det,
              F2_ArrivalTime_Det, F2_ArrivalLocation_Det)
        print("DETAILS of FLIGHT2 from REVIEW SCREEN :"+F2_DepartureTime_Rev, F2_DepartureLocation_Rev, F2_ArrivalTime_Rev, F2_ArrivalLocation_Rev)
        print(F2_duration_Rev, F2_Airlines_name_Rev, F2_Seat_type_Rev)

        """---ASSERTION OF FLIGHT1 DETAILS----"""
        Flight1_Departure_Time = self.sd.VerifyExpected_and_Actual_Result(F1_DepartureTime_Det,F1_DepartureTime_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch",Flight1_Departure_Time,"Flight Departure time verified for Flight 1")
        Flight1_Departure_Location = self.sd.VerifyExpected_and_Actual_Result(F1_DepartureLocation_Det, F1_DepartureLocation_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight1_Departure_Location,"Flight Departure location verified for Flight 1")
        Flight1_Arrival_Time = self.sd.VerifyExpected_and_Actual_Result(F1_ArrivalTime_Det,F1_ArrivalTime_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight1_Arrival_Time,
                             "Flight Arrival time verified for Flight 1")
        Flight1_Arrival_Location = self.sd.VerifyExpected_and_Actual_Result(F1_ArrivalLocation_Det,F1_ArrivalLocation_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight1_Arrival_Location,
                             "Flight Arrival location verified for Flight 1")
        Flight1_Duration = self.sd.VerifyExpected_and_Actual_Result(F1_duration_Det,F1_duration_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight1_Duration,
                             "Flight1 Duration verified ")
        Flight1_Airlies_name = self.sd.VerifyExpected_and_Actual_Result(F1_AirlinesName_Det, F1_Airlines_name_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight1_Airlies_name,
                             "Flight1 Airlines name verified ")
        Flight1_SeatType = self.sd.VerifyExpected_and_Actual_Result(F1_SeatType_Det, F1_Seat_type_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight1_SeatType,
                             "Flight1 SeatType verified ")

        """---ASSERTION OF FLIGHT2 DETAILS----"""
        Flight2_Departure_Time = self.sd.VerifyExpected_and_Actual_Result(F2_DepartureTime_Det, F2_DepartureTime_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight2_Departure_Time,
                             "Flight Departure time verified for Flight 2")
        Flight2_Departure_Location = self.sd.VerifyExpected_and_Actual_Result(F2_DepartureLocation_Det,
                                                                              F2_DepartureLocation_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight2_Departure_Location,
                             "Flight Departure location verified for Flight 2")
        Flight2_Arrival_Time = self.sd.VerifyExpected_and_Actual_Result(F2_ArrivalTime_Det, F2_ArrivalTime_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight2_Arrival_Time,
                             "Flight Arrival time verified for Flight 2")
        Flight2_Arrival_Location = self.sd.VerifyExpected_and_Actual_Result(F2_ArrivalLocation_Det,
                                                                            F2_ArrivalLocation_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight2_Arrival_Location,
                             "Flight Arrival location verified for Flight 2")
        Flight2_Duration = self.sd.VerifyExpected_and_Actual_Result(F2_duration_Det, F2_duration_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight2_Duration,
                             "Flight2 Duration verified ")
        Flight2_Airlies_name = self.sd.VerifyExpected_and_Actual_Result(F2_AirlinesName_Det, F2_Airlines_name_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight2_Airlies_name,
                             "Flight2 Airlines name verified ")
        Flight2_SeatType = self.sd.VerifyExpected_and_Actual_Result(F2_SeatType_Det, F2_Seat_type_Rev)
        self.ts.mark_Partial("test_TC_02_VerifyFlightSearch", Flight2_SeatType,
                             "Flight2 SeatType verified ")
        TotalFlight_Price_verify = self.ofs.VerifyTotalTrip_Price(Flight1_price_Det,Flight2_price_Det)
        self.ts.markFinal("test_TC_02_VerifyFlightSearch", TotalFlight_Price_verify,
                             "Total trip cost verified ")
        driver.quit()

