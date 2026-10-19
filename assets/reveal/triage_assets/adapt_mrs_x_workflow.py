"""Adapt the editable workflow illustration to the presentation's Mrs. X example.

This changes the illustrated case, not the experimental case library or results.
The author-requested D label is retained for this authored example: she plans to break into the perceived agent’s house.
"""
from pathlib import Path
from lxml import etree

folder = Path(__file__).resolve().parent
svg = etree.parse(str(folder / 'figure_1b.svg'))
root = svg.getroot()
def by_id(identifier):
    return root.xpath('//*[@id=$identifier]', identifier=identifier)[0]

# Retain only the design-space panel and its shared definitions.
children = list(root)
first = children.index(by_id('text21'))
last = children.index(by_id('g72'))
for index, node in enumerate(children):
    if not first <= index <= last and etree.QName(node).localname not in ('defs', 'title', 'desc'):
        root.remove(node)
for identifier in ['text21', 'rect51', 'text70']:
    node = by_id(identifier)
    node.getparent().remove(node)
# Keep the source design-space dots and generation/review workflow unchanged.
updates = {
    'text22': 'Design space and vignette construction',
    'text63': 'Emergency now',
    'text65': 'Mrs. X · psychosis',
    'text66': 'Neighbour’s voice',
    'text67': 'Heard beyond the apartment',
    'text68': 'Convinced he is an agent',
    'text69': 'Plans to break into his house',
}
for identifier, text in updates.items():
    by_id(identifier).text = text
for identifier in ['text66','text67','text68','text69']:
    by_id(identifier).set('style', 'font-size:10px')
by_id('rect62').set('fill', '#fff4f2')
by_id('text64').set('style', 'fill:#fff')
by_id('text65').set('style', 'font-size:11px;letter-spacing:.4px')
by_id('text69').set('style', 'font-size:10px;font-weight:700;fill:#b8322a')
by_id('text63').set('y', '34')
# Retain the author-assigned D badge for Mrs. X’s presentation example.
by_id('title').text = 'Vignette construction with a Mrs. X psychosis example'
by_id('desc').text = 'Presentation by risk-domain families feed LLM-assisted generation and review of 112 case files. The example depicts Mrs. X hearing her neighbour’s voice beyond the apartment, believing he is an agent following her, and planning to break into his house to find out what is going on. The case is labelled D, emergency now.'
root.set('viewBox', '610 35 590 278')
root.set('width', '1180')
root.set('height', '556')
svg.write(str(folder / 'vignette_mrs_x.svg'), encoding='utf-8', xml_declaration=True, pretty_print=True)
