"""AtCoder Contest Country Ranking"""

import json
import urllib2

from unidecode import unidecode


contest_code = raw_input('Please enter a contest code (e.g. agc017): ')
country_code = raw_input('Please enter a country code (e.g. BY, HK): ')
link = 'http://' + contest_code + '.contest.atcoder.jp/standings'
html = urllib2.urlopen(urllib2.Request(link)).read().split('\n')

for i in range(0, len(html)):
    if 'ATCODER.standings' in html[i]:
        start = html[i + 2].index('[')
        end = html[i + 2].rindex(']')
        js = json.loads(html[i + 2][start:end + 1])
        data = [('rank', 'user', 'handle', 'rating', 'solved')]
        leng = [0, 0, 0, 0, 0]
        for j in js:
            if j['country'] == country_code:
                solved = 0
                for k in j['tasks']:
                    if 'score' in k and k['score'] > 0:
                        solved += 1
                data.append((str(j['rank']),
                             unidecode(j['user_name']),
                             j['user_screen_name'],
                             str(j['rating']),
                             '%d / %d' % (solved, len(j['tasks']))))
        for j in data:
            for k in range(5):
                leng[k] = max(leng[k], len(j[k]) + 1)
        leng = tuple(leng)
        for j, k in enumerate(data):
            print ('%%%ds %%%ds %%%ds %%%ds %%%ds' % leng) % k
            if j == 0:
                print '-' * (sum(leng) + 4)
        break
