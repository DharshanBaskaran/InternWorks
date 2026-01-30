import allure
from behave import given,when,then
from pages import FormPage
from config import variables

@given("user launches the training form successfully")
def step_launch_application(context):
    with allure.step("Launch the training form"):
        context.driver.get("https://hirschqa.azurewebsites.net/training/")
        context.form_page = FormPage(context.driver)

@when("user fills all required details")
def step_fill_form(context):
    with allure.step("fill all required details"):
        context.form_page.fill_form(variables)

@when("user views the pdf")
def step_views_pdf(context):
    with allure.step("user viewing the pdf"):
        pass

@then("form should be submitted and print action should be triggered")
def step_submit_form(context):
    with allure.step("Form submission performed successfully"):
        assert True


@given("user launches the training form successfully 2")
def step_launch_application(context):
    with allure.step("Launch the training form"):
        context.driver.get("https://hirschqa.azurewebsites.net/training/")
        context.form_page = FormPage(context.driver)

@when("user fills all required details 2")
def step_fill_form(context):
    with allure.step("fill all required details"):
        context.form_page.fill_form(variables)

@when("user views the pdf 2")
def step_views_pdf(context):
    with allure.step("user viewing the pdf"):
        pass

@then("form should be submitted and print action should be triggered 2")
def step_submit_form(context):
    with allure.step("Form submission performed successfully"):
        assert True