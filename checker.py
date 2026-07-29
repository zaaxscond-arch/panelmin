import requests
import json

class LinkChecker:
    def __init__(self):
        with open('config/headers.json', 'r') as f:
            self.headers = json.load(f)
    
    def check(self, base_url, path, path_type):
        full_url = f"{base_url}/{path}" if not base_url.endswith('/') else f"{base_url}{path}"
        
        try:
            response = requests.get(
                full_url,
                timeout=5,
                headers=self.headers['user_agent'],
                allow_redirects=True
            )
            
            if response.status_code == 200:
                return {
                    'url': full_url,
                    'status': 'WORKING',
                    'type': path_type,
                    'code': response.status_code
                }
            else:
                return {
                    'url': full_url,
                    'status': f'HTTP {response.status_code}',
                    'type': path_type,
                    'code': response.status_code
                }
                
        except requests.exceptions.Timeout:
            return {'url': full_url, 'status': 'TIMEOUT', 'type': path_type, 'code': 0}
        except requests.exceptions.ConnectionError:
            return {'url': full_url, 'status': 'CONNECTION ERROR', 'type': path_type, 'code': 0}
        except Exception as e:
            return {'url': full_url, 'status': f'ERROR: {str(e)[:20]}', 'type': path_type, 'code': 0}
