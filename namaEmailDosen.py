from BeautifulSoup import BeautifulSoup
import urllib2

req = urllib2.Request('http://ptiik.ub.ac.id/page/read/dosen/461acea')
response = urllib2.urlopen(req)
the_page = response.read()

parsed_replay = BeautifulSoup(the_page)
parsed1 = parsed_replay.body.find('div', attrs={'class' : 'mixit-content'})
allUrl = parsed1.findAll('a')

response.close()
for urlList in allUrl:
    href = urlList.get("href")
    req = urllib2.Request(href)
    response = urllib2.urlopen(req)
    the_page = response.read()
    parsed_replay = BeautifulSoup(the_page)
    parsed2 = str(parsed_replay.body.find('ol', attrs={'class' : 'breadcrumb'}))
    parsed2_1 = parsed2.splitlines()
    parsed2_2 = parsed2_1[3]
    name = parsed2_2[104:-12]

    parsed3 = parsed_replay.body.findAll('ul', attrs={'class' : 'profile-list list-unstyled'})
    parsed4 = str(parsed3[1])
    parsed5 = parsed4.splitlines()
    parsed6 = parsed5[3]
    parsed7 = parsed6[42:-5]
    parsed8 = parsed7.replace(' ','')
    parsed9 = parsed8.replace('[dot]','.')
    email = parsed9.replace('[at]','@')

    print name
    print"\tEmail : ", email
    print

'''
Muhammad Abyan Safitra              125150200111098
Mochammad Syaifullah Ferryansyah    125150200111101
Muhammad Harisuddin Thohir          125150200111103
Elsa Nur Amilus Shofia              125150202111006
'''