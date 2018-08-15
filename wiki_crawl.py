import requests

def html_crawl(key1,content):

    wiki_indx = [i+len(key1) for i, j in enumerate(content) if content[i:i+len(key1)] == key1]

    wiki_titles = []
    end_key = '">'
    for ii,indx in enumerate(wiki_indx):
        for mm in range(0,200):
            if content[indx+mm:indx+mm+len(end_key)]==end_key:
                wiki_titles.append(content[indx:indx+mm])
                break

    return wiki_titles

def wiki_crawl():
    page = requests.get('https://en.wikipedia.org/wiki/Special:RecentChanges?hidebots=0&hidecategorization=1&hideWikibase=1&hidelog=1&limit=50&days=1&urlversion=1')
    content = page.text
    key1 = 'class="mw-changeslist-diff" title="'

    wiki_edits = html_crawl(key1,content)
    return wiki_edits

if __name__=="__main__":
    wiki_edits = wiki_crawl()
