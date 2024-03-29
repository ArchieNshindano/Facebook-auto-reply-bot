import time
import pickle
import unittest
import tracemalloc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium_stealth import stealth


'''MY ACCOUNT'''
active_chats = []
allChats = []



messagesElements = []
repliesElements = []

messages = []
replies = []
chitChats = []

cookies = 0
options = webdriver.ChromeOptions()
options.add_argument("--detach")
driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
user = 'DaVinci'

'''   DA VINCI '''
chatsXPATH = '//div[@class="x78zum5 xdt5ytf x1iyjqo2 x5yr21d x6ikm8r x10wlt62"]/descendant::div[@class ="x1n2onr6"]/descendant::a[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq"]'
newMsgIndicatorXPATH = './/div[@class="x6s0dn4 x78zum5 xozqiw3"]'
messageXPATH = '//div[@class="x78zum5 xdt5ytf x1iyjqo2"]/descendant::div[@class="x1n2onr6"]/descendant::div[@class="__fb-dark-mode x1n2onr6"]/descendant::div[@class="x6prxxf x1fc57z9 x1yc453h x126k92a x14ctfv"]'
repliesXPATH = '//div[@class="x78zum5 xdt5ytf x1iyjqo2"]/descendant::div[@class="x1n2onr6"]/descendant::div[@class="__fb-dark-mode x1n2onr6"]/descendant::div[@class="x6prxxf x1fc57z9 x1yc453h x126k92a xzsf02u"]'
textBoxAccountXPATH = '//div[@class="x5yr21d x1uvtmcs x78zum5 x1iyjqo2"]/descendant::div[@class="xuk3077 x78zum5 x6prxxf xz9dl7a xsag5q8"]/descendant::div[@class="x78zum5 x1a02dak x13a6bvl"]'
sendIconXPATH = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/div'
dialogXPATH = '//div[@class="x78zum5 xdt5ytf x1iyjqo2"]/descendant::div[@class="x1n2onr6"]/descendant::div[@class="__fb-dark-mode x1n2onr6"]'

'''     CHATGPT    '''
letsGoXPATH = '//div[@class="absolute inset-0"]/descendant::div[@class="relative col-auto col-start-2 row-auto row-start-2 w-full rounded-lg text-left shadow-xl transition-all left-1/2 -translate-x-1/2 bg-white dark:bg-gray-900 max-w-md"]/descendant::div[@class="p-4 sm:p-6 sm:pt-4"]/descendant::div[@class="flex flex-row justify-end"]'
emailXPATH = '//*[@id="username"]'
passWordXPATH = '//*[@id="password"]'
chatGPTXPATH = '//div[@class="flex-col flex-1 transition-opacity duration-500 -mr-2 pr-2 overflow-y-auto"]/descendant::li[@class="relative z-[15]"]/descendant::div[@class="flex-1 text-ellipsis max-h-5 overflow-hidden break-all relative"]'
mySentMessagesXPATH = '//div[@role="presentation"]/descendant::div[@style="--avatar-color: #19c37d;"]/descendant::div[@class="relative flex w-[calc(100%-50px)] flex-col gizmo:w-full lg:w-[calc(100%-115px)] gizmo:text-gizmo-gray-600 gizmo:dark:text-gray-300"]'
gptRepliesXPATH =  '//div[@role="presentation"]/descendant::div[@style="--avatar-color: #19c37d;"]/descendant::div[@class="relative flex w-[calc(100%-50px)] flex-col gizmo:w-full lg:w-[calc(100%-115px)] agent-turn"]'
textBoxGPTXPATH = '//*[@id="prompt-textarea"]'
loginGPTXPATH = '//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/button[1]'
mikePrompt     = 'I want you to act as my Secretary named Mike, I will be sending you messages from pretend customers and you will reply to them first with a greeting. I want your reply and nothing else. Do not write explanations. Do not type commands unless I instruct you to do so. When I need to give you further instructions I will do so by putting text inside curly brackets like this {instruction}.'
instructionsPrompt = '{We sell laptops [such as dell , lenovo] ranging from 2500 t0 10000} {our currency is kwacha[eg K1000], location[zambia(country),copperbelt(province),kitwe(town),nkana east(area)} {We have laptops available in that range , you are to try and convince customers without being too technical yet marketing in style}'




'''MY ACOUNT METHODS'''

def wait(xpath):

        then = time.time()
        diff = 0
        now = 0

        while True:

            try:
                time.sleep(1)
                driver.find_element(By.XPATH,xpath)
                break

            except:
                pass

            now = time.time()
            diff = then - now

            if int(diff % 60) == 30:
                then = now
                refresh()







def refresh():

    driver.get(driver.current_url)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )






def login():

        driver.get('https://web.facebook.com/messages/t/')

        time.sleep(5)

        cookies = pickle.load(open(user, 'rb'))

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()





def  activeChats():

      wait(chatsXPATH)
      allChats = driver.find_elements(By.XPATH,chatsXPATH)

      for chat in allChats:

          try:
              status = chat.find_element(By.XPATH, newMsgIndicatorXPATH).find_element(By.XPATH, './/span')
              active_chats.append(chat)

          except Exception:
              pass


      return active_chats





def getMyMessages():

        temp = activeChats()

        for chat in temp:

            chat.click()
            wait(messageXPATH)
            messagesElements = driver.find_elements(By.XPATH,messageXPATH)


            for messageElement in messagesElements:

                messages.append(messageElement.text)

        return messages



def getMyReplies():

        temp = activeChats()

        for chat in temp:

            chat.click()
            wait(repliesXPATH)
            repliesElements = driver.find_elements(By.XPATH, repliesXPATH)

            for reply in repliesElements:
                replies.append(reply.text)


        return replies

