import sys
import os
import sys

base_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_path)
sys.path.append(parent_dir)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
from Util.handle_excel import execl_data
from base.base_request import case_requests
from Util.handle_result import handle_result, handle_result_json


class RunMain:
    def run_case(self, index=0):
        """
        case 运行
        """
        # case_value = []
        # 将execl_data实例化给rows
        rows = execl_data(index)

        # 获取execl用例，发送请求
        for row in range(2, rows.get_rows() + 1):
            case_value = rows.get_rows_value(row)
            if case_value['is_run'] == 1:
                method = case_value['method']  # 获取用例中的method
                url = case_value['url']       # 获取用例中的url 与配置文件中的host进行拼接
                data = case_value['data']    # 获取用例中的data
                excepect_method = case_value['预期类型']
                datam_message = str(case_value['预期结果'])  #获取用例中的预期结果
                res = case_requests.run_main(method=method, url=url)
                message = handle_result(url, res['data']['errorcode'])

                # logging.info(f'{url}<------>{message}<----->{datam_message}')
                if excepect_method == 'message':
                    if message == datam_message:
                        logging.info('case成功')
                    else:
                        logging.info('case失败')

                if excepect_method == 'errorcode':
                    if datam_message == res['data']['errorcode']:
                        logging.info('case成功')
                    else:
                        logging.info('case失败')

                if excepect_method == 'json':
                    data_value = handle_result_json(datam_message, url)
                    if data_value:
                        logging.info(f'{url}<--->case成功')
                    else:
                        logging.info(f'{url}<--->case失败')


if __name__ == '__main__':
    sss = RunMain()
    sss.run_case()
