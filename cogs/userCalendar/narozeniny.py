from discord import Member
from enum import Enum
from datetime import date

from databaseApi import select_user_by_id, \
    insert_user, update_user_by_id


class NarozeninyError(Enum):
    OK = 0
    AlreadySet = 1
    DateNotExists = 2
    InsertError = 3
    UpdateError = 4


async def set_narozeniny(
    user: Member,
    bdate: date,
) -> tuple[NarozeninyError, str]:
    db_entry = await select_user_by_id(user.id)

    data = {
        "id": user.id,
        "dc_name": user.global_name,
        "naroz_Den": bdate.day,
        "naroz_Mesic": bdate.month,
    }

    if "status" not in db_entry or db_entry["status"] == '200':
        if db_entry["naroz_Den"] == bdate.day \
                and db_entry["naroz_Mesic"] == bdate.month:
            return NarozeninyError.AlreadySet, None
        else:
            result = await update_user_by_id(user.id, data)
            if "status" in result and result["status"] != '200':
                return NarozeninyError.UpdateError, str(result)
            elif db_entry["naroz_Den"] is not None \
                    and db_entry["naroz_Mesic"] is not None:
                bdate = date(
                    year=2024,
                    day=db_entry["naroz_Den"],
                    month=db_entry["naroz_Mesic"]
                )
            return NarozeninyError.OK, bdate
    else:
        result = await insert_user(data)
        if "status" in result and result["status"] != '201':
            return NarozeninyError.InsertError, str(result)
        return NarozeninyError.OK, bdate
