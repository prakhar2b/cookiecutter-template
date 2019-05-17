from selenium import webdriver
import pytest

@pytest.fixture
def test_setup():
  global driver
  driver = webdriver.Chrome(executable_path = 'chromedriver')
  driver.implicitly_wait({{cookiecutter.global_step_wait}})
 
