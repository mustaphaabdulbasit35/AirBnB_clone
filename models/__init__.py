#!/usr/bin/python3
"""
Represents the dunder initialisation module
for the models' directory. It loads as soon as the models
dir is initialised
"""
from models.engine.file_storage import FileStorage


storage = FileStorage
storage.reload