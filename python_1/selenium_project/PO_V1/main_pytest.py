# _*_ coding:utf-8 _*_
# @Time    :2019/10/29 14:56
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :main_pytest.py

import pytest

if __name__ == '__main__':
    # pytest.main(["-v","-s","-m","pytest_login_smoke","--alluredir=Outputs/allure_report"])
    # pytest.main(["-v","-s","-m","pytest_login_smoke","--html=Outputs/reports/pytest_run_report.html"])
    pytest.main(["-v", "-s", "-m", "pytest_invest_smoke"])























