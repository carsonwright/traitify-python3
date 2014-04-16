import http.client, urllib, base64, json
class Assessment:
	def __init__(self, attributes):
		self.id = attributes["id"]
		self.user_id = attributes["user_id"]
		self.deck_id = attributes["deck_id"]
		self.completed_at = attributes["completed_at"]
		self.created_at = attributes["created_at"]

class Traitify:
	def __init__(self, configurations = {"host":"", "secret_key":"", "public_key":"", "deck_id":""}):
		self.host = configurations["host"]
		self.secret_key = configurations["secret_key"]
		self.public_key = configurations["public_key"]
		self.deck_id = configurations["deck_id"]

	def create_assessment(self):
		headers = {"Accept":"application/json", "Content-Type":"application/json", "Authorization": "Basic "+self.private_key+":x"}
		conn = http.client.HTTPConnection(self.host)
		conn.request("POST", "/"+self.version+"/assessments", '{"deck_id":"'+self.deck_id+'"}', headers)
		response = conn.getresponse()
		data = response.read().decode()
		conn.close()
		json_data = json.loads(str(data))
		return Assessment(json_data)