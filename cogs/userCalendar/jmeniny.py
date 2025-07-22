from discord import Member
from enum import Enum

from databaseApi import select_user_by_id, select_daymonth_by_nameday, \
    insert_user, update_user_by_id


class JmeninyError(Enum):
    OK = 0
    AlreadySet = 1
    NameNotFound = 2
    InsertError = 3
    UpdateError = 4


async def set_jmeniny(
    user: Member,
    name: str,
) -> tuple[JmeninyError, str]:
    db_entry = await select_user_by_id(user.id)

    if "first_Name" in db_entry:
        if db_entry["first_Name"] is not None:
            return JmeninyError.AlreadySet, db_entry["first_Name"]

    result = await select_daymonth_by_nameday(name)
    if "status" in result:
        return JmeninyError.NameNotFound, name

    data = {
        "id": user.id,
        "first_Name": name,
        "dc_name": user.global_name,
    }
    if "first_Name" in db_entry:
        result = await update_user_by_id(user.id, data)
        if "status" in result:
            if result['status'] == '200':
                return JmeninyError.OK, name
        return JmeninyError.UpdateError, str(result)
    else:
        result = await insert_user(data)
        if "status" in result:
            if result['status'] == '200':
                return JmeninyError.OK, name
        return JmeninyError.InsertError, str(result)
    return JmeninyError.OK, name
