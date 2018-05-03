# combine script 1 and 2 using try and except
word= "cat"
url= 'https://www.google.co.in/search?q=define%20' +word+ '#cns=1'
response = requests.get(url, headers={"user-agent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0"})

html= response.content
final_soup = BeautifulSoup(html,"html5lib")
example = ""
try:
    example =final_soup.find('div',{'class':'bkWMgd'}).find('div',{'class':'ifM9O'}).find('div',{'class':'qtR3Y'}).find('span').text
    print(example)
except:
    pass   
try:
    example =final_soup.find('div',{'class':'g knavi obcontainer mod'}).findAll('div',{'class':'lr_dct_ent vmod'})[0].find('div',{'class':'PNlCoe'}).find('span').text
    print(example)
except:
    print("Please check the word again")