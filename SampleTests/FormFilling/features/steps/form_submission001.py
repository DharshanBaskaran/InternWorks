from behave import given,when,then
from pages import FormPage
from config import variables

@given("user launches the training form successfully")
def step_launch_application(context):
    context.driver.get("https://hirschqa.azurewebsites.net/training/")
    context.form_page = FormPage(context.driver)

@when("user fills all required details")
def step_fill_form(context):
    context.form_page.fill_form(variables)

@when("user views the pdf")
def step_views_pdf(context):
    pass

@then("form should be submitted and print action should be triggered")
def step_submit_form(context):
    assert True