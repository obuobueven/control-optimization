import json
import pprint
import pandas as pd
from cpeslog.log_code import _logging
from Model.optimization_day import opt_day, to_csv


if __name__ == '__main__':
    # g_load={'g_load_18':([3800]*11+[2200]*7+[3800]*6)*60,
    # #         'g_load_26':([2500]*11+[1600]*7+[2500]*6)*60,
    #         # 'g_load_32':([3200]*11+[2000]*7+[3200]*6)*60
    
    #         }
    # pd.DataFrame(g_load).to_csv('hh38.csv')
    _logging.info('start')
    time_length = 24*3
    try:
        with open("Config/config.json", "rb") as f:
            input_json = json.load(f)
    except BaseException as E:
        _logging.error('读取config失败,错误原因为{}'.format(E))
        raise Exception
    # 读取输入excel
    try:
        load = pd.read_excel('input_720/input_720h.xls')
    except BaseException as E:
        _logging.error('读取input_720h的excel失败,错误原因为{}'.format(E))
        raise Exception
    try:
        sto = pd.read_excel('input_720/input_now.xls')
    except BaseException as E:
        _logging.error('读取input_now的excel失败,错误原因为{}'.format(E))
        raise Exception
    try:
        sto_end = pd.read_excel('input_720/input_end.xls')

    except BaseException as E:
        _logging.error('读取input_end的excel失败,错误原因为{}'.format(E))
        raise Exception
    sto_end['time'] = time_length
    sto_end.index = [time_length]
    # 优化主函数
    # try:
    dict_control, dict_load = opt_day(parameter_json=input_json, load_json=load, begin_time=0,
                                      time_scale=time_length, storage_begin_json=sto, storage_end_json=sto_end)
    # except BaseException as E:
    #     _logging.error('优化主函数执行失败，错误原因为{}'.format(E))
    #     raise Exception
    # print(dict_control)
    # print(dict_plot)

    # 写入输出Excel
    to_csv(dict_control, "dict_opt_plot")
    to_csv(dict_load,"dict_opt_load")
