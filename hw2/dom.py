
from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("videogames2.xml")
file_handle = open("videogames2.xml","wb")

collection = DOMTree.documentElement

games = collection.getElementsByTagName("game")

for game in games:
      
      # sales = game.getElementsByTagName('sales')[0]

      # na_sales = sales.getElementsByTagName('na_sales')[0].childNodes[0].data
      # eu_sales = sales.getElementsByTagName('eu_sales')[0].childNodes[0].data
      
      # print(na_sales)
      
      
      review_scores = game.getElementsByTagName('review_scores')[0]

      critic_score = review_scores.getElementsByTagName('critic_score')[0].childNodes[0].data
      user_score = review_scores.getElementsByTagName('user_score')[0].childNodes[0].data
      
      critic_count = review_scores.getElementsByTagName('critic_count')[0].childNodes[0].data
      user_count = review_scores.getElementsByTagName('user_count')[0].childNodes[0].data
      
      avg_score = (critic_score * critic_count) + (user_score * user_count)/user_count + critic_count


      review_scores.createElement("avg")

collection