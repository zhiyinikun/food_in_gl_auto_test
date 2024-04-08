import os.path

import requests
from jenkins import Jenkins

jenkins_url = "http://192.168.112.128:8080/"
# 登录Jnekins
server = Jenkins(jenkins_url, username="admin", password="123456")
job_name = "job/food in gl_auto_test"
job_url = server.get_info(job_name)["url"]
job_last_number = server.get_info(job_name)["lastBuild"]["number"]
report_url = job_url + str(job_last_number) + "/allure"


def push_message():
    """
    封装数据
    :return:
    """
    content = {}
    #提取在服务器上prometheusData.txt文件里存的数据。
    prometheus_data_file_path = os.path.dirname(os.getcwd()) + "/allure-report/export/prometheusData.txt"
    # 读取文件，按行循环读取
    with open(prometheus_data_file_path, 'r') as f:
        for line in f.readlines():
            # 使用空格分割每行的左右值
            parts = line.strip('\n').split(' ')
            launch_name = parts[0]
            launch_num = parts[1]
            # 添加到字典中
            content.update({launch_name: launch_num})
        f.close()
        passed_num = content["launch_status_passed"]  # 通过数量
        failed_num = content["launch_status_failed"]  # 失败数量
        broken_num = content["launch_status_broken"]  # 阻塞数量
        skipped_num = content["launch_status_skipped"]  # 跳过数量
        case_num = content["launch_retries_run"]  # 总数量
        """
        通过钉钉的webhoook向钉钉发送消息
        """
        webhook = "https://oapi.dingtalk.com/robot/send?access_token=11adae4ec1e5804a55f3d05996eadb60f0aa92b11a31c6b07a76714da55c3fb5"
        message = (f"接口自动化脚本执行结果：\n运行总数: {case_num}\n"
                   f"通过数量: {passed_num}\n"
                   f"失败数量: {failed_num}\n"
                   f"阻塞数量: {broken_num}\n"
                   f"跳过数量: {skipped_num}\n"
                   f"构建地址: {job_url}\n"
                   f"报告地址: {report_url}")


        stringBody = {
            "msgtype": "text",
            "text": {
                "content": message
            }
        }
        requests.post(url =webhook,json = stringBody, verify=False)


push_message()
