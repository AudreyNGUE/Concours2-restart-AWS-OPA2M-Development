import copy
import random
import datetime


#Définition des modèles

productDictionnary= {

    "Reference" : "",
    "Nom du Produit" :"",
    "Prix":0.0,
    "Quantité":0

}

custumerDictionnary={
    "Nom" : "",
    "Id" : "",
    "Montant Total Achat" : 0.0,
    "Nombre de points Hebdommadaires" : 0,
    "Nombre de points Total" : 0,
    "Point convertis en argent" : 0.0
}


productCatalogue=[]
custumerList=[]

#Enoncé des fonctionnalités
#Ajouter un produit au catalogue

#Fonction de verification de l'existence d'un produit
def productVerification(refProduct,productCatalogue):
    for product in productCatalogue:
        if product['Reference']==refProduct :
            return True
    

#Fonction de confirmation avant la création d'un produit
def productConfirmCreation(refProduct,nameProduct,priceProduct,qtyProduct):
    print("Vous allez créer le produit {}, de reference {} dont la quantité est {} et qui coute {} F l'unité".format(nameProduct,refProduct,qtyProduct,priceProduct))
    userInputConfirmation=input("Confirmez-vous la création de ce produit ?(Entrez \"Yes\" pour confirmer, \"No\" pour annuler__")
    if userInputConfirmation=="Yes":
        return True

#Fonction de creation d'un produit
def productCreation(refProduct,nameProduct,priceProduct,qtyProduct):
    if productVerification(refProduct,productCatalogue):
        print("Votre produit existe déjà")
    else:
        if productConfirmCreation(refProduct,nameProduct,priceProduct,qtyProduct):
            currentProductDictionnary=copy.deepcopy(productDictionnary)
            currentProductDictionnary['Reference']=refProduct
            currentProductDictionnary['Nom du Produit']=nameProduct
            currentProductDictionnary['Prix']=priceProduct
            currentProductDictionnary['Quantité']=qtyProduct

            productCatalogue.append(currentProductDictionnary)
            return currentProductDictionnary

        else:
            print("MENU")

#fonction de confirmation de modification du stock
def productConfirmStockModification(refProduct,newQtyProduct):
    print("Vous allez modifier le stock du produit de reference {}.La nouvelle quantité sera {} ".format(refProduct,newQtyProduct))
    userInputConfirmation=input("Confirmez-vous la modification du stock de ce produit ?(Entrez \"Yes\" pour confirmer, \"No\" pour annuler__")
    if userInputConfirmation=="Yes":
        return True

#fonction de modification d'un produit 
def productModification(userInputChoice):
    refProduct=input("Reference :")
    if (userInputChoice=="1"):
        newQtyProduct=input("Enter:")
        newStock=productStockModification(refProduct,productCatalogue,newQtyProduct)
        print(newStock)
    elif (userInputChoice=="2"):
        newPriceProduct=input("eNTEROH:")
        newProduct=productPriceModification(refProduct,productCatalogue,newPriceProduct)
        print(newProduct)
    else:
        print("MENU")

#fonction de modification du stock d'un produit
def productStockModification(refProduct,productCatalogue,newQtyProduct):
        if productVerification(refProduct,productCatalogue):
           for product in productCatalogue:
                if productConfirmStockModification(refProduct,newQtyProduct):
                    product['Quantité']=newQtyProduct  
                return productCatalogue

#fonction de confirmation de modification du prix
def productConfirmPriceModification(refProduct,newPriceProduct):
    print("Vous allez modifier le prix du produit de reference {}.Le nouveau prix sera {} ".format(refProduct,newPriceProduct))
    userInputConfirmation=input("Confirmez-vous la modification du prix de ce produit ?(Entrez \"Yes\" pour confirmer, \"No\" pour annuler__")
    if userInputConfirmation=="Yes":
        return True

#fonction de modification du prix d'un produit
def productPriceModification(refProduct,productCatalogue,newPriceProduct):
        if productVerification(refProduct,productCatalogue):
           for product in productCatalogue:
                if productConfirmPriceModification(refProduct,newPriceProduct):
                    product['Prix']=newPriceProduct  
                return productCatalogue

#fonction de confirmation de suppression d'un produit
def productConfirmDelete(refProduct):
    print("Vous allez supprimer le produit de reference {}".format(refProduct))
    userInputConfirmation=input("Confirmez-vous la suppression de ce produit ?(Entrez \"Yes\" pour confirmer, \"No\" pour annuler__")
    if userInputConfirmation=="Yes":
        return True


