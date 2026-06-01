import os

crosswalk_path = '/win/linux/Code/Text/ai-research-reports/data/docx-md-crosswalk.toml'

with open(crosswalk_path, 'r') as f:
    lines = f.readlines()

# Read the entire file and modify it correctly. We'll append the new items at the end.
# We also need to update counts in [summary].

# Update summary stats
for i, line in enumerate(lines):
    if line.startswith('docx_count = '):
        lines[i] = 'docx_count = 94\n'
    elif line.startswith('md_project_count = '):
        lines[i] = 'md_project_count = 105\n'
    elif line.startswith('linked_docx_count = '):
        lines[i] = 'linked_docx_count = 94\n'

# Add [[docx]] blocks
lines.append('\n')
lines.append('[[docx]]\n')
lines.append('file = "American Conservatism and the Liberal-Revolutionary Founding.docx"\n')
lines.append('md_project = "american-conservatism"\n')
lines.append('status = "linked"\n')
lines.append('match_basis = "manual"\n')
lines.append('\n')
lines.append('[[docx]]\n')
lines.append('file = "Formalizing the Connection Between Modern Progressive Politics and Marxism.docx"\n')
lines.append('md_project = "modern-progressive-marxism"\n')
lines.append('status = "linked"\n')
lines.append('match_basis = "manual"\n')

# Add [[md_project]] blocks
lines.append('\n')
lines.append('[[md_project]]\n')
lines.append('folder = "american-conservatism"\n')
lines.append('docx = "American Conservatism and the Liberal-Revolutionary Founding.docx"\n')
lines.append('status = "linked"\n')
lines.append('empty = false\n')
lines.append('title = "American Conservatism and the Liberal-Revolutionary Founding"\n')
lines.append('subtitle = ""\n')
lines.append('\n')
lines.append('[[md_project]]\n')
lines.append('folder = "modern-progressive-marxism"\n')
lines.append('docx = "Formalizing the Connection Between Modern Progressive Politics and Marxism.docx"\n')
lines.append('status = "linked"\n')
lines.append('empty = false\n')
lines.append('title = "Formalizing the Connection Between Modern Progressive Politics and Marxism"\n')
lines.append('subtitle = ""\n')

with open(crosswalk_path, 'w') as f:
    f.writelines(lines)

# Also update ledger_docx_list.txt
ledger_txt_path = '/win/linux/Code/Text/ai-research-reports/data/ledger_docx_list.txt'
with open(ledger_txt_path, 'a') as f:
    f.write('American Conservatism and the Liberal-Revolutionary Founding.docx\n')
    f.write('Formalizing the Connection Between Modern Progressive Politics and Marxism.docx\n')
