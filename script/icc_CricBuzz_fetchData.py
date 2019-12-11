from selenium import webdriver
from xlwt import Workbook
from dataFile import *

print("Program is reading the data from CricBuzz.com..... Please wait.")
driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.implicitly_wait(30)
driver.maximize_window()
for i in URL:
    driver.get(i)
    pageTitle = driver.title


    ballList = driver.find_elements_by_xpath(XPATH_BALLNO)
    ballText = driver.find_elements_by_xpath(XPATH_BALLTEXT)


    wb = Workbook()
    partsOfTitle = pageTitle.partition(",")
    sheet1 = wb.add_sheet(partsOfTitle[0], cell_overwrite_ok=True)
    j = 1
    #Column for Balls
    sheet1.write(0, 0, 'Ball')
    for i in ballList[::-1]:
        strOfi = i.text
        sheet1.write(j, 0, strOfi)
        j += 1

    # Column for Bowler
    sheet1.write(0, 1, 'Bowler')
    if j != 1:
        j = 1
    for i in ballText[::-1]:

        strOfBowler = i.text
        tbowler = strOfBowler.partition(" to")
        sheet1.write(j, 1, tbowler[0])
        j += 1

    #Column for Striker
    sheet1.write(0, 2, 'Striker')
    if j != 1:
        j = 1
    for i in ballText[::-1]:
        strOfBowler = i.text
        tbowler = strOfBowler.partition("to ")
        rpart = tbowler[2].partition(",")
        sheet1.write(j, 2, rpart[0])
        j += 1

    #Column for RunList
    sheet1.write(0, 3, 'Run')
    sheet1.write(0, 4, "Wickets")
    if j != 1:
        j = 1
    for i in ballText[::-1]:
        strOfBowler = i.text
        if strOfBowler.__contains__("no run"):
            sheet1.write(j, 3, "0")
        elif strOfBowler.__contains__("1 run"):
            sheet1.write(j, 3, "1")
        elif strOfBowler.__contains__("2 run"):
            sheet1.write(j, 3, "2")
        elif strOfBowler.__contains__("3 run"):
            sheet1.write(j, 3, "3")
        elif strOfBowler.__contains__("FOUR"):
            sheet1.write(j, 3, "4")
        elif strOfBowler.__contains__("SIX"):
            sheet1.write(j, 3, "6")
        elif strOfBowler.__contains__("no ball"):
            sheet1.write(j, 3, "1")
        elif strOfBowler.__contains__("wide"):
            tu=strOfBowler.partition("wide")
            if tu[0].__contains__("2"):
                sheet1.write(j, 3, "2")
            else:
                sheet1.write(j, 3, "1")
        elif strOfBowler.__contains__("out"):
            sheet1.write(j, 3, "0")
            sheet1.write(j, 4, "Wicket")
        else:
            sheet1.write(j, 3, "-")
        j += 1

    xlsFile = crPath + "/ExtractedData/" + partsOfTitle[0] + '.xls'

    wb.save(xlsFile)

driver.close()