def identifier(data):
        if  data.isalnum() and len(data) >= 1 and len(data) <= 6 and data[0].isalpha():
            return True
        else:
            return False