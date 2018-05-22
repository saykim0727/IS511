#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# pip install selenium
# http://selenium-python.readthedocs.io/
# http://chromedriver.chromium.org/getting-started // must be setting up path
# https://www.blazemeter.com/blog/6-easy-steps-testing-your-chrome-extension-selenium

class AutomatedTest:
  def __init__(self, path=''):
    self.driver = None
    self.setExtensionPath(path)

  def __del__(self):
    self.clean()

  def init(self):
    assert self.ext_path != ''

    desired = DesiredCapabilities.CHROME
    desired['loggingPrefs'] = {
      'browser': 'ALL'
    }

    options = webdriver.ChromeOptions()
    options.add_extension(self.getExtensionPath())

    self.driver = webdriver.Chrome(
      chrome_options=options,
      desired_capabilities=desired
    )

  def clean(self):
    if self.driver != None:
      self.driver.close()
      self.driver = None

  def setExtensionPath(self, path):
    self.ext_path = path

  def getExtensionPath(self):
    return self.ext_path

  def getLogs(self):
    return self.driver.get_log('browser')

  def start(self, urls, callback):
    self.init()

    for i in urls:
      self.driver.get(i)
      callback(self.getLogs())

    self.clean()

if __name__ == '__main__':
  a = AutomatedTest('/path/to/extension.crx')
  def output(result):
    print result
    print '-' * 64
  a.start([
    'https://www.google.com/',
    'https://www.facebook.com/',
    'https://www.twitter.com/',
    'https://www.naver.com/',
    'https://www.daum.net/'
  ], output)
