def bio_tree(names):
    from collections import OrderedDict
    from Bio import Entrez
    from ete2 import NCBITaxa, PhyloTree
    from lxml import etree

    Entrez.email = 'peytonsarmiento@gmail.com'
    ncbi = NCBITaxa()
    ids = []
    for name in names:
        handle = Entrez.esearch(db='taxonomy', term=name)
        while True:
            line = handle.readline()
            if not line: break
            if '<Id>' in line:
                ids.append(int(line.strip('<Id></Id>\n')))
    scientific_tree = ncbi.get_topology(ids)
    return scientific_tree.get_ascii(attributes=['sci_name'])
