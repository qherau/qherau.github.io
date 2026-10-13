#!/usr/bin/env python3
"""Build Quentin's portable personal page. No Git writes or publication."""
from pathlib import Path
from html import escape
import hashlib
import json

ROOT = Path(__file__).resolve().parent
SITE = ROOT if (ROOT / 'assets').is_dir() else ROOT / 'Personal'
STYLE_VERSION = hashlib.sha256((SITE / 'assets/personal.css').read_bytes()).hexdigest()[:12]
SCHOLAR = 'https://scholar.google.com/citations?user=dxHTZAkAAAAJ&hl=en'
BASE = ['Quentin Herau', 'Nathan Piasco', 'Moussab Bennehar', 'Luis Roldão', 'Dzmitry Tsishkou', 'Cyrille Migniot', 'Pascal Vasseur', 'Cédric Demonceaux']
PAPERS = [
 dict(name='STRIKE', year=2026, venue='Preprint · 2026', topic='worlds', title='STRIKE: Learning Visual State Transitions for Physical World Modeling', authors=['Wenbin Teng','Tianshuo Xu','Depu Meng','Yuelei Li','Quentin Herau','Yihan Hu','Yajie Zhao','Wei Zhan'], description='Predict scene changes through learned visual state transitions, then generate the intervening video.', image='strike-teaser.png', alt='Published STRIKE comparison: a robotic gripper attaches to a cube before lifting it, using learned visual transitions.', paper='https://arxiv.org/abs/2610.09514', project='https://strike-applied.github.io/'),
 dict(name='S2Tok', year=2026, venue='Preprint · 2026', topic='reconstruction', title='S2Tok: Streaming 3D Gaussian Reconstruction with Persistent Spatial Tokens', authors=['Fang Li','Jiraphon Yenphraphai','Quentin Herau','Depu Meng','Yihan Hu','Tianshuo Xu','Narendra Ahuja','Wei Zhan'], description='Maintain persistent spatial tokens as new images arrive, then decode them into 3D Gaussians.', image='s2tok-teaser.jpg', alt='Published S2Tok reconstructions of outdoor, indoor and AI-generated scenes from sequential images.', paper='https://arxiv.org/abs/2610.08978', project='https://s2tok.github.io/', code='https://github.com/Applied-Intuition-Open-Source/S2Tok'),
 dict(name='Building Rome', year=2026, venue='Preprint · 2026', topic='reconstruction', title='Building Rome from a Single Image', authors=['Jiraphon Yenphraphai','Fang Li','Tianshuo Xu','Depu Meng','Quentin Herau','Yihan Hu','Raymond A. Yeh','Wei Zhan'], description='Generate complete indoor and outdoor scene meshes from one image using adaptive spatial chunks.', image='building-rome-teaser.jpg', alt='Published Building Rome reconstruction of the Colosseum, shown with surface normals and a 47 metre height annotation.', paper='https://arxiv.org/abs/2610.08790', project='https://build-rome.github.io/', code='https://github.com/Applied-Intuition-Open-Source/BuildRome'),
 dict(name='ReMind', year=2026, venue='NeurIPS 2026', topic='worlds', title='Teaching Video Generators to Remember: Eliciting Dynamic Memory for Out-of-Sight State Evolution', authors=['Tianshuo Xu','Yichen Xie','Depu Meng','Chensheng Peng','Quentin Herau','Bo Jiang','Yihan Hu','Wei Zhan'], description='Video generation with memory that tracks how hidden states evolve through interruptions.', image='remind-teaser.png', alt='Published ReMind overview of evolving scene states and memory across interrupted observations.', paper='https://arxiv.org/abs/2605.25333', project='https://remind-applied.github.io/', code='https://github.com/Applied-Intuition-Open-Source/ReMind'),
 dict(name='URoPE', year=2026, venue='ECCV 2026 · Spotlight', topic='reconstruction', title='URoPE: Universal Relative Position Embedding across Geometric Spaces', authors=['Yichen Xie','Depu Meng','Chensheng Peng','Yihan Hu','Quentin Herau','Masayoshi Tomizuka','Wei Zhan'], description='Relative position encoding that connects image tokens through camera geometry.', image='urope-teaser.jpg', alt='Published URoPE concept figure connecting positions across views and geometric spaces.', paper='https://arxiv.org/abs/2604.18747', project='https://urope-pe.github.io/', code='https://github.com/Applied-Intuition-Open-Source/URoPE'),
 dict(name='SpectralSplat', year=2026, venue='Preprint · 2026', topic='reconstruction', title='SpectralSplat: Appearance-Disentangled Feed-Forward Gaussian Splatting for Driving Scenes', authors=['Quentin Herau','Tianshuo Xu','Depu Meng','Jiezhi Yang','Chensheng Peng','Spencer Sherk','Yihan Hu','Wei Zhan'], description='Separate geometry and appearance to transfer lighting across reconstructed driving scenes.', image='spectral-original.jpg', alt='Published SpectralSplat reconstruction of a street scene.', paper='https://arxiv.org/abs/2604.03462'),
 dict(name='UniQueR', year=2026, venue='ECCV 2026', topic='reconstruction', title='UniQueR: Unified Query-based Feedforward 3D Reconstruction', authors=['Chensheng Peng','Quentin Herau','Jiezhi Yang','Yichen Xie','Yihan Hu','Wenzhao Zheng','Matthew Strong','Masayoshi Tomizuka','Wei Zhan'], description='Reconstruct scenes from unposed images using sparse 3D queries that generate Gaussians.', image='uniquer-teaser.png', alt='Published comparison of pixel-aligned and query-based 3D scene representations.', paper='https://arxiv.org/abs/2603.22851', project='https://uniquer3d.github.io/'),
 dict(name='LFG', year=2026, venue='CVPR 2026', topic='worlds', title='Learning to Drive is a Free Gift: Large-Scale Label-Free Autonomy Pretraining from Unposed In-The-Wild Videos', authors=['Matthew Strong','Wei-Jer Chang','Quentin Herau','Jiezhi Yang','Yihan Hu','Chensheng Peng','Wei Zhan'], description='Learn geometry, semantics and motion for driving directly from unposed video.', image='lfg-teaser.png', alt='Published LFG teaser showing observed and predicted scene geometry, semantics and motion.', paper='https://openaccess.thecvf.com/content/CVPR2026/html/Strong_Learning_to_Drive_is_a_Free_Gift_Large-Scale_Label-Free_Autonomy_CVPR_2026_paper.html', project='https://lfg-ai.github.io/', code='https://github.com/Applied-Intuition-Open-Source/LFG'),
 dict(name='AVoptim / MOISST++', year=2026, venue='IEEE RA-L 2026', topic='calibration', title='Refining Ground Truth Poses in Autonomous Driving Datasets via Neural Rendering', authors=['Quentin Herau','Nathan Piasco','Moussab Bennehar','Luis Roldão','Dzmitry Tsishkou','Bingbing Liu','Cyrille Migniot','Pascal Vasseur','Cédric Demonceaux'], description='Refine sensor calibration and ego-trajectories, and assess pose quality through complementary measurements.', image='avoptim-teaser.JPG', alt='Published AVoptim pose refinement comparisons and evaluation plots.', paper='https://arxiv.org/abs/2504.15776', project='https://qherau.github.io/AVoptim/', code='https://github.com/qherau/neural-calibration', benchmark='https://github.com/qherau/avoptim-benchmark'),
 dict(name='3DGS-Calib', year=2024, venue='IROS 2024 · Oral', topic='calibration', title='3DGS-Calib: 3D Gaussian Splatting for Multimodal SpatioTemporal Calibration', authors=['Quentin Herau','Moussab Bennehar','Arthur Moreau','Nathan Piasco','Luis Roldão','Dzmitry Tsishkou','Cyrille Migniot','Pascal Vasseur','Cédric Demonceaux'], description='Use differentiable Gaussian rendering anchored to LiDAR geometry to calibrate cameras.', image='gs-method.png', alt='Published 3DGS-Calib architecture from LiDAR geometry to camera calibration.', paper='https://arxiv.org/abs/2403.11577', project='https://qherau.github.io/3DGS-Calib/', code='https://github.com/qherau/neural-calibration'),
 dict(name='SOAC', year=2024, venue='CVPR 2024', topic='calibration', title='SOAC: Spatio-Temporal Overlap-Aware Multi-Sensor Calibration using Neural Radiance Fields', authors=BASE, description='Calibrate a multi-sensor rig using camera-specific neural fields and shared scene visibility.', image='soac-teaser.png', alt='Published SOAC overview of neural scene fitting and sensor calibration.', paper='https://openaccess.thecvf.com/content/CVPR2024/html/Herau_SOAC_Spatio-Temporal_Overlap-Aware_Multi-Sensor_Calibration_using_Neural_Radiance_Fields_CVPR_2024_paper.html', project='https://qherau.github.io/SOAC/', code='https://github.com/qherau/neural-calibration'),
 dict(name='MOISST', year=2023, venue='IROS 2023', topic='calibration', title='MOISST: Multimodal Optimization of Implicit Scene for SpatioTemporal Calibration', authors=BASE, description='Jointly optimize a shared neural scene and the spatial and temporal alignment of cameras and LiDAR.', image='moisst-teaser.png', alt='Published MOISST sensor alignment and image/depth overview.', paper='https://arxiv.org/abs/2303.03056', project='https://qherau.github.io/MOISST/', code='https://github.com/qherau/neural-calibration'),
]

