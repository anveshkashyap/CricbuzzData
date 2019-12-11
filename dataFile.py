import os

crPath = os.getcwd().replace('\\','/').replace("/script","")
CHROME_PATH = crPath+"/drivers/chromedriver.exe"
URL = ["https://www.cricbuzz.com/cricket-scores/15803/wi-vs-ind-2nd-semi-final-icc-world-t20-2016"]
XPATH_BALLNO = "//span[contains(@class,'cb-col cb-col-8 text-bold')]"
XPATH_BALLTEXT = "//p[contains(@class,'cb-col cb-col-90 cb-com-ln')]"


#MatchLink
#"https://www.cricbuzz.com/cricket-scores/20280/sl-vs-ind-match-44-icc-cricket-world-cup-2019"
#"//span[contains(@class,'cb-col cb-col-8 text-bold')]"
#"//p[contains(@class,'cb-col cb-col-90 cb-com-ln')]"


#"https://www.cricbuzz.com/cricket-scores/15803/wi-vs-ind-2nd-semi-final-icc-world-t20-2016"
#"//span[contains(@class,'cb-col cb-col-8 text-bold')]"
#"//p[contains(@class,'cb-col cb-col-90 cb-com-ln')]"