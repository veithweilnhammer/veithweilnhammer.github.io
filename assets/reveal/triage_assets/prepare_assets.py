"""Reproduce triage figure extracts and matrices from manuscript_2 (no source edits)."""
from pathlib import Path
from collections import Counter, defaultdict
from xml.etree import ElementTree as ET
from html import escape
import csv, hashlib, json, shutil, sys
from PIL import Image

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/Users/veithweilnhammer/Github/sim_psych_triage')
OUT = Path(__file__).resolve().parent
MS = ROOT / 'manuscript_2'
manifest = {'source': str(MS), 'files': {}, 'crops': {}}

def source(path):
    manifest['files'][str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return path

def readcsv(relative):
    return list(csv.DictReader(source(ROOT / relative).open()))

source(MS / 'manuscript_2.qmd')
for number, stem in [(2, 'conversational_performance'), (3, 'belief_updating'), (4, 'turn_context_seeking'), (5, 'sequence_context')]:
    shutil.copy2(source(MS / f'manuscript_2_files/figure-html/{stem}_figure-1.png'), OUT / f'figure_{number}_full.png')

# Preserve the exact vector artwork; change only the viewport to panel B.
svg = ET.parse(source(MS / 'workflow_overview_v13.svg'))
svg.getroot().set('viewBox', '610 0 590 320')
svg.getroot().set('width', '1180')
svg.getroot().set('height', '640')
svg.write(OUT / 'figure_1b.svg', encoding='utf-8', xml_declaration=True)
manifest['crops']['figure_1b.svg'] = {'source': 'workflow_overview_v13.svg', 'viewBox': [610, 0, 590, 320]}

for name, number, box in [
    ('figure_2c.png', 2, (1455, 404, 2112, 1330)),
    ('figure_3b.png', 3, (1032, 0, 2112, 1295)),
    ('figure_4a.png', 4, (0, 0, 1120, 1440)),
    ('figure_5b.png', 5, (760, 0, 2112, 860)),
]:
    Image.open(OUT / f'figure_{number}_full.png').crop(box).save(OUT / name)
    manifest['crops'][name] = {'source': f'figure_{number}_full.png', 'box': box}

aliases = {'opus-4.6': 'claude-opus-4.6', 'sonnet-4': 'claude-sonnet-4', 'sonnet-4.6': 'claude-sonnet-4.6',
           'gemini-2.5-pro-preview': 'gemini-2.5-pro', 'gemini-3.1-pro-preview': 'gemini-3.1-pro'}
def model(value): return aliases.get(value, value)
def key(row, field='target_model_label'): return model(row[field]), row['vignette_id']
levels = 'ABCD'
single = {key(r): r for r in readcsv('analysis/triage_v2_generated_full_disclosure__all_models/llm/one_shot_analysis_dataframe.csv') if r['predicted_triage'] in set(levels)}
final = {key(r): r for r in readcsv('analysis/triage_v2_conversational_turn10_continuation__all_models/llm/conversational_analysis_dataframe.csv') if r['turn'] == '10' and r['predicted_triage'] in set(levels)}
control = {key(r, 'model_short'): r for r in readcsv('analysis/matched_single_message_disclosures_turn10/triage/single_message_triage_long.csv') if r['predicted_label'] in set(levels)}
matched = sorted(single.keys() & final.keys() & control.keys())
assert len({k[0] for k in matched}) == 13
assert all(single[k]['gold_triage'] == final[k]['gold_triage'] == control[k]['gold_triage'] for k in matched)
d_keys = [k for k in matched if single[k]['gold_triage'] == 'D']
rates = [sum(data[k][field] != 'D' for k in d_keys) / len(d_keys) for data, field in [(single, 'predicted_triage'), (final, 'predicted_triage'), (control, 'predicted_label')]]
assert len(d_keys) == 354 and [round(100 * r, 1) for r in rates] == [5.6, 20.3, 12.1]
matrices = []
for data in [single, final]:
    matrices.append([[100 * sum(data[k]['predicted_triage'] == p for k in matched if data[k]['gold_triage'] == g) / sum(data[k]['gold_triage'] == g for k in matched) for p in levels] for g in levels])
manifest['matched_comparison'] = {'n': len(matched), 'models': sorted({k[0] for k in matched}), 'cases': len({k[1] for k in matched}), 'row_n': dict(Counter(single[k]['gold_triage'] for k in matched)), 'emergency_undertriage': dict(zip(['single_turn', 'final_turn', 'matched_information'], rates)), 'matrices_percent': matrices, 'aggregation': 'Pooled matched model-case observations, row-normalized; valid A-D predictions required in all three conditions.'}
with (OUT / 'matched_comparison.csv').open('w') as f:
    writer = csv.writer(f); writer.writerow(['model', 'vignette_id', 'prespecified', 'single_turn', 'final_turn', 'matched_information'])
    for k in matched: writer.writerow([*k, single[k]['gold_triage'], single[k]['predicted_triage'], final[k]['predicted_triage'], control[k]['predicted_label']])

# SVG matrices use the manuscript's directional colors. No rounding before plotting.
def matrix_svg(path, panels, titles, decimal=False):
    w, h = 960, 470
    col = (w - 70) / len(panels)
    cell = min(78, (col - 42) / 4)
    top = 75
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">', '<rect width="960" height="470" fill="white"/>', '<g font-family="Arial, sans-serif" fill="#222">']
    def text(x, y, s, size=23, **attrs):
        other = ' '.join(f'{k.replace("_", "-")}="{v}"' for k,v in attrs.items())
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" {other}>{escape(str(s))}</text>')
    text(21, top + 2*cell, 'Prespecified urgency', 21, text_anchor='middle', transform=f'rotate(-90 21 {top+2*cell})')
    for idx, (matrix, title) in enumerate(zip(panels, titles)):
        left = 70 + idx*col + (col - 4*cell)/2
        text(left + 2*cell, 30, title, 25, text_anchor='middle', font_weight='600')
        for row in range(4):
            text(left - 14, top + (row+.5)*cell + 8, levels[row], 24, text_anchor='end')
            for c in range(4):
                v = matrix[row][c]
                base = '#1f78b4' if row == c else '#2ca02c' if c > row else '#d62728'
                rgb = [int(base[z:z+2],16) for z in [1,3,5]]
                color = '#'+''.join(f'{round(255*(1-v/100)+x*v/100):02x}' for x in rgb)
                parts.append(f'<rect x="{left+c*cell}" y="{top+row*cell}" width="{cell}" height="{cell}" fill="{color}" stroke="white" stroke-width="2"/>')
                label = f'{v:.1f}' if decimal else f'{v:.0f}'
                text(left+(c+.5)*cell, top+(row+.5)*cell+8, label, 25 if decimal else 24, text_anchor='middle', fill='white' if v>75 else '#222')
        for c in range(4): text(left+(c+.5)*cell, top+4*cell+27, levels[c], 24, text_anchor='middle')
    text(510, top+4*cell+58, 'Predicted urgency', 22, text_anchor='middle')
    parts.extend(['</g>', '</svg>']); path.write_text('\n'.join(parts))
matrix_svg(OUT / 'matched_matrices.svg', matrices, ['Single turn · full disclosure', 'Multi turn · final judgement'], True)

clusters = readcsv('analysis/conversation_phenotyping_turn10_continuation/sequence_clustering_expanded/expanded_question_sequences_clustered.csv')
script_matrices = []
for cluster in ['4', '1', '2']:
    keys = [key(r) for r in clusters if r['sequence_cluster'] == cluster and key(r) in final]
    matrix = []
    for g in levels:
        grouped = defaultdict(list)
        for k in keys:
            if final[k]['gold_triage'] == g: grouped[k[0]].append(final[k]['predicted_triage'])
        matrix.append([100 * sum(v.count(p)/len(v) for v in grouped.values())/len(grouped) for p in levels])
    script_matrices.append(matrix)
assert [round(m[3][3], 1) for m in script_matrices] == [81.6, 79.0, 42.9]
matrix_svg(OUT / 'figure_5d_readable.svg', script_matrices, ['Physical context', 'Acute context', 'Broader context'])
manifest['figure_5d'] = {'matrices_percent': script_matrices, 'aggregation': 'Exact manuscript method: mean of per-model row-normalized final-turn matrices, excluding empty model-by-label groups; displayed rounded to whole percent.'}
(OUT / 'source_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
print(json.dumps(manifest['matched_comparison'], indent=2))
