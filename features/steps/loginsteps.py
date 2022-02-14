from behave import *
from selenium import webdriver


@given(u'I launch chrome browser')
def launchChrome(context):
    context.driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe")


@when(u'I open safaricomtaleonet homepage')
def OpenHomePage(context):
    context.driver.get("https://safaricom.taleo.net/careersection/saf_external_professional/jobsearch.ftl?lang=en&portal=12100020963")


@when(u'I click on sign in')
def clickSignIn(context):
    context.driver.find_element_by_xpath("//*[@id='topNavInterface.loginAction']").click()


@then(u'I should be taken to the login page')
def openLogin(context):
    context.driver.get("https://safaricom.taleo.net/careersection/iam/accessmanagement/login.jsf?lang=en&redirectionURI=https%3A%2F%2Fsafaricom.taleo.net%2Fcareersection%2Fsaf_external_professional%2Fjobsearch.ftl%3Fpostdata%3D%24cWayQkVVQsCYt7CmFW_37g%26lang%3Den%26ftlcompclass%3DLoginComponent&TARGET=https%3A%2F%2Fsafaricom.taleo.net%2Fcareersection%2Fsaf_external_professional%2Fjobsearch.ftl%3Fpostdata%3D%24cWayQkVVQsCYt7CmFW_37g%26lang%3Den%26ftlcompclass%3DLoginComponent")


@when(u'I enter my username "{user}" and password "{pwd}"')
def enterDetails(context, user, pwd):
    context.driver.find_element_by_id("dialogTemplate-dialogForm-login-name1").send_keys(user)
    context.driver.find_element_by_id("dialogTemplate-dialogForm-login-password").send_keys(pwd)


@when(u'I click on login button')
def clickLogin(context):
    context.driver.find_element_by_id("dialogTemplate-dialogForm-login-defaultCmd").click()


@then(u'I should be taken to my dashboard')
def displaydashboard(context):
    context.driver.get("https://safaricom.taleo.net/careersection/saf_external_professional/mysubmissions.ftl?postdata=$qsmXa-rof8OutmajAsSlYQ&lang=en&ftlcompclass=PageComponent")
    context.driver.implicitly_wait(20)
    context.driver.close()
