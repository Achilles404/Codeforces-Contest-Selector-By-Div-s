import requests

url = "http://codeforces.com/api"
options = '/contest.list'
link = 'http://codeforces.com/contest/'

data = requests.get(url+options)
data = data.json()

edu = []
div1 = []
div2 = []
div3 = []
div4 = []

if data['status'] == 'OK':
    data = data['result']
    for i in data:
        if 'Educational' in i['name']:
            edu.append(int(i['id']))

        if ('Div. 1' in i['name']) & ('Div. 2' not in i['name']):
            div1.append(int(i['id']))

        if ('Div. 2' in i['name']) & ('Educational' not in i['name']) &  ('Div. 1' not in i['name']):
            div2.append(int(i['id']))

        if 'Div. 3' in i['name']:
            div3.append(int(i['id']))

        if 'Div. 4' in i['name']:
            div4.append(int(i['id']))


    edu.sort()
    div1.sort()
    div2.sort()
    div3.sort()
    div4.sort()

    f = open("educational.txt","w+")
    cnt = 1
    for i in edu:
        temp = 'Educational Round '
        temp += str(cnt)
        temp += ':  '
        temp += link+str(i)
        temp += '\n'
        f.write(temp)
        cnt+=1
    f.close()

    f = open("div1.txt","w+")
    cnt = 1
    for i in div1:
        temp = 'Div1 '
        temp += str(cnt)
        temp += ':  '
        temp += link+str(i)
        temp += '\n'
        f.write(temp)
        cnt+=1
    f.close()

    f = open("div2.txt","w+")
    cnt = 1
    for i in div2:
        temp = 'Div2 '
        temp += str(cnt)
        temp += ':  '
        temp += link+str(i)
        temp += '\n'
        f.write(temp)
        cnt+=1
    f.close()

    f = open("div3.txt","w+")
    cnt = 1
    for i in div3:
        temp = 'Div3 '
        temp += str(cnt)
        temp += ':  '
        temp += link+str(i)
        temp += '\n'
        f.write(temp)
        cnt+=1
    f.close()

    f = open("div4.txt","w+")
    cnt = 1
    for i in div4:
        temp = 'Div4 '
        temp += str(cnt)
        temp += ':  '
        temp += link+str(i)
        temp += '\n'
        f.write(temp)
        cnt+=1
    f.close()

else:
    print('There may be some issues on Codeforces or the servers or not responding');
    print('Please Wait and try it after few minutes');