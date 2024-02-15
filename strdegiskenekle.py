a="ile"
print("ali",a,"veli")      # 1. yöntem

print("ali " +a+" veli")   # 2. yöntem

b="aliveli"                # 3. yöntem
b2=b[:3]+" "+a+" "+b[3:]
print(b2)

c="ali {} veli"            # 4. yöntem
print(c.format(a))