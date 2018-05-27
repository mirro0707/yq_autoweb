
def test_screenshot_on_test_failure(browser):
    browser.get("https://www.baidu.com")
    assert False