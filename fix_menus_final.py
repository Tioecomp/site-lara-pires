import os

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

desktop_template = """<!-- Dropdown Menu -->
                        <div
                            class="absolute left-0 top-full -mt-2 w-64 bg-[#1A1A1A]/95 backdrop-blur-md border border-gray-800 shadow-xl py-2 rounded-sm transform origin-top opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50">
                            <a href="blefaroplastia.html"
                                class="block px-6 py-3 text-xs {c_blef} hover:text-primary {b_blef} transition-colors uppercase tracking-wide">Blefaroplastia</a>
                            <a href="peeling-quimico.html"
                                class="block px-6 py-3 text-xs {c_peeling} hover:text-primary {b_peeling} transition-colors uppercase tracking-wide">Peeling
                                Químico</a>
                            <a href="full-face.html"
                                class="block px-6 py-3 text-xs {c_full} hover:text-primary {b_full} transition-colors uppercase tracking-wide">Full
                                Face</a>
                            <a href="bioestimuladores.html"
                                class="block px-6 py-3 text-xs {c_bio} hover:text-primary {b_bio} transition-colors uppercase tracking-wide">Bioestimuladores</a>
                            <a href="fios-de-pdo.html"
                                class="block px-6 py-3 text-xs {c_fio} hover:text-primary {b_fio} transition-colors uppercase tracking-wide">Fios
                                de PDO</a>
                            <a href="microagulhamento.html"
                                class="block px-6 py-3 text-xs {c_micro} hover:text-primary {b_micro} transition-colors uppercase tracking-wide">Microagulhamento</a>
                            <a href="rinomodelacao.html"
                                class="block px-6 py-3 text-xs {c_rino} hover:text-primary {b_rino} transition-colors uppercase tracking-wide">Rinomodelação</a>
                            <a href="preenchimento-de-mento.html"
                                class="block px-6 py-3 text-xs {c_mento} hover:text-primary {b_mento} transition-colors uppercase tracking-wide">Preenchimento
                                de Mento</a>
                        </div>"""

