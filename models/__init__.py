#!/usr/bin/python3
"""
    This is the model init module.
"""
from models.engine.file_storage import FileStorage
"""
Retrieves the storage instance
"""
storage = FileStorage()
storage.reload()
