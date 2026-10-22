"""Builds index.html for 4travel.pro (v2 design, Oct 22 2026). Run: python3 build_index.py"""
import json

KEEP = json.load(open('/tmp/keep.json')) if __import__('os').path.exists('/tmp/keep.json') else json.load(open('i18n_keep.json'))
json.dump(KEEP, open('i18n_keep.json', 'w'), ensure_ascii=False, indent=1)

K = ["navFlights","navHolidays","navIdeas","heroA","heroB","heroSub","tr1","tr2","tr3","destTitle","destCta",
     "cBarcelona","cLondon","cLisbon","cParis","cMilan","cAthens","holTitle","hol1","hol1d","hol2","hol2d","hol3","hol3d",
     "holCta","howTitle","h1","h1d","h2","h2d","h3","h3d","langLabel","mapTitle","mapSub","destSub","calTitle","calSub","tabFlights","tabHotels","tabTransfer","tabCars","tabEsim","tabTours","tabComp","hotelText","hotelBtn","altLabel"]
T = {
"en": ["Flights","Holidays","Weekend ideas","Cheap flights and holidays,","in one search",
 "We compare hundreds of airlines and travel agencies. You pick the best price and book directly with them.",
 "Hundreds of airlines and agencies","No extra fees from us","You book directly with the seller",
 "Where to this weekend?","Search flights →","Barcelona","London","Lisbon","Paris","Milan","Athens",
 "Holidays with flight + hotel","3-day city break","Flight and a central hotel, booked together.",
 "Christmas and New Year","The busiest dates of the year: compare early.","Sun and sea","Beach holidays for every budget.",
 "Search flight + hotel →","How it works","Search once","Hundreds of airlines and agencies in one list.",
 "Compare the real price","See times, stops and baggage before you choose.","Book directly",
 "You pay the airline or agency you pick. 4travel.pro adds no fees.","Language","Cheap flights on the map","Prices from your city to destinations around the world. Drag and zoom the map, then tap a city.","The lowest fares found to each city, from different departure airports. Tap a price to see the flights.","When is it cheapest to fly?","Pick a destination and see the lowest price for every month of the year.","Flights","Hotels","Airport transfer","Car rental","eSIM","Tours & tickets","Flight delayed?","Hotels, apartments and resorts for every budget, on Trip.com.","Search hotels on Trip.com →","Also try:"],
"ro": ["Zboruri","Vacanțe","Idei de weekend","Zboruri ieftine și vacanțe,","într-o singură căutare",
 "Comparăm sute de companii aeriene și agenții de turism. Tu alegi cel mai bun preț și rezervi direct la ele.",
 "Sute de companii aeriene și agenții","Fără taxe în plus de la noi","Rezervi direct la vânzător",
 "Unde zbori în weekend?","Caută zboruri →","Barcelona","Londra","Lisabona","Paris","Milano","Atena",
 "Vacanțe cu zbor + hotel","City break de 3 zile","Zbor și hotel central, rezervate împreună.",
 "Crăciun și Revelion","Cele mai aglomerate date din an: compară din timp.","Soare și mare","Vacanțe la plajă pentru orice buget.",
 "Caută zbor + hotel →","Cum funcționează","Cauți o dată","Sute de companii aeriene și agenții, într-o singură listă.",
 "Compari prețul real","Vezi orele, escalele și bagajul înainte să alegi.","Rezervi direct",
 "Plătești compania sau agenția aleasă. 4travel.pro nu adaugă taxe.","Limba","Zboruri ieftine pe hartă","Prețuri din orașul tău spre destinații din toată lumea. Mișcă harta, mărește și apasă pe un oraș.","Cele mai mici prețuri găsite spre fiecare oraș, din mai multe aeroporturi de plecare. Apasă pe un preț ca să vezi zborurile.","Când e cel mai ieftin să zbori?","Alege o destinație și vezi cel mai mic preț pentru fiecare lună din an.","Zboruri","Cazări","Transfer aeroport","Închirieri auto","eSIM","Tururi și bilete","Zbor întârziat?","Hoteluri, apartamente și resorturi pentru orice buget, pe Trip.com.","Caută hotel pe Trip.com →","Mai poți încerca:"],
"fr": ["Vols","Séjours","Idées week-end","Vols pas chers et séjours,","en une seule recherche",
 "Nous comparons des centaines de compagnies aériennes et d'agences. Vous choisissez le meilleur prix et réservez directement chez elles.",
 "Des centaines de compagnies et d'agences","Aucuns frais de notre part","Vous réservez directement auprès du vendeur",
 "Où partir ce week-end ?","Chercher un vol →","Barcelone","Londres","Lisbonne","Paris","Milan","Athènes",
 "Séjours vol + hôtel","City break de 3 jours","Vol et hôtel central, réservés ensemble.",
 "Noël et Nouvel An","Les dates les plus demandées de l'année : comparez tôt.","Soleil et mer","Vacances à la plage pour tous les budgets.",
 "Chercher vol + hôtel →","Comment ça marche","Une seule recherche","Des centaines de compagnies et d'agences dans une seule liste.",
 "Le vrai prix","Horaires, escales et bagages visibles avant de choisir.","Réservation directe",
 "Vous payez la compagnie ou l'agence choisie. 4travel.pro n'ajoute aucuns frais.","Langue","Vols pas chers sur la carte","Les prix depuis votre ville vers le monde entier. Déplacez et zoomez la carte, puis touchez une ville.","Les prix les plus bas trouvés vers chaque ville, depuis plusieurs aéroports de départ. Touchez un prix pour voir les vols.","Quand est-ce le moins cher ?","Choisissez une destination et voyez le prix le plus bas pour chaque mois de l'année.","Vols","Hôtels","Transfert aéroport","Location de voiture","eSIM","Visites et billets","Vol retardé ?","Hôtels, appartements et resorts pour tous les budgets, sur Trip.com.","Chercher un hôtel sur Trip.com →","Essayez aussi :"],
"de": ["Flüge","Urlaub","Wochenend-Ideen","Günstige Flüge und Urlaub,","in einer Suche",
 "Wir vergleichen Hunderte Airlines und Reiseanbieter. Du wählst den besten Preis und buchst direkt bei ihnen.",
 "Hunderte Airlines und Anbieter","Keine Zusatzgebühren von uns","Du buchst direkt beim Verkäufer",
 "Wohin am Wochenende?","Flüge suchen →","Barcelona","London","Lissabon","Paris","Mailand","Athen",
 "Urlaub mit Flug + Hotel","3 Tage Städtereise","Flug und zentrales Hotel, zusammen gebucht.",
 "Weihnachten und Silvester","Die gefragtesten Termine des Jahres: früh vergleichen.","Sonne und Meer","Strandurlaub für jedes Budget.",
 "Flug + Hotel suchen →","So funktioniert es","Einmal suchen","Hunderte Airlines und Anbieter in einer Liste.",
 "Echten Preis vergleichen","Zeiten, Umstiege und Gepäck sehen, bevor du wählst.","Direkt buchen",
 "Du zahlst die gewählte Airline oder den Anbieter. 4travel.pro erhebt keine Gebühren.","Sprache","Günstige Flüge auf der Karte","Preise von deiner Stadt zu Zielen weltweit. Karte verschieben und zoomen, dann eine Stadt antippen.","Die günstigsten gefundenen Preise in jede Stadt, von verschiedenen Abflughäfen. Tippe auf einen Preis, um die Flüge zu sehen.","Wann ist Fliegen am günstigsten?","Wähle ein Ziel und sieh den niedrigsten Preis für jeden Monat des Jahres.","Flüge","Hotels","Flughafentransfer","Mietwagen","eSIM","Touren & Tickets","Flug verspätet?","Hotels, Apartments und Resorts für jedes Budget, bei Trip.com.","Hotels bei Trip.com suchen →","Auch interessant:"],
"es": ["Vuelos","Vacaciones","Ideas de fin de semana","Vuelos baratos y vacaciones,","en una sola búsqueda",
 "Comparamos cientos de aerolíneas y agencias. Tú eliges el mejor precio y reservas directamente con ellas.",
 "Cientos de aerolíneas y agencias","Sin comisiones nuestras","Reservas directamente con el vendedor",
 "¿A dónde este fin de semana?","Buscar vuelos →","Barcelona","Londres","Lisboa","París","Milán","Atenas",
 "Vacaciones con vuelo + hotel","Escapada de 3 días","Vuelo y hotel céntrico, reservados juntos.",
 "Navidad y Año Nuevo","Las fechas más buscadas del año: compara con tiempo.","Sol y playa","Vacaciones de playa para cualquier presupuesto.",
 "Buscar vuelo + hotel →","Cómo funciona","Buscas una vez","Cientos de aerolíneas y agencias en una sola lista.",
 "Comparas el precio real","Horarios, escalas y equipaje antes de elegir.","Reservas directamente",
 "Pagas a la aerolínea o agencia elegida. 4travel.pro no añade comisiones.","Idioma","Vuelos baratos en el mapa","Precios desde tu ciudad a destinos de todo el mundo. Mueve y amplía el mapa y toca una ciudad.","Los precios más bajos encontrados a cada ciudad, desde varios aeropuertos de salida. Toca un precio para ver los vuelos.","¿Cuándo es más barato volar?","Elige un destino y mira el precio más bajo de cada mes del año.","Vuelos","Hoteles","Traslado aeropuerto","Alquiler de coche","eSIM","Tours y entradas","¿Vuelo retrasado?","Hoteles, apartamentos y resorts para cualquier presupuesto, en Trip.com.","Buscar hotel en Trip.com →","Prueba también:"],
"it": ["Voli","Vacanze","Idee per il weekend","Voli economici e vacanze,","in un'unica ricerca",
 "Confrontiamo centinaia di compagnie aeree e agenzie. Scegli il prezzo migliore e prenoti direttamente con loro.",
 "Centinaia di compagnie e agenzie","Nessun costo aggiuntivo da parte nostra","Prenoti direttamente con il venditore",
 "Dove andare questo weekend?","Cerca voli →","Barcellona","Londra","Lisbona","Parigi","Milano","Atene",
 "Vacanze volo + hotel","City break di 3 giorni","Volo e hotel in centro, prenotati insieme.",
 "Natale e Capodanno","Le date più richieste dell'anno: confronta presto.","Sole e mare","Vacanze al mare per ogni budget.",
 "Cerca volo + hotel →","Come funziona","Cerchi una volta","Centinaia di compagnie e agenzie in un'unica lista.",
 "Confronti il prezzo reale","Orari, scali e bagaglio prima di scegliere.","Prenoti direttamente",
 "Paghi la compagnia o l'agenzia scelta. 4travel.pro non aggiunge costi.","Lingua","Voli economici sulla mappa","Prezzi dalla tua città verso destinazioni in tutto il mondo. Sposta e ingrandisci la mappa, poi tocca una città.","I prezzi più bassi trovati verso ogni città, da diversi aeroporti di partenza. Tocca un prezzo per vedere i voli.","Quando conviene volare?","Scegli una destinazione e vedi il prezzo più basso per ogni mese dell'anno.","Voli","Hotel","Transfer aeroporto","Noleggio auto","eSIM","Tour e biglietti","Volo in ritardo?","Hotel, appartamenti e resort per ogni budget, su Trip.com.","Cerca hotel su Trip.com →","Prova anche:"],
"hu": ["Repülőjegyek","Nyaralás","Hétvégi ötletek","Olcsó repülőjegyek és nyaralások,","egyetlen kereséssel",
 "Több száz légitársaságot és utazási irodát hasonlítunk össze. Te választod ki a legjobb árat, és közvetlenül náluk foglalsz.",
 "Több száz légitársaság és iroda","Tőlünk nincs extra díj","Közvetlenül az eladónál foglalsz",
 "Hová utazz a hétvégén?","Járatok keresése →","Barcelona","London","Lisszabon","Párizs","Milánó","Athén",
 "Nyaralás repülővel + szállással","3 napos városlátogatás","Repülőjegy és belvárosi szálloda együtt foglalva.",
 "Karácsony és szilveszter","Az év legkeresettebb időpontjai: hasonlíts korán.","Nap és tenger","Tengerparti nyaralás minden pénztárcához.",
 "Repülő + szálloda keresése →","Hogyan működik","Egyszer keresel","Több száz légitársaság és iroda egy listában.",
 "A valódi árat látod","Időpontok, átszállások és poggyász a választás előtt.","Közvetlenül foglalsz",
 "A választott légitársaságnak vagy irodának fizetsz. A 4travel.pro nem számít fel díjat.","Nyelv","Olcsó járatok a térképen","Árak a városodból úti célokba szerte a világon. Mozgasd és nagyítsd a térképet, majd koppints egy városra.","A talált legolcsóbb árak minden városba, több indulási repülőtérről. Koppints egy árra a járatokért.","Mikor a legolcsóbb repülni?","Válassz úti célt, és nézd meg a legalacsonyabb árat az év minden hónapjára.","Repülőjegyek","Szállás","Reptéri transzfer","Autóbérlés","eSIM","Túrák és jegyek","Késett a járat?","Szállodák, apartmanok és üdülők minden pénztárcához a Trip.com-on.","Szállás keresése a Trip.com-on →","Próbáld ki ezt is:"],
"tr": ["Uçuşlar","Tatiller","Hafta sonu fikirleri","Ucuz uçuşlar ve tatiller,","tek aramada",
 "Yüzlerce havayolunu ve acenteyi karşılaştırıyoruz. En iyi fiyatı sen seçer, doğrudan onlardan rezervasyon yaparsın.",
 "Yüzlerce havayolu ve acente","Bizden ek ücret yok","Doğrudan satıcıdan alırsın",
 "Bu hafta sonu nereye?","Uçuş ara →","Barselona","Londra","Lizbon","Paris","Milano","Atina",
 "Uçuş + otel tatilleri","3 günlük şehir turu","Uçuş ve merkezi otel birlikte.",
 "Yılbaşı ve Noel","Yılın en yoğun tarihleri: erkenden karşılaştır.","Güneş ve deniz","Her bütçeye plaj tatili.",
 "Uçuş + otel ara →","Nasıl çalışır","Bir kez ara","Yüzlerce havayolu ve acente tek listede.",
 "Gerçek fiyatı karşılaştır","Saatleri, aktarmaları ve bagajı seçmeden önce gör.","Doğrudan rezervasyon",
 "Seçtiğin havayoluna veya acenteye ödersin. 4travel.pro ücret eklemez.","Dil","Haritada ucuz uçuşlar","Şehrinden dünyanın dört bir yanına fiyatlar. Haritayı kaydır, yakınlaştır ve bir şehre dokun.","Her şehre farklı kalkış havalimanlarından bulunan en düşük fiyatlar. Uçuşları görmek için bir fiyata dokun.","Ne zaman uçmak en ucuz?","Bir yer seç ve yılın her ayı için en düşük fiyatı gör.","Uçuşlar","Oteller","Havalimanı transferi","Araç kiralama","eSIM","Turlar ve biletler","Uçuş gecikti mi?","Her bütçeye otel, daire ve tatil köyü, Trip.com'da.","Trip.com'da otel ara →","Şunu da dene:"],
"ar": ["رحلات الطيران","العطلات","أفكار لعطلة نهاية الأسبوع","رحلات طيران رخيصة وعطلات،","في بحث واحد",
 "نقارن مئات شركات الطيران ووكالات السفر. أنت تختار أفضل سعر وتحجز مباشرة لديهم.",
 "مئات شركات الطيران والوكالات","لا رسوم إضافية منّا","تحجز مباشرة لدى البائع",
 "إلى أين في عطلة نهاية الأسبوع؟","ابحث عن رحلات ←","برشلونة","لندن","لشبونة","باريس","ميلانو","أثينا",
 "عطلات مع الطيران + الفندق","عطلة مدينة لمدة 3 أيام","رحلة طيران وفندق في المركز، محجوزان معًا.",
 "عيد الميلاد ورأس السنة","أكثر مواعيد السنة طلبًا: قارن مبكرًا.","شمس وبحر","عطلات شاطئية لكل الميزانيات.",
 "ابحث عن طيران + فندق ←","كيف يعمل","ابحث مرة واحدة","مئات شركات الطيران والوكالات في قائمة واحدة.",
 "قارن السعر الحقيقي","اطّلع على المواعيد والتوقفات والأمتعة قبل الاختيار.","احجز مباشرة",
 "تدفع لشركة الطيران أو الوكالة التي تختارها. لا يضيف 4travel.pro أي رسوم.","اللغة","رحلات رخيصة على الخريطة","الأسعار من مدينتك إلى وجهات حول العالم. حرّك الخريطة وكبّرها ثم اضغط على مدينة.","أقل الأسعار التي وجدناها إلى كل مدينة من مطارات مغادرة مختلفة. اضغط على سعر لرؤية الرحلات.","متى يكون الطيران أرخص؟","اختر وجهة وشاهد أقل سعر لكل شهر من السنة.","رحلات الطيران","الفنادق","التوصيل من المطار","تأجير السيارات","شريحة eSIM","جولات وتذاكر","تأخرت رحلتك؟","فنادق وشقق ومنتجعات لكل الميزانيات على Trip.com.","ابحث عن فندق على Trip.com ←","جرّب أيضًا:"],
}
TR = {}
for lang, vals in T.items():
    assert len(vals) == len(K), (lang, len(vals))
    d = dict(zip(K, vals)); d.update(KEEP[lang]); TR[lang] = d
