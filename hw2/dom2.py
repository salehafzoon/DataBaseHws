from xml.dom import minidom
import io
xmldoc = minidom.parse("videogames.xml")

ratings = xmldoc.getElementsByTagName("rating")
plat_type = xmldoc.getElementsByTagName("platform_type")
games = xmldoc.getElementsByTagName("game")

for node in ratings:
    parent = node.parentNode
    parent.removeChild(node) 

for node in plat_type:
    parent = node.parentNode
    parent.removeChild(node) 


for game in games:
    
    sales = game.getElementsByTagName('sales')[0]
    na_sales = sales.getElementsByTagName('na_sales')[0].childNodes[0].data
    eu_sales = sales.getElementsByTagName('eu_sales')[0].childNodes[0].data
    jp_sales = sales.getElementsByTagName('jp_sales')[0].childNodes[0].data
    other_sales = sales.getElementsByTagName('other_sales')[0].childNodes[0].data
    
    global_sales = 0
    global_sales = float(na_sales) + float(eu_sales) + float(jp_sales) + float(other_sales)

    global_sales_tag = xmldoc.createElement("global_sales")

    text = xmldoc.createTextNode(str(global_sales))
    global_sales_tag.appendChild(text)

    # game.removeChild(sales)
    game.appendChild( global_sales_tag )


    # review_scores = game.getElementsByTagName('review_scores')[0]
    # critic_score = review_scores.getElementsByTagName('critic_score')[0].childNodes[0].data

    # review_scores = game.getElementsByTagName('review_scores')
    # print(critic_score)

with io.open("res.xml", "w", encoding="utf-8") as fs:
    fs.write(xmldoc.toxml())
    fs.close()

# print(xmldoc.toxml())