import os
import yaml
from datetime import datetime

metadata_template = """---
title: "{title}"
subtitle: ""
linkTitle: "{title}"
description: ""
summary: ""
abstract: ""
slug: "{slug}"
url: ""
aliases: []
date: "{date}"
publishDate: "{date}"
lastmod: "{date}"
expiryDate: ""
draft: true
status: "draft"
edition: "1.0"
revision: "1.0.0"
author:
- Salvador Guzman
- ChatGPT
authors:
- Salvador Guzman
- ChatGPT
creator:
- Salvador Guzman
publisher: "Marginalia"
rights: "CC0-1.0"
license: "CC0-1.0"
lang: "en"
language: "English"
identifier: "urn:gva:{slug}"
dataset_id: "{slug}"
plate_id: ""
type: "report"
format: "text/markdown"
reference-section-title: "References"
categories:
- Politics
tags:
- politics
- history
keywords:
- politics
subject:
- Politics
subjects:
- Politics
library_of_congress_classification:
  class: ""
  label: ""
  description: ""
series: ""
series-title: ""
series-number: 0
series_title: ""
series_number: 0
report-no: ""
report-number: ""
report-year: ""
report_no: 0
report_number: 0
report_year: 0
layout: ""
markup: ""
toc: true
toc-depth: 3
toc-title: "Contents"
number-sections: true
weight: 0
cover-image: ""
cover_image: ""
epub-cover-image: ""
epub_cover_image: ""
epub-title-page: false
epub-chapter-level: 2
epub-stylesheet: "epub.css"
highlight-style: "tango"
outputs: []
headless: false
isCJKLanguage: false
translationKey: ""
resources: []
build:
  list: "always"
  render: "always"
  publishResources: true
cascade: {{}}
sitemap:
  changefreq: ""
  priority: 0
  filename: "sitemap.xml"
report:
  id: "urn:gva:{slug}"
  code: ""
  name: "{title}"
  organization: "Marginalia"
  collection: ""
  series: ""
  number: ""
  year: 2026
  version: "1.0.0"
  kind: "report"
  type: "report"
  domain: ""
  discipline: ""
  subdiscipline: ""
  topic: ""
  subject: ""
  scope: ""
  scope_years: ""
  time_scope: ""
  time_span: ""
  period: ""
  period_covered: ""
  region: ""
  region_focus: ""
  audience: "general"
  level: ""
  focus: ""
  emphasis: ""
  structure: ""
  intent: ""
  methods: []
  method: ""
  primary_texts: []
  population_focus: ""
  stance: ""
  is_report: true
  notes: ""
  conversion:
    source_docx: "{docx_name}"
    tool: "pandoc 3.6"
    date: "{date}"
...
"""

def create_yaml(slug, title, docx_name):
    date_str = datetime.now().strftime("%Y-%m-%d")
    content = metadata_template.format(title=title, slug=slug, date=date_str, docx_name=docx_name)
    with open(f"/win/linux/Code/Text/ai-research-reports/data/md/{slug}/article.yaml", "w") as f:
        f.write(content)

create_yaml("american-conservatism", "American Conservatism and the Liberal-Revolutionary Founding", "American Conservatism and the Liberal-Revolutionary Founding.docx")
create_yaml("modern-progressive-marxism", "Formalizing the Connection Between Modern Progressive Politics and Marxism", "Formalizing the Connection Between Modern Progressive Politics and Marxism.docx")
