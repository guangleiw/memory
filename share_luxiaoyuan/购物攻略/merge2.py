#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import datetime
import time

sys.path.append(os.getenv('HIVE_TASK'))
from HiveTask import HiveTask
ht = HiveTask()
sdate='2019-03-21'
edate='2019-03-21'

dest_db = 'app'
dest_table_name = 'app_s04_cx_src'

# 小文件合并
merge_part_dir = []
while sdate <= edate:
    # print(sdate)
    for tp in ['day', 'month', 'week']:
        for dp in ['g_bu_first1','g_dept1_first1','g_dept2_first1','g_bu_refer1','g_dept1_refer1','g_dept2_refer1','g_bu_first4','g_bu_refer4','g_bu_first3','g_dept2_first3','g_dept1_refer3','g_dept2_first4','g_bu_first2','g_dept1_first2','g_dept2_first2','g_bu_refer2','g_dept1_refer2','g_dept2_refer2','g_dept1_first4','g_dept1_refer4','g_dept1_first3','g_bu_refer3','g_dept2_refer3','g_dept2_refer4']:
            for cur_page_first_class_cd in ['1014']:
                if tp == 'month' and not sdate.endswith('01'):
                    # 月的话是1号
                    pass
                elif tp == 'week' and datetime.datetime.strptime(sdate, "%Y-%m-%d").strftime('%w') != '1':
                    # 周的话是周一
                    pass
                else:
                    merge_part_dir.append('dt=' + sdate + '/tp=' + tp + '/dp=' + dp + '/cur_page_first_class_cd=' + cur_page_first_class_cd)
    sdate = (datetime.datetime.strptime(sdate, '%Y-%m-%d') + datetime.timedelta(1)).strftime('%Y-%m-%d')
# print(merge_part_dir)
ht.exec_sql(schema_name = dest_db,
			table_name = dest_table_name,
			sql = """""",
			merge_flag = True,
			merge_type='mr',
			merge_part_dir = merge_part_dir)