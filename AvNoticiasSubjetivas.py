import nltk

dicionariotreino =[
('grande', 'parcial'),
('eminente', 'parcial'),
('lendário', 'parcial'),
('visionário', 'parcial'),
('notável', 'parcial'),
('célebre', 'parcial'),
('extraordinário', 'parcial'),
('brilhante', 'parcial'),
('famoso', 'parcial'),
('pequeno', 'parcial'),
('renomado', 'parcial'),
('prestigioso', 'parcial'),
('de nível mundial', 'parcial'),
('respeitado', 'parcial'),
('excepcional', 'parcial'),
('excelente', 'parcial'),
('virtuoso', 'parcial'),
('fácil', 'parcial'),
('difícil', 'parcial'),
('complicado', 'parcial'),
('raramente', 'parcial'),
('falso', 'parcial'),
('eu', 'parcial'),
('nós', 'parcial'),
('acho', 'parcial'),
('acredito', 'parcial'),
('bom', 'parcial'),
('ruim', 'parcial'),
('mal', 'parcial'),
('diferente', 'parcial'),
('verdadeiro', 'parcial'),
('culto', 'parcial'),
('racista', 'parcial'),
('perverso', 'parcial'),
('horrível', 'parcial'),
('seita', 'parcial'),
('fundamentalista', 'parcial'),
('extremista', 'parcial'),
('negacionista', 'parcial'),
('terrorista', 'parcial'),
('libertador', 'parcial'),
('pseudo', 'parcial'),
('controverso', 'parcial'),
('suposto', 'parcial'),
('alegado', 'parcial'),
('pretenso', 'parcial'),
('acusado', 'parcial'),
('não é', 'parcial'),
('novidade', 'parcial'),
('chamado', 'parcial'),
('notavelmente', 'parcial'),
('interessantemente', 'parcial'),
('claramente', 'parcial'),
('certamente', 'parcial'),
('sem dúvida', 'parcial'),
('é claro', 'parcial'),
('acerta', 'parcial'),
('legítima', 'parcial'),
('louvável', 'parcial'),
('sempre', 'parcial'),
('afortunadamente', 'parcial'),
('felizmente', 'parcial'),
('infelizmente', 'parcial'),
('tragicamente', 'parcial'),
('precocemente', 'parcial'),
('bastante', 'parcial'),
('mais', 'parcial'),
('menos', 'parcial'),
('subiu', 'parcial'),
('devastador', 'parcial'),
('grande', 'parcial'),
('impossível', 'parcial'),
('fundamental', 'parcial'),
('imprescindível', 'parcial'),
('suficiente', 'parcial'),
('possível', 'parcial'),
('mas', 'imparcial'),
('contudo', 'imparcial'),
('porém', 'imparcial'),
('entretanto', 'imparcial'),
('no entanto', 'imparcial'),
('ou', 'imparcial'),
('ora', 'imparcial'),
('alguns dizem', 'imparcial'),
('acredita-se', 'imparcial'),
('muitos têm a opinião', 'imparcial'),
('a maioria sente', 'imparcial'),
('especialistas afirmam', 'imparcial'),
('frequentemente se relata', 'imparcial'),
('é a opinião corrente', 'imparcial'),
('estudos mostram', 'imparcial'),
('a ciência diz', 'imparcial'),
('provou-se que', 'imparcial'),
('revelou', 'imparcial'),
('indicou', 'imparcial'),
('expôs', 'imparcial'),
('explicou', 'imparcial'),
('encontrou', 'imparcial'),
('notou', 'imparcial'),
('observou', 'imparcial'),
('insistiu', 'imparcial'),
('especulou', 'imparcial'),
('conjeturou', 'imparcial'),
('alegou', 'imparcial'),
('afirmou', 'imparcial'),
('admitiu', 'imparcial'),
('confessou', 'imparcial'),
('negou', 'imparcial'),
('disse', 'imparcial'),
('escreveu', 'imparcial'),
('de acordo com', 'imparcial'),
('como diz', 'imparcial'),
(' " " ', 'imparcial'),
('Um turista de Minas Gerais, de 38 anos, ficou com manchas no corpo após tomar um banho de mar na manhã do último sábado, na Praia de Corurupe, em Ilhéus, no sul da Bahia. \
A Vigilância em Saúde Ambiental do município investiga se há relação do problema com as manchas de óleo que atingem o litoral do Nordeste.', 'imparcial')
]

