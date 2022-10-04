from flask import Flask

app = Flask(__name__)

@app.route("/")

def homepage():
	return "<H1> Olá digite /paulinho<p> Se quiser ver Mais sobre ele Ou se não<p> /cerol ou /nobru ou /Fre ou /Creditos "

@app.route("/paulinho")

def paulo():
	return "<H1> Paulinho! <p> Ele é de Minas gerais!<p> O nome de seu canal do youtube é<p> Modder dois pos Quando ele era criança ele<p> Era um modder que dava dinheiro pros outros no caso hack<p> Acredito eu o significado do dois é por que<p> Em algumas cidades Do fivem Ele é admin E<p> Tambem hacker1 e agora admin2 em algumas cidades que ele pega o admin!<p> Seu canal ficou famoso por fazer anti rp<p> E seu videos muitos engraçados e quem gosta desse tipo de conteudo<p> Fica preso Nois videos dele Sempre Querendo assistir mais um<p> Já hoje em dia tem até fivem pra o celular!<p> A sua voz de criança Que ele faz é muito engraçado tambem<p> E seus videos muito famosos por Ser um cara muito gente boa!<p> E sempre Estando Animado e Estando no personagem<p> Muito dificil voce ver ele Ficar triste em algum video dele!<p> E por conta dele ser assim muita gente gosta dele e até reconhece ele<p> No proprio Jogo em varios tipos de servidor Que ele joga<p>Uma coisa que ninguem esperava aconteceu!<p> O paulinho e o Nobru! Caso não conhece o nobru ele faz parte do fluxo<p> E o Cerol Outro cara conhecido no youtube é o dono do fluxo<p> Se quiser saber mais Sobre os dois Pesquise no youtube Nobru e O cerol depois Pra dar uma<p> Olhada lá Digite /Nobru"
	
@app.route("/Nobru")

def nobru():
	return "<H1>Nobru foi conhecido por jogar fre fri em 2018 sempre dando tiro na cabeça dos inimigos<p> E quando ele fazia isso e soltava a frase ain nobru apelão!!<p> E que ficou muito famoso Por ter uma voz sua de vovo E sua jogabilidade No jogo Que hoje em dia ele não joga muito<p> Ele fazia live lá em 2018 E Ele Girava numa roleta no jogo<p> E sempre quando Ele achava que ia vir uma Coisa legal não vinha o que ele queria :(<p> E isso fazia muitas pessoas cair na rissada!<p> Se voce quiser sobre o cerol digite /cerol E sobre o fre fri caso não conheça<p> Digite /Fre"
	

@app.route("/Cerol")	

def cerol():
	return "<H1>Cerol é o dono do fluxo Onde o Nobru participa do time dele de fre fri sendo um time muito famoso<p> E até mesmo um time que muita gente<p> Gostaria de entrar Nele pra jogar No time e <p> Representar o fluxo O seu canal do youtube é cerol <p> Se passar por lá vai ver uns videos dele e Vai gostar um cara muito<p> Gente boa E ele tambem joga gta rp Nei sei qual servidor mais ele joga<p> So que sem fazer ante rp kk<p> Seu canal do youtube Tem muitos inscritos E o do nobru e do Paulinho"

@app.route("/Fre")

def Fre():
	return "<H1>Fre fri ficou muito famosos apos 2018 Atraindo<p> Muitos jogadores Pra o fre fri Sendo um jogo muito bacana Sendo até hoje em dia<p> Sendo um jogo muito famoso e que muita gente ama<p> E joga tambem !<p> Se quiser ver Sobre eu o dono do site<p> Digite /Creditos"

@app.route("/Creditos")

def creditos():
	return "<H1>Olá eu sou o dono do site e Meu nome é pedro<p> E é so isso mesmo :) "


	



if __name__ == "__main__":
	app.run(debug= True)
