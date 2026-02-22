import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update x-data wrapper
    content = re.sub(
        r'<nav x-data="\{\s*scrolled:\s*false\s*\}"',
        r'<nav x-data="{ scrolled: false, mobileMenuOpen: false }"',
        content
    )

    # 2. Update Mobile Menu Button
    btn_search = r'<div class="md:hidden">\s*<button class="text-white hover:text-primary focus:outline-none">\s*<span class="material-icons-outlined">menu</span>\s*</button>\s*</div>'
    btn_replacement = '''<div class="md:hidden">
                    <button @click="mobileMenuOpen = !mobileMenuOpen" class="text-white hover:text-primary focus:outline-none p-2">
                        <span class="material-icons-outlined" x-text="mobileMenuOpen ? \'close\' : \'menu\'">menu</span>
                    </button>
                </div>'''
    content = re.sub(btn_search, btn_replacement, content)

    # 3. Add Mobile Menu Panel before closing </nav>
    prefix = "" if file == "index.html" else "index.html"
    
    mobile_menu_panel = f"""
        <!-- Mobile Menu -->
        <div x-show="mobileMenuOpen" 
             x-transition:enter="transition ease-out duration-200"
             x-transition:enter-start="opacity-0 -translate-y-2"
             x-transition:enter-end="opacity-100 translate-y-0"
             x-transition:leave="transition ease-in duration-150"
             x-transition:leave-start="opacity-100 translate-y-0"
             x-transition:leave-end="opacity-0 -translate-y-2"
             class="md:hidden bg-[#1A1A1A]/95 backdrop-blur-md border-b border-gray-800 absolute top-[100%] left-0 w-full shadow-xl"
             style="display: none;">
            <div class="px-4 pt-4 pb-6 space-y-2 bg-[#1A1A1A]">
                <div x-data="{{ openProcedimentos: false }}" class="py-2 border-b border-gray-800/50">
                    <button @click="openProcedimentos = !openProcedimentos" class="w-full flex justify-between items-center text-xs uppercase tracking-[0.15em] text-white hover:text-primary transition-colors py-2 focus:outline-none">
                        Procedimentos
                        <span class="material-icons-outlined text-sm transition-transform duration-300" :class="openProcedimentos ? 'rotate-180' : ''">expand_more</span>
                    </button>
                    <div x-show="openProcedimentos" class="pl-4 py-3 space-y-4" style="display: none;" x-transition>
                        <a @click="mobileMenuOpen = false" href="blefaroplastia.html" class="block text-xs text-gray-400 hover:text-primary transition-colors uppercase tracking-wide">Blefaroplastia</a>
                        <a @click="mobileMenuOpen = false" href="peeling-quimico.html" class="block text-xs text-gray-400 hover:text-primary transition-colors uppercase tracking-wide">Peeling Químico</a>
                        <a @click="mobileMenuOpen = false" href="full-face.html" class="block text-xs text-gray-400 hover:text-primary transition-colors uppercase tracking-wide">Full Face</a>
                        <a @click="mobileMenuOpen = false" href="bioestimuladores.html" class="block text-xs text-gray-400 hover:text-primary transition-colors uppercase tracking-wide">Bioestimuladores</a>
                        <a @click="mobileMenuOpen = false" href="fios-de-pdo.html" class="block text-xs text-gray-400 hover:text-primary transition-colors uppercase tracking-wide">Fios de PDO</a>
                        <a @click="mobileMenuOpen = false" href="microagulhamento.html" class="block text-xs text-gray-400 hover:text-primary transition-colors uppercase tracking-wide">Microagulhamento</a>
                    </div>
                </div>
                <a @click="mobileMenuOpen = false" href="{prefix}#about" class="block text-xs uppercase tracking-[0.15em] text-white hover:text-primary transition-colors py-3 border-b border-gray-800/50">Nosso Espaço</a>
                <a @click="mobileMenuOpen = false" href="{prefix}#contact" class="block text-xs uppercase tracking-[0.15em] text-white hover:text-primary transition-colors py-3 border-b border-gray-800/50">Contato</a>
                <a @click="mobileMenuOpen = false" href="{prefix}#blog" class="block text-xs uppercase tracking-[0.15em] text-white hover:text-primary transition-colors py-3 border-b border-gray-800/50">Blog</a>
                <div class="pt-4 pb-2">
                    <a @click="mobileMenuOpen = false" href="{prefix}#contact" class="block w-full px-6 py-4 bg-primary text-[#1A1A1A] text-xs font-bold uppercase tracking-widest rounded-sm hover:bg-white transition-colors text-center shadow-lg">Agendar Avaliação</a>
                </div>
            </div>
        </div>
    </nav>"""
    
    if '<!-- Mobile Menu -->' not in content:
        content = re.sub(r'\s*</nav>', '\n' + mobile_menu_panel, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {{file}}")
