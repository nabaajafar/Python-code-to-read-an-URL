import requests
r =requests.get('https://www.google.com')
print (r.text)
file = open("url Data.txt","w")

file.write(r.text)

file.close()
