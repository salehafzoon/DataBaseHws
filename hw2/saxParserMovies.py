
#!/usr/bin/python3

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""
      self._id = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "movie":
         self.title = attributes["title"]
        

   # Call when an elements ends
   def endElement(self, tag):
      # if self.CurrentData == "type":
      #    print ("Type:", self.type)
      # elif self.CurrentData == "format":
      #    print ("Format:", self.format)
      # elif self.CurrentData == "year":
      #    print ("Year:", self.year)
      # elif self.CurrentData == "rating":
      #    print ("Rating:", self.rating)
      # elif self.CurrentData == "stars":
      #    print ("Stars:", self.stars)
      if self.CurrentData == "description":
         print "title:", self.title,"type:", self.type,"format:", self.format
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("movies.xml")