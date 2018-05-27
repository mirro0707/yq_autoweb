# coding=utf-8
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from time import sleep
import pytest

try:
    from page.baidu_page import BaiduPage
except ImportError:
    from page.baidu_page import BaiduPage


# 百度搜索
def test_baidu_search1(browser):
    bd= BaiduPage(browser)
    bd.open()
    bd.search_input("pytest")
    bd.search_button()
    sleep(1)
    title = bd.search_title()
    assert title == "pytest_百度搜索"


# 百度搜索 --参数化
@pytest.mark.parametrize(
    "name, searchkey",
    [("1", "Selenium"),
     ("2", "pytest文档"),
     ])
def test_baidu_search(name, searchkey, browser):
    bd = BaiduPage(browser)
    bd.open()
    bd.search_input(searchkey)
    bd.search_button()
    sleep(1)
    title = bd.search_title()
    assert title == searchkey+"_百度搜索"


if __name__ == "__main__":
    pytest.main(["-s", "test_baidu_search.py"])
