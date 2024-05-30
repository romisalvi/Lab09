import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.dao=DAO()
        self.g=nx.Graph()
        self.voli=self.dao.getAllFlights()
        self.aeroporti=self.dao.getAllAirports()


    def creaGrafo(self, distMin):
        dist_min=distMin
        self.g.add_nodes_from(self.aeroporti)
        dizionarioDist={}
        dizionarioNum={}
        dizAer = {}
        for aer in self.aeroporti:
            dizAer[aer.id] = aer
        for volo in self.voli:
            lista=[]
            lista.append(volo.origin_airport_id)
            lista.append(volo.destination_airport_id)
            l2=sorted(lista)
            stringa=str(l2[0])+" "+str(l2[1])
            if stringa not in dizionarioDist:
                dizionarioDist[stringa]=volo.distance
                dizionarioNum[stringa]=1
            else:
                dizionarioDist[stringa]+=volo.distance
                dizionarioNum[stringa]+=1
        for element in dizionarioDist:
            media=float(dizionarioDist[element])/float(dizionarioNum[element])
            if media>dist_min:
                codici=element.split(" ")
                air1=dizAer[int(codici[0])]
                air2=dizAer[int(codici[1])]
                self.g.add_edge(air1,air2, weight=media)
        print("OK")

    def getNNodes(self):
        return len(self.g.nodes)
    def getNEdges(self):
        return len(self.g.edges)
    def clearG(self):
        self.g.clear()
    def allEdges(self):
        return self.g.edges(data="weight")