import pytest
import time

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、用例运行策略，
*  -s 指定运行目录或文件，例: -s  ./test_case/ ,  -s  /test_case/test_demo.py
*  --html  指定测试报告目录及文件名。
*  --self-contained-html 表示创建独立的测试报告。
*  --reruns 3   指定用例失败重跑次数。
'''

if __name__ == "__main__":
    now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
    # args = ["-s", "./cases/","--html=./test_report/"+now_time+"report.html","--self-contained-html","--reruns", "0"]
    # pytest.main(args)

    # pytest.main(["-s","-v","./cases/test_aa.py","--html=./report/"+now_time+"report.html"]) #ok!
    # pytest.main(["-s","-v","./cases/test_baidu_search.py","--html=./report/"+now_time+"report.html"])
    pytest.main(["-s","-v","./cases/","--html=./report/"+now_time+"report.html"])

