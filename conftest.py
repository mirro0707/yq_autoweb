from selenium import webdriver
import pytest
import os
driver = None

# base_dir = os.path.split(os.path.realpath(__file__))[0] # 项目路径

# 生成pytest-html报告
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            # 提取出图片名称
            # 获取当前case的路径
            # 存放截图的路径./report/screenshots/
            len = str(file_name).split("/").__len__() # yq
            file_name = "report/screenshots/"+str(file_name).split("/")[len-1] # yq
            # print("pytest_runtest_makereport的file_name:"+file_name) # yq
            _capture_screenshot(file_name)

            # file_name 改为report的相对路径
            file_name = "../"+file_name # yq
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

# 用例失败截图
def _capture_screenshot(name):
    '''
    :param name: 图片存放的地址
    :return:
    '''
    driver.get_screenshot_as_file(name)
    # print("_capture_screenshot截图的name"+name)


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("======================test end!========================")

if __name__ == "__main__":
    _capture_screenshot("test_search_python.png")