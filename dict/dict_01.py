singer = {}

singer['이름'] = '트와이스'
singer['구성원 수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

# singer.keys() : dict_keys(['이름', '구성원 수', '데뷔', '대표곡'])
for k in singer.keys() :
    print(f'{k} --> {singer[k]}')

print(list(singer.keys()))

