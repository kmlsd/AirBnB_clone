#!/usr/bin/python3
"""
    This is the model init module.
"""
from .engine.file_storage import FileStorage
"""
Retrieves the storage instance
"""
storage = FileStorage()
storage.reload()
