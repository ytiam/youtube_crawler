from youtubecrawlerfunctionmode import youtube_crawler

import urllib, json

def youtube(search_term):

    DEVELOPER_KEY = "your youtube-api key"
    
    
    crawleddata=youtube_crawler(search_term)
    
    dic_link_com={}
    
    for i in range(0,len(crawleddata)):
    
        link_id=crawleddata['v_id'][i]
    
    
        url=("https://www.googleapis.com/youtube/v3/commentThreads?key="+DEVELOPER_KEY+"&textFormat=plainText&part=snippet&videoId="+link_id+'&maxResults='+'100').encode("ascii","ignore")
    
        response = urllib.urlopen(url)
    
        data = json.loads(response.read())
        
        dic_com={}
        
        if str(data.keys()[0])=="error":
            dic_com=dic_com
        else:
        
            for k in range(0,data['pageInfo']['totalResults']):
    
                comment=data['items'][k]['snippet']['topLevelComment']['snippet']['textDisplay'].encode('ascii','ignore')
                name=data['items'][k]['snippet']['topLevelComment']['snippet']['authorDisplayName'].encode('ascii','ignore')
                dic_com[name]= comment
        
        dic_link_com[link_id]=dic_com
        
    
    final_output=[crawleddata,dic_link_com]
    
    return(final_output)
    


if __name__ == "__main__":
    #youtube_crawler()
    youtube()
