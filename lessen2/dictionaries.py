#collection of items , mutabel ,not indexble, works on a pair key:value
contact_into={
    "alma":"049777777",
    "bkia":"049777777"

}
print(contact_into)
alma_info=contact_into["alma"]
print(alma_info)
contact_into["leart"]="04777777"
contact_into["leart"]="04777777"
del contact_into["leart"]
print(contact_into)
keys=contact_into.keys()
print(keys)
values=contact_into.values()
print(values)
items=contact_into.items()
print(items)#print out the key-vales pair as e lists
