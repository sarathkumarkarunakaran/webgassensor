import os

import cherrypy
from cherrypy.lib.static import serve_file
from urllib import urlopen
import urllib2


path   = os.path.abspath(os.path.dirname("__file__"))
tutconf = os.path.join(os.path.dirname("__file__"), 'app.conf')



class App:

  @cherrypy.expose
  def index(self):
    return serve_file(os.path.join(path, 'index.html')) 

  @cherrypy.expose
  @cherrypy.tools.json_out()
  def getData(self):
 
   #response = urllib2.urlopen("http://arduino.local/arduino/temperature")
   response = urllib2.urlopen("http://192.168.0.54")
   page_source = response.read()
   str = unicode(page_source, errors='replace')
   #print(page_source)
   return {
    'sensorData' : str
   }



if __name__ == '__main__':
  cherrypy.quickstart(App(), '/',tutconf)