# Intrinsic sizes of the unchanged public images reserve space before lazy loading.
IMAGE_SIZES = {
 'strike-teaser.png': (2028, 600), 's2tok-teaser.jpg': (4800, 2266),
 'building-rome-teaser.jpg': (1024, 1024), 'remind-teaser.png': (2047, 1063),
 'urope-teaser.jpg': (3713, 2067), 'spectral-original.jpg': (518, 350),
 'uniquer-teaser.png': (4374, 1048), 'lfg-teaser.png': (2633, 1108),
 'avoptim-teaser.JPG': (1217, 577), 'gs-method.png': (1425, 684),
 'soac-teaser.png': (727, 277), 'moisst-teaser.png': (850, 468),
}

def link(url, label, cls=''):
    preview=''
    for name in ['MOISST','SOAC','3DGS-Calib','AVoptim']:
        if url==f'https://qherau.github.io/{name}/':preview=f' data-preview-path="../{name}/"'
    return f'<a class="{cls}" href="{escape(url, quote=True)}"{preview}>{label}</a>'

def site_switcher():
    entries=[('Personal page','https://qherau.github.io/','../Personal/')]+[(name,f'https://qherau.github.io/{name}/',f'../{name}/') for name in ['MOISST','SOAC','3DGS-Calib','AVoptim']]
    links=''.join(f'<a href="{url}" data-preview-path="{preview}"'+(' aria-current="page"' if label=='Personal page' else '')+f'>{label}</a>' for label,url,preview in entries)
    return '<details class="site-switcher" data-site-switcher><summary>Research websites</summary><nav class="site-options" aria-label="Research websites">'+links+'</nav></details>'


