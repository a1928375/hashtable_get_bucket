def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(table))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

table = [[['Francis', 13], ['Ellis', 11]], 
          [], 
          [['Bill', 17],['Zoe', 14]], 
          [['Coach', 4]], 
          [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print hashtable_get_bucket(table, "Zoe")
print hashtable_get_bucket(table, "Brick")
print hashtable_get_bucket(table, "Lilith")
