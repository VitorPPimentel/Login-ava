from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
import time
import json
import os

def before_all(context):
    try: 
        with open(str(os.getcwd())+"/features/profiles/default.json", "r") as profile_file:
            default_profile_json = json.load(profile_file)
            context.variables = default_profile_json
        profile = context.config.userdata["profile"]
        with open(str(os.getcwd()) + "\\features\\profiles\\" + profile + ".json", "r") as profile_file:
            chosen_profile_json = json.load(profile_file)
            default_profile_json.update(chosen_profile_json)
            context.variables = default_profile_json
    except:
        print("Problems with profiles...", profile)
    options = webdriver.ChromeOptions()

    if context.variables["headless"]:
        options.add_argument("--headless")

    try:
      context.browser = webdriver.Chrome("tools/chromedriver.exe", chrome_options=options)
    except SessionNotCreatedException:
        update_Chromedriver()
        context.browser = webdriver.Chrome("tools/chromedriver.exe", chrome_options=options)

    context.browser.implicitly_wait(int(context.variables["element_load_timeout"]))
    context.browser.maximize_window()


def before_feature(context, feature):
    if context.variables["retry"]:
        for scenario in feature.walk_scenarios():
            patch_scenario_with_autoretry(scenario, max_attempts=3)


def before_scenario(context, scenario):
    context.browser.refresh()


def after_scenario(context, scenario):    
    context.browser.execute_script('localStorage.clear();')
    

def after_all(context):
    context.browser.quit()


def after_step(context, step):
    time.sleep(2)
    #if context.variables["screenshot"] and step.status == "failed": 
    #    allure.attach(context.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
