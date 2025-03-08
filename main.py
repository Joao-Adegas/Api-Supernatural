from model import Personagens 
from fastapi import FastAPI,status,HTTPException,Depends
from typing import Optional,Any

api = FastAPI()

personagens = {
    "1": {
		"nome": "Sam Winchester",
		"apelido": "Sammy, Moose",
		"tipo": "Caçador (com habilidades psíquicas)",
		"caracteristicas": "Inteligente, estudioso, habilidades psíquicas, ponderado, leal",
		"img": "https://static.wikia.nocookie.net/supernatural/images/7/77/Sam_Season_15.png/revision/latest?cb=20191010173615"
	},
	"2": {
		"nome": "Dean Winchester",
		"apelido": "Dean-o, Squirrel",
		"tipo": "Caçador",
		"caracteristicas": "Habilidoso, leal, carismático, sarcástico, aprecia carros e rock 'n' roll",
		"img": "https://static.wikia.nocookie.net/supernatural/images/d/d2/Dean_S15_Promo.jpg/revision/latest?cb=20191010173549"
	},
	"3": {
		"nome": "John Winchester",
		"apelido": "Nenhum proeminente",
		"tipo": "Caçador",
		"caracteristicas": "Obsessivo, habilidoso, determinado",
		"img": "https://static.wikia.nocookie.net/supernatural/images/a/a4/Johnwinchester.jpg/revision/latest?cb=20120227184227"
	},
	"4": {
		"nome": "Mary Winchester",
		"apelido": "Nenhum proeminente",
		"tipo": "Caçadora",
		"caracteristicas": "Habilidosa, forte, protetora",
		"img": "https://static.wikia.nocookie.net/supernatural/images/d/d9/Mary_Winchester_S12.png/revision/latest?cb=20161014163539"
	},
	"5": {
		"nome": "Castiel",
		"apelido": "Cas",
		"tipo": "Arcanjo",
		"caracteristicas": "Poderoso, inicialmente ingênuo, leal, questiona a autoridade celestial",
		"img": "https://static.wikia.nocookie.net/supernatural/images/c/c2/Castiel_S15.png/revision/latest?cb=20191010173646"
	},
	"6": {
		"nome": "Bobby Singer",
		"apelido": "Nenhum proeminente",
		"tipo": "Caçador",
		"caracteristicas": "Experiente, mentor, figura paterna, ranzinza, leal",
		"img": "https://static.wikia.nocookie.net/supernatural/images/d/d4/BobbySinger.jpg/revision/latest?cb=20101115201115"
	},
	"7": {
		"nome": "Charlie Bradbury",
		"apelido": "Nenhum proeminente",
		"tipo": "Humana",
		"caracteristicas": "Hacker genial, amiga leal, inteligente, excêntrica",
		"img": "https://static.wikia.nocookie.net/supernatural/images/5/52/Charlie_Bradbury.jpg/revision/latest?cb=20130207194452"
	},
	"8": {
		"nome": "Jody Mills",
		"apelido": "Nenhum proeminente",
		"tipo": "Humana/Caçadora",
		"caracteristicas": "Forte, justa, protetora, habilidosa",
		"img": "https://static.wikia.nocookie.net/supernatural/images/0/07/JodyMills.jpg/revision/latest?cb=20121127025816"
	},
	"9": {
		"nome": "Crowley",
		"apelido": "Rei do Inferno",
		"tipo": "Demônio",
		"caracteristicas": "Astuto, manipulador, complexo, sarcástico, ambicioso",
		"img": "https://static.wikia.nocookie.net/infinitas-guerras/images/b/b1/B22f0c63c3d7d90735f457cca912322d--supernatural-season--supernatural-pictures.jpg/revision/latest?cb=20170715133129&path-prefix=pt-br"
	},
	"10": {
		"nome": "Lúcifer",
		"apelido": "Nenhum proeminente",
		"tipo": "Arcanjo/Demônio",
		"caracteristicas": "Poderoso, carismático, rebelde, vingativo, caótico",
		"img": "https://static.wikia.nocookie.net/supernatural/images/d/d3/Lucifer_S13.png/revision/latest?cb=20171013210452"
	},
	"11": {
		"nome": "Azazel",
		"apelido": "Demônio dos olhos amarelos",
		"tipo": "Demônio",
		"caracteristicas": "Poderoso, cruel, manipulador",
		"img": "https://static.wikia.nocookie.net/supernatural/images/d/d5/Azazel.jpg/revision/latest?cb=20110419205542"
	},
	"12": {
		"nome": "Lilith",
		"apelido": "Nenhum proeminente",
		"tipo": "Demônio",
		"caracteristicas": "Poderosa, cruel, leal a Lúcifer, manipuladora",
		"img": "https://static.wikia.nocookie.net/supernatural/images/7/7b/Lilith.jpg/revision/latest?cb=20120227183616"
	},
	"13": {
		"nome": "Metatron",
		"apelido": "Nenhum proeminente",
		"tipo": "Arcanjo",
		"caracteristicas": "Manipulador, trapaceiro, ambicioso",
		"img": "https://static.wikia.nocookie.net/supernatural/images/5/52/Metatron_S9.png/revision/latest?cb=20131018233519"
	},
	"14": {
		"nome": "Amara/A Escuridão",
		"apelido": "A Escuridão",
		"tipo": "Força primordial",
		"caracteristicas": "Poderosa, caótica, vingativa",
		"img": "https://static.wikia.nocookie.net/supernatural/images/5/5a/Amara_S11.png/revision/latest?cb=20151105001150"
	},
	"15": {
		"nome": "Deus/Chuck Shurley",
		"apelido": "Chuck",
		"tipo": "Deus",
		"caracteristicas": "Poderoso, manipulador, ausente, egoísta",
		"img": "https://static.wikia.nocookie.net/supernatural/images/d/de/God_S15.png/revision/latest?cb=20191010173715"
	},
	"16": {
		"nome": "Jack Kline",
		"apelido": "Nenhum proeminente",
		"tipo": "Nephilim",
		"caracteristicas": "Poderoso, ingênuo, curioso, conflito interno, apegado aos Winchesters",
		"img": "https://static.wikia.nocookie.net/supernatural/images/0/07/Jack_Kline_S15.png/revision/latest?cb=20191010173747"
	},
	"17": {
		"nome": "Meg Masters",
		"apelido": "Nenhum proeminente",
		"tipo": "Demônio",
		"caracteristicas": "Manipuladora, leal, sarcástica",
		"img": "https://static.wikia.nocookie.net/supernatural/images/e/e0/Meg_Masters_S5.jpg/revision/latest?cb=20120227183711"
	},
	"18": {
		"nome": "Kevin Tran",
		"apelido": "Nenhum proeminente",
		"tipo": "Profeta",
		"caracteristicas": "Inteligente, leal, corajoso, ajuda os Winchesters a decifrar a tábua de Deus",
		"img": "https://static.wikia.nocookie.net/supernatural/images/d/d4/Kevin_Tran.jpg/revision/latest?cb=20121004222045"
	},
	"19": {
		"nome": "Jo Harvelle",
		"apelido": "Nenhum proeminente",
		"tipo": "Caçadora",
		"caracteristicas": "Corajosa, leal, habilidosa, amiga dos Winchesters, proprietária do Roadhouse",
		"img": "https://static.wikia.nocookie.net/supernatural/images/e/e9/JoHarvelle.jpg/revision/latest?cb=20101115201235"
	},
	"20": {
		"nome": "Ellen Harvelle",
		"apelido": "Nenhum proeminente",
		"tipo": "Caçadora",
		"caracteristicas": "Forte, experiente, protetora, amiga dos Winchesters, proprietária do Roadhouse",
		"img": "https://static.wikia.nocookie.net/supernatural/images/2/22/EllenHarvelle.jpg/revision/latest?cb=20101115201217"
	},
	"21": {
		"nome": "Gabriel",
		"apelido": "O Trapaceiro",
		"tipo": "Arcanjo",
		"caracteristicas": "Poderoso, brincalhão, sarcástico, leal, momentos de humor e reviravoltas importantes",
		"img": "https://static.wikia.nocookie.net/supernatural/images/5/53/Gabriel_S5.png/revision/latest?cb=20120227183818"
	},
	"22": {
		"nome": "Bela Talbot",
		"apelido": "Nenhum proeminente",
		"tipo": "Humana",
		"caracteristicas": "Ladrã habilidosa, misteriosa, manipuladora, participação importante na terceira temporada",
		"img": "https://static.wikia.nocookie.net/supernatural/images/5/54/Bela_Talbot.jpg/revision/latest?cb=20120227183748"
	},
	"23": {
		"nome": "Rufus Turner",
		"apelido": "Nenhum proeminente",
		"tipo": "Caçador",
		"caracteristicas": "Experiente, amigo de Bobby Singer, participação em alguns episódios, grande amizade com Bobby",
		"img": "https://static.wikia.nocookie.net/supernatural/images/5/5e/RufusTurner.jpg/revision/latest?cb=20120227184132"
	},
	"24": {
		"nome": "Michael",
		"apelido": "Nenhum proeminente",
		"tipo": "Arcanjo",
		"caracteristicas": "Poderoso, antagonista, irmão mais velho de Lúcifer, principal antagonista em algumas temporadas",
		"img": "https://static.wikia.nocookie.net/supernatural/images/b/b2/Michael_S5.png/revision/latest?cb=20120227183852"
	}
}

@api.get("/personagens")
async def personagen():
    return personagens

@api.get("/personagens/{id}")
async def read_personagens_by_Id(id:int):
    vilao = Personagens[id]
    if(id in Personagens):
        return vilao
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"O vilao com id:{id} nao existe")
        
@api.post("/personagens",status_code=status.HTTP_201_CREATED)
async def create_Personagens(personagen:Optional[Personagens] = None):
    add_id = len(personagens)+ 1
    personagens[add_id] = personagen
    del personagen.id
    return personagen

@api.put("/personagens/{id}")
async def edit_personagem(id:int,personagem:Personagens):
    if(id in personagens):
        personagens[id] = personagem
        personagem.id = id
        del id
        return personagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Não existe personagem com id:{id}")

@api.delete("/personagens/{id}")
async def delete_personagem(id:int):
    if(id in personagens):
        del personagens[id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Nao foi possivel deletar, pois nao existe personagem com o id{id}")

    
if(__name__  == "__main__"):
    import uvicorn
    uvicorn.run("main:api",host="127.0.0.1",port=8000,log_level="info",reload=True)
# @app.put("/viloes{id}")
# async def edit_viloes(id):

