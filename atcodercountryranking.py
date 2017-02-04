# -*- coding: utf-8 -*-

import urllib2
import json

link = 'http://agc010.contest.atcoder.jp/standings'
country_code = 'HK'

class AtCoderCountryRanking:
	def main(self):
		html = urllib2.urlopen(urllib2.Request(link)).read().split('\n')
		for i in range(0, len(html)):
			if 'ATCODER.standings' in html[i]:
				start = html[i+2].index('[')
				end = html[i+2].rindex(']')
				j = json.loads(html[i+2][start:end+1])
				print('%5s %15s %15s %7s %7s' % ('rank', 'user', 'handle', 'rating', 'solved'))
				out = ''
				for k in range(5 + 1 + 15 + 1 + 15 + 1 + 7 + 1 + 7) :
					out += '-'
				print out
				for k in j:
					if k['country'] == country_code:
						solved = 0
						for t in k['tasks']:
							if 'score' in t and t['score'] > 0:
								solved += 1
						print('%5d %15s %15s %7d %3d/%3d' % (k['rank'], k['user_name'], k['user_screen_name'], k['rating'], solved, len(k['tasks'])))
				break

if __name__ == '__main__':
	AtCoderCountryRanking().main()