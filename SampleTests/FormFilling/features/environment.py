from utils.driver_factory import get_driver
from utils.logger import logger

def before_all(context):
    logger.info("Test Execution Starts!!..")

def before_feature(context, feature):
    logger.info(f"feature starts: {feature.name}")

def before_scenario(context, scenario):
    logger.info(f"scenario starts: {scenario.name}")
    context.driver = get_driver(kiosk_printing=True)

def before_step(context, step):
    logger.info(f"step starts: {step.name}")

def after_step(context, step):
    if step.status == "failed":
        logger.error(f"step failed: {step.name}")

def after_scenario(context, scenario):
    if scenario.status == "failed":
        logger.error(f"scenario failed: {scenario.name}")

    if context.driver:
        context.driver.quit()
        logger.info("Browser Closed")

def after_feature(context, feature):
    logger.info(f"feature ends: {feature.name}")

def after_all(context):
    logger.info("All tests Completed!!!")
