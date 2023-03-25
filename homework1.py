#SORU1
# string(str), float, boolean(bool), integer(int)
strMeaning = "String metinsel ifadeler icin kullanilir."
floatMeaning = "Float ondalikli sayilari ifade eder."
boolMeaning = "Boolean True yada False ifadelerini ifade eder."
intMeaning = "Integer ifade tam sayirlari ifade eder."

result = 'soru1', strMeaning, floatMeaning, boolMeaning, intMeaning

print (result)


print ("************************************************************************************************************************************************************************************")
#SORU2
# Kurs isimleri veri tipi string. 
# Kurs tamamlamasi yuzdesi integer. 
#Kullanici 


#SORU3
userName= "Alper"

userPassword= "0000"

userName1= input("lütfen Id'nizi giriniz: ")
userPassword1 = (input("lütfen sifrenizi giriniz: "))

if userName1 == userName and userPassword1 == userPassword:
  print("Onaylandi ")
else:
  print("kullanici adi yada sifre hatali olabilir")