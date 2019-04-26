from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

#change my name to your username
driver_path = "/Users/kylelitton/FinalProject/chromedriver"
browser = webdriver.Chrome(driver_path)
f = open("fall2019", "w+")

def moveInView(x):
    browser.execute_script("arguments[0].scrollIntoView(true);",x)

browser.get("http://sis.rutgers.edu/soc/#subjects?semester=92019&campus=NB&level=U")
browser.implicitly_wait(30)

dropButton = browser.find_element_by_xpath("""//*[@id="widget_dijit_form_FilteringSelect_0"]/div[1]/input""")
dropButton.click()

dropMenu = browser.find_element_by_xpath("""//*[@id="dijit_form_FilteringSelect_0_popup"]""")

departments = [x for x in dropMenu.find_elements_by_css_selector(".dijitReset.dijitMenuItem")]

#go through each department
count = 0

while count < len(departments):

    time.sleep(1)
    departments = [x for x in dropMenu.find_elements_by_css_selector(".dijitReset.dijitMenuItem")]
    moveInView(departments[count])
    departments[count].click()

    courseList = [x for x in browser.find_elements_by_css_selector(".courseExpandIcon")]

    #go through each class in the department
    classCount = 0
    while classCount < len(courseList):

        time.sleep(1)
        courseList = [x for x in browser.find_elements_by_css_selector(".courseExpandIcon")]
        moveInView(courseList[classCount])
        courseList[classCount].find_element(By.TAG_NAME, 'img').click()
        
        #gets each sections information
        courseData = [x for x in browser.find_elements_by_css_selector(".courseData")]
        sectionInfoList = [x for x in courseData[classCount].find_elements_by_css_selector(".sectionData")]
        
        #go through each section
        sectionCount = 0
        while sectionCount < len(sectionInfoList):

            time.sleep(1)
            courseData = [x for x in browser.find_elements_by_css_selector(".courseData")]
            sectionInfoList = [x for x in courseData[classCount].find_elements_by_css_selector(".sectionData")]
            moveInView(sectionInfoList[sectionCount])

            classesPerWeek = len([x for x in sectionInfoList[sectionCount].find_elements_by_css_selector(".meetingTimeDay")])
            
            #print hours for class
            meetingCount = 0
            while meetingCount < classesPerWeek:

                courseData = [x for x in browser.find_elements_by_css_selector(".courseData")]
                sectionInfoList = [x for x in courseData[classCount].find_elements_by_css_selector(".sectionData")]
                
                dayList = [x for x in sectionInfoList[sectionCount].find_elements_by_css_selector(".meetingTimeDay")]
                hourList = [x for x in sectionInfoList[sectionCount].find_elements_by_css_selector(".meetingTimeHours")]
                campusList = [x for x in sectionInfoList[sectionCount].find_elements_by_css_selector(".meetingTimeCampus")]
                buildingList = [x for x in sectionInfoList[sectionCount].find_elements_by_css_selector(".meetingTimeBuildingAndRoom")]

                print(dayList[meetingCount].text, hourList[meetingCount].text, campusList[meetingCount].text, buildingList[meetingCount].text)
                newEntry = dayList[meetingCount].text + ' ' + hourList[meetingCount].text + ' ' + campusList[meetingCount].text + ' ' + buildingList[meetingCount].text + "\n"
                f.write(newEntry)

                meetingCount = meetingCount+1





            sectionCount = sectionCount+1

        #close drop down to prevent loop
        moveInView(courseList[classCount])
        courseList[classCount].find_element(By.TAG_NAME, 'img').click()
        classCount = classCount+1






    dropButton.click()
    count = count + 1

