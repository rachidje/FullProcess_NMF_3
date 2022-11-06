

def getInputs():
    mots_erreur = [["lycer","élyser","journer","elyser","elyséé","elysee","annee","anner","ider","tropher","champs-elyséé","champs-elyser","soirer","mosquer","valler","marer","orchider","alizer"],
    ["liberter","handicaper","faculter","universiter","retraiter","salarier","employer","députer","créer","spécialiser","téléviser","solidariter","inapproprier","infonder","erroner","prématurer","aiser","mobiliter","inadapter","insenser","fermeter","ferrer","éhonter","aîner","côter","effréner","écœurer","sous-titrer","impayer","inopiner","lâcheter","simultaner","spontaner","injustifier","ainer","intégriter","ather","contrarier","ager","incontrôler","fortuner","malintentionner","sous-évaluer","délibérer","dubliner","sous-dimensionner","sus-citer","inchanger","sous-financer","sous-représenter","instantaner","non-autoriser","non-désirer","dédubliner","sous-signer","gallinacer","hupper","sous-doter","inoccuper","graminer","fatiguer","inappliquer","inexploiter","raciser","inavouer","esseuler"],
    ["épreuves","opérateurs","éoliennes","crèches",'handicapés','lycées','blancs',"parcs","relais","antenne-relais","verts","chasseurs","docteure","morale","citoyens","moyenner","crécher","élyséer","elyséer","moyenner","victimer","materneller","bêter","handicape","future","professeure","amie","humaine","écrivaine","avocate","sociale","incendier","sommer","libres","permanente","permanente","majeure","principale","lister","amender","commerciale","noire","lourde","valls","présidente","business","élèves","incendier","quartiers","router","ligner",'nationale',"unir","journéer","insuffisante","âgée","champs-elyséer","disparaitrer","amianter","bruyante","coute","coûte","coûté","aisée","inhumaine","ondes","légitimer","téléspectateurs","légale","payante","vaccins","télécommunications","dirigeante","polyhandicapé","écœurés","fers","ferrés","impuissante","financiere","dégénératives","trainéer","lycéens","inappropriés","étudiants","inopinée","trophéer","légender","idéer","spontanée","flagrante","directeurs","émergente","éhontée","œuvres","acheteurs","dégénérativer","défaillante","instituteurs","mers","champs-elysées","lecteurs","terrifiante","entraineurs","entraînera","trains","train(","paysager","paysans","intégrale","écœurée","écœurante","athée","athènes","qualifications","qualifiera","qualificatifs","représentante","pesticides","annéer","formateurs","soiréer","opératoirer","mosquéer","incontrôlée","fortunes","vallées","délibérée","maréer","dublinée","sous-dimensionnés","sous-dimensionnée","rivierer","sus-citée","inchangée","édifiante","injustifiee","injustifiée","sous-financée","considèrera","sous-traitante","représentativer","codéiner","non-autorisée","menaçante","reconnaîtrer","récupérabler","soussignée","aides-soignants","goutter","huppés","sous-dotée","inoccupée","sens-uniquer","génocider","graminée","croissante","itinérante","itinérants","itinérantn","itinéraires","fatiguée","inexploitée","reconnaitrer","reconnaitrez","valléer","gammer","affligeante","podcasts","cris","bretons","addicte","addicts","antenner","antennes"],
    ["éolienne","chienne","chatte","présidentielle","étudiant.e","insuffisanter","infondéer","erronéer","couter","coûter","agéer","terrifianter","inadaptéer","dirigeanter","polyhandicaper","polyhandicapés","écœuréer","enleverer","paysanne","lycéenne","étudianter","étudiant·e","étudiant-e","étudiantes","inopinéer","prématuréer","lacherer","simultanéer","spontanéer","flagranter","flagrant.c","éhontéer","défaillanter","exaspéranter","elysée55","inexistanter","impuissanter","aînéer","entrainerer","criminelle","train(s","trainerer","payanter","acheterer","acheterai","acheteron","écœuranter","abimerer","athéer","qualifier.a","effrénéer","incessanter","couterer","impayéer","injustifiees","aiséer","opérationnelle","génèrerer","incontrôléer","incontrôlées","sous-évaluéer","sous-dimensionnéer","inchangéer","injustifiéer","édifianter","sous-financéer","protègerer","protègerai","considère-t","instantanéer","espèrerer","panzerer","dédublinéer","bienfaisanter","bienfaisantes","sous-signéer","toléreron","accèderer","accélèrerer","aides-soignantes","aides-soignanter","gallinacéer","huppéer","graminéer","décéderer","gouterer","croissanter","insenséer","dérangeanter","règlementer","règlerer","intègrerer","fatiguanter","sus-citéer","inappliquéer","étudier.l","raciséer","malintentionnéer","sous-traitanter","affligeanter","sous-représentéer","amiantéer","podcaster","codéinéer","recupererer","bretonne","cèderer","frequenterer","exercerai","exerceron","inintéressanter","empecherer","legaliserer","defigurerer","décèderer","non-autoriséer","réfrigéranter","sous-titréer","addicter"],
    ["maîtresse","coûtent","coûtant","coûtera","dirigeant.e.","étudiant.e.","étudiant·e·","étudiant-e-","étudiant•e•","étudiant.es","étudiant·er","étudiant-er","étudiant⋅er","polyhandicapéer","léger.il","acheter.je","acheter.et","acheter.le","aîné·e·","lycée(*2","opérationnelles","opérationneller","génèreront","décèderont","étudieront","bretonner","exerceront","entraîneront"],
    ["maternel"],
    ["développemer","mouvemer","accompagnemer","financièremer","établissemer","logemer","gratuitemer","fonctionnemer","engagemer","libremer","abusivemer","enlèvemer","remplacemer","équipemer","aménagemer","détrimer","renforcemer","renouvellemer","rayonnemer","remboursemer","déconfinemer","prélèvemer","automatiquemer","déroulemer","temporairemer","dangereusemer","rapatriemer","départemer","enregistremer","brutalemer","déplacemer","rassemblemer","démantèlemer","manquemer","changemer","rétablissemer","endettemer","aisémer","objectivemer","entrainemer","téléchargemer","enlevemer","inopinémer","prématurémer","idéologiquemer","idéalemer","simultanémer","spontanémer","considérablemer","intégralemer","incessamer","dérangemer","délibérémer","agrandissemer","débordemer","règlemer","précèdemmer","entraînemer"],
    ["indépender","élépher","insuffiser","bruyer","inexister","impuisser","défailler","incesser","flagrer","bienfaiser","aides-soigner","croisser","itinérer"],
    ["grèv","fermetur","marseill","toulous","faun","pôl","touch","écrir","journalist","pist","musiqu","grenobl","problèm","interdir","land","enceint","cinéast","marn","contraint","méthod","planèt","territoir","cibl","construir","calvair","parol","martiniqu","laboratoir","cirqu","voil","secrétair","centr","ensembl","carbon","républiqu","journé","bibliothèqu","excus","mond","peintr","censur","amiant","lycé","trophé","idé","crim","disparaîtr","pest","aisn","ais","mosqué","mosque","fortun","valle","maré","lettoni","rivièr","rivier","considerabl","génocid","règlementair","fatigu","racist","racist","gamm","regl","cèdr","antenn"],
    ["déclaré","arrivé","classé","composé","fermé","engagé","chargé","autorisé","installé","levé","abandonné","appliqué","indiqué","proposé","réclame","cherche","applique","traite","joue","participe","indique","arrêté","maltraité","dirigé","écoute","ecoute","brûle","brûlé","brulé","arrete","contacte","embrasse","explique","entraine","moque","entraîne","sensé","sense","traîne","suscite","considéré","dirige","enleve","enlevé","dégénéré","étudié","laché","lâché","suscité","abimé","abime","abîme","abîmé","émerge","plie","œuvré","acheté","achete","bénéficie","intégré","crie","mange","mangé","sous-estimé","sous-estime","traîné","traine","trainé","crit","payé","paye","considere","integré","qualifié","qualifie","represente","representa","représenté","opere","opéré","génère","dérange","dérangé","floute","grandisse","protège","considère","irraisonné","incarne","incarné","réfrigéré","légalise","légalisé","legalisé","legalise","représenté","espère","débordé","décède","décédé","décéda","contrôlé","recupere","récupéré","réprésente","accède","accélère","supprime","supprimé","goute","goûte","goûté","décrète","décédé","décéda","délibéré","intègre","récupère","change","suffise","précède","étudie","espere","considère","afflige","controlé","critique","reconnaisse","résiste","déborde","exerce","exercé","entraîna","empeche","defigure","libera","libere","éléve","élévé","subsidié","edifié"
    ,"créé","concerne","existe","obligé"],
    ["demandon","sauvon","mobilison","signon","rappelon","refuson","appelon","allon","oublion","arrêton","laisson","accepton","réclamon","donnon","montron","préservon","penson","reston","aidon","stoppon","réjouisson","résiston","reconnaisson","gardon","espéron","cesson","parlon","boycotton","continuon","qualifion","trouvon","supprimon","oson","payon","essayon","étudion","crion","aimon","lâchon","créon","imaginon","empechon","représenton","noton","œuvron","passon","toléron","recuperon","récupéron","contrôlon","représenton","légalison","inviton","remercion","souhaiton","libéron","hésitez","laissez","sauvez","pensez","imaginez","enlevez","résistez","trouvez","œuvrez","arrêtez","mobilisez","cliquez","votez","souhaitez","montrez","cessez","proposez","supprimez","allez","protégez","restez","osez","cherchez","libérez","liberez","criez","sous-estimez","retrouvez","empechez","participez","engagez","mangez","ecoutez","écoutez","arretez","contactez","légalisez","goûtez","bénéficiez","achetez","expliquez","étudiez","retirez","payez","pliez","trainez","brulér","arrivée","portée","lancée","menée","imposée","classée","levée","chargée","payée","fermée","considérée","considérés","considéron","acheton","bénéficion","exaspérés","exaspérez","changez","exercez","considérez","dirigés","dirigez","reconnaissez","lâchez","qualifiez","abimés","pliée","intégrée","brulée","sous-estimée","sous-estimez","sous-estimon","traînée","trainée","entrainée","criée","payen","payan","payee","consideran","qualifiée","qualifiés","representan","dérangés","légalisée","débordés","décédée","toleree","décarbonnée","controlée","débordée","exercés","liberés"],
    ["utilisent","existent","mobilisent","laissent","imposent","méritent","augmentent","participent","aiment","circulent","profitent","œuvrent","sous-estiment","appellent","accordent","crient","hésitent","élèvent","demeurent","provoquent","étudient","proposent","dénoncent","posent","osent","assurent","contrôlent","ajoutent","demandent","dérangent","touchent","refusent","suscitent","suscitant","suscitait","expriment","préfèrent","démontrent","portent","accèdent","attestent","appliquent","qualifient","traînent","écoutent","brulent","protègent","lâchent","entrainent","entraînent","exercent","ferment","débordent","précèdent","suffisent","embrassent","considèrent","expliquent","espèrent","abiment","accélèrent","suppriment","reconnaissent","mangent","abîment","dirigent","génèrent","payent","intègrent","réjouissent","récupèrent","changent","affligent","œuvrons","exigeon","mangeon","protégeon","changeon","partageon","mangion","dirigeer","censéer","senséer","payons","fermons","considérées","émergéer","œuvrant","bénéficiait","bénéficiant","bénéficions","bénéficient","achetion","bénéficiéer","terrifiait","traînant","réjouissant","dégénéréer","dégénérant","entrainant","entrainéer","exaspérant","criant","payant","intégrant","intégré-e","intégrait","qualifiant","qualifiait","qualifiées","pesant","dérangeer","dérangé·e","anonymiséer","grandissant","grandissent","protègeon","légalisant","côtière","toleréer","supprimées","dispachéer","délibérant","délibéréer","changeer","protègeer","affligeer","terrifiant","controléer","recuperant","cèdent","élévéer","susréféréer","sous-estiméer"]]

    mots_accent = [['college','mere','pere','acces',"riviere","regle"],
    ['hopital','hotel'],
    ['foret',"arreter"],
    ['egalite','medical','elephant','etudiant','elu','education','television','decision','etat','solidarite','etats-unis',"gerard","etats","region","creation","edition","regulation","declaration","reunion","legal","inopine","aîne","injustifie","operation","dubline"],
    ['maitre','maitresse',"ile-de-france","ile","chaine","entrainement","disparaitre","entrainer","entraineur","entrainement","trainer","ainé","abimer"],
    ["cout","couteux","bruler","gouter","gout"],
    ['republique','egalité','election','etranger','proteger','economie','medecin','etude','electoral','equipe','ecologie','etablissement','developpement','ecole','edouard',"president","elève","periode","invite","epargne","veran","stephane","reclamer","defendre","present","resident","elysée","champs-elysée","ecouter","trophee","considerer","integrer","operer","mosquee","vallee","instantanement","legaliser","deborder","debordement","considerable","tolerer","tolerance","operer","present","presentation","presenter","recuperer","regler","reglementer","resister","frequenter","legaliser","defigurer","liberer","alizee","edifier"],
    ['liberte']]

    list_bigrams = ["covid 19","président république","mise place","parent élève","service public","mettre place","donner lieu","droit homme","crise sanitaire","faire face","réseau social","éducation national","mis place","pouvoir public","mettre fin","assemblée national","école maternelle","conseil municipal","animal sauvage","faire partie","condition travail","sécurité social","gilet jaune","transport commun","qualité vie","union européen","faire appel","protection animal","compte tenu","port masque","bon sens","point vue","liberté expression","espace vert","fin année","intérêt général","nuisance sonore","année scolaire","établissement scolaire","conseil départemental","mettre œuvre","conseil général","espace public","mettre danger","animal compagnie","code pénal","centre ville","développement durable","parti politique","parti socialiste","parti communiste","mise œuvre","enseignement supérieur","cadre vie","élection présidentielle","bien-être animal","réchauffement climatique","site internet","chat errant","chien errant","école primaire","conseil administration","logement social","rentrée scolaire","élection municipal","droit humain","service social","animal domestique","fonction public","vivre ensemble","geste barrière","faune flore","antenne relai","nation unir","nation unie","état urgence","droit enfant","mettre péril","ministre intérieur","ministère intérieur","lieu public","vie priver","secteur priver","directeur général","metteur scène","piste cyclable","nicolas sarkozy","grand surface","eau potable","contrôler continu","côte ivoire","pays européen","conseil régional","élu local","conseiller municipal","chiffre affaire","droit femme","droit animal","changement climatique","procureur république","maison retraite","françois hollande","centre hospitalier","titre séjour","crise économique","distanciation social","opinion public","second tour","homme politique","assurance maladie","assistant maternelle","pôle emploi","chômage partiel","poids lourd","famille accueil","espèce protéger","espèce menacer","assemblée générale","code civil","gaz serre","brigitte bardot","main œuvre","main courante","vice président","jean luc","jean pierre", "jean jaurès", "jean moulin","jean paul", "week end","médico social","micro onde","burn out","anti douleur","auto entrepreneur","auto école","socio économique","hydro alcoolique","non violent","hold up","fast food","vidéo surveillance","orang outan","corona virus","éco responsable","skate park","hong kong","sri lanka","force ordre","ligne droite","mise ligne","mettre ligne","sécurité intérieur","réglement intérieur","extrême droite","air france","tour france","île réunion","radio france","france culture","france inter","france bleu","france info","france télévision","france 2","france 3","france 5","france insoumis","équipe france","parc attraction","maître conférence","coupe monde","langue maternelle","point relai","émission co2","téléphonie mobile","bureau poste","front national","école élémentaire","inspection académique","corps médical","corps humain","temps partiel","emploi temps","temps plein","marine pen","club canin","club med","transport animal","classe politique","classe confort","classe économique","femme homme","homme femme","femme enfant","enfant femme","dame paris","voix nord","eric zemmour","centre hospitalier","centre commercial","centre loisir","centre accueil","centre culturel","centre formation","centre rétention","françois fillon","jean françois","jean marc","jean macé","jean marie","luc ferry","plage horaire","place public","coup état","coup pouce","coup sûr","place stationnement","place parking","lieu travail","lieu vie","second plan","convention collectif","jeu olympique","jeu vidéo","jeu paralympique","campagne électoral","intérêt général","trouble comportement","libre arbitre","cadre vie","piste cyclable","conflit intérêt","ligne téléphonique","droit auteur","abus pouvoir","recherche emploi","vidéo surveillance","ligne tension","libre accès","campagne publicitaire","travail équipe","conseil constitutionnel","conseil état","cour école","cour récréation","particule fin","air libre","guerre mondial","mettre valeur","mise valeur","carte séjour","carte identité","carte bleu","carte bancaire","carte vital","carte gris","grand section","couleur peau","coupe davis","permis conduire","peine mort","mettre garde","mise garde","garde vue","garde sceau","garde corps","grève faim","édouard philippe","abbé pierre","lettre moderne","fur mesure","poids mesure","chaîne alimentaire","règle art","règle général","application mobile","mettre application","mise application","code route","feu vert","feu artifice","feu rouge","feu amour","station épuration","aire repos","aire jeu","passage piéton","poumon vert","chemin fer","tour eiffel","contrôle continu","salle bain","art plastique","contrôle judiciaire","mission local","contrôle technique","pouvoir achat","allocation familial","manuel vall","nicolas hulot","jacques chirac","femme ménage","service militaire","service technique","service client","service proximité","chef service","agent service","code travail","lien social","protection social","assistant social","centre social","travailleur social","poste travail","poste police","voie public","dépense public","fonds public","grand public","secteur activité","activité physique","collectivité local","population local","agent sécurité","fermer oeil","fermer porte","direction général","congé maternité","territoire national","aménagement territoire","agence immobilier","science politique","science physique","ressource humain","espèce humain","droit humain","culture général","art code","chef état","faire état","bon état","mauvais état","remise état","diplôme état","secrétaire état","état santé","état uni","état civil","état général","état lieu","état esprit","état sauvage","état service","huissier justice","moteur recherche","hôtel ville","quartier populaire","parc automobile","parc industriel","parc loisir","parc sport","parc activité","parc prince","faire lieu","espace vie","maison édition","droit visite","droit faire","droit vie","droit vivre","droit pouvoir","face situation","crèche noël","bon vivre","joie vivre","chien garde","fils électrique","fille garçon","garçon fille","vacance scolaire","système scolaire","cité scolaire","tendre enfance","père famille","vie famille","mère famille","père noël","père fondateur","feuille route","sécurité routier","accident route","personne âgé","site web","vie quartier","quartier nord","quartier résidentiel","pays origine","pays loire","pays basque","pays france","france pays","rue piétonne","personne rue","vivre rue","dormir rue","famille rue","coin rue","porte parole","promoteur immobilier","feuille route","code rural","garde enfant","juge enfant","jeu enfant","faire enfant","5 enfant","3 enfant","2 enfant","famille enfant","enfant famille","maman enfant","parent enfant","bien-être enfant","enfant 3","enfant 5","enfant faire","classe chimique","michael jackson","nelson mandela","journal télévisé","jeu télévisé","fer cheval", "non droit","bien sûr","bien commun","mener bien","dernier année","dernier temps","année dernier","servir rien","monde animal","collectif citoyen","accès soin","intérêt public","secrétaire général","état général","général gaulle","histoire france","histoire art","histoire contemporain","rapport force","rapport sexuel","cancer sein","mobilité réduire","loir cher","sens unique","sens interdire","sens circulation","sens responsabilité","sens inverse","bon sens","aucun sens","non sens","égalité chance","bon volonté","prélèvement source","eau source","ordre médecin","tour monde","charger mission",""]

    list_trigrams = ["liberté égalité fraternité","agence régional santé","organisation mondial santé","république démocratique congo","tribunal grand instance","allocation adulte handicapé","seconde guerre mondiale","auxiliaire vie scolaire","trouble ordre public","patrimoine mondial unesco","école normal supérieur","martin luther king"]

    more_stopwords = ["paul","françois","philippe","laurent","alain","olivier","nicolas","jacques","christophe","louis","bernard","michel","jean","martin","anne","david","stéphane","eric","charles","jean-luc","frédéric","frédérique","julien","bruno","maurice","gérard","andré","agnès","robin","ben","richard","victor","valérie","céline","jackson","nelson","alizée","val","marne","marseille","paris","france","faire","mettre","pouvoir","écrire","supprimer","donner","faire","fermer","opposer","exprimer","changer","imposer","partager","finir","mis","mise","âgé","agé","pris","pris_compte","pris_connaissance","pris_conscience","pri_position","mettre_application","mise_application","mise_place","mise_oeuvre","mise_disposition","rendu","repose","portée","tenu","arrêter","engager","revient","placer","arriver","lancer","mener","indiquer","établir","installer","réclamer","chercher","appliquer","adresser","indiquer","décider","laisser","parler","noter","appeler","aller","oublier","accepter","montrer","penser","rester","aider","garder","espérer","cesser","demander","signer","rappeler","continuer","trouver","essayer","aimer","imaginer","passer","remercier","souhaiter","hésiter","cliquer","proposer","exiger","utiliser","mériter","profiter","appeller","accorder","demeurer","dénoncer","poser","assurer","ajouter","toucher","préfèrer","démontrer","porter","attester","contacter","expliquer","susciter","plier","lacher","lâcher","considérer","génèrer","grandisser","representer","représenter","considerer","changer","suffiser","reconnaisser","réjouisser", "défendon","attendon","batton","rendon","vivon","metton","faison","soyon","soutenon","agisson","dison","unisson","prenon","pourron","réagisson","voyon","dénonçon","interdison","ayon","auron","accepteron","lançon","savez","soutenez","soyez","sachez","venez","voyez","connaissez","croyez","voulez","agissez","recevez","prenez","saviez","ayez","joignez","comprenez","ouvrez","pourriez","lisez","souvenez","rendez","mettez","rejoignez","viennent","deviennent","prennent","sentent","vivent","finissent","veulent","connaissent","meurent","offrent","rendent","agissent","naissent","permettent","fassent","souhaiteraient","proviennent","sortent","perdent", "fin","vie","année","compte","condition","point","titre","moyenne","temps","droite","suppression","personne","personn","mars","application","porte","agent","qualité","art_code","président","site","appel","recherche","activité","service","situation","espace","quartier","horaire","ouverture","rue","avenue","plan","réouverture","chiffre","euro","degré","enfer","période","lien","minute","liste","touch","touche","marche_arrière","marche","bon_état","bon_vivre","joie_vivre",'fonction',"partie","présent","journée","représentant","femme_homme","homme_femme","femme_enfant","enfant_femme","père_famille","mère_famille","supérieur","ensemble","face","grand","lourd","second","coup_sûr","capital","bon","auto","commun","majeur","principal","super","normal","permanent","inopinément","prématurément","idéologiquement","idéalement","simultanément","spontanément","considérablement","aisément","objectivement","fermement","exceptionnel","représentatif","représentative","considérable","contrarié","fort","haut","long","agé","ages","sous-signé","soussigné","19","2","3","5", "non","bien_sûr","bien","dernier","rien","général","volonté","ordre","charger","pierre","concerner","parole"]

    return [mots_erreur, mots_accent, list_bigrams, list_trigrams, more_stopwords, None]