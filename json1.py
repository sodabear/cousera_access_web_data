import json
import urllib

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

'''
input = 
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  } 
]

'''

info = json.loads(html)
print 'User count:', len(info)

list_comments = info["comments"]
_sum = 0
Retrieved = 0 
for item in list_comments:
    print 'Name', item['name']
    Retrieved += len(item['name'])
    print 'Count', item['count']
    _sum += item['count']

print "Sum",_sum
print "Retrieved",Retrieved
