#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 0_test.py
# @Author: guolei
# @Time  : 02/05/2019 10:49 AM
# @Desc  :
# @Ans   :

nums = [1,2,3]
print [4] + [1,2,3]
print nums[:1] + nums[2:]

print [-1 for i in xrange(3)]

for i in nums[:-1]:
    print i

print ord('A'),ord('Z'),ord('a'),ord('z'),ord('z')-ord('A')

select
  a.query,
  a.show_province_id,
  a.show_city_id,
  a.pv,
  a.epv,
  a.shows
  from
(select
 *
from
  zp_show
where
  show_province_id != 2
  and day >= 20190429
  and day <= 20190505）) a