def authors(names):
    return ', '.join('<strong>Quentin Herau</strong>' if n == 'Quentin Herau' else escape(n) for n in names)

def paper(p):
    resource = link(p['paper'], 'Paper')
    for key, label in [('project','Project'), ('code','Code'), ('benchmark','Benchmark')]:
        if key in p: resource += link(p[key], label)
    width, height = IMAGE_SIZES[p['image']]
    slug = p['name'].split(' /')[0].lower().replace(' ', '-')
    venue_class = 'venue-badge venue-preprint' if p['venue'].startswith('Preprint') else 'venue-badge venue-published'
    venue, _, distinction = p['venue'].partition(' · ')
    if p['venue'].startswith('Preprint'):
        venue, distinction = p['venue'].replace(' · ', ' '), ''
    venue_label = f'<span class="{venue_class}">{escape(venue)}</span>'
    if distinction:
        venue_label += f'<span class="venue-distinction">{escape(distinction)}</span>'
    return f'''<article class="paper" data-topic="{p['topic']}" id="paper-{slug}">
    <a class="paper-image zoom-image" href="assets/{p['image']}" data-caption="{escape(p['alt'], quote=True)}" aria-label="Enlarge {p['name'].split(' /')[0]} figure"><img src="assets/{p['image']}" width="{width}" height="{height}" alt="{p['alt']}" loading="lazy"><span class="image-corner" aria-hidden="true">↗</span></a>
    <div class="paper-content"><div class="paper-meta">{venue_label}<span class="paper-name">{p['name']}</span></div>
    <h3>{link(p['paper'], escape(p['title']))}</h3><p class="authors">{authors(p['authors'])}</p><p class="paper-description">{p['description']}</p><div class="paper-links">{resource}</div></div></article>'''

