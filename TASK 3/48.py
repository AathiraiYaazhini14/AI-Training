cf={
    "host":"localhost",
    "port":8080,
    "debug":True,
    "timeout":30
}

rk={"host","port","debug","log_level"}

ck=set(cf.keys())
mk=rk-ck
ek=ck-rk

print(mk)
print(ek)
