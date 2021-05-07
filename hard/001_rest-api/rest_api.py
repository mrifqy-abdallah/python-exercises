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
            
            response = {"users": []}

            for user in self.db["users"]:
                if user["name"] in collect_users:
                    response["users"].append(user)
                if len(response["users"]) == len(collect_users):
                    break

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

            for user in self.db["users"]:
                lender_is_updated = False
                borrower_is_updated = False

                if user["name"] == lender:
                    user["balance"] += amount
                    # In case the lender owes the borrower
                    if borrower in user["owes"]:
                        # Check if the borrower wants to owe money more than the lender owes
                        check_count = user["owes"][borrower] - amount 
                        # Is True if the borrower wants to owe money more than the lender owes
                        if check_count <= 0:
                            # Avoid the case of record ` "owed_by": {<someone>: 0.0} `
                            if check_count != 0:
                                user["owed_by"][borrower] = -check_count
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
                    # In case the borrower is owed by the lender
                    if lender in user["owed_by"]:
                        # Check if the borrower wants to owe money more than owed by the lender
                        check_count = user["owed_by"][lender] - amount
                        # Is True if the borrower wants to owe money more than owed by the lender
                        if check_count <= 0:
                            # Avoid the case of record ` "owes": {<someone>: 0.0} `
                            if check_count != 0:
                                user["owes"][lender] = -check_count
                            del user["owed_by"][lender]
                        else:
                            user["owed_by"][lender] = check_count
                    else:
                        if lender not in user["owes"]:
                            user["owes"][lender] = 0
                        user["owes"][lender] += amount
                    response.append(user)
                    lender_is_updated = True

                if lender_is_updated and borrower_is_updated:
                    break
            
            response = {"users": response}
            return json.dumps(response)