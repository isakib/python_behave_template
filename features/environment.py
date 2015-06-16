from selenium import webdriver


def before_all(context):
     print("Executing before all")

def before_feature(context, feature):
     print("Before feature\n")

#Scenario level objects are popped off context when scenario exits
def before_scenario(context,scenario):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    print("Before scenario\n")

def after_scenario(context,scenario):
    context.browser.quit()

def after_feature(context,feature):
     print("\nAfter feature")

def after_all(context):
     print("Executing after all")