def sendMessageOnACCOUNT(message):
    sendMessage = driver.find_element(By.XPATH,textBoxAccountXPATH).find_element(By.XPATH, './/p')
    sendMessage.send_keys(message)


''' CHATGPT METHODS '''


def loginGPT():

    driver.get('https://chat.openai.com/')

    time.sleep(2)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    wait(loginGPTXPATH)
    login = driver.find_element(By.XPATH,loginGPTXPATH)
    login.click()

    wait(emailXPATH)
    email = driver.find_element(By.XPATH, emailXPATH)
    email.send_keys('EMAIL SHOULD BE HERE')
    email.send_keys(Keys.ENTER)

    wait(passWordXPATH)
    passWord = driver.find_element(By.XPATH,passWordXPATH )
    passWord.send_keys('PASSWORD SHOULD BE HERE')
    passWord.send_keys(Keys.ENTER)


    wait(letsGoXPATH)
    letsGo = driver.find_element(By.XPATH,letsGoXPATH).find_element(By.XPATH, './/button')
    letsGo.click()

    wait(chatGPTXPATH)
    chat = driver.find_element(By.XPATH,chatGPTXPATH)
    chat.click()


def getGPTreply():

    wait(gptRepliesXPATH)
    temp = driver.find_elements(By.XPATH,gptRepliesXPATH)

    for reply in temp:

            replies.append(reply.text)

    return replies



def sendMessageToGPT(messageForGPT):

    wait(textBoxGPTXPATH)
    sendText = driver.find_element(By.XPATH,textBoxGPTXPATH)
    sendText.send_keys(messageForGPT)
    sendText.send_keys(Keys.ENTER)
    sendText.send_keys(Keys.ENTER)

#GPT METHODS END

count = 1

while True:

    if count == 1:

        login()
        myAccountTab = driver.current_window_handle

        driver.switch_to.new_window('GPT WINDOW')
        loginGPT()
        gptTab = driver.current_window_handle
        driver.switch_to.window(myAccountTab)

        chitChats = activeChats()

    print(chitChats)
    for chat in chitChats:
        chat.click()

        wait(dialogXPATH)
        dialogue = driver.find_elements(By.XPATH, dialogXPATH)
        dialogueTxt = ''

        for msg in dialogue:
            dialogueTxt += '    '+ msg.text.replace('\n','  -------  ')


        allReplies = getMyReplies()
        lastReply = allReplies[len(allReplies) - 1]

        driver.switch_to.window(gptTab)
        this = '{Using the chat history to get the context of the conversation , produce an appropriate reply}'

        prompt = mikePrompt + '{ Chat history with this customer:  ' + dialogueTxt + ' } ' + this + f' CUSTOMER MESSAGE TO REPLY TO AND REPLY TO PREVIOUS MESSAGES IN THE HISTORY IF NECESSARY: {lastReply} '+ ' {this is the current message}  ' + instructionsPrompt

        sendMessageToGPT(prompt)

        time.sleep(10)

        allGptREPLIES = getGPTreply()
        lastIndex = len(allGptREPLIES) - 1
        lastGptReply = allGptREPLIES[lastIndex]

        driver.switch_to.window(myAccountTab)
        sendMessageOnACCOUNT(lastGptReply)
        iconButton = driver.find_element(By.XPATH, sendIconXPATH)

        iconButton.click()

        driver.switch_to.window(myAccountTab)
        chitChats = activeChats()



    active_chats = []
    count += 1
    driver.switch_to.window(myAccountTab)

    time.sleep(1)

    #time.sleep(30)
    #login()



print('HELLO WORLD')




time.sleep(100)



driver = webdriver.Chrome()
driver.get('https://web.facebook.com/messages/t/')


cookies = pickle.load(open('Archie.pkl','rb'))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

time.sleep(10)
chatList = driver.find_elements(By.XPATH, '//div[@class="x78zum5 xdt5ytf x1iyjqo2 x5yr21d x6ikm8r x10wlt62"]/descendant::div[@class ="x1n2onr6"]/descendant::a[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq"]')
activeChats = 0
status = 0
newList = []
myMessages = []
replyMessages = []

for chat in chatList:

    try:
     status = chat.find_element(By.XPATH,'.//div[@class="x6s0dn4 x78zum5 xozqiw3"]').find_element(By.XPATH,'.//span')
     print(chat.text)
     newList.append(chat)

    except Exception:
        pass



for i , chat in enumerate(chatList):

    chat.click()
    time.sleep(5)
    messages = driver.find_elements(By.XPATH,'//div[@class="x78zum5 xdt5ytf x1iyjqo2"]/descendant::div[@class="x1n2onr6"]/descendant::div[@class="__fb-dark-mode x1n2onr6"]/descendant::div[@class="x6prxxf x1fc57z9 x1yc453h x126k92a x14ctfv"]')
    replies =  driver.find_elements(By.XPATH,'//div[@class="x78zum5 xdt5ytf x1iyjqo2"]/descendant::div[@class="x1n2onr6"]/descendant::div[@class="__fb-dark-mode x1n2onr6"]/descendant::div[@class="x6prxxf x1fc57z9 x1yc453h x126k92a xzsf02u"]')
    #dialogue = driver.find_elements(By.XPATH,'//div[@class="x78zum5 xdt5ytf x1iyjqo2"]/descendant::div[@class="x1n2onr6"]/descendant::div[@class="__fb-dark-mode x1n2onr6"]')

    for info in dialogue:
        print('THIS CONVO: ')
        print(info.text)


time.sleep(5)
chatList[1].click()

time.sleep(5)



time.sleep(1000)









