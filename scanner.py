import json
import os
from datetime import datetime
from src.core.checker import LinkChecker
from src.utils.colors import Colors
from src.utils.storage import StorageManager

class PanelMinScanner:
    def __init__(self):
        self.colors = Colors()
        self.checker = LinkChecker()
        self.storage = StorageManager()
        self.working_links = []
        self.failed_links = []
        self.databases = []
        
        # Load config
        with open('config/paths.json', 'r') as f:
            self.paths = json.load(f)
    
    def get_base_url(self, web):
        if not web.startswith(('http://', 'https://')):
            web = 'https://' + web
        if web.endswith('/'):
            web = web[:-1]
        return web
    
    def admin_finder(self):
        print(f"\n{self.colors.CYAN}╔═══════════════════════════════════════════╗")
        print(f"║  {self.colors.YELLOW}ADMIN FINDER - Scan Login Paths{self.colors.CYAN}   ║")
        print(f"╚═══════════════════════════════════════════╝\n")
        
        web = input(f"{self.colors.WHITE}🔗 Masukkan URL target: ")
        base_url = self.get_base_url(web)
        
        print(f"\n{self.colors.YELLOW}⏳ Scanning {len(self.paths['login'])} paths...\n")
        print(f"{self.colors.CYAN}{'='*60}")
        
        for i, path in enumerate(self.paths['login'], 1):
            result = self.checker.check(base_url, path, "ADMIN")
            if result['status'] == 'WORKING':
                self.working_links.append(result)
                print(f"{self.colors.GREEN}✓ [{i:03d}] {result['url']} [200 OK]{self.colors.RESET}")
            else:
                self.failed_links.append(result)
                print(f"{self.colors.RED}✗ [{i:03d}] {result['url']} [{result['status']}]{self.colors.RESET}")
        
        self._show_summary()
        self.storage.save_results(self.working_links, self.failed_links)
        input(f"\n{self.colors.YELLOW}Tekan Enter untuk kembali...{self.colors.RESET}")
    
    def login_scanner(self):
        self.admin_finder()  # Same function
    
    def database_scanner(self):
        print(f"\n{self.colors.CYAN}╔═══════════════════════════════════════════╗")
        print(f"║  {self.colors.YELLOW}DATABASE SCANNER{self.colors.CYAN}                     ║")
        print(f"╚═══════════════════════════════════════════╝\n")
        
        web = input(f"{self.colors.WHITE}🔗 Masukkan URL target: ")
        base_url = self.get_base_url(web)
        
        print(f"\n{self.colors.YELLOW}⏳ Scanning database paths...\n")
        print(f"{self.colors.CYAN}{'='*60}")
        
        for i, path in enumerate(self.paths['database'], 1):
            result = self.checker.check(base_url, path, "DATABASE")
            if result['status'] == 'WORKING':
                self.databases.append(result)
                print(f"{self.colors.GREEN}✓ [{i:03d}] {result['url']} [200 OK]{self.colors.RESET}")
            else:
                print(f"{self.colors.RED}✗ [{i:03d}] {result['url']} [{result['status']}]{self.colors.RESET}")
        
        print(f"\n{self.colors.CYAN}{'='*60}")
        print(f"{self.colors.GREEN}✓ Database ditemukan: {len(self.databases)}{self.colors.RESET}")
        
        for db in self.databases:
            print(f"  {self.colors.GREEN}• {db['url']}{self.colors.RESET}")
        
        input(f"\n{self.colors.YELLOW}Tekan Enter untuk kembali...{self.colors.RESET}")
    
    def export_xls(self):
        from src.utils.exporter import XLSExporter
        exporter = XLSExporter()
        exporter.export(self.working_links, self.failed_links)
    
    def _show_summary(self):
        print(f"\n{self.colors.CYAN}{'='*60}")
        print(f"{self.colors.GREEN}✓ WORKING: {len(self.working_links)} link ditemukan")
        print(f"{self.colors.RED}✗ FAILED: {len(self.failed_links)} link")
        print(f"{self.colors.CYAN}{'='*60}{self.colors.RESET}")
