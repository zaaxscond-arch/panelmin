import os
import json
import shutil
from datetime import datetime
from src.utils.colors import Colors

class StorageManager:
    def __init__(self):
        self.colors = Colors()
        self.storage_dir = "storage"
        self.results_dir = f"{self.storage_dir}/results"
        
    def create(self):
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
    
    def save_results(self, working, failed):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Save working links
        if working:
            with open(f"{self.results_dir}/working_{timestamp}.txt", 'w') as f:
                for link in working:
                    f.write(f"{link['url']} [{link['status']}]\n")
        
        # Save all results
        all_results = working + failed
        if all_results:
            with open(f"{self.results_dir}/all_results_{timestamp}.json", 'w') as f:
                json.dump(all_results, f, indent=2)
        
        print(f"\n{self.colors.GREEN}✓ Results saved to: {self.results_dir}{self.colors.RESET}")
    
    def manager(self):
        print(f"\n{self.colors.CYAN}╔═══════════════════════════════════════════╗")
        print(f"║  {self.colors.YELLOW}STORAGE MANAGER{self.colors.CYAN}                     ║")
        print(f"╚═══════════════════════════════════════════╝\n")
        
        if not os.path.exists(self.results_dir):
            print(f"{self.colors.RED}✗ No results found!{self.colors.RESET}")
            input(f"\n{self.colors.YELLOW}Tekan Enter untuk kembali...{self.colors.RESET}")
            return
        
        files = os.listdir(self.results_dir)
        
        if not files:
            print(f"{self.colors.YELLOW}⚠ Storage kosong!{self.colors.RESET}")
            input(f"\n{self.colors.YELLOW}Tekan Enter untuk kembali...{self.colors.RESET}")
            return
        
        print(f"{self.colors.CYAN}📂 Files in storage ({len(files)}):\n")
        
        for i, file in enumerate(files, 1):
            size = os.path.getsize(f"{self.results_dir}/{file}")
            size_str = f"{size/1024:.2f} KB" if size < 1024*1024 else f"{size/(1024*1024):.2f} MB"
            print(f"  {self.colors.WHITE}[{i:02d}] {self.colors.GREEN}{file} {self.colors.WHITE}({size_str})")
        
        print(f"\n{self.colors.CYAN}Options:")
        print(f"  {self.colors.WHITE}[1] Delete all storage")
        print(f"  {self.colors.WHITE}[2] Back")
        
        choice = input(f"\n{self.colors.YELLOW}⌨ Pilih [1-2]: ")
        
        if choice == '1':
            confirm = input(f"{self.colors.RED}⚠ Hapus semua data? (y/n): ")
            if confirm.lower() == 'y':
                shutil.rmtree(self.results_dir)
                os.makedirs(self.results_dir)
                print(f"{self.colors.RED}✓ Storage deleted!{self.colors.RESET}")
                input(f"\n{self.colors.YELLOW}Tekan Enter untuk kembali...{self.colors.RESET}")
