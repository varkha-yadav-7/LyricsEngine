from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import HttpResponse
import requests

def homepage(request):
    url='https://www.lyricsmint.com/'
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    soup=soup.find('div',{'class':"flex flex-wrap m-0 overflow-hidden"})
    a=[]
    for i in soup.find_all('a'):
        dict={}
        dict['link']='https://www.lyricsmint.com'+i['href']
        dict['img']=i.find('img')['src']
        dict['text']=i.text
        a.append(dict)
    return render(request,'homepage.html',{'a':a})

def search(request):
    page=request.POST.get('page')
    url='https://www.lyricsmint.com/search?utf8=%E2%9C%93&query='
    if page!=None:
        url=url+page
    else:
        query=request.POST.get('search')
        query=query.replace(' ','+')
        query=query.lower()
        url=url+query
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    soup=soup.find('div',{'class':'container mx-auto my-2'})
    a=[]
    for i in soup.find_all('a'):
        dict={}
        try:
            dict['link']='https://www.lyricsmint.com'+i['href']
        except:
            pass
        try:
            dict['h3']=i.find('h3').text
        except:
            pass
        try:
            dict['span1']=i.find_all('span')[0].text
        except:
            pass
        try:
            dict['span2']=i.find_all('span')[1].text
        except:
            pass
        try:
            dict['span3']=i.find_all('span')[2].text
        except:
            pass
        try:
            dict['span4']=i.find_all('span')[3].text
        except:
            pass
        try:
            s=i.find_all('div')[1]['style']
            s=s[22:-2]
            dict['img']=s
        except:
            pass
        a.append(dict)
    ex={'4':url+'&page=4','3':url+'&page=3','2':url+'&page=2','1':url}
    return render(request,'artists.html',{'artist':a,'e':ex,'h2':'Search Results','footer':'yes'})

def lyrics(request):
    next=request.POST.get('next')
    url=''
    if next==None:
        url=request.POST.get('link')
    else:
        url='https://www.lyricsmint.com'+next
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    more=[]
    h3=soup.find('h3',{'class':"text-base uppercase pb-2 md:pb-4"}).text
    mor=soup.find('div',{'class':"container mx-auto related mt-5 text-center md:text-left"})
    for i in mor.find_all('a'):
        dict={}
        dict['text']=i.text
        dict['link']=i['href']
        more.append(dict)
    inf=[]
    info=soup.find('section',{'class':'credits px-5 pt-5'})
    for i in info.find_all('tr'):
        s=''
        for j in i.find_all('td'):
            s=s+j.text+' : '
        inf.append(s[:-2])
    back=soup.find('section',{'class':'relative font-sans h-auto w-full bg-black text-white flex flex-col justify-center bg-black bg-center bg-no-repeat bg-cover'})['style']
    soup=soup.find('div',{'class':'text-base lg:text-lg pb-2 text-center md:text-left'})
    ly=[]
    for i in soup.find_all('p'):
        ly.append(i.text)
    back=back[22:]
    back=back[:back.index('background')]
    back=back[:-3]
    return render(request,'result.html',{'lyrics':ly,'back':back,'info':inf,'h':h3,'more':more})

def collections(request):
    query=request.POST.get('search')
    url='https://www.lyricsmint.com/collections'+query
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    soup=soup.find('div',{'class':"block w-full md:w-3/5 md:pr-5"})
    h2=soup.find('h2').text
    a=[]
    for i in soup.find_all('div',{'class':'flex-no-grow flex-no-shrink w-full h-auto overflow-hidden shadow m-0 mb-5 rounded-xl st-bg-gradient-2'}):
        dict={}
        try:
            dict['h3']=i.find('h3').text
        except:
            pass
        try:
            dict['span2']=i.find_all('span')[0].text
        except:
            pass
        try:
            dict['span3']=i.find_all('span')[1].text
        except:
            pass
        try:
            dict['span4']=i.find_all('span')[2].text
        except:
            pass
        try:
            dict['img']=i.find('img')['src']
        except:
            pass
        try:
            dict['link']='https://www.lyricsmint.com'+i.find('a')['href']
        except:
            pass
        a.append(dict)
    return render(request,'artists.html',{'artist':a,'h2':h2})
