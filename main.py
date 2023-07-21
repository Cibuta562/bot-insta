import pyautogui
import time
import random

####### Sobolan resolution #######

# Cand vrei sa lucrezi comentezi toata partea mea si decomentezi pe a ta
# Pentru a comenta selectezi codul pe care vrei sa il comentezi si apesi Ctrl + /

##################################

pyautogui.moveTo(1000, 313, duration=3.4)
pyautogui.leftClick(1000, 313)
pyautogui.moveTo(1137, 234, duration=1.4)
pyautogui.click()

list_of_has = ["#digitalmarketingagency", "#marketingagency", "#digitalmarketing"]
has_index = random.randint(0,len(list_of_has)-1)
chosen_has = list_of_has[has_index]

pyautogui.typewrite(chosen_has)
time.sleep(2.95)
pyautogui.moveTo(1227, 372, duration=1.8)
pyautogui.click()
pyautogui.moveTo(1767, 193, duration=2.3)
pyautogui.click(1767, 193)
time.sleep(2.1)

######################

num_steps = 6
pause_time = 0.5

for i in range(num_steps):
    pyautogui.scroll(-174)
    time.sleep(pause_time)

time.sleep(3.2)
pyautogui.moveTo(1205, 505, duration=1.6)
pyautogui.click()
counter = 0
max_iterations = 20

list_of_coms = ["Keep up the good posts! 📈", "Great post! 👀", "This post is so well made! 🔥"]
list_of_coms = random.sample(list_of_coms,len(list_of_coms))
coms_index = random.randint(0,len(list_of_coms)-1)
chosen_coms = list_of_coms[coms_index]


while counter < max_iterations:
     coms_index = random.randint(0, len(list_of_coms) - 1)
     chosen_coms = list_of_coms[coms_index]
     time.sleep(3.4)
     pyautogui.moveTo(1347, 690, duration=2)
     pyautogui.click()
     pyautogui.moveTo(1448, 805, duration=1.8)
     pyautogui.click()
     time.sleep(1.2)
     pyautogui.typewrite(chosen_coms)
     pyautogui.moveTo(1782, 809, duration=1.4)
     pyautogui.click()
     pyautogui.moveTo(1863, 557, duration=2)
     pyautogui.click()
     print("Iteration", counter +1)
     counter += 1
time.sleep(2.7)
pyautogui.moveTo(1864, 131, duration=2)
pyautogui.click()
pyautogui.moveTo(1000, 335, duration=2)
pyautogui.click()
time.sleep(3.9)
pyautogui.typewrite(chosen_has)
time.sleep(2.7)
pyautogui.moveTo(1214, 405, duration=2)
pyautogui.click()
pyautogui.moveTo(1813, 358, duration=3)
time.sleep(1)

num_steps = 6
pause_time = 0.4


for i in range(num_steps):
    pyautogui.scroll(245)
pyautogui.click()


####################################


########## Murloc Resolution ##########


# pyautogui.moveTo(1000, 80, duration=1)
# pyautogui.leftClick(1000, 313)
# pyautogui.moveTo(1137, 234, duration=1.4)
# pyautogui.click()
#
# list_of_coms = ["#digitalmarketingagency", "#marketingagency", "#digitalmarketing"]
# coms_index = random.randint(0,len(list_of_coms))
# chosen_com = list_of_coms[coms_index]
#
# pyautogui.typewrite(list_of_coms)
# time.sleep(2.95)
# pyautogui.moveTo(1227, 372, duration=1.8)
# pyautogui.click()
# pyautogui.moveTo(1767, 193, duration=2.3)
# pyautogui.click(1767, 193)
# time.sleep(2.1)
#
# ######################
#
# num_steps = 6
# pause_time = 0.5
#
# for i in range(num_steps):
#     pyautogui.scroll(-500)
#     time.sleep(pause_time)
#
# time.sleep(3.2)
# pyautogui.moveTo(1451, 462, duration=1.6)
# pyautogui.click()
# counter = 0
# max_iterations = 2
#
# while counter < max_iterations:
#      pyautogui.moveTo(1347, 690, duration=2)
#      pyautogui.click()
#      pyautogui.moveTo(1863, 557, duration=2)
#      pyautogui.click()
#      print("Iteration", counter +1)
#      counter += 1
# time.sleep(2.7)
# pyautogui.moveTo(1864, 131, duration=2)
# pyautogui.click()
# pyautogui.moveTo(1000, 335, duration=2)
# pyautogui.click()
# time.sleep(3.8)
# text_to_type = "#socialmediamarketing"
# pyautogui.typewrite(text_to_type)
# pyautogui.moveTo(1214, 405, duration=2)
# pyautogui.click()
# pyautogui.moveTo(1813, 358, duration=3)
# time.sleep(1.89)
# num_steps = 6
# pause_time = 0.5
#
#
# for i in range(num_steps):
#     pyautogui.scroll(500)
# pyautogui.click(1767, 193)