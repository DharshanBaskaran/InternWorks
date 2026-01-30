import allure
from utils.driver_factory import get_driver
from utils.logger import logger

def before_all(context):
    logger.info("Test Execution Starts!!..")
    context.driver = get_driver(kiosk_printing=True)

def before_feature(context,feature):
    logger.info(f"feature starts: {feature.name}")
    allure.dynamic.feature(feature.name)

def before_scenario(context, scenario):
    logger.info(f"scenario starts: {scenario.name}")
    context.driver = get_driver(kiosk_printing=True)
    allure.dynamic.title(scenario.name)

def before_step(context, step):
    logger.info(f"step starts: {step.name}")
    context.allure_step = allure.step(step.name)
    context.allure_step.__enter__()

def after_step(context, step):
    if hasattr(context,"allure_step"):
        context.allure_step.__exit__(None, None, None)

    if step.status == "failed":
        logger.error(f"step failed: {step.name}")
        if hasattr(context,"driver"):
            screenshot=context.driver.get_screenshot_as_png()
            allure.attach(screenshot, name=step.name, attachment_type=allure.attachment_type.PNG)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        logger.error(f"scenario failed: {scenario.name}")

    if context.driver:
        context.driver.quit()
        logger.info("Browser Closed")

def after_feature(context,feature):
    logger.info(f"feature ends: {feature.name}")

def after_all(context):
    logger.info("All tests Completed!!!")