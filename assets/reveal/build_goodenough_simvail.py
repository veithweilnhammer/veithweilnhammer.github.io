"""Append the SIM-VAIL slides to the unchanged Goodenough Reveal deck."""

from copy import deepcopy
from pathlib import Path

from lxml import etree, html


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "goodenough_simvail.html"

goodenough = (HERE / "talk_goodenough.html").read_text(encoding="utf-8")
sim_document = html.parse(str(HERE / "simvail_lambda.html"))
sim_slides = sim_document.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " slides ")]/section')


def prepare(section):
    section = deepcopy(section)
    for part in [section, *section.xpath(".//section")]:
        part.set("class", (part.get("class", "") + " simvail-slide").strip())
        if part.get("data-background-color"):
            part.attrib.pop("data-background-color")
    leaves = section.xpath(".//section[not(section)]") if section.xpath("./section") else [section]
    for leaf in leaves:
        wrapper = etree.Element("div", {"class": "simvail-fit"})
        wrapper.text = leaf.text
        leaf.text = None
        for child in list(leaf):
            if child.tag == "aside" and "notes" in child.get("class", "").split():
                continue
            leaf.remove(child)
            wrapper.append(child)
        leaf.insert(0, wrapper)
    return section


sim_markup = "\n".join(
    html.tostring(prepare(section), encoding="unicode", method="html")
    for section in sim_slides
)

css = """
<style id="simvail-appended-styles">
  /* SIM-VAIL components inherit the Goodenough deck's white theme and type. */
  .simvail-slide { --accent: #2a6496; --accent-light: #e8f0fa; --risk-high: #c0392b; --risk-low: #27ae60; }
  .simvail-slide .muted { color: #777; font-weight: 400; }
  .simvail-slide .small { font-size: .8em; line-height: 1.35; }
  .simvail-slide .xsmall { font-size: .7em; line-height: 1.35; }
  .simvail-slide .tight p { margin: .35em 0; }
  .simvail-slide img.borderless, .simvail-slide video.borderless { background: none; border: none; box-shadow: none; }
  .simvail-slide .twocol { display: flex; align-items: center; gap: 2rem; }
  .simvail-slide .col { flex: 1; }
  .simvail-slide .center { text-align: center; }
  .simvail-slide .fig-full { max-height: 680px; width: auto; max-width: 100%; }
  .simvail-slide .look-for { font-size: .6em; color: #444; margin-top: .2em; text-align: left; }
  .simvail-slide .look-for li { margin-bottom: .15em; }
  .simvail-slide.section-divider { background: transparent; color: #222; }
  .simvail-slide.section-divider h2, .simvail-slide.section-divider h3 { color: #222; }
  .simvail-slide.section-divider .muted { color: #777; }
  .simvail-slide .accent-box { background: transparent; border-left: 3px solid #aaa; padding: .55em 1em; margin: .5em 0; }
  .simvail-slide .risk-high { color: var(--risk-high); font-weight: 700; }
  .simvail-slide .risk-low { color: var(--risk-low); font-weight: 700; }

  /* Only appended slides use a fit layer. Goodenough markup and layout stay native. */
  .reveal .slides section.simvail-slide:not(.stack) { height: 700px !important; }
  .reveal .slides section.simvail-slide > .simvail-fit {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 960px;
    max-width: none;
    transform: translate(-50%, -50%) scale(var(--fit-scale, 1));
    transform-origin: center center;
  }
</style>
"""

fit_script = """
<script id="simvail-appended-fit">
  function fitAppendedSlide(slide) {
    if (!slide || !slide.classList.contains('simvail-slide')) return;
    const content = Array.from(slide.children).find(child => child.classList.contains('simvail-fit'));
    if (!content) return;
    const slideRect = slide.getBoundingClientRect();
    if (!slideRect.width || !slideRect.height) return;
    content.style.setProperty('--fit-scale', '1');
    const centerX = slideRect.left + slideRect.width / 2;
    const centerY = slideRect.top + slideRect.height / 2;
    let extentX = 0;
    let extentY = 0;
    for (const node of content.querySelectorAll('*')) {
      const rect = node.getBoundingClientRect();
      if (!rect.width && !rect.height) continue;
      extentX = Math.max(extentX, Math.abs(rect.left - centerX), Math.abs(rect.right - centerX));
      extentY = Math.max(extentY, Math.abs(rect.top - centerY), Math.abs(rect.bottom - centerY));
    }
    const ownRect = content.getBoundingClientRect();
    extentX = Math.max(extentX, ownRect.width / 2);
    extentY = Math.max(extentY, ownRect.height / 2);
    const scale = Math.min(1, slideRect.width * .47 / extentX, slideRect.height * .46 / extentY);
    content.style.setProperty('--fit-scale', String(scale));
  }
  function fitCurrentAppendedSlide() { fitAppendedSlide(Reveal.getCurrentSlide()); }
  Reveal.on('ready', fitCurrentAppendedSlide);
  Reveal.on('slidechanged', () => requestAnimationFrame(fitCurrentAppendedSlide));
  window.addEventListener('resize', fitCurrentAppendedSlide);
  document.querySelectorAll('.simvail-fit img, .simvail-fit video').forEach(media => {
    media.addEventListener('load', () => fitAppendedSlide(media.closest('section')));
    media.addEventListener('loadedmetadata', () => fitAppendedSlide(media.closest('section')));
  });
</script>
"""

goodenough = goodenough.replace("</head>", css + "\n</head>", 1)
closing = '\n\t\t</div>\n\n\t\t<script src="dist/reveal.js"></script>'
assert goodenough.count(closing) == 1
goodenough = goodenough.replace(closing, "\n\n<!-- SIM-VAIL slides appended after Goodenough -->\n" + sim_markup + closing, 1)
goodenough = goodenough.replace("\n\t</body>", fit_script + "\n\t</body>", 1)
OUTPUT.write_text(goodenough, encoding="utf-8")
print(OUTPUT)
