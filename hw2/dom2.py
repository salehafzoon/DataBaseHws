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

def make_sales_global(game):
    sales = game.getElementsByTagName('sales')[0]
    na_sales = sales.getElementsByTagName('na_sales')[0].childNodes[0].data
    eu_sales = sales.getElementsByTagName('eu_sales')[0].childNodes[0].data
    jp_sales = sales.getElementsByTagName('jp_sales')[0].childNodes[0].data
    other_sales = sales.getElementsByTagName('other_sales')[0].childNodes[0].data
    
    global_sales = 0
    global_sales = float(na_sales) + float(eu_sales) + float(jp_sales) + float(other_sales)

    global_sales_tag = xmldoc.createElement("global_sales")

    text = xmldoc.createTextNode(str(format(global_sales, '.2f') ))
    global_sales_tag.appendChild(text)

    game.removeChild(sales)
    game.appendChild( global_sales_tag )

def change_review_scores(game):
    review_scores = game.getElementsByTagName('review_scores')[0]

    critic_score = review_scores.getElementsByTagName('critic_score')[0]
    user_score = review_scores.getElementsByTagName('user_score')[0]
    critic_count = review_scores.getElementsByTagName('critic_count')[0]
    user_count = review_scores.getElementsByTagName('user_count')[0]

    critic_score_val = int(critic_score.childNodes[0].data)
    user_score_val = int(user_score.childNodes[0].data)
    critic_count_val = int(critic_count.childNodes[0].data)
    user_count_val = int(user_count.childNodes[0].data)
    
    avg_score = (critic_score_val * critic_count_val) + (user_score_val * user_count_val)/user_count_val + critic_count_val

    review_scores.removeChild(critic_score)
    review_scores.removeChild(user_score)
    review_scores.removeChild(critic_count)
    review_scores.removeChild(user_count)

    score_text = ""
    if avg_score > 80 :
        score_text = "very positive"
    elif avg_score > 60 :
        score_text = "mostly positive"
    elif avg_score > 40 :
        score_text = "mixed"
    elif avg_score > 20 :
        score_text = "mostly negative"
    else :
        score_text = "very negative"
        
        
    text = xmldoc.createTextNode(score_text)
    review_scores.appendChild(text)

for game in games:
    
    make_sales_global(game)
    change_review_scores(game)

with io.open("res.xml", "w", encoding="utf-8") as fs:
    fs.write(xmldoc.toxml())
    fs.close()
