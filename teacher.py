from selenium import webdriver
import os, time
from selenium.webdriver.common.keys import Keys
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
import random        

# change path
PATH = ('C:\\Program Files (x86)\\Chrome\\Application\\chromedriver.exe') 
# declaring vars
driver = webdriver.Chrome(PATH)
f = Faker()

driver.get('https://www.ixl.com/membership/teachers/trial')
time.sleep(2)
for x in range(0, 1):
  driver.find_element_by_xpath('/html/body/main/form/section[2]/div[1]/input').send_keys(f.name())
  driver.execute_script("window.open('');")
  driver.switch_to.window(driver.window_handles[1])
  time.sleep(1)
  driver.get("https://mailpoof.com/")
  driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[2]/form[2]/input[2]').click()
  time.sleep(2)
  driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div').click()
  driver.switch_to.window(driver.window_handles[0])
  driver.find_element_by_xpath('/html/body/main/form/section[2]/div[2]/input').send_keys(Keys.CONTROL, 'v')
  time.sleep(2)
  driver.find_element_by_xpath('/html/body/main/form/section[3]/div/div[2]/div[1]/input').send_keys('90011')
  time.sleep(2)
  driver.find_element_by_class_name('select-institutionId').click()
  driver.find_element_by_xpath('/html/body/main/form/section[3]/div/div[2]/div[2]/div/select/optgroup[1]/option[1]').click()
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[1]/input').send_keys('876')
  var2 = (random.randint(20933849,209338493))
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[1]/input').send_keys(var2)
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[1]/input').send_keys('876')
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[2]/label').click()
  time.sleep(2)
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[1]/label').click()
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[3]/label').click()
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[4]/label').click()
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[6]/div/button').click()
  time.sleep(9)
  driver.find_element_by_xpath('/html/body/main/div/section[2]/form/div[2]/div/label/input').click()
  driver.find_element_by_xpath('/html/body/main/div/section[2]/form/div[2]/div/label/input').send_keys(var2)
  driver.find_element_by_xpath('/html/body/main/div/section[2]/form/div[2]/div/label/input').send_keys('abc')
  driver.find_element_by_xpath('/html/body/main/div/section[2]/form/div[2]/div/label/input').click()
  driver.find_element_by_xpath('/html/body/main/div/section[2]/form/div[3]/button').click()
  driver.switch_to.window(driver.window_handles[1])
  driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div').click()
  time.sleep(2)
  print('waiting email to appear')
  driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div').click()
  time.sleep(3)
  time.sleep(3)
  time.sleep(3)
  print('please wait')
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div').click()
  time.sleep(2)
  info = driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div/div[3]')
  info2 = info.text
  print(info2)
  driver.delete_all_cookies()
  driver.close();
  driver.switch_to.window(driver.window_handles[0])
  driver.get('https://www.ixl.com/membership/teachers/trial')

  driver.get('https://www.ixl.com/membership/teachers/trial')
  time.sleep(2)
  driver.find_element_by_xpath('/html/body/main/form/section[2]/div[1]/input').send_keys(f.name())
  driver.execute_script("window.open('');")
  driver.switch_to.window(driver.window_handles[1])
  time.sleep(1)
  driver.get("https://mailpoof.com/")
  driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[2]/form[2]/input[2]').click()
  time.sleep(2)
  driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div').click()
  driver.switch_to.window(driver.window_handles[0])
  driver.find_element_by_xpath('/html/body/main/form/section[2]/div[2]/input').send_keys(Keys.CONTROL, 'v')
  time.sleep(2)
  driver.find_element_by_xpath('/html/body/main/form/section[3]/div/div[2]/div[1]/input').send_keys('90011')
  time.sleep(2)
  driver.find_element_by_class_name('select-institutionId').click()
  driver.find_element_by_xpath('/html/body/main/form/section[3]/div/div[2]/div[2]/div/select/optgroup[1]/option[1]').click()
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[1]/input').send_keys('876')
  var2 = (random.randint(20933849,209338493))
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[1]/input').send_keys(var2)
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[1]/input').send_keys('876')
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[2]/label').click()
  time.sleep(2)
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[1]/label').click()
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[3]/label').click()
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[4]/label').click()
  driver.find_element_by_xpath('/html/body/main/form/section[4]/div[6]/div/button').click()
  time.sleep(9)
  driver.switch_to.window(driver.window_handles[1])
  driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div').click()
  time.sleep(2)
  print('waiting email to appear')
  driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div').click()
  time.sleep(3)
  time.sleep(3)
  time.sleep(3)
  print('please wait')
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div').click()
  time.sleep(2)
  info = driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div/div[3]')
  info2 = info.text
  print(info2)
  driver.delete_all_cookies()
  driver.close();
  driver.switch_to.window(driver.window_handles[0])
  driver.get('https://www.ixl.com/membership/teachers/trial')

