---
title: "Voorraadbeheer in de cloud: barcodes, scanners en een centrale database"
description: "Een cloudgebaseerd voorraadsysteem verplaatst de database naar een datacenter. Hoe scanners, barcode etiketten en koppelingen dan samenwerken, en waar op te letten bij storingen en gegevensbeheer."
date: 2026-09-21
category: "Toepassing"
reading_time: 4
---

Voorraadbeheer draaide lang op een server in het eigen pand of op een spreadsheet op één computer. Cloudgebaseerde voorraadsystemen verplaatsen de database naar een datacenter, bereikbaar vanaf elke scanner, telefoon of laptop met een internetverbinding. Dat verandert niet alleen waar de gegevens staan, maar ook hoe de koppeling met het magazijn werkt.

## Hoe het werkt

Een cloudvoorraadsysteem is meestal een SaaS-dienst. De aanbieder beheert de software en de database, de gebruiker werkt via een browser of een app. Scanners en mobiele terminals in het magazijn sturen elke scan via wifi of mobiel internet naar de centrale database. Een webshop, een boekhoudpakket of een verzendsysteem is via een API aan dezelfde database gekoppeld. Een verkoop in de webshop verlaagt zo direct de voorraad die het magazijn ziet.

## De barcode als schakel

De verbinding tussen de fysieke voorraad en de database is de barcode. Elke locatie en elk artikel krijgt een code die overeenkomt met een record in het systeem. Code 128 is voor interne artikel- en locatiecodes het meest gebruikt. Een QR-code bevat meer gegevens en is met de camera van een telefoon te lezen, wat handig is als er geen aparte scanners worden aangeschaft.

Een barcode verwijst alleen naar een record. Voorraadaantallen en andere wisselende gegevens staan niet op het etiket, maar in de database. Daardoor blijft het etiket geldig, ook als de gegevens veranderen.

## Etiketten op stelling en vak

Op stalen stellingen zijn magnetische etiketten gangbaar, omdat ze zonder lijmresten meeverhuizen als de indeling verandert. Op hout of kunststof werkt een zelfklevend etiket beter. Bij [MMS Magneetservice](https://www.mms-magneet.nl/barcode-etiketten/) zijn magazijnetiketten in beide uitvoeringen te krijgen, kant-en-klaar gedrukt op basis van aangeleverde gegevens of om zelf te printen. Een export van de locatiecodes uit het cloudsysteem vormt dan de basis voor de etiketten.

## Offline en storingen

Een cloudsysteem is afhankelijk van de verbinding. Valt het internet of de wifi in het magazijn weg, dan komen scans niet aan. Veel apps bewaren scans tijdelijk op het apparaat en sturen ze door zodra de verbinding terug is. Bij de keuze voor een systeem is het verstandig na te gaan hoe dat is geregeld en hoe dubbele verwerking wordt voorkomen. Een goede wifidekking tussen de stellingen hoort bij de voorbereiding.

## Gegevens en verantwoordelijkheid

Ook bij voorraadbeheer geldt het model van [gedeelde verantwoordelijkheid](/kennisbank/gedeelde-verantwoordelijkheid/). De aanbieder zorgt voor de beschikbaarheid en beveiliging van het platform, de gebruiker voor accounts, rechten en de juistheid van de gegevens. Een export van de voorraadgegevens op vaste momenten beschermt tegen dataverlies en maakt een overstap naar een andere aanbieder eenvoudiger.

## Stapsgewijs invoeren

Invoeren gaat het best in fasen, net als bij een [cloudmigratie](/kennisbank/cloudmigratie-in-fasen/). Eerst de locatiecodes in het systeem en op de stellingen, daarna een proef met één productgroep en pas dan de rest. Over etiketmateriaal en houders is telefonisch advies te krijgen via [mms-magneet.nl](https://www.mms-magneet.nl/).

Een centrale database met goede etiketten in het magazijn geeft iedereen dezelfde, actuele stand van de voorraad, van de orderpicker tot de boekhouding.
