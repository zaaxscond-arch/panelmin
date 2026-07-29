#!/usr/bin/env python3
# PanelMin Tools v2.0 - Main Entry Point
# [ MR DIOZZ EXECUTOR ]

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.core.scanner import PanelMinScanner
from src.utils.colors import Colors
from src.utils.storage import StorageManager

class PanelMinTools:
    def __init__(self):
        self.scanner = PanelMinScanner()
        self.storage = StorageManager()
        self.colors = Colors()
        
    def banner(self):
        return f"""
{self.colors.RED}╔═══════════════════════════════════════════════════════════╗
║  {self.colors.YELLOW}PANELMIN TOOLS v2.0{self.colors.RED}                         ║
║  {self.colors.CYAN}Admin Login Finder • Database Scanner • XLS Export{self.colors.RED} ║
║  {self.colors.MAGENTA}Executor: Mr Diozz Executor{self.colors.RED}                ║
╚═══════════════════════════════════════════════════════════════╝
"""
    
    def menu(self):
        print(self.banner())
        print(f"""
{self.colors.CYAN}╔═══════════════════════════════════════════════════════════╗
║  {self.colors.WHITE}[1] {self.colors.GREEN}Admin Finder                          {self.colors.CYAN}║
║  {self.colors.WHITE}[2] {self.colors.GREEN}Pencari Login Admin                 {self.colors.CYAN}║
║  {self.colors.WHITE}[3] {self.colors.GREEN}Database Scanner                   {self.colors.CYAN}║
║  {self.colors.WHITE}[4] {self.colors.GREEN}Download XLS Login                  {self.colors.CYAN}║
║  {self.colors.WHITE}[5] {self.colors.GREEN}Storage Manager                    {self.colors.CYAN}║
║  {self.colors.WHITE}[6] {self.colors.RED}Exit                                 {self.colors.CYAN}║
╚═══════════════════════════════════════════════════════════════╝
{self.colors.YELLOW}⌨  Pilih menu [1-6]: """, end="")
    
    def run(self):
        self.storage.create()
        while True:
            self.menu()
            choice = input()
            
            if choice == '1':
                self.scanner.admin_finder()
            elif choice == '2':
                self.scanner.login_scanner()
            elif choice == '3':
                self.scanner.database_scanner()
            elif choice == '4':
                self.scanner.export_xls()
            elif choice == '5':
                self.storage.manager()
            elif choice == '6':
                print(f"\n{self.colors.RED}Exiting... Mr Diozz Executor siap melayani lagi{self.colors.RESET}")
                sys.exit(0)
            else:
                print(f"{self.colors.RED}✗ Pilihan tidak valid!{self.colors.RESET}")

if __name__ == "__main__":
    try:
        app = PanelMinTools()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}⛔ Interrupted by user. Exiting...{Colors.RESET}")
        sys.exit(0)
