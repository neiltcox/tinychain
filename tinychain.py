#!/usr/bin/env python3
"""
A simple blockchain
"""
__author__ = "Neil Schultz-Cox"

import hashlib
import datetime
from collections import defaultdict


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        return hashlib.sha256( \
        str(self.index) + \
        str(self.timestamp) + \
        str(self.data) + \
        str(self.previous_hash))
    
    def __str__(self):
        return "================================" \
        + "\nIndex: " + str(self.index) \
        + "\nTimestamp: " + str(self.timestamp) \
        + "\nData: " + self.data \
        + "\nPrevious Hash: " + str(self.previous_hash.hexdigest()) \
        + "\nHash: " + str(self.hash.hexdigest()) \
        + "\n================================"

blockchain = defaultdict(Block)
current_head = None

def create_genesis_block():
    genesis_block = Block(0, datetime.datetime.now(), "GENESIS BLOCK", hashlib.sha256("-1"))
    blockchain[genesis_block.hash] = genesis_block
    return genesis_block

def add_block(last_block, data):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = data
    last_hash = last_block.hash
    new_block = Block(this_index, this_timestamp, this_data, last_hash)
    blockchain[new_block.hash] = new_block
    return new_block

def explore(block):
    if block.index == 0:
        print(block)
        return
    else:
        print(block)
        explore(blockchain[block.previous_hash])

def main():
    print("Creating genesis block...")
    current_head = create_genesis_block()
    
    print("\nExploring blockchain:")
    explore(current_head)
    
    print("\nAdding blocks...")
    for i in range(0, 5):
        current_head = add_block(current_head, "I'M BLOCK #" + str(i))
    
    print("\nExploring blockchain:")
    explore(current_head)

if __name__ == "__main__":
    main()