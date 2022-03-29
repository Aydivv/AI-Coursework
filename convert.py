f = open('data.csv','r+')

data = f.read()


data = data.replace('\t',',')

f.write(data)

f.close()

