import sys

def sorting():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if len(sys.argv) == 2:
        task = sys.argv[1]
        res = []
        if task == "call_center":
            for notviewer in clients:
                if notviewer not in recipients:
                    res.append(notviewer)

        elif task == "potential_clients":
            for part in participants:
                if part not in clients:
                    res.append(part)
        elif task =="loyalty_program":
            for client in clients:
                if client not in participants:
                    res.append(client)
        else:
            print("wrong task")

        if res:
            print(res)
if __name__ == '__main__':
    sorting()