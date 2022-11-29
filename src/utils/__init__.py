import utils.database
from utils.config import config
import constants


# example of usage: send_no_permission(query.answer)
async def send_no_permission(answer_func: callable):
    await answer_func(constants.language.no_permission)

