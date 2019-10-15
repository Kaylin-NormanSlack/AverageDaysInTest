import unittest
import json
from datetime import datetime as dt
import AverageDayCalculator as Calculator

class CalculateAverageDayTests(unittest.TestCase):

#=========================
# Happy Path Tests
#=========================    
    
    def test_CalculateAverageDay_Returns_Correct_Data_From_json(self):
        calc = Calculator.CalculateAverageDay()    
        file_data = calc.load_data_from_file('TestDayAverageVariables.json')
        self.assertEqual("kaylin.norman-slack@efinancial.com",file_data['Username'])

    def test_CalculateAverageDay_When_Jira_Login_Attempted_Should_Return_Client(self):
        calc = Calculator.CalculateAverageDay()
        file_data = calc.load_data_from_file('TestDayAverageVariables.json')
        jiraClient = calc.login_to_jira(file_data['Username'],file_data['ApiKey'],file_data['Server Options'])
        self.assertIsNotNone(jiraClient.server_info)

    def test_CalculateAverageDay_Returns_Issue_Dictionary_Length_Greater_Than_Zero(self):
        calc = Calculator.CalculateAverageDay()    
        file_data = calc.load_data_from_file('TestDayAverageVariables.json')
        jiraClient = calc.login_to_jira(file_data['Username'],file_data['ApiKey'],file_data['Server Options'])
        issues = calc.get_issues(jiraClient,file_data['JQL Query'])
        self.assertNotEqual(0,len(issues))

    def test_CalculateAverageDay_Returns_Date_ThirteenWeeks_Earlier_Than_Date(self):
        calc = Calculator.CalculateAverageDay()
        result = calc.get_new_minimum_date('2019-10-01')
        self.assertEqual('2019-07-02',result)

    def test_CalculateAverageDay_Returns_Different_Query_From_Original_When_Updated(self):
        calc = Calculator.CalculateAverageDay()
        test_query = "project in (EAR) AND status in ('In Test','UAT','Closed', Resolved) AND created >= 2019-01-01 AND created <= 2020-01-01 AND QA in (Kaylin.Norman-Slack) ORDER BY priority DESC"
        new_query = calc.set_new_start_date_in_jql_query(test_query,'2019-10-01')
        self.assertNotEqual(test_query,new_query)

if __name__ == '__main__':
    unittest.main()