dicionarioteste =[
('Não nos parece que seja assim, nessa extensão, mas a virulência do presidente contra os veículos que ele enxerga como inimigos – notadamente a Rede Globo e a Folha de S.Paulo – é objetivamente, e independentemente da intenção, um gravíssimo ataque a um dos pilares centrais da democracia','parcial'),
('Aliás, nenhum cidadão de bem, ainda que nutra desapreço por uma ou outra emissora e grande apreço por um ou outro governante, pode alegrar-se com o que aconteceu','parcial'),
('Foi essa postura que ajudou a mostrar ao povo o grande mal que o PT havia feito ao país, alimentando uma reação que contribuiu para a eleição de Bolsonaro','parcial'),
('É impossível, aqui, não fazer um paralelo com José Afonso Pinheiro, o ex-zelador do Condomínio Solaris, no Guarujá','parcial'),
('Até o momento da primeira reportagem dava-se como fidedigna a informação dada pelo porteiro do condomínio de Bolsonaro em depoimento à polícia','parcial'),
('Não se pode falar em uma conspiração jornalística que fez uso de informações desatualizadas para atacar um presidente da República','parcial'),
('Cheguei a pensar que ele pudesse estar exagerando na quantidade, o que tende a sacrificar a qualidade','parcial'),
('Mas sua mais recente obra, Como aprendi a pensar, é um excelente resumo dos filósofos que ajudaram a formar seu pensamento e, de tabela, uma breve história da filosofia em si','parcial'),
('Não é fácil ter consciência da própria finitude, de nossas fraquezas, da falta de sentido','parcial'),
('É preciso repudiar tal atitude do presidente da forma mais veemente possível e denunciá-la como a de um homem que, hoje não se tem mais ilusões, não comunga dos valores democráticos mais básicos', 'parcial'),
('Nós praticamos muito mais autoengano que os clássicos, pois não suportamos a luz da verdade','parcial'),
('Todos somos pecadores, e eis onde entra o conceito de misericórdia, de graça divina','parcial'),
('Pela primeira vez, desde as eleições, parece haver uma ideia mais clara de como funcionam as engrenagens da política e do que ele pretende e pode fazer com as engrenagens da economia','parcial'),
('Pois eu acredito no mérito, não acredito na meritocracia – se compreendida como palavra-de-ordem ou abracadabra de todos os problemas econômicos e sociais', 'parcial'),
('O historiador e defensor público federal Yuri Costa, destaca o que representou o AI-5', 'imparcial'),
('Assim, ele se projetou, do ponto de vista formal, de maneira uniforme sobre todo o brasil. Então o Maranhão é diretamente atingido pelo Ato, por tudo aquilo que ele previu em termos de dissoluções de instituições, de suspensão de liberdades, de direitos individuais e coletivos', 'imparcial'),
('Tudo isso se projetou de maneira uniforme sobre o Brasil, não só do ponto de vista da norma formal, mas também concretamente em termos de atos', 'imparcial'),
('Mas há um problema nessa implementação do WhatsApp: você é obrigado a usar a impressão digital, e não há uma alternativa para desbloquear o aplicativo', 'imparcial'),
('Ou seja, caso seu leitor de digitais pare de funcionar, o WhatsApp não poderá ser desbloqueado', 'imparcial'),
('O Planejamento Regional Integral evidencia o conjunto de diretrizes, objetivos, metas, ações e serviços para a garantia do acesso e da resolubilidade da atenção por meio da organização da Rede de Atenção à Saúde', 'imparcial'),
('O assessor especial da SES e coordenador do PRI para o Maranhão, Allan Rodrigues Patrício, ressalta a organização das redes de atenção à saúde e os mecanismos de governança regional', 'imparcial'),
('Esse processo abrange ações de assistência à saúde, como atenção primária, urgência e emergência, atenção psicossocial e atenção ambulatorial especializada e hospitalar', 'imparcial'),
('O secretário municipal de saúde e membro integrante da CIR de Cajari, Diego Jardim Ferreira, observou que', 'imparcial'),
('De acordo com a empresa, com a autorização fica liberada a capacidade de cerca 8 de toneladas de ferro por ano', 'imparcial'),
('A Vale confirmou, no entanto, seu guidance', 'imparcial'),
('A Operação Verde Brasil, que teve por finalidade o combate a incêndios florestais e crimes ambientais na região da Amazônia Legal, concluiu seus trabalhos', 'imparcial'),
('A Polícia Federal disse ter prendido', 'imparcial'),
('A PF prendeu membros de um grupo supostamente envolvido em um grande esquema de contrabando de pessoas', 'imparcial')
]

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')