#fonction de retrait d'un produit du catalogue
def productRemove(refProduct,productCatalogue):
    if productVerification(refProduct,productCatalogue):
         for product in productCatalogue:
            if productConfirmDelete(refProduct):
                productCatalogue.remove(product)   

            return productCatalogue 
        
#Sprint 2

#Fonction de verification de l'existence d'un vlient
def custumerVerification(Identifiant,custumerList):
    for client in custumerList:
        if client['Id']==Identifiant :
            return True

#Fonction d'identification d'un client
def custumerIdentify(Nom,Id):
    if custumerVerification(Id,custumerList):
         print('Cet identifiant est déja associé à un utilisateur, Veuillez le changer svp')
    else:
        currentCustumer=copy.copy(custumerDictionnary)
        currentCustumer["Nom"] = Nom
        currentCustumer["Id"] = Id
        custumerList.append(currentCustumer)
        return currentCustumer
    
#Fonnction de confirmation avant achat
def productBuyingConfirmation(qtyProduct,nameProduct,priceProduct):
    print("Vous allez acheter {} exemplaires du produit {} coutant {} F l'unité".format(qtyProduct,nameProduct,priceProduct))
    userInputConfirmation=input("Confirmez-vous l'achat ? (Entrez \"Yes\" pour confirmer, \"No\" pour annuler__")
    if userInputConfirmation=="Yes":
        return True

# Fonction d'achat d'un produit avec ses points
def productBying(Nom, nameProduct, Quantité):
    for product in productCatalogue:
        if product["Nom du Produit"] == nameProduct:
            if product["Quantité"] >= Quantité:
                refProduct=product["Reference"]
                priceProduct=product["Prix"]
                if productVerification(refProduct,productCatalogue):
                    if productBuyingConfirmation(Quantité,nameProduct,priceProduct):
                        for product in productCatalogue:
                            if product["Reference"] == refProduct:
                                product["Quantité"] -= Quantité 
                                for client in custumerList:
                                    if client["Nom"] == Nom:
                                        client["Montant Total Achat"] += product["Prix"]*Quantité
                                        print("Votre achat de {} {} vous a couté {} Francs CFA".format(Quantité,nameProduct,product["Prix"]*Quantité))
                                        priceInPointConversion()
                else:
                    print("Le produit {} n'existe pas! ".format(nameProduct))
            else:
                print("Vous ne pouvez pas acheter {} {} ! Veuillez revoir votre quantité ".format(Quantité, nameProduct))

#Fonction d'affichage du catalogue
def viewCatalogue():
    numeroArticle=1
    print('         Liste des produits')
    for product in productCatalogue:
        print("{}. {} -> Prix: {} ; Quantité: {}".format(numeroArticle, product['Nom du Produit'],product['Prix'], product['Quantité'])) 
        numeroArticle+=1

#Fonction d'affichage de la liste des clients
def viewCustumerList():
    numeroClient=1
    print('           Liste des clients')
    for client in custumerList:
        print("{}. {} -> Identifiant : {} ; Montant Total Achat: {} F ; NB de points Hebdo : {}  ; NB de points Total: {} ; Gain totaux : {}".format(numeroClient, client['Nom'],client['Id'], client['Montant Total Achat'],client['Nombre de points Hebdommadaires'],client["Nombre de points Total"], client["Point convertis en argent"])) 
        numeroClient+=1

#Fonction de conversion du prix en nombre() et etre notifié si j’ai gagné des points
def priceInPointConversion():
    for price in custumerList:
        price["Nombre de points Hebdommadaires"]+=price["Montant Total Achat"]//10000
        if price["Nombre de points Hebdommadaires"] >= 1:
            print("Vous avez gagné {} Points.".format(price["Nombre de points Hebdommadaires"]))

#Fonction de conversion des points en argent
def pointInMoneyConversion(name):
    for client in custumerList:
        if client["Nom"] == name:
            montant=client["Nombre de points Hebdommadaires"]*1000
            client["Point convertis en argent"] = montant
            client["Nombre de points Hebdommadaires"] = 0
            return montant

#Afficher le catalogue des produits qu'il peut acheter avec ses points cumulés
def viewProductPointBuyingCatalogue(name):
    montantUtilisable=pointInMoneyConversion(name)
    numeroArticle=1
    print('         Liste des produits')
    for product in productCatalogue:
        if product["Prix"] <= montantUtilisable:
            print("{}. {} -> Prix: {} ; Quantité: {}".format(numeroArticle, product['Nom du Produit'],product['Prix'], product['Quantité'])) 
            numeroArticle+=1

