"""Inhoudsdata voor de begrippenlijst en de vragenpagina.

Los gehouden van de templates zodat dezelfde bron zowel de zichtbare
inhoud als de JSON-LD (DefinedTermSet, FAQPage) voedt.
"""

TERMS = [
    ("API", "Een afspraak waarmee softwaresystemen onderling gegevens en functies uitwisselen, zonder dat de onderliggende werking bekend hoeft te zijn."),
    ("AVG", "De Algemene verordening gegevensbescherming, de Europese wet die eisen stelt aan de verwerking en beveiliging van persoonsgegevens."),
    ("Container", "Een verpakking van een applicatie samen met alles wat die nodig heeft om te draaien, zodat de applicatie zich overal hetzelfde gedraagt."),
    ("Datacenter", "Een beveiligd gebouw vol servers, netwerk- en koelapparatuur waarin cloudaanbieders hun diensten laten draaien."),
    ("DevOps", "Een werkwijze die de ontwikkeling en het beheer van software dichter bij elkaar brengt om sneller en betrouwbaarder op te leveren."),
    ("Disaster recovery", "Het geheel aan maatregelen en procedures om een omgeving na een grote verstoring weer volledig werkend te krijgen."),
    ("Edge computing", "Het verwerken van data dicht bij de plek waar die ontstaat, in plaats van in een centraal datacenter, om vertraging te beperken."),
    ("Hybride cloud", "Een combinatie van publieke en private cloud, waarbij werklast wordt verdeeld naar wat per onderdeel het beste past."),
    ("IaaS", "Infrastructuur als dienst: de aanbieder levert rekenkracht, opslag en netwerk, terwijl de afnemer daarop zelf software beheert."),
    ("Latentie", "De vertraging tussen een verzoek en het antwoord, doorgaans gemeten in milliseconden. Lagere latentie betekent een snellere reactie."),
    ("Load balancing", "Het verdelen van verkeer over meerdere servers, zodat geen enkele server overbelast raakt en de dienst beschikbaar blijft."),
    ("Multicloud", "Het naast elkaar gebruiken van diensten van meerdere cloudaanbieders om afhankelijkheid van één partij te verminderen."),
    ("PaaS", "Platform als dienst: de aanbieder levert een omgeving om software te bouwen en te draaien, zonder dat de afnemer de infrastructuur beheert."),
    ("Private cloud", "Een cloudomgeving die exclusief voor één organisatie draait, met meer controle en isolatie tegen hogere kosten en meer beheer."),
    ("Publieke cloud", "Gedeelde cloudinfrastructuur die een aanbieder aan meerdere afnemers levert, schaalbaar en met afrekening naar gebruik."),
    ("SaaS", "Software als dienst: een kant-en-klare applicatie die via internet wordt gebruikt, waarbij de aanbieder onderhoud en updates verzorgt."),
    ("Schaalbaarheid", "De mate waarin een omgeving mee kan groeien of krimpen met de vraag, zonder dat nieuwe hardware nodig is."),
    ("Serverless", "Een model waarbij code alleen draait wanneer die wordt aangeroepen en de aanbieder automatisch de capaciteit regelt."),
    ("SLA", "Een service level agreement: een afspraak over het niveau van een dienst, zoals de gegarandeerde beschikbaarheid en reactietijden."),
    ("Uptime", "Het deel van de tijd dat een dienst beschikbaar is, vaak uitgedrukt in een percentage over een bepaalde periode."),
    ("Virtualisatie", "De techniek om van één fysieke machine meerdere virtuele machines te maken die onafhankelijk van elkaar draaien."),
]

