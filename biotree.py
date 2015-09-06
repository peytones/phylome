def bio_tree():
    from collections import OrderedDict
    from Bio import Entrez
    from ete2 import NCBITaxa, PhyloTree
    from lxml import etree

    Entrez.email = 'peytonsarmiento@gmail.com'
    ncbi = NCBITaxa()
    names = str(raw_input('Enter species names: '))
    names = map(lambda x:x.strip(), names.split(','))
    ids = []
    for name in names:
        handle = Entrez.esearch(db='taxonomy', term=name)
        while True:
            line = handle.readline()
            if not line: break
            if '<Id>' in line:
                ids.append(int(line.strip('<Id></Id>\n')))
    scientific_tree = ncbi.get_topology(ids)
    print scientific_tree.get_ascii(attributes=['sci_name','rank', 'name'])
    species =  ncbi.get_common_names(ids)
    species = OrderedDict(sorted(species.items() ,key=lambda t:t[0]))
    scientific_species = ncbi.get_taxid_translator(ids)
    scientific_species = OrderedDict(sorted(scientific_species.items(), key=lambda t:t[0]))
    scientific_s = []
    s = []
    for keys,values in species.items():
        s.append(values)
    for keys, values in scientific_species.items():
        scientific_s.append(values)
    for i in range(len(s)):
        print scientific_s[i] + ' : ' + s[i]

bio_tree()
