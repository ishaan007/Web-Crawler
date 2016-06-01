
import csv

from pyquery import PyQuery as pq
import os
import glob
import csv
import xlwt
import pandas

_RESOURCE_ = 'http://www.kic.ae/about-us/staff-members/senior-management/'

rlen = lambda x: range(len(x))


def obtain_user_data(sub_dom):
  '''Return user data from DOM'''
  join_info = lambda x: ' '.join([x.eq(_).text() for _ in rlen(x)])

  return {
    'name': sub_dom.find('.mem-info span').text(),
    'info': join_info(sub_dom.find('.mem-info em')),
    'email': sub_dom.find('.mem-info a').text()
  }


def obtain_resource():
  '''Main entry point'''
  dom = pq(url=_RESOURCE_)
  users_dom = dom.find('.staff-member .span8')

  for i in rlen(users_dom):
    yield obtain_user_data(users_dom.eq(i))


if __name__ == '__main__':
  max_pages = 1
  page = 1
  c = csv.writer(open("seniormanagement.csv", "wb"))
  c.writerow(["University", "Name", "Info", "Email"])
  while page <= max_pages:
    for user in obtain_resource():
      # print(user)
      # c.writerow([str(["DU"]),str(user["name"]),str(user['subjects']),str(user['interests']),"Not Found","Not Found"])
      a = user["name"].encode('ascii', 'ignore')
      b = user['info'].encode('ascii', 'ignore')
      d = user['email'].encode('ascii', 'ignore')
      print a
      print b
      print d
      c.writerow(["AL KIC", a, b, d])
      # print "name", user["name"]
      # print "Interests ",user['interests']
      # print "SUBJECTS ", user['subjects']
    page = page + 1
  _RESOURCE_ = 'http://www.kic.ae/about-us/staff-members/staff-auh-academic/'
  max_pages = 1
  page = 1
  c = csv.writer(open("staffacademic.csv", "wb"))
  c.writerow(["University", "Name", "Info", "Email"])
  while page <= max_pages:
      for user in obtain_resource():
          # print(user)
          # c.writerow([str(["DU"]),str(user["name"]),str(user['subjects']),str(user['interests']),"Not Found","Not Found"])
          a = user["name"].encode('ascii', 'ignore')
          b = user['info'].encode('ascii', 'ignore')
          d = user['email'].encode('ascii', 'ignore')
          print a
          print b
          print d
          c.writerow(["AL KIC", a, b, d])
          # print "name", user["name"]
          # print "Interests ",user['interests']
          # print "SUBJECTS ", user['subjects']
      page = page + 1
  _RESOURCE_ = 'http://www.kic.ae/about-us/staff-members/aa-academic/'
  max_pages = 1
  page = 1
  c = csv.writer(open("aaacademic.csv", "wb"))
  c.writerow(["University", "Name", "Info", "Email"])
  while page <= max_pages:
      for user in obtain_resource():
          # print(user)
          # c.writerow([str(["DU"]),str(user["name"]),str(user['subjects']),str(user['interests']),"Not Found","Not Found"])
          a = user["name"].encode('ascii', 'ignore')
          b = user['info'].encode('ascii', 'ignore')
          d = user['email'].encode('ascii', 'ignore')
          print a
          print b
          print d
          c.writerow(["AL KIC", a, b, d])
          # print "name", user["name"]
          # print "Interests ",user['interests']
          # print "SUBJECTS ", user['subjects']
      page = page + 1



