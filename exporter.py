import csv
import os
from datetime import datetime
from src.utils.colors import Colors

class XLSExporter:
    def __init__(self):
        self.colors = Colors()
        self.storage_dir = "storage"
        self.export_dir = f"{self.storage_dir}/exports"
        
    def export(self, working, failed):
        if not os.path.exists(self.export_dir):
            os.makedirs(self.export_dir)
        
        if not working and not failed:
            print(f"{self.colors.RED}✗ Tidak ada data untuk diexport!{self.colors.RESET}")
            return
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        xls_file = f"{self.export_dir}/login_data_{timestamp}.xls"
        
        with open(xls_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(['No', 'URL', 'Status', 'Type', 'HTTP Code', 'Timestamp'])
            
            all_data = working + failed
            for i, link in enumerate(all_data, 1):
                writer.writerow([
                    i,
                    link['url'],
                    link['status'],
                    link.get('type', '-'),
                    link.get('code', '-'),
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ])
        
        print(f"\n{self.colors.GREEN}✓ XLS file saved: {xls_file}")
        print(f"{self.colors.GREEN}✓ Total data: {len(working) + len(failed)} entries")
        print(f"{self.colors.GREEN}✓ Working: {len(working)}, Failed: {len(failed)}")
        
        input(f"\n{self.colors.YELLOW}Tekan Enter untuk kembali...{self.colors.RESET}")
