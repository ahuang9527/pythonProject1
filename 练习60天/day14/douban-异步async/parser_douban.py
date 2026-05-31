# parser_douban.py

def parse_movie(movie_json):
    """解析单部电影的 JSON 数据，提取关键字段"""
    return {
        'title':        movie_json.get('title', ''),
        'score':        movie_json.get('score', ''),
        'rating':       movie_json.get('rating', ['', '']),
        'types':        movie_json.get('types', []),
        'regions':      movie_json.get('regions', []),
        'release_date': movie_json.get('release_date', ''),
        'vote_count':   movie_json.get('vote_count', 0),
        'actors':       movie_json.get('actors', []),
        'url':          movie_json.get('url', ''),
        'rank':         movie_json.get('rank', 0),
    }
# 字段来源：[reference:9]