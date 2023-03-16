from aiogram.dispatcher.filters.state import State, StatesGroup
from data_base import sqlite_db

class NewsStates(StatesGroup):
    title = State()
    content = State()
    image = State()

class CreateGroupStates(StatesGroup):
    group_name = State()

class DeleteGroupStates(StatesGroup):
    group_name = State()

class StartGroupStates(StatesGroup):
    group_name = State()

class SelectGroupStates(StatesGroup):
    group_name = State( )

class ScheduleStates(StatesGroup):
    select_group = State()
    image = State()

class DeleteScheduleStates(StatesGroup):
    select_group = State()