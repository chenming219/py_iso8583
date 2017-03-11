#! /usr/bin/env python
# -*- coding: utf-8 -*

class deal_content_type:
    def BCD_unpack(self,data,len,offset):
        len=len
        padding=1 if len%2 else 0
        return (data[offset:offset+len],len+padding)
    
    def BINARY_unpack(self,data,len,offset):
        len=len/4
        return (data[offset:offset+len],len)

    def BCD_UNC_unpack(self,data,len,offset):
        len=len*2
        return (data[offset:offset+len],len)

    def ASCII_unpack(self,data,len,offset):
        len=len*2
        return (data[offset:offset+len].decode("hex"),len)
    
    #pack
    def BCD_pack(self,data):
        data_len=len(data)
        padding="0" if data_len%2 else ""
        d_data = data + padding
        return d_data
    
    def BINARY_pack(self,data):
        return data

    def BCD_UNC_pack(self,data):
        return data

    def ASCII_pack(self,data):
        return data.encode("hex")
    
class deal_len_type:
    def fixed_unpack(self,cfg,data,offset):
        return (cfg["max_len"],0)

    def fixed_b_unpack(self,cfg,data,offset):
        return (cfg["max_len"],0)
    
    def fixed_ub_unpack(self,cfg,data,offset):
        return (cfg["max_len"],0)   
    
    def LLVAR_unpack(self,cfg,data,offset):
        len = 2
        data_len=int(data[offset:offset+len])
        assert data_len <= 99,"LLVAR len err"
        return (data_len,len)

    def LLVAR_ASC_unpack(self,cfg,data,offset):
        len = 2*2
        data_len=int(data[offset:offset+len].decode('hex'))
        assert data_len <= 99,"LLVAR len err"
        return (data_len,len)
    
    def LLLVAR_unpack(self,cfg,data,offset):
        len = 2*2
        data_len=int(data[offset:offset+len])
        assert data_len <= 999,"LLLVAR len err"
        return (data_len,len)

    def LLLVAR_ub_unpack(self,cfg,data,offset):
        len = 3*2
        data_len=int(data[offset:offset+len].decode('hex'))
        assert data_len <= 999,"LLLVAR len err"
        return (data_len,len)

    def LLLVAR_ASC_unpack(self,cfg,data,offset):
        len = 3*2
        data_len=int(data[offset:offset+len].decode('hex'))
        assert data_len <= 999,"LLLVAR len err"
        return (data_len,len)
    
    #pack
    def fixed_pack(self,cfg,data):
        max_len = cfg["max_len"]
        data_len = len(data)
        assert data_len == max_len,"fixed len err"
        len_val = ""
        return len_val
    
    def fixed_ub_pack(self,cfg,data):
        max_len = cfg["max_len"]
        data_len = len(data)
        assert data_len == max_len*2,"fixed_b len err"
        len_val = ""
        return len_val

    def fixed_b_pack(self,cfg,data):
        max_len = cfg["max_len"]
        data_len = len(data)
        assert data_len*4 == max_len,"fixed_b len err"
        len_val = ""
        return len_val
    
    def LLVAR_pack(self,cfg,data):
        max_len = cfg["max_len"]
        data_len = len(data)
        assert data_len <= max_len,"LLVAR len err"
        len_val = "%02d" % data_len
        return len_val

    def LLVAR_ASC_pack(self,cfg,data):
        max_len = cfg["max_len"]
        data_len = len(data)/2
        assert data_len <= max_len,"LLVAR len err"
        len_val = ("%02d" % data_len).encode('hex')
        return len_val
    
    def LLLVAR_pack(self,cfg,data):
        max_len = cfg["max_len"]
        data_len = len(data)
        assert data_len <= max_len,"LLLVAR len err"
        len_val = "0%03d" % data_len
        return len_val

    def LLLVAR_ub_pack(self,cfg,data):
        max_len = cfg["max_len"]
        data_len = len(data)/2
        assert data_len <= max_len,"LLLVAR len err"
        len_val = ("%03d" % data_len).encode('hex')
        return len_val

    def LLLVAR_ASC_pack(self,cfg,data):
        max_len = cfg["max_len"]
        data_len = len(data)
        assert data_len <= max_len,"LLLVAR len err"
        len_val = ("%03d" % data_len).encode('hex')
        return len_val