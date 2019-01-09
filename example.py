import scholarly as sc


title = 'The interaction of maturational constraints and intrinsic motivations in active motor development'

print 'Searching for',title
sq = sc.search_pubs_query(title)

pp = next(sq)

print 'Found: ',pp.bib['title']

print
print 'Searching cited by'
cb = pp.get_citedby()

print
print 'Data from citations'
for citation in cb:
	print 'Article\t\t',citation.bib['title']
	print 'Authors\t\t',citation.bib['author']
	print 'Volume\t\t',citation.bib['volume']
	print 'Publisher\t\t',citation.bib['publisher']
	print