def stemmizar(texto):
    stemmer = nltk.stem.RSLPStemmer()
    textostemming = []
    for (termos, classe) in texto:
        comstemm = [str(stemmer.stem(p)) for p in termos.split() if p not in stopwordsnltk]
        textostemming.append((comstemm, classe))
    return textostemming

textocomstemmingtreino = stemmizar(dicionariotreino)
textocomstemmingteste = stemmizar(dicionarioteste)

def procuratermos(texto):
    todostermos = []
    for (termos, classe) in texto:
        todostermos.extend(termos)
    return todostermos

termostreino = procuratermos(textocomstemmingtreino)
termosteste = procuratermos(textocomstemmingteste)

def encontrafrequencia(termos):
    termos = nltk.FreqDist(termos)
    return termos

frequenciatreino = encontrafrequencia(termostreino)
frequenciatestada = encontrafrequencia(termosteste)

def procuratermosunicos(repeticao):
    freq = repeticao.keys()
    return freq

termosunicostreino = procuratermosunicos(frequenciatreino)
termosunicosteste = procuratermosunicos(frequenciatestada)

def extracaotermos(textos):
    text = set(textos)
    atributos = {}
    for termos in termosunicostreino:
        atributos['%s'% termos] = (termos in text)
    return atributos

dicionariofinaltreino = nltk.classify.apply_features(extracaotermos, textocomstemmingtreino)
dicionariofinalteste = nltk.classify.apply_features(extracaotermos, textocomstemmingteste)

classificador = nltk.NaiveBayesClassifier.train(dicionariofinaltreino)
print(classificador.labels())

print(nltk.classify.accuracy(classificador, dicionariofinalteste))


errosMatriz = []
for (termos, classe) in dicionariofinalteste:
    result = classificador.classify(termos)
    if result != classe:
       errosMatriz.append((classe, result, termos))

from nltk.metrics import ConfusionMatrix
espera = []
real = []
for (texto, classe) in dicionariofinalteste:
    result = classificador.classify(texto)
    real.append(result)
    espera.append(classe)

matrizConfusao = ConfusionMatrix(espera, real)
print(matrizConfusao)


noticia = 'Em uma derrota para o governo do presidente Jair Bolsonaro, a Câmara aprovou na noite desta terça-feira, 5, uma versão desidratada do projeto de lei do Executivo que tratava sobre a posse e o porte de armas. Depois de uma série de tentativas de se aprovar a matéria em plenário, parlamentares fecharam um acordo para votar apenas partes do projeto que tratam de regras para colecionadores, atiradores e caçadores (CACs), além de mudar penas de crimes com armas e outros temas. O projeto foi aprovado com 283 votos a favor e 140 contra, além de duas abstenções.\
Em maio, Bolsonaro editou um decreto que facilitou o porte de arma e o acesso a munições para os CACs. Mas, no fim de junho, o presidente revogou o texto e outros dois, também sobre armas, e enviou ao Congresso esse projeto que originalmente tratava também sobre o registro, posse e comercialização de armas de fogo e munição e também sobre o Sistema Nacional de Armas (Sinarm). Além de retirar algumas medidas previstas no texto do governo, os deputados também incluíram aumento de algumas penas previstas, como a para quem for flagrado em posse ou portando, de maneira irregular, uma arma.\
Foi aprovada ainda uma emenda do deputado Arthur Lira (PP-AL) que especifica que o atirador esportivo, maior de 25 anos, terá direito ao porte de armas somente depois de cinco anos da primeira emissão do certificado de registro, em vez de dois anos depois, como constava da redação proposta pelo relator, deputado Alexandre Leite (DEM-SP). Foram retiradas do texto qualquer possibilidade de estender porte e posse a outras categorias, como queria o governo. Agora, o Executivo deve enviar um novo texto à Câmara amanhã para tratar da ampliação das categorias que têm direito a porte de arma para o exercício de sua profissão e outros assuntos. No fim de agosto, a Câmara aprovou a flexibiização da posse estendida de armas de fogo em propriedades rurais, a primeira legislação pró-arma aprovada no Congresso desde o início do governo Bolsonaro.'
noticiastemming = []
stemmer = nltk.stem.RSLPStemmer()
for (termostreino) in noticia.split():
    temstem = [p for p in termostreino.split()]
    noticiastemming.append(str(stemmer.stem(temstem[0])))

noticiaclass = extracaotermos(noticiastemming)
distribuir = classificador.prob_classify(noticiaclass)

print("RESULTADO:")
print(classificador.classify(noticiaclass))
