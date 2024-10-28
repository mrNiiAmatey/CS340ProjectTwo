#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:36:42 2024

@author: niiamateytago_snhu
"""
from pymongo import MongoClient, errors


class Animal_Shelter(object):
    
    def __init__(self, username= 'aacuser', password= 'skibolski', host= 'nv-desktop-services.apporto.com', port=30709, db='AAC', collection='animals'):
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.database = self.client[db]
        self.collection =self.database[collection]
    
    def create(self, data):
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            
            except Exception as e:
                print("An exception occured during insert:", e)
                return False
            
        else:
            raise ValueError("This is an Empty Data parameter")
                
                
    def read(self, query):
        
        if query is not None:
            try:
                cursor = self.collection.find(query)
                return list(cursor)
        
            except Exception as e:
                print("An exception occured during read:", e)
                return []
            else:
                raise ValueError("Query parameter is empty, cannot perform read operation")
    
    def update(self, query, new_values):
        if query and new_values:
            try:
                result = self.collection.update_one(query, {'$set': new_values})
                if result.modified_count > 0:
                    return True
                else:
                    return False
            except Exception as e:
                print("An exception occured during update:", e)
                return False
        else:
            raise ValueError("Query or new_values parameter is empty, cannot perform update operation")
    
    def delete(self, query):
        if query:
            try:
                result = self.collection.delete_one(query)
                if result.delete_count > 0:
                    return True
                else:
                    return False
            except Exception as e:
                print("An exception occured during delete:", e)
                return False
        else:
            raise ValueError("Query parameter is empty, cannot perform delete operarion")
            



    

            