en = TR["en"]
def t(k): return f'<span data-key="{k}">{en[k]}</span>'

ICONS = {"flights": "M17.8 19.2L16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z", "hotels": "M3 21V7l9-4 9 4v14M9 21v-6h6v6M8 10h.01M12 10h.01M16 10h.01", "transfer": "M5 17h14M6 17l1.5-6h9L18 17M7 17v2M17 17v2M9 7h6l1 4H8z", "cars": "M3 13l2-6h14l2 6v5H3zM7 18v2M17 18v2M6.5 14.5h.01M17.5 14.5h.01", "esim": "M7 3h7l5 5v13H7zM10 12h6v6h-6z", "tours": "M4 7h16v4a2 2 0 000 4v4H4v-4a2 2 0 000-4zM12 7v12", "comp": "M12 8v4l3 2M12 21a9 9 0 100-18 9 9 0 000 18z"}
TABDEF = [('flights', 'tabFlights'), ('hotels', 'tabHotels'), ('transfer', 'tabTransfer'), ('cars', 'tabCars'), ('esim', 'tabEsim'), ('tours', 'tabTours'), ('comp', 'tabComp')]
DEST = [("barcelona","cBarcelona"),("london","cLondon"),("lisbon","cLisbon"),("paris","cParis"),("milan","cMilan"),("athens","cAthens")]
IATA = {"barcelona":"BCN","london":"LON","lisbon":"LIS","paris":"PAR","milan":"MIL","athens":"ATH"}
tabs = "".join(f'''<button type="button" class="svc" role="tab" data-svc="{k}" aria-selected="{'true' if k=='flights' else 'false'}"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{ICONS[k]}"/></svg><span data-key="{lk}">{en[lk]}</span></button>''' for k,lk in TABDEF)
dest = "\n".join(f'''      <li class="w-card"><div class="tp-route" data-dest="{IATA[f]}"></div></li>''' for f,k in DEST)
chips = "".join(f'''<button type="button" class="chip" data-dest="{IATA[f]}"><img src="/img/{f}.jpg" alt="" width="64" height="64" loading="lazy"><span data-key="{k}">{en[k]}</span></button>''' for f,k in DEST)
HOL = [("citybreak","hol1","hol1d"),("winter","hol2","hol2d"),("beach","hol3","hol3d")]
hol = "\n".join(f'''      <li><a class="hol" href="#search"><img src="/img/{f}.jpg" alt="" width="900" height="600" loading="lazy"><span class="hol-body"><span class="hol-title" data-key="{a}">{en[a]}</span><span class="hol-desc" data-key="{b}">{en[b]}</span><span class="hol-cta" data-key="holCta">{en["holCta"]}</span></span></a></li>''' for f,a,b in HOL)

