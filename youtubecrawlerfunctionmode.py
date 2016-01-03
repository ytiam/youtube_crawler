def youtube_crawler(search_term):
    

    from apiclient.discovery import build #pip install google-api-python-client
    from apiclient.errors import HttpError #pip install google-api-python-client
    from oauth2client.tools import argparser #pip install oauth2client
    import pandas as pd
    import argparse
    
    
    
    DEVELOPER_KEY = "your youtube_api key"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", help="Search term", default=search_term)
    parser.add_argument("--max-results", help="Max results", default=50)
    #default number of results which are returned. Google free api has max limit as 50
    args = parser.parse_args()
    options = args
    
    
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    
    # Call the search.list method to retrieve results matching the specified
     # query term.
    search_response = youtube.search().list(
     q=options.q,
     type="video",
     part="id,snippet",
     maxResults=options.max_results
    ).execute()
    
    
    videos = {}
    
    # Add each result to the appropriate list, and then display the lists of
     # matching videos.
     # Filter out channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]
     
     
     
     
    s = ','.join(videos.keys())
    
    
    videos_list_response = youtube.videos().list(
     id=s,
     part='id,statistics'
    ).execute()
    
    
    res = []
    for i in videos_list_response['items']:
        temp_res = dict(v_id = i['id'], v_title = videos[i['id']])
        temp_res.update(i['statistics'])
        res.append(temp_res)
     
     
    res=pd.DataFrame.from_dict(res)
    
    return(res)



if __name__ == "__main__":
    youtube_crawler()