#Fonction d'achat d'un produit en utilisant les points cumules
def productByingWithPoint(Nom, nameProduct, Quantité):
    for product in productCatalogue:
        if product["Nom du Produit"] == nameProduct:
            if product["Quantité"] >= Quantité:
                refProduct=product["Reference"]
                priceProduct=product["Prix"]
                if productVerification(refProduct,productCatalogue):
                    if productBuyingConfirmation(Quantité,nameProduct,priceProduct):
                        for product in productCatalogue:
                            if product["Reference"] == refProduct:
                                product["Quantité"] -= Quantité 
                                for client in custumerList:
                                    if client["Nom"] == Nom:
                                        pointInMoneyConversion(Nom)
                                        if client["Point convertis en argent"] >= product["Prix"]:
                                            client["Point convertis en argent"] -= product["Prix"]*Quantité
                                            print("Votre achat de {} {} vous a couté {} Francs. CFA déduis de vos points".format(Quantité,nameProduct,product["Prix"]*Quantité))
                                        else :
                                            print("Vous n'avez pas assez de points pour acheter cet article")
                else:
                    print("Le produit {} n'existe pas! ".format(nameProduct))
            else:
                print("Vous ne pouvez pas acheter {} {} ! Veuillez revoir votre quantité ".format(Quantité, nameProduct))


#Fonction pour Consulter mon solde : mes points cumulés
def viewPoints(name):
    for client in custumerList:
        if client["Nom"] == name:
            print("Nom : {} -> Nombre de points : {}".format(name, client["Nombre de points Hebdommadaires"]))

listeDesMontants = []
Sortedliste = []

#fonction pour désigner le gagnant du tirage au sort
def gagnantTirageAuSort():
    for user in custumerList:
        listeDesMontants.append(user["Montant Total Achat"])
    listeDesMontants2 = [int(val) for val in listeDesMontants]
    listeDesMontants2.sort(reverse=True)
    
    for montant in listeDesMontants2:
        for user in custumerList:
            if montant == user["Montant Total Achat"]:
                Sortedliste.append(user)
    listeSelectionnes = []
    #Ne pas oublier de changer le range à 10
    for i in range(2):

        listeSelectionnes.append(Sortedliste[i])
    vainqueur = random.choice(listeSelectionnes)
    print(vainqueur["Nom"] + " est le gagnant du tirage au sort et beneficie d'un bon d'achat d'une valeur de 10000F valide une semaine ")
    return vainqueur["Nom"]

#Fonction pour afficher l'alarme
def alarmStock():
    listeProduitInf=[]
    for product in productCatalogue:
        if product["Quantité"] < 20:
            listeProduitInf.append(product)
    if listeProduitInf != []:
      print('Le stocck de {} est inférieur à 20'.format(product["Nom"]))
      
#Fonction pour consulter mon solde : mes bons d'achat
def viewBonAchat(name):
        if gagnantTirageAuSort() == name:
            print("Felicitation {} !".format(name))
        else :
            print("Vous n'avez aucun bon d'achat")

#Fonction pour générer les Logs du système
LogFile = 'ecoShop.log' 
def addToLogFile(actionnerName,description):
    #on ouvre le fichier en mode d'ajout 
    date = datetime.datetime.now()
    logContent = ''
    logContent += date.strftime('%A')+' le '+ str(date.day) +'-'+str(date.month)+'-'+str(date.year) +' a '+str(date.hour)+':'+str(date.minute) +' '+ actionnerName +' '+description
    logFile = open(LogFile,'a')
    logFile.write(logContent +'\n')
    logFile.close()



custumerIdentify("Audrey",55545)
#custumerIdentify("Maeva",5555545)
bread=productCreation("P098766","Pain",15000,10)
#bread=productCreation("P0987645","Lait",2000,20)
#bread3=productCreation("P098754645","Bonbon",15550,20)
#productBuyingConfirmation(15,"Riz",1500)
productBying("Audrey", "Pain",5)
#priceInPointConversion()
viewCustumerList()
#viewCatalogue()
#productBying("Maeva", "Lait",10)

#pointInMoneyConversion("Audrey")
productByingWithPoint("Audrey", "Pain", 1)
#viewPoints('Audrey')
#print(custumerList)
viewCustumerList()
#print(gagnantTirageAuSort())
#viewBonAchat('Audrey')
#viewCatalogue()
#addToLogFile("Audrey","a ajoute un produit au catalogue")
#viewProductPointBuyingCatalogue("Audrey")
#print(productCatalogue)


#print(custumerList)
#print(pointInMoneyConversion("Audrey"))

#test=productModification("2")
#breadNew=productPriceModification("P098765",productCatalogue,250)
#print(breadNew)

#breadExist=productVerification("P098765",productCatalogue)