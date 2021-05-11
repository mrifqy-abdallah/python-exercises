import json


class RestAPI:
    def __init__(self, database:dict=None):
        # Valid database format should be: {"users": [{<user1>}, {<user2>}, {<user3>}]} 
        # Or just leave it empty: {"users": []}
        self.db = database

    def get(self, url:str, payload:str=None):
        ''' GET user(s) data. If payload is None, respond with all users data. '''
        # Valid payload format should be: '{"users": ["<user1>", "<user2>", "<user3>"]}'
        if url == "/users":
            if payload is None:
                return json.dumps(self.db)

            payload = json.loads(payload)
            collect_users = tuple(payload["users"])
            
            response = []

            for user in self.db["users"]:
                if user["name"] in collect_users:
                    response.append(user)
                if len(response) == len(collect_users):
                    break

            response = {"users": response}
            return json.dumps(response)
            

    def post(self, url:str, payload:str=None):
        '''POST new user data (/add) or IOU transaction (/iou). If payload is None, no response will be given.'''
        if payload is None:
            return None

        if url == "/add":
            # Payload format should be: {"user":<name of new user (unique)>}             
            payload = json.loads(payload)
            
            for user in self.db["users"]:
                if user["name"] == payload["user"]:
                    raise Exception("Name already taken, please choose another name.")
            
            response = {"name": payload["user"], "owes": {}, "owed_by": {}, "balance": 0.0}
            self.db["users"].append(response)
            return json.dumps(response)

        elif url == "/iou":
            # Payload format MUST be: {"lender":<name of lender>,"borrower":<name of borrower>,"amount":5.25}
            response = []
            payload = json.loads(payload)
            try:
                lender = payload["lender"]
                borrower = payload["borrower"]
                amount = payload["amount"]
            except KeyError:
                print('Payload format must be in:\n\'{"lender":<name of lender>,"borrower":<name of borrower>,"amount":5.25}\'')

            # Now imagine special cases like where self.db has this value,
            # {"users": [
            #         {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
            #         {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0}
            # ]}
            # And then the payload is one of these:
            #
            # Case 1: {"lender": "Adam", "borrower": "Bob", "amount": 2.0}
            #         This is where the lender owes the borrower by record
            #         Therefore we need to check this case before assigning the payload to self.db
            # 
            # Case 2: {"lender": "Adam", "borrower": "Bob", "amount": 4.0}
            #         It's just like Case 1, but the borrower wants to owe money MORE THAN the lender owes
            #         The output of this case MUST be
            #               {"name": "Adam", "owes": {}, "owed_by": {"Bob": 1.0}, "balance": 1.0},
            #               {"name": "Bob", "owes": {"Adam": 1.0}, "owed_by": {}, "balance": -1.0}
            #
            # Case 3: {"lender": "Adam", "borrower": "Bob", "amount": 3.0}
            #         It's also like Case 1, but the borrower wants to owe money EXACTLY as the lender owes
            #         This one case is actually the same as collecting a debt
            #         The output like this:
            #               {"name": "Adam", "owes": {"Bob": 0.0}, "owed_by": {}, "balance": 0.0},
            #               {"name": "Bob", "owes": {}, "owed_by": {"Adam": 0.0}, "balance": 0.0}
            #         where `owes` or `owed_by` contains 0.0 (or less) must be avoided

            lender_is_updated = False
            borrower_is_updated = False

            for user in self.db["users"]:
                if lender_is_updated and borrower_is_updated:
                    break

                if user["name"] == lender:
                    user["balance"] += amount
                    # In case of Case 1
                    if borrower in user["owes"]:
                        # Set value checker
                        check_count = user["owes"][borrower] - amount 
                        # Is True if the payload happens to be just like Case 2 or Case 3
                        if check_count <= 0:
                            # Set an if to avoid the case of Case 3
                            if check_count != 0:
                                user["owed_by"][borrower] = abs(check_count)
                            del user["owes"][borrower]
                        else:
                            user["owes"][borrower] = check_count
                    else:
                        if borrower not in user["owed_by"]:
                            user["owed_by"][borrower] = 0
                        user["owed_by"][borrower] += amount
                    response.append(user)
                    lender_is_updated = True

                elif user["name"] == borrower:
                    user["balance"] -= amount
                    # In case of Case 1
                    if lender in user["owed_by"]:
                        # Set value checker
                        check_count = user["owed_by"][lender] - amount
                        # Is True if the payload happens to be just like Case 2 or Case 3
                        if check_count <= 0:
                            # Set an if to avoid the case of Case 3
                            if check_count != 0:
                                user["owes"][lender] = abs(check_count)
                            del user["owed_by"][lender]
                        else:
                            user["owed_by"][lender] = check_count
                    else:
                        if lender not in user["owes"]:
                            user["owes"][lender] = 0
                        user["owes"][lender] += amount
                    response.append(user)
                    borrower_is_updated = True
            
            response = {"users": response}
            return json.dumps(response)