LANGS = [("en","English"),("ro","Română"),("fr","Français"),("de","Deutsch"),("es","Español"),("it","Italiano"),("hu","Magyar"),("tr","Türkçe"),("ar","العربية")]
opts = "".join(f'<option value="{c}">{n}</option>' for c,n in LANGS)

html = f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>4travel.pro – Cheap flights and holidays in one search</title>
<meta name="description" content="Compare cheap flights and flight + hotel holidays from hundreds of airlines and travel agencies, then book directly with them. Free, no extra fees.">
<link rel="canonical" href="https://www.4travel.pro/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.4travel.pro/">
<meta property="og:title" content="4travel.pro – Cheap flights and holidays in one search">
<meta property="og:description" content="Compare hundreds of airlines and agencies, then book directly. Free, no extra fees.">
<meta property="og:image" content="https://www.4travel.pro/img/hero.jpg">
<meta name="theme-color" content="#0E1E3A">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect width='24' height='24' rx='6' fill='%230E1E3A'/%3E%3Cpath transform='translate(3.2 3.2) scale(.73)' fill='%23F2711C' d='M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600;700&family=Noto+Sans+Arabic:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{{--navy:#0E1E3A;--navy-2:#16294B;--sky:#F3F6FA;--card:#FFFFFF;--line:#D3DBE8;--ink:#0E1E3A;--soft:#4A5A78;--orange:#F2711C;--orange-ink:#B4500A;--peach:#FFE7D6;
--display:"Archivo",system-ui,sans-serif;--body:"Inter",system-ui,-apple-system,"Segoe UI",sans-serif;--wrap:1200px}}
*,*::before,*::after{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
body{{margin:0;background:var(--sky);color:var(--ink);font:400 1.0625rem/1.6 var(--body);-webkit-font-smoothing:antialiased}}
html[dir="rtl"] body{{--display:"Noto Sans Arabic",system-ui,sans-serif;--body:"Noto Sans Arabic",system-ui,sans-serif}}
img{{max-width:100%;height:auto;display:block}}
a{{color:inherit}}
:focus-visible{{outline:3px solid var(--orange);outline-offset:3px;border-radius:6px}}
.sr,.skip{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}.skip:focus{{width:auto;height:auto;clip:auto;top:1rem;inset-inline-start:1rem;background:#fff;color:var(--navy);padding:.5rem 1rem;z-index:30}}
.wrap{{max-width:var(--wrap);margin:0 auto;padding:0 clamp(1rem,4vw,1.5rem)}}
/* top */
.top{{background:var(--navy);color:#fff;padding-bottom:7rem}}
.bar{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:.8rem;padding-top:1.1rem;padding-bottom:1.1rem}}
.logo{{display:flex;align-items:center;gap:.6rem;text-decoration:none;font-family:var(--display);font-weight:800;font-size:1.55rem;letter-spacing:-.01em}}
.logo b{{color:var(--orange);font-weight:800}}
.nav{{display:flex;flex-wrap:wrap;align-items:center;gap:.4rem 1.4rem;font-weight:500;font-size:.95rem}}
.nav a{{text-decoration:none;color:#fff;opacity:.92}}.nav a:hover{{opacity:1;color:var(--orange)}}
.nav select{{height:42px;border-radius:10px;border:1px solid #3A4C6E;background:var(--navy-2);color:#fff;padding:0 .6rem;font:inherit;font-size:.9rem}}
@media (max-width:640px){{.nav a{{display:none}}}}
.hero{{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:2rem;align-items:center;padding-top:2.2rem}}
.hero h1{{margin:0 0 .9rem;font-family:var(--display);font-weight:800;font-size:clamp(2.4rem,5.6vw,3.9rem);line-height:1.02;letter-spacing:-.02em}}
.hero h1 em{{font-style:normal;color:var(--orange);display:block}}
.hero p{{margin:0;font-size:1.15rem;color:#C9D3E6;max-width:46ch}}
.hero img{{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:24px}}
@media (max-width:860px){{.hero{{grid-template-columns:1fr}}.hero img{{display:none}}.top{{padding-bottom:6rem}}}}
/* search */
.search{{margin-top:-5.5rem;position:relative;z-index:2}}
.search-card{{background:var(--card);border-radius:22px;padding:clamp(.8rem,2.5vw,1.6rem);box-shadow:0 22px 50px rgba(14,30,58,.18)}}
.widget-slot{{min-height:190px}}
.svcs{{display:flex;gap:.4rem;overflow-x:auto;margin:0 0 1rem;padding-bottom:.3rem;scrollbar-width:thin}}
.svc{{flex:0 0 auto;display:flex;align-items:center;gap:.45rem;border:0;background:#EEF2F8;color:var(--navy);border-radius:999px;padding:.6rem 1rem;font:600 .95rem inherit;font-family:inherit;cursor:pointer;white-space:nowrap}}
.svc:hover{{background:#E2E8F2}}
.svc[aria-selected="true"]{{background:#F2711C;color:#fff}}
.hotel-panel{{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1rem;background:#EEF2F8;border-radius:16px;padding:1.4rem 1.6rem}}
.hotel-panel p{{margin:0;font-size:1.05rem;font-weight:600;max-width:46ch}}
.big-btn{{display:inline-block;background:#F2711C;color:#fff;font-weight:700;border-radius:12px;padding:.9rem 1.4rem;text-decoration:none}}
.big-btn:hover{{background:#C2540A;color:#fff}}
.alts{{margin:.7rem 0 0;font-size:.95rem;color:var(--soft)}}
.alts a{{font-weight:700;color:#C2540A;margin-inline-end:.8rem}}
.trust{{list-style:none;margin:1rem 0 0;padding:0;display:flex;flex-wrap:wrap;gap:.5rem 1.6rem;font-size:.92rem;font-weight:600;color:var(--soft)}}
.trust li{{display:flex;align-items:center;gap:.45rem}}
.trust svg{{flex:none;color:var(--orange-ink)}}
/* sections */
.sec{{padding-top:3rem}}
.sec h2{{margin:0 0 1.2rem;font-family:var(--display);font-weight:800;font-size:clamp(1.7rem,3.2vw,2.3rem);letter-spacing:-.01em}}
.grid{{list-style:none;margin:0;padding:0;display:grid;gap:1rem}}
.dests{{grid-template-columns:repeat(6,minmax(0,1fr))}}
@media (max-width:1100px){{.dests{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}
@media (max-width:560px){{.dests{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
.dest{{position:relative;display:block;height:240px;border-radius:20px;overflow:hidden;text-decoration:none;color:#fff}}
.dest img{{width:100%;height:100%;object-fit:cover;transition:transform .4s ease}}
.dest:hover img{{transform:scale(1.05)}}
.dest-label{{position:absolute;left:.6rem;right:.6rem;bottom:.6rem;background:rgba(14,30,58,.86);border-radius:14px;padding:.6rem .8rem;display:flex;flex-direction:column}}
.dest-name{{font-family:var(--display);font-weight:800;font-size:1.3rem;line-height:1.15}}
.dest-cta{{font-size:.82rem;font-weight:600;color:#FFC9A3}}
.hols{{grid-template-columns:repeat(3,minmax(0,1fr));gap:1.3rem}}
@media (max-width:860px){{.hols{{grid-template-columns:1fr}}}}
.hol{{display:flex;flex-direction:column;height:100%;background:var(--card);border-radius:22px;overflow:hidden;text-decoration:none;box-shadow:0 2px 8px rgba(14,30,58,.06)}}
.hol img{{width:100%;aspect-ratio:3/2;object-fit:cover}}
.hol-body{{display:flex;flex-direction:column;gap:.35rem;padding:1.1rem 1.3rem 1.4rem}}
.hol-title{{font-family:var(--display);font-weight:800;font-size:1.35rem}}
.hol-desc{{color:var(--soft);font-size:.97rem}}
.hol-cta{{color:var(--orange-ink);font-weight:700;font-size:.95rem;margin-top:.2rem}}
.hol:hover .hol-title{{color:var(--orange-ink)}}
.routes{{grid-template-columns:repeat(2,minmax(0,1fr));gap:1.2rem}}
@media (max-width:760px){{.routes{{grid-template-columns:1fr}}}}
.w-card{{background:var(--card);border-radius:20px;overflow:hidden;padding:.5rem;box-shadow:0 2px 8px rgba(14,30,58,.06);min-height:320px}}
.chips{{display:flex;flex-wrap:wrap;gap:.6rem;margin:0 0 1rem}}
.chip{{display:flex;align-items:center;gap:.55rem;border:2px solid transparent;background:var(--card);border-radius:999px;padding:.3rem 1rem .3rem .3rem;font:600 .97rem var(--body,inherit);color:var(--navy);cursor:pointer;box-shadow:0 1px 4px rgba(14,30,58,.08)}}
.chip img{{width:36px;height:36px;border-radius:50%;object-fit:cover}}
.chip[aria-selected="true"]{{border-color:#F2711C;color:#C2540A}}
.cal-card{{min-height:420px}}
.sec-sub{{margin:-.6rem 0 1.2rem;color:var(--soft);max-width:60ch}}
.map-card{{background:var(--card);border-radius:24px;overflow:hidden;padding:.6rem;box-shadow:0 2px 8px rgba(14,30,58,.06);min-height:300px}}
#tp-map{{border-radius:18px;overflow:hidden}}
.how{{background:var(--card);border-radius:24px;padding:clamp(1.4rem,4vw,2.4rem);display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.6rem;list-style:none;margin:0}}
@media (max-width:760px){{.how{{grid-template-columns:1fr}}}}
.how li{{display:flex;flex-direction:column;gap:.35rem}}
.num{{width:44px;height:44px;border-radius:12px;background:var(--peach);color:var(--orange-ink);display:flex;align-items:center;justify-content:center;font-family:var(--display);font-weight:800;font-size:1.25rem}}
.how strong{{font-family:var(--display);font-weight:800;font-size:1.25rem}}
.how span{{color:var(--soft);font-size:.97rem}}
footer{{margin-top:3.5rem;background:var(--navy);color:#C9D3E6;font-size:.9rem}}
footer .wrap{{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.8rem 2rem;padding-top:1.8rem;padding-bottom:2.2rem}}
footer a{{color:#fff}}
footer p{{margin:0;max-width:70ch}}
</style>
</head>
<body>
<a class="skip" href="#search">Skip to search</a>
<div class="top">
  <div class="wrap bar">
    <a class="logo" href="/"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#F2711C" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17.8 19.2L16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/></svg><span>4travel<b>.pro</b></span></a>
    <nav class="nav" aria-label="Menu">
      <a href="#search">{t("navFlights")}</a>
      <a href="#holidays">{t("navHolidays")}</a>
      <a href="#ideas">{t("navIdeas")}</a>
      <label for="lang" class="sr" data-key="langLabel">{en["langLabel"]}</label>
      <select id="lang">{opts}</select>
    </nav>
  </div>
  <div class="wrap hero">
    <div>
      <h1><span data-key="heroA">{en["heroA"]}</span> <em data-key="heroB">{en["heroB"]}</em></h1>
      <p data-key="heroSub">{en["heroSub"]}</p>
    </div>
    <img src="/img/hero.jpg" alt="" width="1600" height="1000" fetchpriority="high">
  </div>
</div>

<main>
  <section id="search" class="wrap search" aria-label="Search flights">
    <div class="search-card">
      <div class="svcs" role="tablist">{tabs}</div>
      <div class="widget-slot" id="tp-slot"></div>
      <div class="hotel-panel" id="hotel-panel" hidden><p data-key="hotelText">{en["hotelText"]}</p><a class="big-btn" href="https://www.tkqlhce.com/click-101697384-11947208?url=https%3A%2F%2Fwww.trip.com%2Fhotels%2F&amp;sid=4travel-hotels" target="_blank" rel="sponsored noopener" data-key="hotelBtn">{en["hotelBtn"]}</a></div>
      <p class="alts" id="alts" hidden><span data-key="altLabel">{en["altLabel"]}</span> <span id="alt-links"></span></p>
      <ul class="trust">
        <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>{t("tr1")}</li>
        <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>{t("tr2")}</li>
        <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>{t("tr3")}</li>
      </ul>
    </div>
  </section>

  <section id="ideas" class="wrap sec">
    <h2 data-key="destTitle">{en["destTitle"]}</h2>
    <p class="sec-sub" data-key="destSub">{en["destSub"]}</p>
    <ul class="grid routes">
{dest}
    </ul>
  </section>


  <section id="calendar" class="wrap sec">
    <h2 data-key="calTitle">{en["calTitle"]}</h2>
    <p class="sec-sub" data-key="calSub">{en["calSub"]}</p>
    <div class="chips" role="tablist">{chips}</div>
    <div class="map-card cal-card"><div id="tp-cal"></div></div>
  </section>

  <section id="holidays" class="wrap sec">
    <h2 data-key="holTitle">{en["holTitle"]}</h2>
    <ul class="grid hols">
{hol}
    </ul>
  </section>

  <section class="wrap sec">
    <h2 data-key="howTitle">{en["howTitle"]}</h2>
    <ol class="how">
      <li><span class="num">1</span><strong data-key="h1">{en["h1"]}</strong><span data-key="h1d">{en["h1d"]}</span></li>
      <li><span class="num">2</span><strong data-key="h2">{en["h2"]}</strong><span data-key="h2d">{en["h2d"]}</span></li>
      <li><span class="num">3</span><strong data-key="h3">{en["h3"]}</strong><span data-key="h3d">{en["h3d"]}</span></li>
    </ol>
  </section>
</main>

<footer>
  <div class="wrap">
    <p><span data-key="disclosure">{en["disclosure"]}</span></p>
    <p>&copy; <span id="year">2026</span> 4travel.pro · <span data-key="rights">{en["rights"]}</span> · <a href="/privacy.html" data-key="privacy">{en["privacy"]}</a></p>
  </div>
</footer>

<script>
const translations = {json.dumps(TR, ensure_ascii=False)};
const WIDGET_LOCALES = {{en:'en',fr:'fr',de:'de',es:'es',it:'it',tr:'tr'}};
const CURRENCY = {{tr:'try',ar:'usd',hu:'eur',ro:'eur'}};
let svc = 'flights';
const CUR_UP = l => (CURRENCY[l] || 'eur').toUpperCase();
const SVC = {{
  transfer: l => ({{currency: CUR_UP(l), trs:'502962', shmarker:'662933', locale:'en', from:'', to:'', country:'', powered_by:'true', height:'', wtype:'true', transfers_limit:'10', button_color:'#F2711C', button_hover_color:'#C2540A', campaign_id:'1', promo_id:'2949'}}),
  cars: l => ({{trs:'502962', shmarker:'662933', locale:'en', powered_by:'true', border_radius:'12', plain:'true', show_logo:'true', promo_id:'4480', campaign_id:'10'}}),
  esim: l => ({{trs:'502962', shmarker:'662933', locale:'en', powered_by:'true', secondary:'#FFFFFF', dark:'#0E1E3A', light:'#FFFFFF', special:'#C4C4C4', border_radius:'12', plain:'false', no_labels:'true', promo_id:'8588', campaign_id:'541'}}),
  tours: l => ({{currency: CUR_UP(l), trs:'502962', shmarker:'662933', language:'en', locale:'260932', layout:'horizontal', cards:'4', powered_by:'true', campaign_id:'89', promo_id:'3947'}}),
  comp: l => ({{trs:'502962', shmarker:'662933', lang:'en', powered_by:'true', campaign_id:'120', promo_id:'8679'}})
}};
SVC.flights = l => ({{currency: CURRENCY[l] || 'eur', trs:'502962', shmarker:'662933', locale: WIDGET_LOCALES[l] || 'en', stops:'any', show_hotels:'true', powered_by:'true', border_radius:'12', plain:'true', color_button:'#F2711C', color_button_text:'#ffffff', promo_id:'3414', campaign_id:'111'}});
const ALTS = {{
  flights: [['Aviasales', null]],
  transfer: [['GetTransfer', 'https://gettransfer.tpm.lv/iuxFQT02']],
  cars: [['Localrent', 'https://localrent.tpm.lv/tOoD7aJV']],
  esim: [['Drimsim', 'https://drimsim.tpm.lv/TOwhzovo']]
}};
function loadSvc(lang){{
  document.querySelectorAll('.svc').forEach(b => b.setAttribute('aria-selected', String(b.dataset.svc === svc)));
  const slot = document.getElementById('tp-slot'), hp = document.getElementById('hotel-panel');
  hp.hidden = svc !== 'hotels'; slot.hidden = svc === 'hotels';
  const alts = ALTS[svc] || [], box = document.getElementById('alt-links');
  document.getElementById('alts').hidden = !alts.length; box.innerHTML = '';
  alts.forEach(([n, u]) => {{ const a = document.createElement('a'); a.textContent = n + ' →';
    if (u) {{ a.href = u; a.target = '_blank'; a.rel = 'sponsored noopener'; }}
    else {{ a.href = '#'; a.addEventListener('click', e => {{ e.preventDefault(); loadWidget(document.documentElement.lang); document.getElementById('alts').hidden = true; }}); }}
    box.appendChild(a); }});
  if (svc === 'hotels') {{ slot.innerHTML = ''; return; }}
  tpScript(slot, SVC[svc](lang));
}}
document.querySelectorAll('.svc').forEach(b => b.addEventListener('click', () => {{ svc = b.dataset.svc; loadSvc(document.documentElement.lang); }}));
function loadWidget(lang){{
  const slot = document.getElementById('tp-slot');
  slot.innerHTML = '';
  const p = new URLSearchParams({{
    currency: CURRENCY[lang] || 'eur', trs: '502962', shmarker: '662933', show_hotels: 'true', powered_by: 'true',
    locale: WIDGET_LOCALES[lang] || 'en', searchUrl: 'www.aviasales.com/search',
    primary_override: '#F2711C', color_button: '#F2711C', color_icons: '#F2711C', dark: '#0E1E3A', light: '#FFFFFF',
    secondary: '#FFFFFF', special: '#C4C4C4', color_focused: '#F2711C', border_radius: '12', plain: 'true',
    promo_id: '7879', campaign_id: '100'
  }});
  const s = document.createElement('script');
  s.async = true; s.charset = 'utf-8';
  s.src = 'https://tpwidg.com/content?' + p.toString();
  slot.appendChild(s);
}}
const ORIGINS = {{en:['LON',51.5074,-0.1278],ro:['BUH',44.4268,26.1025],fr:['PAR',48.8566,2.3522],de:['BER',52.52,13.405],es:['MAD',40.4168,-3.7038],it:['ROM',41.9028,12.4964],hu:['BUD',47.4979,19.0402],tr:['IST',41.0082,28.9784],ar:['DXB',25.2048,55.2708]}};
function loadMap(lang){{
  const slot = document.getElementById('tp-map'); slot.innerHTML = '';
  const o = ORIGINS[lang] || ORIGINS.en;
  const w = Math.max(300, Math.round(slot.clientWidth || 1100));
  const h = w < 600 ? 420 : 520;
  const p = new URLSearchParams({{
    currency: CURRENCY[lang] || 'eur', trs: '502962', shmarker: '662933', lat: String(o[1]), lng: String(o[2]),
    powered_by: 'true', search_host: 'www.aviasales.com/search', locale: WIDGET_LOCALES[lang] || 'en', origin: o[0],
    value_min: '0', value_max: '1000000', round_trip: 'true', only_direct: 'false', radius: '1', draggable: 'true',
    disable_zoom: 'false', show_logo: 'false', scrollwheel: 'false', primary: '#F2711C', secondary: '#0E1E3A', light: '#ffffff',
    width: String(w), height: String(h), zoom: '3', promo_id: '4054', campaign_id: '100'
  }});
  const s = document.createElement('script'); s.async = true; s.charset = 'utf-8';
  s.src = 'https://tpwidg.com/content?' + p.toString();
  slot.appendChild(s);
}}
function tpScript(slot, params){{
  slot.innerHTML = '';
  const s = document.createElement('script'); s.async = true; s.charset = 'utf-8';
  s.src = 'https://tpwidg.com/content?' + new URLSearchParams(params).toString();
  slot.appendChild(s);
}}
function lazy(slot, fn){{
  if (!('IntersectionObserver' in window)) {{ fn(); return; }}
  const io = new IntersectionObserver(es => {{ if (es.some(e => e.isIntersecting)) {{ io.disconnect(); fn(); }} }}, {{rootMargin:'400px'}});
  io.observe(slot);
}}
function loadRoutes(lang){{
  document.querySelectorAll('.tp-route').forEach(slot => lazy(slot, () => tpScript(slot, {{
    currency: CURRENCY[lang] || 'eur', trs: '502962', shmarker: '662933', destination: slot.dataset.dest,
    target_host: 'www.aviasales.com/search', locale: WIDGET_LOCALES[lang] || 'en', limit: '6', powered_by: 'true',
    primary: '#F2711C', promo_id: '4044', campaign_id: '100'
  }})));
}}
let calDest = null;
function loadCal(lang){{
  const o = (ORIGINS[lang] || ORIGINS.en)[0];
  const chips = [...document.querySelectorAll('.chip')];
  if (!calDest || calDest === o) calDest = (chips.find(c => c.dataset.dest !== o) || chips[0]).dataset.dest;
  chips.forEach(c => {{ c.setAttribute('aria-selected', String(c.dataset.dest === calDest)); c.hidden = c.dataset.dest === o; }});
  const slot = document.getElementById('tp-cal');
  lazy(slot, () => tpScript(slot, {{
    currency: CURRENCY[lang] || 'eur', trs: '502962', shmarker: '662933', searchUrl: 'www.aviasales.com/search',
    locale: WIDGET_LOCALES[lang] || 'en', powered_by: 'true', one_way: 'false', only_direct: 'false', period: 'year', range: '3,7',
    origin: o, destination: calDest,
    primary: '#F2711C', color_background: '#ffffff', dark: '#0E1E3A', light: '#FFFFFF', achieve: '#45AD35',
    promo_id: '4041', campaign_id: '100'
  }}));
}}
document.querySelectorAll('.chip').forEach(c => c.addEventListener('click', () => {{ calDest = c.dataset.dest; loadCal(document.documentElement.lang); }}));
function setLang(lang){{
  const t = translations[lang]; if (!t) return;
  document.documentElement.lang = lang; document.documentElement.dir = t.dir;
  document.querySelectorAll('[data-key]').forEach(el => {{ const v = t[el.dataset.key]; if (v !== undefined) el.textContent = v; }});
  document.getElementById('lang').value = lang;
  try {{ localStorage.setItem('lang', lang); }} catch (e) {{}}
  loadSvc(lang);
  loadRoutes(lang);
  loadCal(lang);
}}
document.getElementById('lang').addEventListener('change', e => setLang(e.target.value));
document.getElementById('year').textContent = new Date().getFullYear();
(function initLang(){{
  let lang = null;
  const q = new URLSearchParams(location.search).get('lang');
  if (q && translations[q]) lang = q;
  if (!lang) {{ try {{ lang = localStorage.getItem('lang'); }} catch (e) {{}} }}
  if (!lang || !translations[lang]) {{
    const nav = (navigator.languages || [navigator.language || 'en']).map(l => l.slice(0, 2).toLowerCase());
    lang = nav.find(l => translations[l]) || 'en';
  }}
  setLang(lang);
}})();
</script>
<script data-noptimize="1" data-cfasync="false" data-wpfc-render="false">
  (function () {{
      var script = document.createElement("script");
      script.async = 1;
      script.src = 'https://emrldtp.com/NTAyOTYy.js?t=502962';
      document.head.appendChild(script);
  }})();
</script>
</body>
</html>
'''
open("index.html", "w", encoding="utf-8").write(html)
print("ok", len(html))
