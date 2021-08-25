from datetime import datetime
from base.selenium_driver import SeleniumDriver
import logging
import utilities.custome_logger as cl



class OrbitzFlightSearch(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _account_balance = "acc-balance"
    _past30_days_charges = "past30-days-charges"
    _utility_charge = "utility-charge"
    _last_updated_date = "last-update"
    _account_status_active = "//div[contains(text(),'Active')]"
    _AverageDaily_charge = "avg-daily-charge"
    _AverageDailyUtility_charge = "avg-utility-charge"
    _electric_charge = "electric-charge"
    _ele_last_usage = "ele-last-usage"
    _water_last_usage = "water-last-usage"
    _sewer_last_usage = "sewer-last-usage"
    _ele_past30days_avg = "ele-past30days-avg"
    _water_past30days_avg = "water-past30days-avg"
    _sewer_past30days_avg = "sewer-past30days-avg"
    _ele_last_posted = "ele-last-posted"
    _water_last_posted = "water-last-posted"
    _sewer_last_posted = "sewer-last-posted"
    _electric_charge_um = "ele-last-usage"
    _water_charge_um = "ele-last-usage"
    _water_charge = "water-charge"
    _sewer_charge = "sewer-charge"
    _avg_daily_charge = "avg-daily-charge"
    _unpaid_balance = "unpaid-balance"
    _estimated_days = "estimated_days"
    _estimated_date = "estimated_date"
    _last_payment = "last-payment"
    _last_payment_date = "last-payment-date"

    def WaitFor_AccountSummaryScreen(self):
        self.waitForElement(self._account_status_active, locatorType="xpath")

    def VerifyAccountActive(self):
        result = self.isElementPresent(self._account_status_active, locatorType="xpath")
        return result

    def getAccountBalance_From_AccountSummaryScreen(self):
        Balance_Ammount_summary = self.getText(self._account_balance)
        print(Balance_Ammount_summary)
        return Balance_Ammount_summary

    def getElectricCharge_From_AccountSummaryScreen(self):
        # self.waitForElement(self._electric_charge)
        ElectricCharge = self.getText(self._electric_charge)
        print(ElectricCharge)
        return ElectricCharge

    def getAccountBalance_Past30DaysCharges_UtilityChargeChangedBy_LastUpdatedOn(self):
        UtilityChargeChangedBy = self.getText(self._utility_charge)
        LastUpdatedDate = self.getText(self._last_updated_date)
        Past30DaysCharges = self.getText(self._past30_days_charges)
        return UtilityChargeChangedBy, LastUpdatedDate, Past30DaysCharges

    def getElectricLastUsage_Past30DaysAvg_From_AccountSummaryScreen(self):
        # self.waitForElement(self._electric_charge)
        ElectricLastUsage = self.getText(self._ele_last_usage)
        ElectricPast30DayAvg = self.getText(self._ele_past30days_avg)
        Electric_LastPostedOn = self.getText(self._ele_last_posted)
        return ElectricLastUsage, ElectricPast30DayAvg, Electric_LastPostedOn

    def getWaterLastUsage_Past30DaysAvg_From_AccountSummaryScreen(self):
        # self.waitForElement(self._electric_charge)
        WaterLastUsage = self.getText(self._water_last_usage)
        WaterPast30DaysAvg = self.getText(self._water_past30days_avg)
        Water_LastPostedOn = self.getText(self._water_last_posted)
        return WaterLastUsage, WaterPast30DaysAvg, Water_LastPostedOn

    def getSewerLastUsage_Past30DaysAvg_From_AccountSummaryScreen(self):
        # self.waitForElement(self._electric_charge)
        SewerLastUsage = self.getText(self._sewer_last_usage)
        SewerPast30DaysAvg = self.getText(self._sewer_past30days_avg)
        Sewer_LastPostedOn = self.getText(self._sewer_last_posted)
        return SewerLastUsage, SewerPast30DaysAvg, Sewer_LastPostedOn

    def getElectricCharge_From_AccountSummaryScreenUM_Account(self):
        # self.waitForElement(self._electric_charge)
        ElectricCharge = self.getText(self._electric_charge_um)
        print(ElectricCharge)
        return ElectricCharge

    def getWaterCharge_From_AccountSummaryScreen(self):
        # self.waitForElement(self._water_charge)
        WaterCharge = self.getText(self._water_charge)
        print(WaterCharge)
        return WaterCharge

    def getWaterCharge_From_AccountSummaryScreen_UMAccount(self):
        # self.waitForElement(self._water_charge)
        WaterCharge = self.getText(self._water_charge_um)
        print(WaterCharge)
        return WaterCharge

    def getSewerCharge_From_AccountSummaryScreen(self):
        # self.waitForElement(self._sewer_charge)
        SewerCharge = self.getText(self._sewer_charge)
        print(SewerCharge)
        return SewerCharge

    def getAverageDailyCharge_From_AccountSummaryScreen(self):
        AverageDailyCharge = self.getText(self._AverageDaily_charge)
        print(AverageDailyCharge)
        return AverageDailyCharge

    def getAverageDailyUtilityCharge_From_AccountSummaryScreen(self):
        AverageDailyUtilityCharge = self.getText(self._AverageDailyUtility_charge)
        print(AverageDailyUtilityCharge)
        return AverageDailyUtilityCharge

    def getUnpaidBalance_From_AccountSummaryScreen(self):
        UnpaidBalance = self.getText(self._unpaid_balance)
        print(UnpaidBalance)
        return UnpaidBalance

    def getEstimatedDaysLeft_From_AccountSummaryScreen(self):
        EstimatedDays = self.getText(self._estimated_days)
        EstimatedDays_split = str(EstimatedDays).split()
        EstimatedDays = EstimatedDays_split[0] + " " + EstimatedDays_split[1]
        return EstimatedDays

    def getEstimatedDate_From_AccountSummaryScreen(self):
        EstimatedDate = self.getText(self._estimated_date)
        print(EstimatedDate)
        return EstimatedDate

    def getLastPayment_From_AccountSummaryScreen(self):
        LastPayment = self.getText(self._last_payment)
        print(LastPayment)
        return LastPayment

    def VerifyExpectedAndActual(self, expected, actual):
        result = self.VerifyExpected_and_Actual_Result(expected, actual)
        return result

    def UsagesAmountCalculation(self, account_type="", reading1="", reading2="", Usage_rate_name="",
                                tax_jurisdiction="", service_type="", account_no="", Usage_description="",
                                meter_type=""):
        print("DEBUG")
        print(account_type, reading1, reading2, Usage_rate_name, tax_jurisdiction, service_type, account_no,
              Usage_description)
        print(type(account_no))
        if account_type == "UsageMonitor":
            self.consumption = int(reading2) - int(reading1)
            print("DEBUG2")
            self.Usage = self.consumption
            return self.Usage
        if account_type == "Prepay":
            if Usage_description != None:
                meter_no_li = self.cc.getMeters_Associated_With_Account(account_no, meter_type)
                meter_no = meter_no_li[0]
                self.LastUsage, LastPostedOn = self.cc.getLastUsage(meter_no)
                self.LastPosted_On = datetime.strftime(LastPostedOn, "%m/%d/%Y")
                print("LASTUSAGE")
                print(self.LastUsage)
                UsageAmount = self.cc.getUsageAmount(account_no, Usage_description)
                tax_on_usage_amount = self.cc.getTotalTaxUsageAmount(account_no, Usage_description)
                self.Past30Days_consumption = self.cc.getPast30Days_TotalUsage(meter_no)
                Usage = UsageAmount + tax_on_usage_amount
                Usage = abs(numpy.round(Usage, 2))
                self.Usage = '{:,.2f}'.format(Usage)
                Past30DaysAvgUsage = round(self.Past30Days_consumption / 30)
                return self.Usage, Past30DaysAvgUsage, int(self.LastUsage), self.LastPosted_On
            else:
                print("DEBUG4")
                self.consumption = int(reading2) - int(reading1)
                usage_rate = self.cc.getUsageRate(Usage_rate_name)
                tax_rate = self.cc.getTaxRate(tax_jurisdiction, service_type)
                Usage_amount = self.consumption * usage_rate
                Tax_On_Usage_amount = Usage_amount * tax_rate
                Usage = Usage_amount + Tax_On_Usage_amount
                Usage = numpy.round(Usage, 2)
                self.Usage = '{:,.2f}'.format(Usage)
                self.LastUsage = self.consumption
                Past30DaysAvgUsage = round(self.consumption / 30)
                return self.Usage, Past30DaysAvgUsage, self.LastUsage

    def Calculation_AccountBalanceTyle(self, account_no, Usage_charge):
        Total_Charge = self.cc.getSumOfDailyCharge_TaxonDailyCharge(account_no)
        Past30days_charges = Total_Charge + float(Usage_charge)
        return Past30days_charges

    def CalculateEstimatedDaysLeft(self, account_balance, AverageDailyUsage):
        EstimatedDaysLeft = account_balance / AverageDailyUsage
        EstimatedDaysLeft = round(EstimatedDaysLeft)
        return EstimatedDaysLeft

    def VerifyLastPaymentMade_Amount_Date(self, account_no):
        LastPayment_AccountSummary = self.getText(self._last_payment)
        LastPaymentDate_AccountSummary = self.getText(self._last_payment_date)
        LastPayment_db, LastPayment_Date_db = self.cc.getLastPayment_Amount_and_date(account_no)
        print(type(LastPayment_Date_db))
        LastPayment_Date_db = datetime.strftime(LastPayment_Date_db, "%m/%d/%Y")
        result = self.VerifyExpected_and_Actual_Result("$" + str(LastPayment_db), LastPayment_AccountSummary)
        result1 = self.VerifyExpected_and_Actual_Result(str(LastPayment_Date_db), LastPaymentDate_AccountSummary)
        return result, result1

    def getPast30DaysCharges_UtilityChargeChangedBy_LastUpdatedOn_FromDB(self, account_no):
        Past30DaysCharges_db = self.cc.getSumOf_Past30DaysCharges(account_no)
        Past30DaysCharges_db = '{:,.2f}'.format(Past30DaysCharges_db)
        UpdatedBalance_db, LastUpdatedDate_db = self.cc.getAccountBalance_LastUpdatedDate(account_no)
        UpdatedBalance_db = '{:,.2f}'.format(UpdatedBalance_db)
        LastUpdatedDate_db = datetime.strftime(LastUpdatedDate_db, "%m/%d/%Y")
        return UpdatedBalance_db, LastUpdatedDate_db, Past30DaysCharges_db















