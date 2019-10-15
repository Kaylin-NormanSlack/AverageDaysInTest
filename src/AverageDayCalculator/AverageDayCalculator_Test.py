import unittest
import json
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
    

if __name__ == '__main__':
    unittest.main()