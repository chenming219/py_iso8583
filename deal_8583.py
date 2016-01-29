#! /usr/bin/env python
# -*- coding: utf-8 -*

class deal_content_type:
    __op=""
    def __init__(self, op):
        __op=op
        
    def BCD(self,data,len,offset):
        len=len
        padding=1 if len%2 else 0
        return (data[offset:offset+len],len+padding)
    
    def BINARY(self,data,len,offset):
        len=len/4
        return (data[offset:offset+len],len)
    
    def ASCII(self,data,len,offset):
        len=len*2
        return (data[offset:offset+len].decode("hex"),len)
    
    
class deal_len_type:
    __op=""
    def __init__(self, op):
        __op=op
        
    def fixed(self,cfg,data,offset):
        return (cfg["max_len"],0)
    
    def LLVAR(self,cfg,data,offset):
        len = 2
        return (int(data[offset:offset+len]),len)
    
    def LLLVAR(self,cfg,data,offset):
        len = 2*2
        return (int(data[offset:offset+len]),len)
    