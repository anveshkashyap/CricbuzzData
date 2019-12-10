from selenium import webdriver
from xlwt import Workbook

driver = webdriver.Chrome(executable_path="C:/Users/acer/PycharmProjects/CricbuzzData/drivers/chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://www.cricbuzz.com/cricket-scores/20280/sl-vs-ind-match-44-icc-cricket-world-cup-2019")

ballList = driver.find_elements_by_xpath("//span[contains(@class,'cb-col cb-col-8 text-bold')]")
ballText = driver.find_elements_by_xpath("//p[contains(@class,'cb-col cb-col-90 cb-com-ln')]")

wb = Workbook()  # Creating object of workbook class
sheet1 = wb.add_sheet("icc", cell_overwrite_ok=True)  # (cell_overwrite_ok=True ) TO Over write in the same Excel Sheet
j = 1
# Column for Balls
sheet1.write(0, 0, 'BallList')  # Row Column Value
for i in ballList[::-1]:  # -1 is reversing the list so it will start reading from rerversed 1st value
    strOfi = i.text  #
    sheet1.write(j, 0, strOfi)
    j += 1

# Column for Bowler
sheet1.write(0, 1, 'BowlerList')
if j != 1:
    j = 1
for i in ballText[::-1]:  # -1 is reversing the list so it will start reading from rerversed 1st value

    strOfBowler = i.text
    tbowler = strOfBowler.partition(" to")  # strOfBowler.partition - splitting the text from the delimiter " to".
    # Partition is used to Split and it always took 1st Occurence of delimiter
    # Return type of partition is Tuple.
    sheet1.write(j, 1, tbowler[0])
    j += 1

# Column for Striker
sheet1.write(0, 2, 'StrikerList')
if j != 1:
    j = 1
for i in ballText[::-1]:  # -1 is reversing the list so it will start reading from rerversed 1st value
    strOfBowler = i.text
    tbowler = strOfBowler.partition("to ")
    rpart = tbowler[2].partition(",")
    sheet1.write(j, 2, rpart[0])
    j += 1

# Column for RunList
sheet1.write(0, 3, 'RunList')
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
        tu = strOfBowler.partition("wide")
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

# wb.save("ODI-SLvsIND.xls")

wb.save("C:/Users/acer/PycharmProjects/CricbuzzData/ExtractedData/ODI-SLvsIND.xls")
driver.close()
