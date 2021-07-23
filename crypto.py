from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open('Data/key', 'wb') as encrypted_file:
        encrypted_file.write(key)


def get_key():
    with open('Data/key', 'rb') as file:
        return Fernet(file.read())


def save_scores(scores_dict):
    key = get_key()
    scores_data = ""
    for i in range(len(scores_dict)):
        line = scores_dict[i+1]
        for j in range(len(line)):
            data = str(line[j])
            scores_data += data
            if j < len(line) - 1:
                scores_data += ", "
            elif i < len(scores_dict) - 1:
                scores_data += "\r\n"

    with open("Data/scores.dat", "wb") as file:
        encrypted_data = key.encrypt(scores_data.encode('utf-8'))
        file.write(encrypted_data)


def load_scores(key, default_scores):
    hall_of_fame = {}
    while not hall_of_fame:
        try:
            with open('Data/scores.dat', 'rb') as encrypted_file:
                decrypted = key.decrypt(encrypted_file.read())

            mylist = decrypted.decode().split('\r\n')
            for line in mylist:
                data = line.split(', ')
                hall_of_fame[int(data[0])] = data
            return hall_of_fame
        except FileNotFoundError:
            save_scores(default_scores)