mobile_template = """<div x-show="openProcedimentos" class="pl-4 py-3 space-y-4" style="display: none;" x-transition>
                        <a @click="mobileMenuOpen = false" href="blefaroplastia.html" class="block text-xs {c_blef_m} hover:text-primary transition-colors uppercase tracking-wide">Blefaroplastia</a>
                        <a @click="mobileMenuOpen = false" href="peeling-quimico.html" class="block text-xs {c_peeling_m} hover:text-primary transition-colors uppercase tracking-wide">Peeling Químico</a>
                        <a @click="mobileMenuOpen = false" href="full-face.html" class="block text-xs {c_full_m} hover:text-primary transition-colors uppercase tracking-wide">Full Face</a>
                        <a @click="mobileMenuOpen = false" href="bioestimuladores.html" class="block text-xs {c_bio_m} hover:text-primary transition-colors uppercase tracking-wide">Bioestimuladores</a>
                        <a @click="mobileMenuOpen = false" href="fios-de-pdo.html" class="block text-xs {c_fio_m} hover:text-primary transition-colors uppercase tracking-wide">Fios de PDO</a>
                        <a @click="mobileMenuOpen = false" href="microagulhamento.html" class="block text-xs {c_micro_m} hover:text-primary transition-colors uppercase tracking-wide">Microagulhamento</a>
                        <a @click="mobileMenuOpen = false" href="rinomodelacao.html" class="block text-xs {c_rino_m} hover:text-primary transition-colors uppercase tracking-wide">Rinomodelação</a>
                        <a @click="mobileMenuOpen = false" href="preenchimento-de-mento.html" class="block text-xs {c_mento_m} hover:text-primary transition-colors uppercase tracking-wide">Preenchimento de Mento</a>
                    </div>"""

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        colors = {
            'c_blef': 'text-gray-300', 'b_blef': 'hover:bg-white/5',
            'c_peeling': 'text-gray-300', 'b_peeling': 'hover:bg-white/5',
            'c_full': 'text-gray-300', 'b_full': 'hover:bg-white/5',
            'c_bio': 'text-gray-300', 'b_bio': 'hover:bg-white/5',
            'c_fio': 'text-gray-300', 'b_fio': 'hover:bg-white/5',
            'c_micro': 'text-gray-300', 'b_micro': 'hover:bg-white/5',
            'c_rino': 'text-gray-300', 'b_rino': 'hover:bg-white/5',
            'c_mento': 'text-gray-300', 'b_mento': 'hover:bg-white/5',
            
            'c_blef_m': 'text-gray-400',
            'c_peeling_m': 'text-gray-400',
            'c_full_m': 'text-gray-400',
            'c_bio_m': 'text-gray-400',
            'c_fio_m': 'text-gray-400',
            'c_micro_m': 'text-gray-400',
            'c_rino_m': 'text-gray-400',
            'c_mento_m': 'text-gray-400',
        }
        
        mapping = {
            'blefaroplastia.html': 'blef',
            'peeling-quimico.html': 'peeling',
            'full-face.html': 'full',
            'bioestimuladores.html': 'bio',
            'fios-de-pdo.html': 'fio',
            'microagulhamento.html': 'micro',
            'rinomodelacao.html': 'rino',
            'preenchimento-de-mento.html': 'mento'
        }
        
        base_name = os.path.basename(f)
        k = mapping.get(base_name)
        if k:
            colors[f'c_{k}'] = 'text-primary'
            colors[f'b_{k}'] = 'bg-white/5'
            colors[f'c_{k}_m'] = 'text-primary'
            
        desktop_menu = desktop_template.format(**colors)
        mobile_menu = mobile_template.format(**colors)
        
        # Replace desktop menu
        try:
            start_d = content.index('<!-- Dropdown Menu -->')
            search_str = '</div>\\n                    </div>\\n\\n                    <a'
            if search_str in content[start_d:]:
                end_d = content.index(search_str, start_d)
            elif '</div>\\n                    </div>\\n                    <a' in content[start_d:]:
                end_d = content.index('</div>\\n                    </div>\\n                    <a', start_d)
            elif '</div>\\n                    </div>\\n\\n                    <div' in content[start_d:]:
                end_d = content.index('</div>\\n                    </div>\\n\\n                    <div', start_d)
            else:
                end_d = content.find('</div>\\n                    </div>', start_d)
            
            # Use real newlines
            search_str = '</div>\n                    </div>\n\n                    <a'
            if search_str in content[start_d:]:
                end_d = content.index(search_str, start_d)
            elif '</div>\n                    </div>\n                    <a' in content[start_d:]:
                end_d = content.index('</div>\n                    </div>\n                    <a', start_d)
            elif '</div>\n                    </div>\n\n                    <div' in content[start_d:]:
                end_d = content.index('</div>\n                    </div>\n\n                    <div', start_d)
            else:
                end_d = content.find('</div>\n                    </div>', start_d)
            
            content = content[:start_d] + desktop_menu + "\\n" + content[end_d:]
            print(f"Replaced desktop menu in {base_name}")
        except ValueError as e:
            print(f"Failed to find desktop menu boundaries in {base_name}: {e}")
            
        # Replace mobile menu
        try:
            start_m = content.index('<div x-show="openProcedimentos"')
            se1 = '</div>\\n                </div>\\n                <a @click="mobileMenuOpen = false" href'
            se2 = '</div>\n                </div>\n                <a @click="mobileMenuOpen = false" href'
            if se2 in content[start_m:]:
                end_m = content.index(se2, start_m)
            else:
                end_m = content.find('</div>\n                </div>\n', start_m)
                if end_m == -1: raise ValueError("Mobile bound not found")
            content = content[:start_m] + mobile_menu + "\\n" + content[end_m:]
            print(f"Replaced mobile menu in {base_name}")
        except ValueError as e:
            print(f"Failed to find mobile menu boundaries in {base_name}: {e}")
            
        # fix mobile toggle button
        if 'class="text-white hover:text-primary focus:outline-none p-2"' not in content:
            target1 = '<button class="text-white hover:text-primary focus:outline-none"><span\\n                            class="material-icons-outlined">menu</span></button>'
            target1_real = '<button class="text-white hover:text-primary focus:outline-none"><span\n                            class="material-icons-outlined">menu</span></button>'
            target2 = '<button class="text-white hover:text-primary focus:outline-none"><span class="material-icons-outlined">menu</span></button>'
            
            replacement = '<button @click="mobileMenuOpen = !mobileMenuOpen" class="text-white hover:text-primary focus:outline-none p-2">\n                        <span class="material-icons-outlined" x-text="mobileMenuOpen ? \'close\' : \'menu\'">menu</span>\n                    </button>'
            
            if target1_real in content:
                content = content.replace(target1_real, replacement)
                print(f"Fixed mobile toggle button in {base_name}")
            elif target2 in content:
                content = content.replace(target2, replacement)
                print(f"Fixed mobile toggle button in {base_name}")

        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
