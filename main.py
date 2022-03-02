import copy
#Ajouter un produit au catalogue

productDictionnary= {

    "Reference" : "",
    "Nom du Produit" :"",
    "Prix":0.0,
    "Quantité":0

}

productCatalogue=[]

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


"""def inputUserVerification(priceProduct):
    try:
        type(priceProduct)!=float
    except:
        print("Veuillez entrer un entier valide")
    return type(priceProduct)

  

testTry=inputUserVerification("Hhaha")
print(testTry)"""

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
        






bread=productCreation("P098765","Pain",150,10)
sugar=productCreation("P098764","Sucre",750,20)
breadDel=productRemove("P098765",productCatalogue)
print(breadDel)

#test=productModification("2")
#breadNew=productPriceModification("P098765",productCatalogue,250)
#print(breadNew)
#bread2=productCreation("P098766","Pain",150,10)
#breadExist=productVerification("P098765",productCatalogue)
#print(productCatalogue)
#bread=productConfirmCreation("P098765","Pain",150,10)
#print(bread)

