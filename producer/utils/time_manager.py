from datetime import datetime,timedelta,date
import os
import json
import time

class StateManager:
    def __init__(self,state_file="state.json"):
        self.state_file = state_file
        if not os.path.exists(self.state_file):
            current = datetime.utcnow()
            first_run =  current - timedelta(days=1)

            state = {
                "last_run_timestamp":int(first_run.timestamp()),
                "last_run_date":first_run.strftime("%Y-%m-%d")
            }

            with open(self.state_file,"w") as file:
                json.dump(state,file,indent=4)
    def get_state(self):
        with open(self.state_file,"r") as file:
            return json.load(file)

    def update_state(self):
        current = datetime.utcnow()
        state = {
            "last_run_timestamp":int(current.timestamp()),
            "last_run_date":current.strftime("%Y-%m-%d")
        }

        with open(self.state_file,"w") as file:
            json.dump(state,file,indent=4)


    