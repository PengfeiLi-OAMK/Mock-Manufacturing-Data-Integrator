import requests
from typing import Dict, Any
class PyWATSClient:
	"""
    Mock client for uploading standardized manufacturing test results 
    to a WATS-style backend over a REST API.
    """
	def __init__(self, api_url: str, token: str):
		self.api_url = api_url
		self.headers={
			'Authorization':f'Bearer {token}',
			'Content-Type':'application/json',
			"User-Agent": "Mock-Manufacturing-Data-Integrator/1.0"
		}
	def submit_report(self,report_data:Dict[str,Any])->bool:
		try:
			print(f"Uploading report for Product ID: {report_data.get('product_id', 'Unknown')}...")
			response = requests.post(
				self.api_url,
				json=report_data,
				headers=self.headers,
				timeout=10
			)
			if response.status_code == 200:
				print(f"✅ Success! Server responded: {response.status_code}")
				print(f"[Debug] Server received: {response.json()['json']}") 
				return True
			else:
				print(f"❌ Failed. Status: {response.status_code}")
				print(f"Reason: {response.text}")
				return False
		except requests.exceptions.ConnectionError:
			print("❌ Connection Error: Unable to reach the pyWATS server.")
			return False
		except requests.exceptions.Timeout:
			print("❌ Timeout Error: Server took too long to respond.")
			return False
		except Exception as e:
			print(f"❌ Unexpected Error: {e}")
			return False

   
