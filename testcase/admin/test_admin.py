import allure
import pytest

from core.AdminApiService import AdminApiService
from util.YamlUtil import YamlUtil


@allure.feature("员工相关模块")
class TestAdmin:
    # 登录，并且获取token，更新token.yaml里的token，如果token过期了，执行此方法即可
    @pytest.mark.parametrize("data", YamlUtil().extract_case("login_data.yaml", "user_login"))
    def test_login_token(self, data):
        # 将token从返回参数中通过提取到token.yaml文件内
        AdminApiService().handle_case(data)

    # 测试登录接口
    @pytest.mark.parametrize("data", YamlUtil().extract_case("admin_data.yaml", "user_login"))
    def test_login(self, data):
        AdminApiService().handle_case(data)

    #测试根据id回显员工数据接口
    @pytest.mark.parametrize("data", YamlUtil().extract_case("getbyid_employee_data.yaml", "getbyid"))
    def test_getbyid(self, data, fetch_token):
        AdminApiService().handle_case(data, fetch_token)

    # 测试新增员工接口
    @pytest.mark.parametrize("data", YamlUtil().extract_case("add_employee.yaml", "add"))
    def test_add(self, data, fetch_token):
        AdminApiService().handle_case(data, fetch_token)

    # 测试编辑员工信息
    @pytest.mark.parametrize("data", YamlUtil().extract_case("update_employee.yaml", "add"))
    def test_update(self, data, fetch_token):
        AdminApiService().handle_case(data, fetch_token)

    # 测试分页查询
    @pytest.mark.parametrize("data", YamlUtil().extract_case("page_employee.yaml", "page"))
    def test_page(self, data, fetch_token):
        AdminApiService().handle_case(data, fetch_token)

    # 测试启用禁用账号状态
    @pytest.mark.parametrize("data", YamlUtil().extract_case("status_employee.yaml", "status"))
    def test_status(self, data, fetch_token):
        AdminApiService().handle_case(data, fetch_token)

    # 测试退出登录
    @pytest.mark.parametrize("data", YamlUtil().extract_case("logout_employee.yaml", "logout"))
    def test_logout(self, data, fetch_token):
        AdminApiService().handle_case(data, fetch_token)


