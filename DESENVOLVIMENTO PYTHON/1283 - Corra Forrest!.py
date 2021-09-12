volta=[]
contador=0
media=0
volta.append(input().split())
volta[contador][0] = int(volta[contador][0])
while volta[contador][0]>0:
    contador+=1
    volta.append(input().split())
    volta[contador][0]=int(volta[contador][0])
contador=0
while contador<len(volta)-1:
    media=media+volta[contador][0]
    contador+=1
contador=0
media=media/(len(volta)-1)
print('MEDIA:',"%.2f"% media)
while contador<(len(volta)-1):
    if volta[contador][0]<media:
        print(volta[contador][0])
    contador+=1