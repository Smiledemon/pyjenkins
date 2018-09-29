# coding:utf-8

from HTMLTestRunner import HTMLTestRunner
import unittest
from testcase5_dynamic import WidgetTestCase

if __name__ == '__main__':
	suite = unittest.makeSuite(WidgetTestCase)
	filename = '../reports.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(fp, title=u'my unit test', description=u'This is a report test')
	runner.run(suite)
	fp.close()
