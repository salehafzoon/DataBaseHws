<?xml version = "1.0" encoding = "UTF-8"?>
<xsl:stylesheet version = "1.0" 
xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">   
   <xsl:template match = "/"> 
		
      <html> 
         <body> 
            <h2>Video Games</h2> 
				
            <table border = "1"> 
               <tr border = "1"> 
                  <th>Name</th> 
                  <th>Platform</th> 
                  <th>Year of Release</th> 
                  <th>Genre</th> 
                  <th>Publisher</th> 
                  <th>Developer</th> 
                  <th>Global Sales</th> 
                  <th>Review Scores</th> 
               </tr> 
				
               <xsl:for-each select="video_games/game"> 
                  <tr> 
                     <td>
                        <xsl:value-of select = "@id"/> 
                     </td> 
						
                     <td><xsl:value-of select = "name"/></td> 
                     <td><xsl:value-of select = "platform"/></td> 
                     <td><xsl:value-of select = "year_of_release"/></td> 
                     <td><xsl:value-of select = "genre"/></td> 
                     <td><xsl:value-of select = "publisher"/></td> 
                     <td><xsl:value-of select = "developer"/></td> 
                     <td><xsl:value-of select = "global_sales"/></td> 
                     <td><xsl:value-of select = "review_scores"/></td> 
                     
                  </tr> 
               </xsl:for-each> 
					
            </table> 
         </body> 
      </html> 
   </xsl:template>  
</xsl:stylesheet>