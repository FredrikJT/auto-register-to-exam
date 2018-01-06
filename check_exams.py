# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

def check_if_exams_exist(selenium_parameters):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = selenium_parameters[0]
    verificationErrors = []

    try:
        driver.get(base_url + selenium_parameters[1])
        driver.get(base_url + selenium_parameters[2])
        driver.find_element_by_css_selector("#ctl00_ctl47_login > span").click()
        driver.find_element_by_id("ctl00_ContentPlaceHolder1_PasswordTextBox").clear()
        driver.find_element_by_id("ctl00_ContentPlaceHolder1_PasswordTextBox").send_keys(selenium_parameters[3])
        driver.find_element_by_id("ctl00_ContentPlaceHolder1_UsernameTextBox").clear()
        driver.find_element_by_id("ctl00_ContentPlaceHolder1_UsernameTextBox").send_keys(selenium_parameters[4])
        driver.find_element_by_id("ctl00_ContentPlaceHolder1_SubmitButton").click()
        driver.find_element_by_css_selector("ul.linklist > li > a").click()
    except:
        print("Exception encontered when checking for exams!")
        return "Exception encountered"

    try:
        if u"Inga tentamenstillfällen funna." == driver.find_element_by_id("ctl00_m_g_74e02c7c_2a28_488e_b6d8_389a816ae62b_ctl00_lblNoExams").text:
            return "Inga tentamenstillfällen funna."

    except AssertionError as e:
        verificationErrors.append(str(e))
        print("Exception in check_exams: " + e)
        return "Exception in check_exams: " + e