from .slack_connect import SlackConnect

class MainService:
    
    slack_connector = SlackConnect()
    
    def main(self):
        self.slack_connector.main()
        return {"message": "main funcionando"}