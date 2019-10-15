import base64
import jira.client
from collections import defaultdict
from datetime import datetime as dt
from jira.client import JIRA
from operator import attrgetter
import numpy as np
import json

class StatusDelta:
    def __init__(self,earNumber, createdString,fromString,toString):
        self.earNumber = earNumber
        self.createdString = createdString
        self.fromString = fromString
        self.toString = toString

class CardDurationDelta:
    def __init__(self):
        self.earNumber = ""
        self.qa_start = ""
        self.qa_end = ""


class CalculateAverageDay:
    def __init__(self):
        self.USERNAME = ""
        self.APIKEY = ""
        self.options = {}
        self.JQL_query = ""
        self.from_string_list = []
        self.to_string_list = []
        self.total_sum_of_days = 0
        
    def login_to_jira(self,username,APIKEY,server_options):
        DecodedAPIKey = base64.b64decode(APIKEY)
        jira = JIRA(server_options,basic_auth=(username,DecodedAPIKey))
        return jira

    def get_issues(self,jira,jqlQuery):
        query_results =  jira.search_issues(jqlQuery)
        list_of_issues=[]
        for result in query_results:
            list_of_issues.append(result.key)
        return list_of_issues
    
    #Figure out a way to optimize this! It's O(n^3)!
    def get_sorted_list_of_DeltaObject(self,jira,issueList,fromList,toList):
        status_delta_list = []
        for current_issue in issueList:
            current_issue = jira.issue(current_issue,expand='changelog')
            changelog = current_issue.changelog
            for history in changelog.histories:
                for item in history.items:
                    if item.field == 'status':
                        if (item.fromString in fromList) and (item.toString in toList):
                            temp_delta_object = StatusDelta(current_issue.key,dt.strptime(history.created[:10],"%Y-%m-%d"),item.fromString,item.toString)
                            status_delta_list.append(temp_delta_object)

        return sorted(status_delta_list,key=lambda StatusDelta: StatusDelta.earNumber)

    def get_sorted_issue_dictionary(self,deltaObjectList):
        issueList_dictionary = defaultdict(list)
        for delta_object in deltaObjectList:
            issueList_dictionary[delta_object.earNumber].append(delta_object)
        return issueList_dictionary

    def get_average_of_test_days(self,issueDictionary):
        for issueEARNumber in issueDictionary:
            d1 = issueDictionary[issueEARNumber][0].createdString
            d2 = issueDictionary[issueEARNumber][len(issueDictionary[issueEARNumber])-1].createdString
            delta = d1-d2
            self.total_sum_of_days +=  delta.days
        return round(float(self.total_sum_of_days / len(issueDictionary)),2)
    
    def calculate_average_delta(self,lastAverage,currentAverage):
        if(lastAverage > currentAverage):
            return round((lastAverage - currentAverage),2)
        else:
            return round((currentAverage - lastAverage),2)

    def load_data_from_file(self,file_name):
        with open(file_name,'r+') as outfile:
            json_data = json.load(outfile) 
        return json_data

    def update_json_file(self,outfile,json_data,average_days_in_test,last_reported_average,last_reported_delta,average_delta,total_sum_of_days_in_test,issueList_dictionary):
        with open(outfile,'r+') as newjsonfile:
            json_data = json.load(newjsonfile) 
            json_data['Current Average'] = average_days_in_test
            json_data['Total Sum of Days'] = total_sum_of_days_in_test
            json_data['From Statuses'] = self.from_string_list
            json_data['To Statuses'] = self.to_string_list
            json_data['Username'] = self.USERNAME
            json_data['JQL Query'] = self.JQL_query
            json_data['Last Reported Average'] = last_reported_average
            json_data['Last Reported Average Delta'] = last_reported_delta
            json_data['Average Delta'] = average_delta
            for issueEARNumber in issueList_dictionary:
                json_data['Calculated Issues'].append(issueEARNumber)
            newjsonfile.seek(0)
            json.dump(json_data,newjsonfile,indent=4,sort_keys=True)
            newjsonfile.truncate()
    
    def Run(self):
        deltaObjectList =[]
        file_data = self.load_data_from_file("TestDayAverageVariables.json")
        self.from_string_list = file_data['From Statuses']
        self.to_string_list = file_data['To Statuses']
        self.USERNAME = file_data['Username']
        self.APIKEY =  bytes(file_data['ApiKey'],'utf-8')
        self.JQL_query= file_data['JQL Query']
        self.options = file_data['Server Options']
        last_reported_average = file_data['Last Reported Average']
        last_reported_delta = file_data['Last Reported Average Delta']
        average_delta = file_data['Average Delta']
        jira_client = self.login_to_jira(self.USERNAME,self.APIKEY,self.options)
        issueSearchResults = self.get_issues(jira_client,self.JQL_query)
        deltaObjectList = self.get_sorted_list_of_DeltaObject(jira_client,issueSearchResults,self.from_string_list,self.to_string_list)
        sortedDeltaObjectDictionary = self.get_sorted_issue_dictionary(deltaObjectList)
        average_days = self.get_average_of_test_days(sortedDeltaObjectDictionary)
        average_delta = self.calculate_average_delta(last_reported_average,average_days)
        self.update_json_file('TestDayAverageVariables.json',file_data,average_days,last_reported_average,last_reported_delta,average_delta,self.total_sum_of_days,sortedDeltaObjectDictionary)
        jira_client.close()