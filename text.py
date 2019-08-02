import requests,bs4
#11877 10028
# fix toc

event_id = [100378,100370,84999,87748,87131,86587,85902,86737,86005,87200,85698,91758,73485,88335,88344,89578,87321,88226,91762,85926,91678,92557,80427,78473,89027,85929,91608,87378,85778,10053,87073,87119,87914,84983,98010,88478,10299,96471,85341,96684,10246,97424,89197,96935,85809,100286,98684,88026,86222,88973,10223]
tourn_id = [11772,11772,10038,10621,10180,10364,10192,10401,10210,10537,10161,11057,8739,10691,10692,10844,10560,10680,10615,10196,11050,11148,9432,9270,10768,10197,11044,10569,10171,11564,10512,10519,10646,10037,11652,10701,12159,11254,10081,11552,10864,11622,10796,11447,10181,11877,11722,10663,10274,10763,12082]
for x in range (0,len(event_id)):
    website = 'https://www.tabroom.com/index/tourn/results/ranked_list.mhtml?event_id=' + str(event_id[x]) + '&tourn_id=' + str(tourn_id[x])
    tabroomRes = requests.get(website)
    tabroomSoup = bs4.BeautifulSoup(tabroomRes.text, features="html.parser")
    tournament_name = tabroomSoup.select('div > h2[class="centeralign marno"]')

    for elem in tournament_name:
        fh = open(str(event_id[x]) + '.txt', 'w')
        print(event_id[x])
        fh.write(tabroomRes.text)
        fh.close()