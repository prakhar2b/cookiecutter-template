#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author : Prakhar Pratyush <prakharlabs@gmail.com>
#
#----------------------------------------------------------


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def until_url_changed(driver, max_wait):
	WebDriverWait(driver, max_wait).until(EC.url_changes(driver.current_url))


def get_elem(locators):
	"""
	Supported locator type : attribute, css_selector, xpath
	"""
	elem = None
	for l in locators:
		if not elem:
			if l.type == "attribute":
				try:
			        elem = driver.find_element_by_css_selector("[{}={}]".format(l.key, l.value))
			    except Exception as ex:
			        print(ex)

			elif l.type =="css_selector":
				try:
					elems = driver.find_elements_by_css_selector(l.value)
	        		position = l.position - 1
	        		elem = elems[position] if len(elems) >= position else None
    			except Exception as ex:
    				print(ex)

    		else:
    			if l.type == "xpath":
    				try:
        				elem = chrome_driver.find_element_by_xpath(l.value)
					except Exception as ex:
						print(ex)
		else:
			break
	return elem


def do_steps(step, driver):
	"""
	interface for all the supported selenium test steps
	"""

	if step.type == "input":
		text = step.text
		step_wait = step.config.step_wait
		elem = get_elem(step.locators)

		if not elem:
			raise Exception("Test Failed at step 1")

		elem.send_keys(text)
	    driver.implicitly_wait(step_wait)

	elif step.type == "click":
		step_wait = step.config.step_wait
		elem = get_elem(step.locators)
		if not elem:
        	raise Exception("Test Failed at Step 2")
	    elem_type = elem.get_attribute("type")
	    if elem_type == "submit":
	        elem.submit()
	    else:
	        elem.click()
		driver.implicitly_wait(step_wait)

	elif step.type == "assertion":
		step_wait = step.config.step_wait
		elem = get_elem(step.locators)

		assertion_type = step['assertion_type']
		if assertion_type == "textExists":
			assert elem.text.contains(step['value'])
			driver.implicitly_wait(step_wait)
		else:
			if assertion_type == "elementNotExists":
				pass
		

	elif step.type == "wait":
		until_url_changed(driver, step.value)
		driver.implicitly_wait(step.step_wait)

	else:
		raise Exception("The step type is not supported.")
		
