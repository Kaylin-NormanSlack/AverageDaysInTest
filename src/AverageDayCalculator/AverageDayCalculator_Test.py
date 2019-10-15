import unittest
import json
import AverageDayCalculator

class CalculateAverageDayTests(unittest.TestCase):

    def CalculateAverageDay_Returns_Correct_Data_From_Json(self):
        calc = AverageDayCalculator.CalculateAverageDay()
        file_data = calc.load_data_from_file('TestDayAverageVariables.json')
        self.assertEqual("kaylin.norman-slack@efinancial.com",file_data['Username'])
        pass

    def CalculateAverageDay_When_Jira_Login_Attempted_Should_Return_Client(self):
        calc = AverageDayCalculator.CalculateAverageDay()
        file_data = calc.load_data_from_file('TestDayAverageVariables.json')
        jiraClient = calc.login_to_jira(file_data['Username'],file_data['APIKey'],file_data['Server Options'])
        self.assertIsNotNone(jiraClient.server_info)
        pass


if __name__ == '__main__':
    unittest.main()