def what_is_my_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 20):
        return '����'
    elif (month == 4 and day >= 21) or (month == 5 and day <= 20):
        return '�����'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return '��������'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 21):
        return '���'
    elif (month == 7 and day >= 22) or (month == 8 and day <= 22):
        return '���'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return '����'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return '�����'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return '��������'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return '�������'
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return '�������'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return '�������'
    else:
        return '����'