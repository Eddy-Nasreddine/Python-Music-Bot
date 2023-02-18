import validators
from youtube_search import YoutubeSearch 

class Song:
    def __init__(self,song,ctx):
        self.ctx = ctx
        self.song = song
        self.results = YoutubeSearch(str(song), max_results=1).to_dict()
        
    def get_ctx(self):
        
        return self.ctx
    def get_title(self):
        return self.results[0]["title"]
    
    def get_url(self):
        self.valid = validators.url(self.song)
        if not self.valid:
            return "https://www.youtube.com" + self.results[0]["url_suffix"]
        return self.song
        
    def get_thumbnail(self):
        return self.results[0]["thumbnails"][0]
    
    def get_duration(self):
        return self.results[0]["duration"]