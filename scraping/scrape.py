import urllib2  # Python module used for fetching URLs

# make http request
response = urllib2.urlopen('file:///opt/ActivePerl-5.18/html/index.html')
print "Response:", response

# URL of the resource retrieved, commonly used to determine if a redirect was followed
print "The URL is:", response.geturl()

# return the HTTP status code of the response
print "The code is:", response.code

# meta-info of the page in the for of a mimetools.Message
print "The Header-info is:", response.info()

# Date part of header
#print "The Date is:", response.info()['date']
#print "The Date is:", headers['date']

# Server part of header
#print "The Server is:", response.info()['server']

html = response.read()
print "Get all data:\n", html
print "Get the length:\n", len(html)

# show that file object is iterable
for line in response:
  print line.rstrip()

response.close()

