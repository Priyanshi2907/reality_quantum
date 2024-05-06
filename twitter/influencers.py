influ={
    "Influencers": "[Ankit Handa : https://twitter.com/ankit_handa], [Neeraj Bansal : https://twitter.com/Sirf_Property], [Udaibhan Singh Rathore : https://twitter.com/UdaibhanRathore], [Amit Kalra : https://twitter.com/amitkalra_re], [Vikrant Bhatia : https://twitter.com/vikrant_bhatia], [Maheshwari Estate : https://twitter.com/MaheshwariEstate], [Deepak Kumar : https://twitter.com/DeepakKum177317], [Prateek Rao : https://twitter.com/prateek1805]"
}
for i in influ.values():
    i_list=i.split(",")
    print(type(i_list))
    for j in range(len(i_list)):
       name= i_list[j].split(" : ")[0].replace("[","")
       profile=i_list[j].split(" : ")[1].replace("]","")
    #print(i)
    print("*********")
#print (influ["Influencers"][])