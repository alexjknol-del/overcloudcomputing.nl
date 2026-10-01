---
title: "Microsoft 365 als cloudwerkplek: inrichten, beheren en beveiligen"
description: "Microsoft 365 verplaatst mail, bestanden en samenwerking naar de cloud. Wat er bij de overstap komt kijken, welk beheer daarna doorloopt en welke beveiliging bij de basis hoort."
date: 2026-09-28
category: "Toepassing"
reading_time: 5
---

Microsoft 365 is voor veel Nederlandse organisaties de eerste echte stap naar de cloud. Mail, agenda's, bestanden en overleg verhuizen van een eigen server naar een omgeving die Microsoft in zijn datacenters beheert. Medewerkers werken daarna vanaf elke plek en elk apparaat met dezelfde gegevens. Dat maakt veel eenvoudiger, maar het beheer verdwijnt niet. Het verschuift.

## Wat er in de omgeving zit

Microsoft 365 is een SaaS-dienst. Outlook voor mail en agenda, Teams voor overleg, OneDrive voor persoonlijke bestanden en SharePoint voor gedeelde mappen vormen samen één werkplek. Word, Excel en PowerPoint werken in de browser en als programma op de computer. Een document in SharePoint is door meerdere collega's tegelijk te bewerken, zonder dat er versies per mail heen en weer gaan.

## De overstap in fasen

Een overstap naar Microsoft 365 volgt dezelfde lijn als elke [cloudmigratie](/kennisbank/cloudmigratie-in-fasen/): eerst inventariseren, dan een proef, daarna de rest. Bij de inventarisatie gaat het om mailboxen, gedeelde mappen, rechten en koppelingen met andere software. De domeinnaam krijgt nieuwe DNS-records, zodat mail bij de nieuwe omgeving binnenkomt. Een proef met een paar gebruikers laat zien of agenda's, gedeelde mailboxen en bestandsrechten goed zijn overgekomen voordat de hele organisatie overgaat.

## Beheer na de overstap

Na de overstap begint het dagelijkse beheer. Nieuwe medewerkers krijgen een account en een licentie, vertrekkende medewerkers worden uitgeschakeld en hun gegevens overgedragen. Rechten op gedeelde mappen verschuiven als teams veranderen. Microsoft houdt het platform bij, maar de instellingen van de eigen omgeving blijven de taak van de organisatie. Dat volgt uit het [gedeelde verantwoordelijkheidsmodel](/kennisbank/gedeelde-verantwoordelijkheid/).

Veel organisaties besteden dit beheer uit. Een ICT-bedrijf als [Pixelbyte](https://www.pixelbyte.nl/) uit Alkmaar neemt voor organisaties met 1 tot 100 medewerkers het beheer van gebruikers, licenties en instellingen over, naast netwerk, werkplekken en ondersteuning.

## Beveiliging bij de basis

Een overgenomen account in Microsoft 365 geeft toegang tot mail, bestanden en agenda tegelijk. Multifactorauthenticatie (MFA) maakt inloggen met alleen een gestolen wachtwoord onmogelijk en hoort vanaf de eerste dag aan te staan. Voor mail zijn daarnaast drie DNS-records van belang. SPF geeft aan welke servers namens het domein mogen versturen, DKIM ondertekent berichten digitaal en DMARC bepaalt wat een ontvanger doet met mail die niet aan die controles voldoet. Samen maken ze het lastiger om het domein te misbruiken voor phishing.

Bij een invoering via [pixelbyte.nl](https://www.pixelbyte.nl/diensten/microsoft-office-365/) horen MFA en de records voor SPF, DKIM en DMARC daarom standaard bij de inrichting, net als het beheer van toegangsrechten en back-ups.

## Een eigen back-up

Microsoft bewaart verwijderde items een beperkte tijd, maar dat is geen volledige back-up. Een verwijderde map, een verkeerde synchronisatie of een besmetting kan zich door de omgeving verspreiden. Een aparte back-up van mailboxen, OneDrive en SharePoint, los van Microsoft 365 zelf, maakt herstel naar een eerder moment mogelijk. De afwegingen rond hersteltijd en herstelpunt staan in de gids over [back-up en disaster recovery](/kennisbank/back-up-en-disaster-recovery/).

## Meegroeien en AI

Licenties worden per gebruiker afgenomen, waardoor de omgeving meegroeit met de organisatie. Ook AI-toepassingen zoals Microsoft Copilot werken binnen dezelfde omgeving en gebruiken de bestanden waar een medewerker toegang toe heeft. Goed ingestelde rechten worden daarmee belangrijker: wat een medewerker kan openen, kan Copilot ook gebruiken.

Een cloudwerkplek die goed is ingericht, geeft medewerkers overal dezelfde bestanden en dezelfde beveiliging. Het werk zit niet alleen in de overstap, maar vooral in het beheer dat daarna doorloopt.
