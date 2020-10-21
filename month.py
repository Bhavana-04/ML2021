#displays the events in a particular month with date and day
def months():
        #takes input from the user
        month_name=input("Enter a month name: ")
        if month_name=="January":
            print("The date,day and events days which are celebrated on January")
            print("-----Date: 1,Day: Wednesday,Event: New Year's Day-----")
            print("-----Date: 15,Day: Wednesday,Event: Makara Sankranti-----")
            print("-----Date: 26,Day: Sunday,Event: Republic Day-----")
            print("-----Date: 30,Day: Thursday,Event: Vasant Panchami-----")
        elif month_name=="February":
            print("The date,day and events which are celebrated on February")
            print("-----Date: 21,Day: Friday,Event: Maha Shivaratri-----")
        elif month_name == "March":
            print("The date,day and events which are celebrated on March")
            print("-----Date: 10,Day: Tuesday,Event: Holi-----")
        elif month_name == "April":
            print("The date,day and events which are celebrated on April")
            print("-----Date: 2,Day: Thursday,Event: Ramanavami-----")
            print("-----Date: 25,Day: Wednesday,Event: Ugadi-----")
            print("-----Date: 10,Day: Friday,Event: Good Friday-----")
        elif month_name == "May":
            print("The date,day and events which are celebrated on May")
            print("-----Date: 25,Day: Monday,Event: Ramzan-Eid-----")
        elif month_name == "June":
            print("The date,day and events which are celebrated on June")
            print("-----Date: 3,Day: Tuesday,Event: Rathayatri-----")
        elif month_name == "July":
            print("The date,day and events which are celebrated on July")
            print("-----No Events-----")
        elif month_name == "August":
            print("The date,day and events which are celebrated on August")
            print("-----Date: 3,Day: Monday,EventB: Raksha Bandhan-----")
            print("-----Date: 11,Day: Tuesday,Event: Janmastami-----")
            print("-----Date: 15,Day: Saturday,Event: Independence day-----")
            print("-----Date: 22,Day: Saturday,Event: Vinayaka Chavathi-----")
            print("-----Date: 31,Day: Monday,Event: Onam-----")
        elif month_name == "September":
            print("The date,day and events which are celebrated on September")
            print("-----No Events-----")
        elif month_name == "October":
            print("The date,day and events which are celebrated on October")
            print("-----Date: 2,Day: Friday,Event: Mahatma Gandhi Jayanthi-----")
            print("-----Date: 25,Day: Sunday,Event: Dussehra-----")

        elif month_name == "November":
            print("The date,day and events which are celebrated on November")
            print("-----Date: 14,Day: Saturday,Event: Diwali-----")
        elif month_name == "December":
            print("The date,day and events which are celebrated on December")
            print("-----Date: 25,Day: Friday,Event: Christmas-----")
        #invalid input
        else:
            print("Please check the month name")