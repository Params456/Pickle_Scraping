import requests,json,os
from bs4 import BeautifulSoup
from pprint import pprint

os=os.path.exists("Pickle.json")
if os:
	with open ("Pickle.json","r") as files:
		names=json.loads(json.load(files))
	pprint(names)
	cash=[i["cash"] for i in names]
	cash1=set(cash)
	Rupees={j:[names[i] for i in range(len(cash)) if j==cash[i]] for j in cash1}
	pprint(Rupees)
	Input=input("Enter the cash: ")
	for k in Rupees:
		if Input==k:
			pprint(Rupees[k])

else:
	a=requests.get("https://paytm.com/shop/search?q=pickles&from=organic&child_site_id=1&site_id=1&category=101471")
	print(a)
	soup=BeautifulSoup(a.text,"html.parser")
	tbody=soup.find("div",class_="_3RA-")
	# print(tbody.text)
	tr=tbody.find_all("div",class_="_2i1r")
	list1=[]
	for i in tr:
		dict1={}
		url=i.find("a")["href"]
		dict1["img_url"]=url
		cash=i.find("div",class_="_27VV")
		dict1["cash_back"]=cash.text[:3]
		rs=i.find("span",class_="_1kMS")
		dict1["cash"]=rs.text[3:]
		name=i.find("div",class_="_2apC")
		dict1["name"]=name.text[:-3]
		names=name.text.split("Pickle")
		dict1["Kg"]=names[-1]
		list1.append(dict1)
	pprint(list1)

	with open("Pickle.json","w+") as pickle:
		paran=json.dumps(list1)
		params=json.dump(paran,pickle)

	cash=[i["cash"] for i in list1]
	cash1=set(cash)
	Rupees={j:[names[i] for i in range(len(cash)) if j==cash[i]] for j in cash1}
	pprint(Rupees)
	Input=input("Enter the cash: ")
	for k in Rupees:
		if Input==k:
			pprint(Rupees[k])