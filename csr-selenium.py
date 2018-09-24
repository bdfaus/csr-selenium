from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#INFO TO BE USED FOR USER LOG-IN FORM
nate_num = randint(0,100)*randint(0,100) + randint(0,9)
email = f"natedl98+{nate_num}@gmail.com"
print(email)
password = "password"
confirm_pw = password
first = "Fake_Nate"
last = "Fake_Last"
phone = "555-555-5555"
zip_code = "27705"
dob = "01/01/1980"
resources = "I take orders well"
certs = "Michael Scott CPR"
other = "Nope"
where = "Cuero, TX 77954, USA"
antecedent_text = [phone, resources, certs, other]


#SELENIUM GRUNT WORK STARTS HERE
driver = webdriver.Firefox()
driver.get("http://www.crowdsourcerescue.com")
elem = driver.find_element_by_id("active-disaster-notice")
elem.click()
button = driver.find_element_by_class_name("hhrbuttongreen")
button.click()

#FILL IN MOST SINGLE LINES WITH INFO FROM ABOVE. FIND BY ELEMENT ID. (phone number not included here)
field_id = ['email','pwd','cpwd','datapoint_item_input_51','datapoint_item_input_52','datapoint_item_input_9',
'datapoint_item_input_681', 'pac-input46']
field_text = [email, password, confirm_pw, first, last, zip_code, dob, where]
for el_id, f_input in zip(field_id, field_text):
	field = driver.find_element_by_id(el_id)
	field.click()
	field.clear()
	field.send_keys(f_input)

#important note, text_boxes returns a list (see the plural "elements" in method name)
##things got weird here because of the way classes/ids were used/not used in the HTML.
## .antecedent elements sometimes had an id, and sometimes not. those without an id
## are selected below (2,6,7,8) and then text entered
text_boxes = driver.find_elements_by_class_name("antecedent")
text_boxes = [text_boxes[x] for x in (2,6,7,8)]
for b, text in zip(text_boxes, antecedent_text):
	b.click()
	b.clear()
	b.send_keys(text)

#Add a truck
truck_add = driver.find_element_by_link_text("Add Truck or High Water Vehicle")
truck_add.click()

truck_spec_high = driver.find_element_by_id("datapoint_item_input_679")
select = Select(truck_spec_high)
select.select_by_visible_text("12-24'")

truck_spec_people = driver.find_element_by_id("datapoint_item_input_680")
select = Select(truck_spec_people)
select.select_by_visible_text("2")

datapoint_nums = ['655', '656', '659', '660']
for num in datapoint_nums:
	datapoint_element = f"datapoint_item_input_{num}"
	select = Select(driver.find_element_by_id(datapoint_element))
	select.select_by_index(1)

#Hit the submit button
submit = driver.find_element_by_class_name("btn-success")
submit.click()