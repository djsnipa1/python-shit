

with open('text.txt', 'r') as f:  # text file containing the URLS
  with open('anothertest.txt', 'a') as fout:
    for url in f:
      print(u"URL Line: {}".format(url.encode('utf-8')))

      0# you might want to remove endlines and whitespaces from
      # around the URL, which what strip() does
      article = Article(url.strip())
      article.download()
      article.parse()

      # write/append to file
      fout.write(article.title)
      fout.write(article.text)

      print(u"Title: {}".format(article.title.encode('utf-8')))

      # print authors only if there are authors to show.
      if len(article.authors) == 0:
        print('No author!')
      else:
        for author in article.authors:
          print(u"Author: {}".format(author.encode('utf-8')))

      print("Text of the article:")
      print(article.text.encode('utf-8'))