# Antwoorden: 'a' is HTML voor de pagina, 'a_plain' is platte tekst voor de JSON-LD.
FAQS = [
    {
        "q": "Wat is cloud computing?",
        "a": "<p>Cloud computing is het afnemen van rekenkracht, opslag en software via internet, geleverd door een aanbieder in plaats van via eigen apparatuur. Een organisatie gebruikt en betaalt naar behoefte, zonder zelf servers aan te schaffen en te onderhouden.</p>",
        "a_plain": "Cloud computing is het afnemen van rekenkracht, opslag en software via internet, geleverd door een aanbieder in plaats van via eigen apparatuur. Een organisatie gebruikt en betaalt naar behoefte, zonder zelf servers aan te schaffen en te onderhouden.",
    },
    {
        "q": "Wat is het verschil tussen cloudopslag en cloud computing?",
        "a": "<p>Cloudopslag gaat alleen over het bewaren van bestanden op servers van een aanbieder. Cloud computing is breder en omvat naast opslag ook rekenkracht, netwerken en complete applicaties. Opslag is dus een onderdeel van cloud computing.</p>",
        "a_plain": "Cloudopslag gaat alleen over het bewaren van bestanden op servers van een aanbieder. Cloud computing is breder en omvat naast opslag ook rekenkracht, netwerken en complete applicaties. Opslag is dus een onderdeel van cloud computing.",
    },
    {
        "q": "Is de cloud veilig?",
        "a": "<p>De grote aanbieders beveiligen hun infrastructuur op een niveau dat de meeste organisaties zelf niet halen. Toch blijft een deel van de beveiliging bij de afnemer, zoals toegangsbeheer en de juiste configuratie. De meeste incidenten ontstaan door een verkeerde instelling en niet door een fout van de aanbieder. Meer hierover staat in de gids over het <a href=\"/kennisbank/gedeelde-verantwoordelijkheid/\">gedeelde verantwoordelijkheidsmodel</a>.</p>",
        "a_plain": "De grote aanbieders beveiligen hun infrastructuur op een niveau dat de meeste organisaties zelf niet halen. Toch blijft een deel van de beveiliging bij de afnemer, zoals toegangsbeheer en de juiste configuratie. De meeste incidenten ontstaan door een verkeerde instelling en niet door een fout van de aanbieder.",
    },
    {
        "q": "Blijft data binnen de Europese Unie?",
        "a": "<p>Dat hangt af van de aanbieder. Veel bekende internationale diensten draaien deels of volledig op servers buiten de EU. Voor organisaties die met persoonsgegevens werken is opslag binnen de EU het uitgangspunt vanwege de AVG. Een aanbieder met servers in Nederland houdt de data binnen de landsgrenzen.</p>",
        "a_plain": "Dat hangt af van de aanbieder. Veel bekende internationale diensten draaien deels of volledig op servers buiten de EU. Voor organisaties die met persoonsgegevens werken is opslag binnen de EU het uitgangspunt vanwege de AVG. Een aanbieder met servers in Nederland houdt de data binnen de landsgrenzen.",
    },
    {
        "q": "Wat kost cloud computing?",
        "a": "<p>De cloud rekent doorgaans af naar gebruik, wat de kosten flexibel maar ook lastig voorspelbaar maakt. Zonder sturing lopen rekeningen op door ongebruikte resources en te ruime instellingen. De gids over <a href=\"/kennisbank/grip-op-cloudkosten/\">grip op cloudkosten</a> beschrijft hoe die kosten beheersbaar blijven.</p>",
        "a_plain": "De cloud rekent doorgaans af naar gebruik, wat de kosten flexibel maar ook lastig voorspelbaar maakt. Zonder sturing lopen rekeningen op door ongebruikte resources en te ruime instellingen.",
    },
    {
        "q": "Wie is verantwoordelijk voor de beveiliging?",
        "a": "<p>Beveiliging is een gedeelde taak. De aanbieder beschermt de onderliggende infrastructuur, terwijl de afnemer verantwoordelijk blijft voor de eigen data, toegang en configuratie. Waar de grens ligt, verschilt per dienstmodel.</p>",
        "a_plain": "Beveiliging is een gedeelde taak. De aanbieder beschermt de onderliggende infrastructuur, terwijl de afnemer verantwoordelijk blijft voor de eigen data, toegang en configuratie. Waar de grens ligt, verschilt per dienstmodel.",
    },
    {
        "q": "Wat is het verschil tussen back-up en disaster recovery?",
        "a": "<p>Een back-up is een kopie van data waarnaar teruggekeerd kan worden. Disaster recovery beschrijft hoe een hele omgeving na een grote verstoring weer draaiend komt. Een back-up is dus een onderdeel van disaster recovery, maar niet het geheel.</p>",
        "a_plain": "Een back-up is een kopie van data waarnaar teruggekeerd kan worden. Disaster recovery beschrijft hoe een hele omgeving na een grote verstoring weer draaiend komt. Een back-up is dus een onderdeel van disaster recovery, maar niet het geheel.",
    },
    {
        "q": "Hoe verloopt een overstap naar de cloud?",
        "a": "<p>Een gefaseerde aanpak werkt het beste: eerst een inventarisatie, dan een keuze per werklast, gevolgd door een proef en een uitrol in golven. Een grote overstap in één keer brengt meer risico met zich mee. De gids over <a href=\"/kennisbank/cloudmigratie-in-fasen/\">cloudmigratie in vijf fasen</a> beschrijft de route.</p>",
        "a_plain": "Een gefaseerde aanpak werkt het beste: eerst een inventarisatie, dan een keuze per werklast, gevolgd door een proef en een uitrol in golven. Een grote overstap in één keer brengt meer risico met zich mee.",
    },
]
