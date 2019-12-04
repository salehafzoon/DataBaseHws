
import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self._id = ""
      self.platform = ""
      self.name = ""
      self.genre = ""
      self.publisher = ""
      self.year_of_release = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "game":
         self._id = attributes["id"]
        

   # Call when an elements ends
   def endElement(self, tag):
      
      if self.CurrentData == "publisher" and self.platform == "PC":
         print self._id,";", self.name,";", self.publisher,";",self.genre,";",self.year_of_release
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "name":
         self.name = content
      elif self.CurrentData == "genre":
         self.genre = content
      elif self.CurrentData == "publisher":
         self.publisher = content
      elif self.CurrentData == "year_of_release":
         self.year_of_release = content
      elif self.CurrentData == "platform":
         self.platform = content
             
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("videogames.xml")