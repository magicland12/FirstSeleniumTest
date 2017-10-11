import webbrowser


new=2

tabUrl='https://google.com/?#q='

term= input('Enter search query: ')

webbrowser.open(tabUrl+term, new=new)