cards = ''.join(paper(p) for p in PAPERS)
SCRIPT_VERSION = hashlib.sha256((SITE/'assets/personal.js').read_bytes()).hexdigest()[:12]

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quentin Herau — Research</title><meta name="description" content="Quentin Herau, Research Engineer at Applied Intuition. Research in 3D reconstruction, neural rendering, world models and sensor calibration.">
<meta name="theme-color" content="#fafaf7"><meta property="og:title" content="Quentin Herau — Research"><meta property="og:description" content="3D reconstruction, neural rendering, world models and multi-sensor calibration."><meta property="og:type" content="website"><link rel="canonical" href="https://qherau.github.io/"><meta property="og:url" content="https://qherau.github.io/"><meta property="og:image" content="https://qherau.github.io/assets/quentin-herau-cvpr.jpg">
<link rel="icon" href="data:,"><link rel="stylesheet" href="assets/personal.css?v={STYLE_VERSION}"><script src="assets/personal.js?v={SCRIPT_VERSION}" defer></script></head>
<body><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><nav class="wrap nav" aria-label="Main navigation"><div class="nav-start"><a class="brand" href="#top">Quentin Herau</a>{site_switcher()}</div><button class="menu-button" type="button" data-menu aria-controls="nav-links" aria-expanded="false">Menu</button><div class="nav-links" id="nav-links"><a href="#top">About</a><a href="#publications">Publications</a><a href="#background">Service</a><a href="mailto:quentin.herau@gmail.com">Contact</a></div></nav></header>
<main id="main"><section class="intro wrap" id="top" aria-labelledby="name"><div class="intro-copy">
<h1 id="name">Quentin Herau</h1>
<p>I’m a Research Engineer at <a href="https://www.appliedintuition.com/">Applied Intuition</a> in Sunnyvale, California, developing neural simulation for autonomous driving and robotics. My research spans <strong>3D reconstruction, neural rendering and world models</strong>, including appearance transfer and scene modeling across repeated traversals.</p>
<p>I build scene representations for closed-loop training and evaluation of driving models, simulation-ready robotics assets, and world action model pretraining. I also mentor PhD research interns.</p>
<p>I completed an <strong>industrial PhD at Huawei Noah’s Ark Lab</strong> with <strong>ICB (CNRS / Université Bourgogne Europe)</strong> in 2025, working on targetless sensor calibration with dense differentiable rendering. Before that, I earned a <strong>diplôme d’ingénieur from ENSEEIHT</strong> in Toulouse and a research master’s degree, spent an exchange semester at National Taiwan University, and worked on active learning at IPAL (NUS / CNRS) in Singapore.</p>
<div class="profile-links"><a href="mailto:quentin.herau@gmail.com">Email</a><span aria-hidden="true">/</span>{link(SCHOLAR,'Google Scholar')}<span aria-hidden="true">/</span>{link('https://github.com/qherau','GitHub')}<span aria-hidden="true">/</span>{link('https://www.linkedin.com/in/quentin-herau-phd-38378b140','LinkedIn')}</div></div>
<figure class="portrait-frame"><img id="profile-photo" src="assets/quentin-herau-cvpr.jpg" width="1280" height="1226" alt="Quentin Herau standing beside the CVPR sign." fetchpriority="high"></figure></section>
<section class="publications-section wrap" id="publications" aria-labelledby="publications-title"><div class="section-heading"><h2 id="publications-title">Publications</h2>{link(SCHOLAR, 'Google Scholar', 'text-link')}</div>
<div class="papers">{cards}</div></section>
<section class="about-section wrap" id="background" aria-labelledby="background-title"><h2 id="background-title">Service &amp; interests</h2><div class="about-copy"><p>Reviewer for IROS (2023–2026), RA-L, IV (2025), NeurIPS (2025–2026), ECCV (2026) and ICLR (2027).</p><p>Outside research, I enjoy game design, oenology, cooking and working out.</p></div></section>
<section class="contact-section wrap" id="contact" aria-labelledby="contact-title"><h2 id="contact-title">Contact</h2><p><a href="mailto:quentin.herau@gmail.com">quentin.herau@gmail.com</a></p></section></main>
<footer class="site-footer"><div class="wrap"><span>© 2026 Quentin Herau</span><a href="#top">Back to top ↑</a><a href="data-terms.html">Dataset credits and terms</a></div></footer>
<dialog id="figure-dialog" aria-labelledby="figure-caption"><div class="dialog-top"><span>Research figure</span><button type="button" id="close-figure" aria-label="Close enlarged figure">Close ×</button></div><img id="dialog-image" alt=""><p id="figure-caption"></p><a id="dialog-source" href="assets/spectral-original.jpg">Open original image ↗</a></dialog><p class="sr-only" id="interaction-status" role="status" aria-live="polite"></p>
</body></html>'''
SITE.mkdir(exist_ok=True)
(SITE/'index.html').write_text(html)
(SITE/'.nojekyll').touch()
if ROOT != SITE:
    (SITE/'data-terms.html').write_text((ROOT/'design/data-terms.html').read_text())
(SITE/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"></svg>')
(SITE/'publications.json').write_text(json.dumps(PAPERS,ensure_ascii=False,indent=2)+'\n')
print(f'Built {SITE}/index.html with {len(PAPERS)} verified papers')
