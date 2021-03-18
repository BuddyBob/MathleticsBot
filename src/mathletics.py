#import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import atexit
import time
import datetime
import random
import config
def script(start):
    try:
        while True:
            #levels 1-4
            level = 4
            driver =  webdriver.Chrome(executable_path='/Users/aspera/Desktop/chromedriver')
            waitshort = WebDriverWait(driver,.5)
            wait = WebDriverWait(driver, 20)
            waitLonger = WebDriverWait(driver, 100)
            visible = EC.visibility_of_element_located
            driver.get('https://login.mathletics.com/?_ga=2.60361444.876282730.1600105337-1065983887.1599670686&_gac=1.50132436.1600106071.Cj0KCQjwqfz6BRD8ARIsAIXQCf3LZK7GSetOE9YHfbj-cm2Z89tzZRmW-QwIs54eqhKvnkce6x8QB_oaAv_AEALw_wcB')
            user = wait.until(visible((By.XPATH,'//*[@id="username"]'))).send_keys(config.USERNAME)
            pwd = wait.until(visible((By.XPATH,'//*[@id="password"]'))).send_keys(config.PWD,Keys.ENTER)

            play = wait.until(visible((By.XPATH,'//*[@id="student-header"]/div[2]/ul/li[3]/header-button/alert-wrap/div/ng-transclude/div'))).click()
            live = wait.until(visible((By.XPATH,'//*[@id="carousel-game-content"]/img'))).click()
                                                
            level = wait.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/level-selector-directive/div/div['+str(level)+']'))).click()
            cpu = wait.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[4]/div/div[2]/button'))).click()
            go = wait.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[4]/div/go-button/div/button[1]'))).click()
            
            for i in range(100):
                if i % 1 == 0:
                    end = datetime.datetime.now()
                    duration = end - start
                    f = open('times.txt','w')
                    duration = str(duration).split(':')
                    f.write(str(duration))
                    f.write(' hours:'+str(duration[0]))
                    f.write(' minutes:'+str(duration[1]))
                    f.write(' seconds:'+str(duration[2].split('.')[0])+'\n')
                    f.close()
                for i in range(87):
                    time.sleep(.5)
                    txt = waitLonger.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div')))
                    question = txt.text
                    question = question.split(' ')

                    num1 = question[0]
                    op = question[1]
                    num2 = question[2]
                    try:
                        num3 = question[3]
                    except:
                        pass
                    symCount = 0


                    for words in question:
                        try:
                            int(words)
                        except:
                            if words != 'Half':
                                pass
                    #
                    
                    #Algebra
                    for sym in question:
                        if sym == '+' or sym == '-':
                            symbolUsed = sym
                            symCount += 1
                    if symCount == 2:
                        try:
                            if symbolUsed == '+':
                                answer = int(question[0]) + int(question[2]) + int(question[4])
                            if symbolUsed == '-':
                                answer = int(question[0]) - int(question[2]) - int(question[4])
                        except:
                            answer = 45
                    elif num2 == '=':
                        num2 = ' '
                        if op == '+':
                            answer = int(num3) - int(num1)
                        if op == '-':
                            answer = (int(num3) - int(num1)) * -1
                        if op == '×':
                            answer = int(num3) / int(num1)
                        if op == '/':
                            answer = int(num1) / int(num3)

                    
                    elif num1 == '=':
                        num1 = ' '
                        if op == '+':
                            
                            answer = int(num3) - int(num2)
                        if op == '-':
                            answer = int(num3) + int(num2)
                        if op == '×':
                            answer = int(num3) / int(num2)
                        if op == '÷':
                            answer = int(num3) * int(num2)
                        
                        



                        
                    #Norm
                    elif op == '+':
                        answer = int(num1) + int(num2)
                    elif op == '-':
                        answer = int(num1) - int(num2)
                    elif op == '×':
                        answer = int(num1) * int(num2)
                    elif op == 'of':
                        answer = int(num2) / 2
                    else:
                        answer = int(num1) / int(num2)
                    #answer
                    inp = wait.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div/input'))).send_keys(int(answer),Keys.ENTER)
                    # //*[@id="livemathletics"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div/input
                    #                 # /html/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div/input
                    #                 # //*[@id="livemathletics"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div/input


                playagain = waitLonger.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[2]/div[1]/div[2]/play-again-box/div/table[2]/tbody/tr/td[1]/button'))).click()
    except:
        print('dumbass error')
        return 2
start = datetime.datetime.now()
for i in range(int(config.ERRORS_ALLOWED_BEFORE_CLOSING)):
    script(start)
end = datetime.datetime.now()
duration = end - start
import sys
try:
    sys.exit(  )              # see also: os._exit, Tk(  ).quit(  )
except SystemExit:
    driver.quit()
    duration = str(duration).split(':')
    print(duration)
    print('hours: '+str(duration[0]))
    print('minutes: '+str(duration[1]))
    print('seconds: '+str(duration[2].split('.')[0]))
# def dur():
#     print(duration)
# atexit.register()