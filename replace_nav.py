import os
import re

files = [
    'c:\\Users\\lbern\\workspace\\Lara Pires - Estética\\Site\\blefaroplastia.html',
    'c:\\Users\\lbern\\workspace\\Lara Pires - Estética\\Site\\peeling-quimico.html',
    'c:\\Users\\lbern\\workspace\\Lara Pires - Estética\\Site\\full-face.html',
    'c:\\Users\\lbern\\workspace\\Lara Pires - Estética\\Site\\bioestimuladores.html',
    'c:\\Users\\lbern\\workspace\\Lara Pires - Estética\\Site\\fios-de-pdo.html',
    'c:\\Users\\lbern\\workspace\\Lara Pires - Estética\\Site\\microagulhamento.html',
    'c:\\Users\\lbern\\workspace\\Lara Pires - Estética\\Site\\rinomodelacao.html',
    'c:\\Users\\lbern\\workspace\\Lara Pires - Estética\\Site\\preenchimento-de-mento.html'
]

# Read blefaroplastia.html as base
with open(files[0], 'r', encoding='utf-8') as file:
    blef_content = file.read()

nav_pattern = re.compile(r'<nav x-data=.*?</nav>', re.DOTALL)
blef_nav_match = nav_pattern.search(blef_content)

if not blef_nav_match:
    print("Failed to extract nav from blefaroplastia")
    exit(1)

base_nav = blef_nav_match.group(0)

for f in files[1:]: # Skip blefaroplastia as it's already fixed
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # We need to set active class for desktop and mobile based on the filename
        current_nav = base_nav
        
        mapping = {
            'peeling-quimico.html': ('Peeling\\n                                Químico</a>', 'Peeling Químico</a>'),
            'full-face.html': ('Full\\n                                Face</a>', 'Full Face</a>'),
            'bioestimuladores.html': ('Bioestimuladores</a>', 'Bioestimuladores</a>'),
            'fios-de-pdo.html': ('Fios\\n                                de PDO</a>', 'Fios de PDO</a>'),
            'microagulhamento.html': ('Microagulhamento</a>', 'Microagulhamento</a>'),
            'rinomodelacao.html': ('Rinomodelação</a>', 'Rinomodelação</a>'),
            'preenchimento-de-mento.html': ('Preenchimento\\n                                de Mento</a>', 'Preenchimento de Mento</a>')
        }
        
        base_name = os.path.basename(f)
        if base_name in mapping:
            # Revert blefaroplastia desktop link to inactive
            current_nav = current_nav.replace('text-primary bg-white/5 transition-colors uppercase tracking-wide">Blefaroplastia</a>', 
                                              'text-gray-300 hover:text-primary hover:bg-white/5 transition-colors uppercase tracking-wide">Blefaroplastia</a>')
            # Revert blefaroplastia mobile link to inactive
            current_nav = current_nav.replace('text-xs text-primary transition-colors uppercase tracking-wide">Blefaroplastia</a>',
                                              'text-xs text-gray-400 hover:text-primary transition-colors uppercase tracking-wide">Blefaroplastia</a>')
            
            desk_label = mapping[base_name][0]
            mob_label = mapping[base_name][1]
            
            # Make the active desktop link active
            current_nav = current_nav.replace(f'text-gray-300 hover:text-primary hover:bg-white/5 transition-colors uppercase tracking-wide">{desk_label}', 
                                              f'text-primary bg-white/5 transition-colors uppercase tracking-wide">{desk_label}')
            
            # Make the active mobile link active
            current_nav = current_nav.replace(f'text-gray-400 hover:text-primary transition-colors uppercase tracking-wide">{mob_label}',
                                              f'text-primary transition-colors uppercase tracking-wide">{mob_label}')
        
        new_content = nav_pattern.sub(current_nav, content, count=1)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
            
        print(f"Updated nav in {base_name}")
