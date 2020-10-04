from webdav3.client import Client

class WebDavClient:
    def __init__(self,settings):
        self._settings = settings
        self.client = Client(self._settings["WebDavClient"])
        self.Name = self._settings["Name"]
        self.UpRemotes()
    
    def UpRemotes(self):
        self.Remotes = self.client.list()
    
    def Upload(self, remote_path="", local_path=""):
        self.client.upload_sync(remote_path=remote_path, local_path=local_path)