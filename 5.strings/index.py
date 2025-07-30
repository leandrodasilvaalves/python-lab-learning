a = """
Lorem ipsum dolor sit amet
sed do eiusmod tempor incididunt
"""

print(a)

a = "Leandro"
b = "Alves"
print(a[0])

for x in "banana":
    print(x)

print(len(a))

# check string
txt = "the best things in life are free!"
print("free" in txt)
print("Free" in txt)
print("foo" in txt)

if "free" in txt:
    print("yes, 'free' is present.")

print("foo" not in txt)

print(a[2:5]) #and
print(a[:5]) #Leand
print(a[2:]) #andro
print(a[-5:]) #andro

print(a[-5:-2]) #and - 
#pega 5 do final pro começo. 
# #desse resuldo remove 2 do final

print(a.upper())
print(a.lower())
print(a.strip())
print(a + " "+ b)

# String Format
age=39
txt = f"My name is Leandro, I am {age}"
print(txt)

price=59.2
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {price * 3:.2f} dollars"
print(txt)

# String Methods
name = "leandro alves"
print(name.capitalize())
print(name.center(40))
print(name.center(40,"-"))
print(name.count('a'))

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49.3))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

a = "hello"
b = "wellcome to the jungle"
c = "10.000"
print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
