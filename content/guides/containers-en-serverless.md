---
title: "Containers en serverless uitgelegd"
description: "Twee manieren om applicaties in de cloud te draaien zonder vaste servers te beheren. Wat containers en serverless inhouden en wanneer welke aanpak past."
date: 2026-06-25
category: "Architectuur"
reading_time: 6
---

Applicaties draaien in de cloud lang niet altijd meer op een vaste, altijd draaiende server. Containers en serverless zijn twee manieren om software uit te voeren met minder beheer en meer flexibiliteit. Ze lossen verschillende problemen op en sluiten elkaar niet uit.

## Wat een container is

Een container verpakt een applicatie samen met alles wat die nodig heeft om te draaien: code, bibliotheken en instellingen. Daardoor gedraagt de applicatie zich overal hetzelfde, van de laptop van een ontwikkelaar tot de productieomgeving. Containers starten snel, verbruiken weinig, en meerdere exemplaren draaien onafhankelijk op dezelfde onderliggende machine.

Bij grotere aantallen containers komt orkestratie in beeld. Die zorgt automatisch voor het starten, verdelen en herstellen van containers over meerdere machines. Zo blijft een applicatie beschikbaar, ook wanneer een onderdeel uitvalt of de belasting toeneemt.

## Wat serverless is

Serverless gaat een stap verder in het uit handen geven van beheer. De code draait alleen wanneer die wordt aangeroepen, en de aanbieder regelt automatisch de capaciteit. Er is geen server die continu draait en betaald wordt. De afrekening volgt het werkelijke gebruik, tot op de uitvoering nauwkeurig.

Die opzet past goed bij taken die met tussenpozen voorkomen: een bestand dat verwerkt moet worden, een melding die verstuurd wordt, een verzoek dat af en toe binnenkomt. Voor werklast die constant en zwaar is, valt de rekening van serverless vaak juist hoger uit.

## Wanneer welke aanpak

De keuze hangt af van het karakter van de werklast. Containers bieden controle en voorspelbaarheid en passen bij applicaties die langdurig draaien. Serverless neemt het beheer vrijwel volledig over en past bij taken die onregelmatig voorkomen. Veel organisaties combineren beide, waarbij ieder onderdeel de vorm krijgt die het beste past.

## Minder beheer, andere aandachtspunten

Beide aanpakken verminderen het beheer van servers, maar brengen eigen aandachtspunten mee. Containers vragen om goede afspraken over versies en beveiliging van de gebruikte onderdelen. Serverless maakt een applicatie afhankelijker van de specifieke aanbieder, wat de overstap later kan bemoeilijken. Een bewuste afweging vooraf voorkomt verrassingen achteraf.
