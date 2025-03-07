
'''
Copyright 2021-2022 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''

# s = "hello"
# x = "Python"
# y = "!!!"
#
# print(s + " Python" + "!!!")
# print((s + ' ') * 3 + " Python" + "!" * 10)
# print("hello %(x)s%(y)s" % {"x": "Python", "y": "!!!"})
# print("hello {0}{1}".format(x, y))
# print("hello {1} {0}".format(x, y))
# print("hello {x}{y}".format(x="Pluto", y="???"))
# print(f"hello {x}{y}")

# ToDO: Format strings coming from user inputs.

n = str(input("Nome:"))
c = str(input("Cognome:"))

print(f"{n} {c} é il nome del cliente.")

nome = None
cognome = None

while not nome:
    nome = input('\ncome fai di nome? ').replace(' ','')
while not cognome:
    cognome = input('\ncome fai di cognome? ').replace(' ','')
print(f"Ciao, {nome} {cognome}")
