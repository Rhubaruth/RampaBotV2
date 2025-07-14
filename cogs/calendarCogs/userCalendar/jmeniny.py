from discord import Member
from enum import Enum

from databaseApi import select_user_by_id, select_date_by_name, \
    insert_user, update_user_by_id


class JmeninyError(Enum):
    OK = 0
    AlreadySet = 1
    NameNotFound = 2
    InsertError = 3
    UpdateError = 4


def set_jmeniny(user: Member, name: str) -> (JmeninyError, str):
    db_entry = await select_user_by_id(user.id)

    if "first_name" in db_entry:
        return JmeninyError.AlreadySet, db_entry["first_name"]

    result = await select_date_by_name(name)
    if "status" in result:
        return JmeninyError.NameNotFound

    if "first_Name" in user:
        data = {"id": user.id, "first_Name": name}
        result = await update_user_by_id(user.id, data)
        if "status" in result:
            return JmeninyError.InsertError
    else:
        data = {"id": user.id, "first_Name": name}
        await insert_user(data)
        if "status" in result:
            return JmeninyError.UpdateError
    return JmeninyError.OK
