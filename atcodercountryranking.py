#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json

link = 'http://code-festival-2016-qualc.contest.atcoder.jp/standings'
country_code = 'HK'

class AtCoderCountryRanking:

	def __init__(self):
		return

	def main(self):
		html = urllib2.urlopen(urllib2.Request(link)).read().split('\n')
		for i in range(0, len(html)):
			if 'ATCODER.standings' in html[i]:
				start = html[i+2].index('[')
				end = html[i+2].rindex(']')
				j = json.loads(html[i+2][start:end+1])
				print('rank user(rating) solved')
				for k in j:
					if k['country'] == country_code:
						solved = 0
						for t in k['tasks']:
							if 'elapsed_time' in t:
								solved += 1
						print("%s %s(%d) %d/%d" % (k['rank'], k['user_name'], k['rating'], solved, len(k['tasks'])))
				break

if __name__ == '__main__':
	obj = AtCoderCountryRanking()
	obj.main()